import re
import PyPDF2
import pandas as pd
import os

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

  

   



def read_multiple_pdfs(directory):
    pdf_texts = {}
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(directory, filename)
            pdf_file = open(pdf_path, 'rb')
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            text = ''
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                text += page.extract_text()
            pdf_texts[filename] = text
            pdf_file.close()
            yield filename, text


def arabic_text_pipline(directory, dictionary):
    for filename, txt in read_multiple_pdfs(directory):

        fixed_text = fix_arabic_text(txt)
        gibberish = is_gibberish(fixed_text, dictionary)
    
    return gibberish

def is_valid(gibberish):
    # if it's valid create 
    # new csv file with the valid ones
    pass

arabic_text_pipline(read_multiple_pdfs('arabic_papers'), arabic_dictionary)



