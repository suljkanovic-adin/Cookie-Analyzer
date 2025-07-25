# reporter.py

import pandas as pd
from jinja2 import Template

REPORT_TEMPLATE = """
<html>
<head><title>Cookie Analysis Report</title></head>
<body>
<h1>Cookie Analysis Report</h1>
<p>Total Cookies: {{ total }}</p>
<p>Risky Cookies: {{ risky }}</p>
<h2>Risky Cookies</h2>
<table border="1">
<tr><th>Domain</th><th>Name</th><th>Risk Level</th></tr>
{% for _, row in risky_cookies.iterrows() %}
<tr>
    <td>{{ row['domain'] }}</td>
    <td>{{ row['name'] }}</td>
    <td>{{ row['risk_level'] }}</td>
</tr>
{% endfor %}
</table>
</body>
</html>
"""

def generate_report(df):
    total = len(df)
    risky = len(df[df['risk_level'] != 'Low'])
    risky_cookies = df[df['risk_level'] != 'Low'][['domain', 'name', 'risk_level']]

    template = Template(REPORT_TEMPLATE)
    html_report = template.render(
        total=total,
        risky=risky,
        risky_cookies=risky_cookies
    )

    with open("cookie_report.html", "w") as f:
        f.write(html_report)

    print("[+] Report saved to cookie_report.html")