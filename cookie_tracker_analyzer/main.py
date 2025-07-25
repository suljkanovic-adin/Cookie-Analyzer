# main.py

from extractor import extract_cookies
from analyzer import analyze_cookies
from visualize import visualize_data
from reporter import generate_report

def main():
    print("[*] Extracting cookies...")
    cookies_df = extract_cookies()

    print("[*] Analyzing cookies...")
    analyzed_df = analyze_cookies(cookies_df)

    print("[*] Visualizing data...")
    visualize_data(analyzed_df)

    print("[*] Generating report...")
    generate_report(analyzed_df)

if __name__ == "__main__":
    main()