from src.feature_extractors.title_feature_extractor import title_structure_extractor
from src.csv_fields import (
    # Title Structural Features
    CSV_TITLE_CHAR_COUNT,CSV_TITLE_WORD_COUNT,
    CSV_TITLE_AVG_WORD_LENGTH,CSV_TITLE_CASE_RATIO,
    CSV_TITLE_ALL_CAP_WORD_COUNT,CSV_TITLE_HAS_NUMBERS,
    CSV_TITLE_HAS_YEAR,CSV_TITLE_HAS_QUESTION_MARK,
    CSV_TITLE_ENDS_WITH_PUNC,
)
def test_title_structure_extractor_valid():
    title1 = "ALL UPPER CASE TEST"
    res1 = title_structure_extractor(title=title1)
    assert res1[CSV_TITLE_CHAR_COUNT] == 16
    assert res1[CSV_TITLE_WORD_COUNT] == 4
    assert res1[CSV_TITLE_AVG_WORD_LENGTH] == 4.0
    assert res1[CSV_TITLE_CASE_RATIO] == 1.0
    assert res1[CSV_TITLE_ALL_CAP_WORD_COUNT] == 4
    assert res1[CSV_TITLE_HAS_NUMBERS] == False
    assert res1[CSV_TITLE_HAS_YEAR] == False
    assert res1[CSV_TITLE_HAS_QUESTION_MARK] == False
    assert res1[CSV_TITLE_ENDS_WITH_PUNC] == False

    title2 = "Can Chat GPT in 2025 win a chess torunament against 32 opponents? Check the Video!"
    res2 = title_structure_extractor(title=title2)
    assert res2[CSV_TITLE_CHAR_COUNT] == 68
    assert res2[CSV_TITLE_WORD_COUNT] == 15
    assert res2[CSV_TITLE_AVG_WORD_LENGTH] == 68/15
    assert res2[CSV_TITLE_CASE_RATIO] == 7/60
    assert res2[CSV_TITLE_ALL_CAP_WORD_COUNT] == 1
    assert res2[CSV_TITLE_HAS_NUMBERS] == True
    assert res2[CSV_TITLE_HAS_YEAR] == True
    assert res2[CSV_TITLE_HAS_QUESTION_MARK] == True
    assert res2[CSV_TITLE_ENDS_WITH_PUNC] == True

def test_title_structure_extractor_failure_cases():
   """Test edge cases and potential failure scenarios."""
   
   # Test Case 1: Empty String
   title = ""
   res = title_structure_extractor(title=title)
   assert res[CSV_TITLE_CHAR_COUNT] == 0
   assert res[CSV_TITLE_WORD_COUNT] == 0
   assert res[CSV_TITLE_AVG_WORD_LENGTH] == 0  # Should handle division by zero
   assert res[CSV_TITLE_CASE_RATIO] == 0       # Should handle division by zero
   assert res[CSV_TITLE_ALL_CAP_WORD_COUNT] == 0
   assert res[CSV_TITLE_HAS_NUMBERS] == False
   assert res[CSV_TITLE_HAS_YEAR] == False
   assert res[CSV_TITLE_HAS_QUESTION_MARK] == False
   assert res[CSV_TITLE_ENDS_WITH_PUNC] == False
   
   # Test Case 2: Only Whitespace
   title = "   \t  \n  "
   res = title_structure_extractor(title=title)
   assert res[CSV_TITLE_CHAR_COUNT] == 0       # No non-whitespace chars
   assert res[CSV_TITLE_WORD_COUNT] == 0       # split() removes empty strings
   assert res[CSV_TITLE_AVG_WORD_LENGTH] == 0  # Division by zero case
   assert res[CSV_TITLE_CASE_RATIO] == 0       # No letters
   assert res[CSV_TITLE_ALL_CAP_WORD_COUNT] == 0
   assert res[CSV_TITLE_HAS_NUMBERS] == False
   assert res[CSV_TITLE_HAS_YEAR] == False
   assert res[CSV_TITLE_HAS_QUESTION_MARK] == False
   assert res[CSV_TITLE_ENDS_WITH_PUNC] == False
   
   # Test Case 3: Only Numbers/Punctuation
   title = "123 !@# 456 ???"
   res = title_structure_extractor(title=title)
   assert res[CSV_TITLE_CHAR_COUNT] == 12      # Numbers and punctuation count
   assert res[CSV_TITLE_WORD_COUNT] == 4       # 4 "words"
   assert res[CSV_TITLE_AVG_WORD_LENGTH] == 3  # Average length
   assert res[CSV_TITLE_CASE_RATIO] == 0       # No letters = division by zero
   assert res[CSV_TITLE_ALL_CAP_WORD_COUNT] == 0  # No actual letter words
   assert res[CSV_TITLE_HAS_NUMBERS] == True
   assert res[CSV_TITLE_HAS_YEAR] == False
   assert res[CSV_TITLE_HAS_QUESTION_MARK] == True
   assert res[CSV_TITLE_ENDS_WITH_PUNC] == True