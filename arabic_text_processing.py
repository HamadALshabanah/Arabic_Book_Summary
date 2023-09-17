import re
import PyPDF2
import pandas as pd


with open('ar_SA.txt', 'r', encoding='utf-8') as file:
    arabic_dictionary = file.read()



def keep_only_arabic(text):
    arabic_text = re.findall(r'[\u0600-\u06FF]+', text)
    return ' '.join(arabic_text)


# يعدل مشكلة تقاطع الحروف الناتجة من ملفات البيدي اف
def fix_arabic_text(text):
    # Remove extra spaces
    text = re.sub(' +', ' ', text).strip()
    
    # Normalize 
    text = text.replace('أ', 'ا').replace('إ', 'ا').replace('آ', 'ا')
    
 
    words = text.split()
    fixed_words = []
    
    for word in words:
        # اذا فيه ا وبعدها حرف ثم ل, رجع اللام ورا خانة وحدة بس
        if word.startswith('ا') and len(word) > 2 and word[2] == 'ل':
            fixed_word = 'ال' + word[1] + word[3:]
        else:
            fixed_word = word
        
        fixed_words.append(fixed_word)
    
    fixed_text = ' '.join(fixed_words)
    
    return fixed_text.strip()



def simple_arabic_tokenizer(text):
   
    return re.findall(r'\b[\u0600-\u06FF]+\b', text)



# يتأكد من نسبة الكلمات الغير موجودة من القاموس
def is_gibberish(text, dictionary, threshold=.30):

    words = simple_arabic_tokenizer(text)
    
    not_dictionary_count = 0
    for word in words:
        if word not in dictionary:
            not_dictionary_count += 1


    if len(words) == 0:
        return True  # Empty error
    proportion_not_in_dictionary = not_dictionary_count / len(words)
    
    return proportion_not_in_dictionary > threshold

  
def process_text(sample_text, dictionary):
    fixed_text = fix_arabic_text(sample_text)
    
    
    gibberish = is_gibberish(fixed_text, dictionary)
    
    return gibberish
   



pdfFileObj = open('442812947@kku.edu_.sa_.pdf', 'rb')

pdfReader = PyPDF2.PdfReader(pdfFileObj)

num_pages = len(pdfReader.pages)


for page_num in range(num_pages):
    # Get a PageObject
    pageObj = pdfReader.pages[page_num]

    # Extract text from the PageObject
    text_content = pageObj.extract_text()

    # Process the text
    process_text(text_content, arabic_dictionary)


def is_valid(gibberish):
    # if it's valid then create 
    # new dataframe with the valid ones
    pass


# Close the PDF file

pdfFileObj.close()


