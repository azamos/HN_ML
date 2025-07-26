from typing import Dict,Union
import re
from src.utils import dbgprint, errprint
from src.constants import (
    # Title Structural Features
    CSV_TITLE_CHAR_COUNT,
    CSV_TITLE_WORD_COUNT,
    CSV_TITLE_AVG_WORD_LENGTH,
    CSV_TITLE_CASE_RATIO,
    CSV_TITLE_ALL_CAP_WORD_COUNT,
    CSV_TITLE_HAS_NUMBERS,
    CSV_TITLE_HAS_YEAR,
    CSV_TITLE_HAS_QUESTION_MARK,
    CSV_TITLE_ENDS_WITH_PUNC,
)
def title_structure_extractor(title: str) -> Dict[str,Union[int,float,bool]]:
    dbgprint(f"Starting title feature extractor for:{title}")
    combined_chars = re.sub(r'\s','',title)
    char_amount = len(combined_chars)
    dbgprint(f"The combined chars are: {combined_chars}. The amount is {char_amount}",
             True)

    words = title.split()
    num_of_words = len(words)
    dbgprint(f"The title words are: {words}. The amount is : {num_of_words}",
             True)

    total_word_len = sum([len(word) for word in words])
    avg_word_len = total_word_len/num_of_words if num_of_words>0 else 0

    dbgprint(f"The total_word_len: {total_word_len}. The avg is : {avg_word_len}",
             True)
    
    capital_count = sum(1 for char in title if char.isalpha() and char.isupper())
    alpha_count = sum(1 for char in title if char.isalpha())

    dbgprint(f"The alpha_count: {alpha_count}. The capital_count is : {capital_count}",
             True)

    case_ratio = capital_count/alpha_count if alpha_count > 0 else 0
    dbgprint(f"The case ratio is : {case_ratio}",
             True)
    
    uppercase_count = sum(1 for word in words if word.isalpha() and word.isupper())
    dbgprint(f"The uppercase_count is : {uppercase_count}",
             True)
    
    has_numbers = any(char.isdigit() for char in title)
    dbgprint(f"Does the title contain any numbers?  : {has_numbers}",
             True)
    
    has_year = bool(re.search(r'\b(19|20)\d{2}\b', title))
    dbgprint(f"Does the title contain a year?  : {has_year}",
             True)
    
    has_question_mark = '?' in title
    dbgprint(f"Does the title contain a question mark : {has_question_mark}",
             True)
    sentence_ending_punctuation = ('.', '!', '?', ':', '…')
    ends_with_punc = title.strip().endswith(sentence_ending_punctuation)
    dbgprint(f"Does the title end with a punctuation mark?  : {ends_with_punc}",
             True)

    return {
        CSV_TITLE_CHAR_COUNT: char_amount,
        CSV_TITLE_WORD_COUNT : num_of_words,
        CSV_TITLE_AVG_WORD_LENGTH: avg_word_len,
        CSV_TITLE_CASE_RATIO: case_ratio,
        CSV_TITLE_ALL_CAP_WORD_COUNT: uppercase_count,
        CSV_TITLE_HAS_NUMBERS: has_numbers,
        CSV_TITLE_HAS_YEAR: has_year,
        CSV_TITLE_ENDS_WITH_PUNC: ends_with_punc,
        CSV_TITLE_HAS_QUESTION_MARK: has_question_mark
    }
