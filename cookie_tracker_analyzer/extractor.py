# extractor.py

import browser_cookie3
import pandas as pd

def extract_cookies():
    cookies = []

    try:
        cj_chrome = browser_cookie3.chrome()
        cookies.extend(cj_chrome)
    except Exception as e:
        print(f"[!] Chrome extraction failed: {e}")

    try:
        cj_firefox = browser_cookie3.firefox()
        cookies.extend(cj_firefox)
    except Exception as e:
        print(f"[!] Firefox extraction failed: {e}")

    try:
        cj_edge = browser_cookie3.edge()
        cookies.extend(cj_edge)
    except Exception as e:
        print(f"[!] Edge extraction failed: {e}")

    cookie_list = [
        {
            "domain": c.domain,
            "name": c.name,
            "value": "MASKED",  # Mask sensitive data
            "path": c.path,
            "expires": c.expires,
            "secure": c.secure,
            "httpOnly": c.httpOnly,
            "sameSite": getattr(c, 'sameSite', None),
        }
        for c in cookies
    ]

    return pd.DataFrame(cookie_list)