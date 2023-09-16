
import re

def simple_arabic_tokenizer(text):
    """
    A simple function to tokenize Arabic text based on spaces and punctuation marks.
    """
    return re.findall(r'\b[\u0600-\u06FF]+\b', text)

# Test the tokenizer
simple_arabic_tokenizer("السلام عليكم، كيف حالك؟")


def is_gibberish(text, dictionary, threshold=0.7):
    """
    Checks if the given text is gibberish based on a dictionary lookup.
    
    Parameters:
    - text (str): The text to check.
    - dictionary (set): The set of valid words.
    - threshold (float): The proportion of unrecognized words above which the text is considered gibberish.
    
    Returns:
    - bool: True if the text is gibberish, False otherawise.
    """
    # Tokenize the text into words
    words = simple_arabic_tokenizer(text)
    
    not_dictionary_count = 0
    for word in words:
        if word not in dictionary:
            not_dictionary_count += 1


    if len(words) == 0:
        return True  # Empty error
    proportion_not_in_dictionary = not_dictionary_count / len(words)
    
    return proportion_not_in_dictionary > threshold

# Test the function with your text and a valid Arabic sentence
with open('dic\\ar_SA.txt', 'r', encoding='utf-8') as file:
    arabic_dictionary = file.read()

is_gibberish1 = is_gibberish('تكسغ مذكمة الجراسة في محاولة رصج الجوافع الشفدية واالجتساعية والسعخفية لمتعخ', arabic_dictionary)
is_gibberish2 = is_gibberish(' يمكننا الحديث عن أفضل المجلات العلمية العربية لنشر الأبحاث دون ذكر المجلة الالكترونية الشاملة متعددة التخصصات، فمنذ صدور عددها الأول في عام 2017، وهي تصدر أعدادها الإلكترونية بشكل', arabic_dictionary)

print(is_gibberish1, is_gibberish2)
