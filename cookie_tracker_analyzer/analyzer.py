# analyzer.py

import pandas as pd
import re
from datetime import datetime, timedelta

TRACKING_DOMAINS = {
    "doubleclick.net",
    "google-analytics.com",
    "facebook.com",
    "adservice.google.com"
}

def analyze_cookies(df):
    df['is_third_party'] = df['domain'].apply(lambda d: any(t in d for t in TRACKING_DOMAINS))
    df['is_long_expiry'] = df['expires'].apply(lambda e: (e > (datetime.now().timestamp() + timedelta(days=365).total_seconds())) if isinstance(e, (int, float)) else False)

    df['risk_level'] = 'Low'
    df.loc[df['is_third_party'] | df['is_long_expiry'], 'risk_level'] = 'Medium'
    df.loc[(df['secure'] == False) | (df['httpOnly'] == False), 'risk_level'] = 'High'

    return df