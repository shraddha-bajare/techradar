import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path

# needs to be changed overall in the website
quality_attributes = ["languages-and-frameworks", "methods-and-patterns", "platforms-and-operations", "tools"]
software_tier = ["analysis code", "prototype tools", "research infrastructure software"]
accessibility = ["CI/CD", "command-line", "online-services", "free", "paid", "license"]

def df2md(row):
    quadrant = np.random.choice(quality_attributes)
    ring = np.random.choice(software_tier)
    tags = np.random.choice(accessibility)
    return f"""---

title: "{row['Name']}"
ring: {ring}
quadrant: {quadrant}
tags: {tags}
---
{row['URL']}
{row['Description']}
"""

# the collection of tools must be downloaded from our owncloud
df = pd.read_csv('collected_tools.csv', on_bad_lines='warn')

outdir = Path(f'{datetime.today().strftime("%Y-%m-%d")}')
outdir.mkdir(parents=True, exist_ok=True)

for ii, row in list(df.iterrows())[2:]:
    markdown = df2md(row)
    slug = row["Name"].lower().replace(" ", "-")
    print(markdown)
    with open(f'{outdir}/{slug}.md', 'w') as f:
        f.write(markdown)
    print(f'Wrote {row["Name"]}.md')