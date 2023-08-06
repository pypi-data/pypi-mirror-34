from cs200.core import BRACKET_START, BRACKET_END
import re



def gen_regex(topic):
    
    regex = ''
    
    for letter in topic:
        if letter != " ":
            upper = letter.upper()
            lower = letter.lower()
            
            combined = BRACKET_START + lower + upper + BRACKET_END
            
            regex += combined
            
        if letter == " ":
            regex += ' '
            
    regex += "[\s\w]*\."

    return regex


def analyze_data(topic, text):
    
    regexp = gen_regex(topic)
    
    return re.findall(regexp, text)

