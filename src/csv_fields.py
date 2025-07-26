from .constants import (
    CSV_TITLE, CSV_URL, CSV_SCORE, CSV_AUTHOR, CSV_NUM_COMM, 
    CSV_PAGE_NUM, CSV_AGE, CSV_TIMESTAMP
    # CSV_AUTH_KARMA, CSV_AUTH_ACCOUNT_AGE, etc. - add as implemented
)

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
    # 'title_char_count': 'title_char_count',
    # 'title_word_count': 'title_word_count',
    # 'title_avg_word_length': 'title_avg_word_length',
    # 'title_case_ratio': 'title_case_ratio',
    # 'title_all_cap_word_count': 'title_all_cap_word_count',
    # 'title_has_numbers': 'title_has_numbers',
    # 'title_has_year': 'title_has_year',
    # 'title_has_question_mark': 'title_has_question_mark',
    # 'title_ends_with_punctuation': 'title_ends_with_punctuation',
    
    # Title Semantic Features
    # 'title_keyword_count': 'title_keyword_count',
    # 'title_language_count': 'title_language_count',
    # 'title_ai_terms_count': 'title_ai_terms_count',
    # 'title_cloud_terms_count': 'title_cloud_terms_count',
    # 'title_business_terms_count': 'title_business_terms_count',
    # 'title_company_name_mentions': 'title_company_name_mentions',
    # 'title_version_numbers_mentioned': 'title_version_numbers_mentioned',
    # 'title_funding_mentions': 'title_funding_mentions',
    
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

# Usage:
# from csv_fields import CSV_FIELDS
# from constants import CSV_TITLE
# 
# # Either approach works:
# df[CSV_FIELDS[CSV_TITLE]] = title_data  # Using dict lookup
# df[CSV_TITLE] = title_data              # Using constant directly