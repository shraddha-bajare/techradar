import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path

# needs to be changed overall in the website
quadrants = ["languages-and-frameworks", "methods-and-patterns", "platforms-and-operations", "tools", "tools trails"]

def df2md(row):
    quadrant = np.random.choice(quadrants)
    ring = np.random.choice(["trial", "hold", "adopt"])
    tags = str(row[5]).split(",") if str(row[5])!="nan" else []
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
df = pd.read_csv('collection_of_tools.csv', sep=';')

outdir = Path(f'{datetime.today().strftime("%Y-%m-%d")}')
outdir.mkdir(parents=True, exist_ok=True)

for ii, row in list(df.iterrows())[2:]:
    markdown = df2md(row)
    slug = row["Name"].lower().replace(" ", "-")
    print(markdown)
    with open(f'{outdir}/{slug}.md', 'w') as f:
        f.write(markdown)
    print(f'Wrote {row["Name"]}.md')