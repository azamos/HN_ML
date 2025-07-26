# Hackernews specific attributes
SOURCE_URL = "https://news.ycombinator.com/?p="
TR_CLASS_NAME = "athing submission"
TITLE_A_CLASS_NAME = "titleline"
USER_CLASS_NAME = "hnuser"
DISCUSS = "discuss"
SCORE_PREFIX = "score_"

# Iteration constants
LIST_START = 0
START = 1
EOF_MOCK = 21 # Locally downloaded 20 pages
LAST_INDEX = -1

# HTML fields and elements
HREF="href"
TR="tr"
ID="id"
SPAN="span"
A="a"
COMMENTS_SPLITTER = "\xa0"
HTML_TEXT_POINTS = "points"

# Initial field names
TITLE = "Title"
URL = "URL"
POINTS = "Points"
AUTHOR = "Author"
NUMBER_OF_COMMENTS = "Number of comments"
PAGE_NUMBER = "Page number"
AGE = "Age"
UNIX_TIMESTAMP = "Unix timstamp"

# Basic Post Features
CSV_TITLE = "title"
CSV_URL = "url"
CSV_SCORE = "score"
CSV_AUTHOR = "author"
CSV_NUM_COMM = "number_of_comments"
CSV_P_NUM = "page_number"
CSV_AGE = "age"
CSV_TIMESTAMP = "timestamp"

# Author Features
CSV_AUTH_KARMA = "author_karma"
CSV_AUTH_ACCOUNT_AGE = "account_age"
CSV_AUTH_RECENT_FREQ = "recent_posting_frequency"
CSV_AUTH_AVG_POST_PERF = "average_post_performance"

# Temporal Features
CSV_HOUR_OF_DAY = "hour_of_day"
CSV_DAY_OF_WEEK = "day_of_week"
CSV_IS_WEEKEND = "posted_during_weekend"
CSV_IS_HOLIDAY = "posted_during_holiday"

# Domain Features
CSV_DOMAIN_NAME = "domain_name"
CSV_DOMAIN_REP_SCORE = "domain_reputation_score"
CSV_IS_SELF_POST = "is_self_post"
CSV_IS_GITHUB_LINK = "is_github_link"
CSV_IS_ACCESSIBLE = "is_accessible"

# Title Structural Features
CSV_TITLE_CHAR_COUNT = "title_char_count"
CSV_TITLE_WORD_COUNT = "title_word_count"
CSV_TITLE_AVG_WORD_LENGTH = "title_avg_word_length"
CSV_TITLE_CASE_RATIO = "title_case_ratio"
CSV_TITLE_ALL_CAP_WORD_COUNT = "title_all_cap_word_count"
CSV_TITLE_HAS_NUMBERS = "title_has_numbers"
CSV_TITLE_HAS_YEAR = "title_has_year"
CSV_TITLE_HAS_QUESTION_MARK = "title_has_question_mark"
CSV_TITLE_ENDS_WITH_PUNC = "title_ends_with_punctuation"

# Title Semantic Features
CSV_TITLE_KEYWORD_COUNT = "title_keyword_count"
CSV_TITLE_PROGRAMMING_LANGUAGES_COUNT = "title_language_count"
CSV_TITLE_AI_TERMS_COUNT = "title_ai_terms_count"
CSV_TITLE_CLOUD_TERMS_COUNT = "title_cloud_terms_count"
CSV_TITLE_BUSINESS_TERMS_COUNT = "title_business_terms_count"
CSV_TITLE_COMPANY_NAMES_MENTIONS = "title_company_name_mentions"
CSV_TITLE_VERSION_NUMBERS_PRESENT = "title_version_numbers_mentioned"
CSV_TITLE_FUNDING_MENTIONS = "title_funding_mentions"

# Title Patterns Features
CSV_TITLE_IS_SHOW_HN = "title_is_show_hn"
CSV_TITLE_IS_ASK_HN = "title_is_ask_hn"
CSV_TITLE_IS_TELL_HN = "title_is_tell_hn"
CSV_TITLE_CONTAINS_HIRING = "title_contains_hiring"
CSV_TITLE_CONTAINS_RELEASE = "title_contains_release"
CSV_TITLE_CONTAINS_ACQUISITION = "title_contains_acquisition"

