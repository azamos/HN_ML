from typing import Dict,Union
import re
from src.utils import dbgprint, errprint
from src.csv_fields import (
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
    # Title Semantic Features
    CSV_TITLE_KEYWORD_COUNT,
    CSV_TITLE_PROGRAMMING_LANGUAGES_COUNT,
    CSV_TITLE_AI_TERMS_COUNT,
    CSV_TITLE_CLOUD_TERMS_COUNT,
    CSV_TITLE_BUSINESS_TERMS_COUNT,
    CSV_TITLE_COMPANY_NAMES_MENTIONS,
    CSV_TITLE_VERSION_NUMBERS_PRESENT,
    CSV_TITLE_FUNDING_MENTIONS
)

import src.keyword_lists as KEYWORDS

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

def title_semantics_extractor(title: str) -> Dict[str,Union[int,float,bool]]:
    title_words_lowered = set(title.lower().split())
    tech_keyword_count = sum( 1 for tech_keyword in KEYWORDS.TECH_KEYWORDS if tech_keyword in title_words_lowered )
    programming_languages_count = sum( 1 for programming_language in KEYWORDS.PROGRAMMING_LANGUAGES if programming_language in title_words_lowered )
    ai_terms_count = sum( 1 for ai_term in KEYWORDS.AI_TERMS if ai_term in title_words_lowered )
    cloud_terms_count = sum( 1 for cloud_term in KEYWORDS.CLOUD_TERMS if cloud_term in title_words_lowered )
    business_terms_count = sum( 1 for business_term in KEYWORDS.BUSINESS_TERMS if business_term in title_words_lowered )
    company_names_count = sum( 1 for company_name in KEYWORDS.COMPANY_NAMES if company_name in title_words_lowered )
    versions_mentioned_count = sum(len(re.findall(pattern, title, re.IGNORECASE)) for pattern in KEYWORDS.VERSION_PATTERNS)
    funding_terms_count = sum( 1 for funding_term in KEYWORDS.FUNDING_TERMS if funding_term in title_words_lowered )

    return {
        CSV_TITLE_KEYWORD_COUNT:tech_keyword_count,
        CSV_TITLE_PROGRAMMING_LANGUAGES_COUNT:programming_languages_count,
        CSV_TITLE_AI_TERMS_COUNT:ai_terms_count,
        CSV_TITLE_CLOUD_TERMS_COUNT:cloud_terms_count,
        CSV_TITLE_BUSINESS_TERMS_COUNT:business_terms_count,
        CSV_TITLE_COMPANY_NAMES_MENTIONS:company_names_count,
        CSV_TITLE_VERSION_NUMBERS_PRESENT:versions_mentioned_count,
        CSV_TITLE_FUNDING_MENTIONS:funding_terms_count
    }

def title_features_extractor(title: str) -> Dict[str,Union[int,float,bool]]:
    return {**title_structure_extractor(title=title),**title_semantics_extractor(title=title)}