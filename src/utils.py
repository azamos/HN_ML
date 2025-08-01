import time
from .constants import (
    HELP_OFFLINE,ERR_LIST_FORMAT,DEFAULT_NUM_POST,
    HELP_NUM_POST,DEAULT_MIN_SCORE,HELP_MIN_SCORE,DEFAULT_MAX_SCORE,HELP_MAX_SCORE,
    DEFAULT_SKIP_PAGES_STR,HELP_SKIP_PAGES,STORE_TRUE,HELP_DEBUG,COMMA,DASH,NOT_FOUND,
    ERR_LIST_MISSING_NUMBER,LENGTH_RANGE_STR,BOTTOM_INDEX,TOP_INDEX
    )
import argparse

def dbgprint(msg,debug_mode = False):
    if(debug_mode):
        print(f"[DEBUG] {msg}")

def errprint(msg):
    print(f"[ERROR] {msg}")

def calculate_elapsed_minutes(time_str):
    stamped = int(time_str)
    curr_time = int(time.time())
    elapsed_seconds = curr_time - stamped
    return elapsed_seconds/60

def build_skip_pages(list_string):
    skip_set = set()
    if not list_string.split():
        return skip_set
    
    splitted = list_string.split(COMMA)
    for raw_str in splitted:
        str = raw_str.strip()
        if not str:
            raise ValueError(ERR_LIST_MISSING_NUMBER)
        if str.find(DASH)==NOT_FOUND:
            skip_set.add(int(str))# if not valid int, will raise its default ValueError
        else:
            further_split = str.split(DASH)
            if len(further_split) != LENGTH_RANGE_STR:
                raise ValueError(ERR_LIST_FORMAT)
            range_bottom = int(further_split[BOTTOM_INDEX].strip())
            range_top = int(further_split[TOP_INDEX].strip())
            if range_bottom > range_top:
                temp = range_top
                range_top = range_bottom
                range_bottom = temp
            skip_set.update([i for i in range(range_bottom,range_top+1)])
    return skip_set

def validate_args(args,debug_mode = False):
    num_post = args.num_post
    min_score = args.min_score
    max_score = args.max_score
    list_string = args.list_string
    if num_post < 0:
        return False
    if(min_score < 0 or min_score <0):
        return False
    if(min_score>max_score):
        return False
    pages = None
    try:
        pages = build_skip_pages(list_string)
        dbgprint(pages,debug_mode)
    except ValueError as v_e:
        errprint(v_e)
        return False
    return True
    

def parse_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_post",type=int,default=DEFAULT_NUM_POST,help=HELP_NUM_POST)
    parser.add_argument("--min_score",type=int,default=DEAULT_MIN_SCORE,help=HELP_MIN_SCORE)
    parser.add_argument("--max_score",type=int,default=DEFAULT_MAX_SCORE,help=HELP_MAX_SCORE)
    parser.add_argument("--list_string",type=str,default=DEFAULT_SKIP_PAGES_STR,help=HELP_SKIP_PAGES)
    parser.add_argument("--offline",action=STORE_TRUE,help=HELP_OFFLINE)
    parser.add_argument("--debug",action=STORE_TRUE,help=HELP_DEBUG)
    return parser.parse_args(args)