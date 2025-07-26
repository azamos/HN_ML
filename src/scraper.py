import requests
from bs4 import BeautifulSoup
import csv
import os
from .constants import (
    UTF_8,HTML_PARSER,TR_CLASS_NAME,TR,TR_CLASS_NAME,ID,SPAN,READ_MODE,
    TITLE_A_CLASS_NAME,A,HREF,EMPTY_STR,USER_CLASS_NAME,LAST_INDEX,COMMENTS_SPLITTER,
    DISCUSS,OUTPUT_FILE_PATH,
    WRITE_MODE,CSV_NEWLINE,LIST_START,ZERO_VALUE,HTML_TEXT_POINTS,SCORE_PREFIX,DEFAULT_TIMEOUT,
    CSV_TITLE,CSV_URL,CSV_SCORE,CSV_AUTHOR,CSV_NUM_COMM,
    CSV_PAGE_NUM,CSV_AGE,CSV_TIMESTAMP,
    )
from .csv_fields import get_active_fields
from .utils import dbgprint, errprint, calculate_elapsed_minutes

def fetch_page(url):
    try:
        response = requests.get(url,timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        errprint(e)
        return None


# Used during development. Will be used when using --offline
def local_parser(file_path):
    dbgprint(f"Parsing for: {file_path}")
    with open(file_path,READ_MODE,encoding=UTF_8) as f:
        html = f.read()
    return parser(html)

def parser(html):
    return BeautifulSoup(html,HTML_PARSER)

def filter_posts(unfiltered_data,min_score,max_score):
    return [data_entry for data_entry in unfiltered_data if data_entry[CSV_SCORE]!=EMPTY_STR and min_score <= data_entry[CSV_SCORE] <= max_score]

def extract_from_soup(soup,p_num):
    extracted_data = []
    for tr in soup.find_all(TR, class_ = TR_CLASS_NAME):
        id = tr[ID]
        title_td = tr.find(SPAN,class_ = TITLE_A_CLASS_NAME)
        title_a = title_td.find(A)
        title = title_a.get_text()
        url = title_a[HREF]

        ages = soup.find_all(A, href = "item?id=" + id)
        if not ages:
            raise ValueError("Can't extract elapsed time...")
        age = ages[0]
        if len(ages) > 2:
            dbgprint(f"ages.len =  {len(ages)}: {ages}",True)
            age=ages[1]
        elapsed_time_approximate = age.get_text()
        age_parent = age.parent
        whole_date = age_parent.get("title")
        if whole_date is None:
            dbgprint(f"whole_date is None: {age}",True)
        unix_timestamp = whole_date.split(" ")[1]
        dbgprint(f"unix timestamp: {unix_timestamp}",True)
        elapsed_time = calculate_elapsed_minutes(unix_timestamp)
        dbgprint(f"elapsed time: {elapsed_time}",True)

        score_sp = soup.find(SPAN,id = SCORE_PREFIX+id)
        score = EMPTY_STR
        num_comments = ZERO_VALUE
        author_name = EMPTY_STR

        if score_sp:# When score is missing, so is author and number of comments.
            score = int(score_sp.get_text().split(HTML_TEXT_POINTS)[LIST_START].strip())
            score_parent = score_sp.parent
            user_a = score_parent.find(A,class_ = USER_CLASS_NAME)
            author_name = user_a.get_text()
            comments_str = score_parent.find_all(A)[LAST_INDEX].get_text()
            try:
                num_comments_str = comments_str.split(COMMENTS_SPLITTER)[LIST_START]
                num_comments = ZERO_VALUE if(num_comments_str == DISCUSS) else int(num_comments_str)
            except Exception as e:
                errprint(e)
            

        extracted_data.append(
            {
            CSV_TITLE:title,
            CSV_URL: url,
            CSV_AUTHOR: author_name,
            CSV_SCORE: score,
            CSV_NUM_COMM: num_comments,
            CSV_PAGE_NUM: p_num,
            CSV_AGE: elapsed_time,
            CSV_TIMESTAMP: unix_timestamp
            })
    return extracted_data

def save_to_csv(posts_list):
    os.makedirs(os.path.dirname(OUTPUT_FILE_PATH),exist_ok=True)
    fields = get_active_fields()

    with open(OUTPUT_FILE_PATH,WRITE_MODE,newline=CSV_NEWLINE,encoding=UTF_8) as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=fields)
        writer.writeheader()
        for post_dict in posts_list:
            writer.writerow(post_dict)