# Title Engagement Features
CSV_TITLE_Q_WORD_COUNT = "title_question_word_count"#how,why,what
CSV_TITLE_ACTION_WORD_COUNT = "title_action_word_count"#build,create
CSV_TITLE_EMOTIONAL_WORD_COUNT = "title_emotional_word_count"#amazing,terrible
CSV_TITLE_SUPERLATIVE_WORD_COUNT = "title_superlative_word_count"#best,worst
CSV_TITLE_STARTS_WITH_HOW = "title_starts_with_how"
CSV_TITLE_STARTS_WITH_WHY = "title_starts_with_why"
CSV_TITLE_CONTAINS_VERSUS = "title_contains_versus"
CSV_TITLE_ENGAGEMENT_WORD_TOTAL_COUNT = "title_engagement_word_total_count"

# Content type features
CSV_POST_TYPE = "post_type" #(Show/Ask/Job/Regular)
CSV_TOPIC_CATEGORY = "topic_category" # if applicable. O.W Generic?
CSV_IS_CONTROVERSIAL = "is_controversial"# Conatains controversial keywords

# Velocity features (for posts aged > 1 hour)
CSV_POINTS_PER_HOUR = "points_per_hour"
CSV_COMMENTS_PER_HOUR = "comments_per_hour"
CSV_POINTS_VELOCITY_TREND = "points_velocity_trend" # increasing/decreasing
CSV_COMMENTS_VELOCITY_TREND = "comments_velocity_trend"

# Title embeddings
CSV_TITLE_EMB_0 = "title_emb_0"
CSV_TITLE_EMB_1 = "title_emb_1"
CSV_TITLE_EMB_2 = "title_emb_2"
CSV_TITLE_EMB_3 = "title_emb_3"
CSV_TITLE_EMB_4 = "title_emb_4"
CSV_TITLE_EMB_5 = "title_emb_5"
CSV_TITLE_EMB_6 = "title_emb_6"
CSV_TITLE_EMB_7 = "title_emb_7"
CSV_TITLE_EMB_8 = "title_emb_8"
CSV_TITLE_EMB_9 = "title_emb_9"

# Calculated scores
CSV_TITLE_TRENDING_SCORE = "title_trending_score"
CSV_DOMAIN_AUTHORITY_SCORE = "domain_authority_score"
CSV_AUTHOR_INFLUENCE_SCORE = "author_influence_score"
CSV_OPTIMAL_TIMING_SCORE = "optimal_timing_score"

# Defailt field values
ZERO_VALUE = 0
EMPTY_STR = ""

# Default values for program arguments
DEFAULT_NUM_POST = 50
DEAULT_MIN_SCORE = 0
DEFAULT_MAX_SCORE = 1000000
DEFAULT_SKIP_PAGES_STR = ""

# Relative paths, files and extentions
STATIC_FILE_PATH = "./tests/data/hackernews"
OUTPUT_FILE_PATH = "./output/result.csv"
HTM_SUFFIX = ".htm"
HTML_SUFFIX = ".html"

# Messages for the -h and --help flags
HELP_NUM_POST = "Maximum numbers of posts to scrape"
HELP_MIN_SCORE = "Minimal score(for filtering). Must be >= 0"
HELP_MAX_SCORE = "Maximal score(for filtering). Must be >= max(0, min_score)"
HELP_SKIP_PAGES = "Specify a list of pages to skip, in the format --pages = int,int,int,..."
HELP_DEBUG = "Allows debug mode printing"
HELP_OFFLINE = "Uses locally stored html pages instead of fetching from the actual site"

# User messages
MSG_SCRAPING = "Scraping"
MSG_WRITING_TO_CSV = "Writing data to csv..."
MSG_DONE = "Done."

# Error messages
ERR_NUM_POST_VALUE = "num_post must be >= 0 "
ERR_NON_POSITIVE_VALUE = "scores must be at least 0"
ERR_MIN_MAX_VALUE = "min_score must be <= max_score"
ERR_LIST_FORMAT = "list must be in the format of int,int,..."
ERR_LIST_MISSING_NUMBER = "Empty string where number should be"
ERR_CONVERT_TO_INT = "invalid literal for int"
ERR_MISSING_FIELDS = "dict contains fields not in fieldnames"

# Encoding and Writing Modes
UTF_8 = "utf-8"
READ_MODE = "r"
WRITE_MODE = "w"
CSV_NEWLINE = ''

# Characters
COMMA = ","
DASH = "-"

# Symbolic Numbers and Strings
NOT_FOUND = -1

# Other magic numbers and strings
STORE_TRUE = "store_true"
HTML_PARSER = "html.parser"
LXML_PARSER = "lxml"
LENGTH_RANGE_STR = 2
BOTTOM_INDEX = 0
TOP_INDEX = 1
OP_IS_SUCCESSUL = 'op_is_successful'
RESULT_KEY = "result"
POSTS_PER_PAGE = 30
ONE = 1
DEFAULT_TIMEOUT = 5
MAX_SAFES_POSTS = 900