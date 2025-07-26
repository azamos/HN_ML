from src.feature_extractors.title_feature_extractor import title_structure_extractor
from src.constants import (
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