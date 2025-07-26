# Basic Post Features
CSV_TITLE = "title"
CSV_URL = "url"
CSV_SCORE = "score"
CSV_AUTHOR = "author"
CSV_NUM_COMM = "number_of_comments"
CSV_PAGE_NUM = "page_number"
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

CSV_FIELDS = {
    # === CURRENTLY IMPLEMENTED ===
    # Basic Post Features
    CSV_TITLE: CSV_TITLE,
    CSV_URL: CSV_URL,
    CSV_SCORE: CSV_SCORE,
    CSV_AUTHOR: CSV_AUTHOR,
    CSV_NUM_COMM: CSV_NUM_COMM,
    CSV_PAGE_NUM: CSV_PAGE_NUM,
    CSV_AGE: CSV_AGE,
    CSV_TIMESTAMP: CSV_TIMESTAMP,
    
    # === TODO: IMPLEMENT NEXT ===
    # Author Features
    # 'author_karma': 'author_karma',
    # 'account_age': 'account_age', 
    # 'recent_posting_frequency': 'recent_posting_frequency',
    # 'average_post_performance': 'average_post_performance',
    
    # === TODO: IMPLEMENT LATER ===
    # Temporal Features
    # 'hour_of_day': 'hour_of_day',
    # 'day_of_week': 'day_of_week',
    # 'posted_during_weekend': 'posted_during_weekend',
    # 'posted_during_holiday': 'posted_during_holiday',
    
    # Domain Features
    # 'domain_name': 'domain_name',
    # 'domain_reputation_score': 'domain_reputation_score',
    # 'is_self_post': 'is_self_post',
    # 'is_github_link': 'is_github_link',
    # 'is_accessible': 'is_accessible',
    
    # Title Structural Features
    CSV_TITLE_CHAR_COUNT : CSV_TITLE_CHAR_COUNT,
    CSV_TITLE_WORD_COUNT : CSV_TITLE_WORD_COUNT,
    CSV_TITLE_AVG_WORD_LENGTH : CSV_TITLE_AVG_WORD_LENGTH,
    CSV_TITLE_CASE_RATIO : CSV_TITLE_CASE_RATIO,
    CSV_TITLE_ALL_CAP_WORD_COUNT : CSV_TITLE_ALL_CAP_WORD_COUNT,
    CSV_TITLE_HAS_NUMBERS : CSV_TITLE_HAS_NUMBERS,
    CSV_TITLE_HAS_YEAR : CSV_TITLE_HAS_YEAR,
    CSV_TITLE_HAS_QUESTION_MARK : CSV_TITLE_HAS_QUESTION_MARK,
    CSV_TITLE_ENDS_WITH_PUNC : CSV_TITLE_ENDS_WITH_PUNC,
    
    # Title Semantic Features
    CSV_TITLE_KEYWORD_COUNT : CSV_TITLE_KEYWORD_COUNT,
    CSV_TITLE_PROGRAMMING_LANGUAGES_COUNT : CSV_TITLE_PROGRAMMING_LANGUAGES_COUNT,
    CSV_TITLE_AI_TERMS_COUNT : CSV_TITLE_AI_TERMS_COUNT,
    CSV_TITLE_CLOUD_TERMS_COUNT : CSV_TITLE_CLOUD_TERMS_COUNT,
    CSV_TITLE_BUSINESS_TERMS_COUNT : CSV_TITLE_BUSINESS_TERMS_COUNT,
    CSV_TITLE_COMPANY_NAMES_MENTIONS : CSV_TITLE_COMPANY_NAMES_MENTIONS,
    CSV_TITLE_VERSION_NUMBERS_PRESENT : CSV_TITLE_VERSION_NUMBERS_PRESENT,
    CSV_TITLE_FUNDING_MENTIONS : CSV_TITLE_FUNDING_MENTIONS
    
    # Title Patterns Features
    # 'title_is_show_hn': 'title_is_show_hn',
    # 'title_is_ask_hn': 'title_is_ask_hn',
    # 'title_is_tell_hn': 'title_is_tell_hn',
    # 'title_contains_hiring': 'title_contains_hiring',
    # 'title_contains_release': 'title_contains_release',
    # 'title_contains_acquisition': 'title_contains_acquisition',
    
    # Title Engagement Features
    # 'title_question_word_count': 'title_question_word_count',  # how, why, what
    # 'title_action_word_count': 'title_action_word_count',  # build, create
    # 'title_emotional_word_count': 'title_emotional_word_count',  # amazing, terrible
    # 'title_superlative_word_count': 'title_superlative_word_count',  # best, worst
    # 'title_starts_with_how': 'title_starts_with_how',
    # 'title_starts_with_why': 'title_starts_with_why',
    # 'title_contains_versus': 'title_contains_versus',
    # 'title_engagement_word_total_count': 'title_engagement_word_total_count',
    
    # Content Type Features
    # 'post_type': 'post_type',  # Show/Ask/Job/Regular
    # 'topic_category': 'topic_category',  # if applicable, otherwise Generic
    # 'is_controversial': 'is_controversial',  # contains controversial keywords
    
    # Velocity Features (for posts aged > 1 hour)
    # 'points_per_hour': 'points_per_hour',
    # 'comments_per_hour': 'comments_per_hour',
    # 'points_velocity_trend': 'points_velocity_trend',  # increasing/decreasing
    # 'comments_velocity_trend': 'comments_velocity_trend',
    
    # Title Embeddings
    # 'title_emb_0': 'title_emb_0',
    # 'title_emb_1': 'title_emb_1',
    # 'title_emb_2': 'title_emb_2',
    # 'title_emb_3': 'title_emb_3',
    # 'title_emb_4': 'title_emb_4',
    # 'title_emb_5': 'title_emb_5',
    # 'title_emb_6': 'title_emb_6',
    # 'title_emb_7': 'title_emb_7',
    # 'title_emb_8': 'title_emb_8',
    # 'title_emb_9': 'title_emb_9',
    
    # Calculated Scores
    # 'title_trending_score': 'title_trending_score',
    # 'domain_authority_score': 'domain_authority_score',
    # 'author_influence_score': 'author_influence_score',
    # 'optimal_timing_score': 'optimal_timing_score',
}

# Helper functions
def get_active_fields():
    """Return list of currently implemented CSV field names."""
    return list(CSV_FIELDS.values())

def get_active_field_count():
    """Return count of currently implemented fields."""
    return len(CSV_FIELDS)