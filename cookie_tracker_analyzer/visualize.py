# visualize.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def visualize_data(df):
    plt.figure(figsize=(10, 6))

    # Risk level bar chart
    risk_counts = df['risk_level'].value_counts()
    sns.barplot(x=risk_counts.index, y=risk_counts.values)
    plt.title("Cookie Risk Levels")
    plt.ylabel("Count")
    plt.savefig("risk_levels.png")
    plt.close()

    # Domain distribution
    top_domains = df['domain'].value_counts().head(10)
    plt.figure(figsize=(10,6))
    sns.barplot(x=top_domains.values, y=top_domains.index)
    plt.title("Top 10 Cookie Domains")
    plt.xlabel("Number of Cookies")
    plt.savefig("top_domains.png")
    plt.close()