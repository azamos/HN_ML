import argparse
import pytest
from src.main import run_scraper
from src.utils import build_skip_pages
from src.constants import (
    EMPTY_STR,CSV_TITLE,CSV_URL,CSV_SCORE,CSV_AUTHOR,CSV_NUM_COMM,
    CSV_PAGE_NUM,CSV_AGE,CSV_TIMESTAMP,
    )
def test_run_scraper_valid():
    expected_keys = {
        CSV_TITLE,CSV_URL,CSV_SCORE,CSV_AUTHOR,CSV_NUM_COMM,
        CSV_PAGE_NUM,CSV_AGE,CSV_TIMESTAMP,
        }
    args1 = argparse.Namespace(
        num_post = 50,
        min_score = 15,
        max_score = 10000,
        list_string ="",
        offline = True,
        debug = True
    )
    extracted_data1 = run_scraper(args1, skip_pages=build_skip_pages(args1.list_string))
    assert len(extracted_data1) > 0
    assert len(extracted_data1) <= args1.num_post
    
    for post_data in extracted_data1:
        assert expected_keys.issubset(post_data.keys())
        assert isinstance(post_data[CSV_TITLE],str)
        assert isinstance(post_data[CSV_URL],str)
        assert isinstance(post_data[CSV_AUTHOR],str)
        if post_data[CSV_SCORE] != EMPTY_STR:
            assert isinstance(post_data[CSV_SCORE],int) and post_data[CSV_SCORE]>=0
        assert isinstance(post_data[CSV_NUM_COMM],int) and post_data[CSV_NUM_COMM]>=0
        assert isinstance(post_data[CSV_PAGE_NUM],int) and post_data[CSV_PAGE_NUM]>=1

def test_run_scraper_invalid():
    args = argparse.Namespace(
        num_post=None,
        min_score=15,
        max_score=10000,
        list_string="",
        offline=True
    )
    
    with pytest.raises(SystemExit) as excinfo:
        run_scraper(args, skip_pages=[])
    
    assert excinfo.value.code == 1
