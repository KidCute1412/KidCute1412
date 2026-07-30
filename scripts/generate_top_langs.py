import urllib.request
import json
import os
import datetime

# Obtain token from environment or fallback to .env token
token = os.environ.get("GITHUB_TOKEN") or os.environ.get("PERSONAL_ACCESS_TOKEN") or os.environ.get("commits_statistics_token")
if not token and os.path.exists(".env"):
    with open(".env", "r") as f:
        for line in f:
            if line.startswith("commits_statistics_token="):
                token = line.strip().split("=", 1)[1]
            elif line.startswith("PERSONAL_ACCESS_TOKEN="):
                token = line.strip().split("=", 1)[1]

username = "KidCute1412"

query_years = """
query($username: String!) {
  user(login: $username) {
    contributionsCollection {
      contributionYears
    }
  }
}
"""

def graphql_query(query, variables=None):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": variables or {}}).encode('utf-8')
    )
    req.add_header("Content-Type", "application/json")
    req.add_header("User-Agent", "Python-Script")
    if token:
        req.add_header("Authorization", f"token {token}")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

data_years = graphql_query(query_years, {"username": username})
years = data_years['data']['user']['contributionsCollection']['contributionYears']

lang_commits = {}
lang_colors = {}

query_year_contribs = """
query($username: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $username) {
    contributionsCollection(from: $from, to: $to) {
      commitContributionsByRepository(maxRepositories: 100) {
        repository {
          nameWithOwner
          languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
            edges {
              size
              node {
                name
                color
              }
            }
          }
        }
        contributions {
          totalCount
        }
      }
    }
  }
}
"""

for yr in sorted(years):
    from_date = f"{yr}-01-01T00:00:00Z"
    to_date = f"{yr}-12-31T23:59:59Z"
    res = graphql_query(query_year_contribs, {"username": username, "from": from_date, "to": to_date})
    contribs = res['data']['user']['contributionsCollection']['commitContributionsByRepository']
    
    for c in contribs:
        repo = c['repository']
        commits = c['contributions']['totalCount']
        edges = repo['languages']['edges']
        if not edges:
            continue
        total_size = sum(e['size'] for e in edges)
        if total_size == 0:
            continue
            
        for edge in edges:
            l_name = edge['node']['name']
            l_color = edge['node']['color'] or "#858585"
            l_size = edge['size']
            weight = (l_size / total_size) * commits
            lang_commits[l_name] = lang_commits.get(l_name, 0.0) + weight
            lang_colors[l_name] = l_color

# Sort languages by weighted commit count
sorted_langs = sorted(lang_commits.items(), key=lambda x: x[1], reverse=True)
total_weighted_commits = sum(v for k, v in sorted_langs)

# Top 8 languages
top_langs = sorted_langs[:8]

def build_svg(top_langs, total_commits, lang_colors):
    width = 350
    item_height = 24
    header_height = 55
    padding_bottom = 20
    height = header_height + len(top_langs) * item_height + padding_bottom

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">')
    svg.append('<style>')
    svg.append("  .bg { fill: #06080c; stroke: #ff007b; stroke-width: 1px; rx: 6px; }")
    svg.append("  .title { font-family: 'Segoe UI', Ubuntu, 'Fira Code', sans-serif; font-size: 16px; font-weight: 700; fill: #00F0FF; }")
    svg.append("  .lang-label { font-family: 'Segoe UI', Ubuntu, sans-serif; font-size: 12px; font-weight: 600; fill: #e2e8f0; }")
    svg.append("  .lang-stat { font-family: 'Segoe UI', Ubuntu, monospace; font-size: 11px; fill: #94a3b8; }")
    svg.append("  .bar-bg { fill: #1e293b; rx: 3px; }")
    svg.append("  .bar-fill { rx: 3px; }")
    svg.append('</style>')

    # Background card
    svg.append(f'<rect x="1" y="1" width="{width-2}" height="{height-2}" class="bg" />')
    
    # Title
    svg.append(f'<text x="20" y="35" class="title">Top Languages by Commit</text>')

    # Language list & progress bars
    y = header_height
    for name, weight in top_langs:
        pct = (weight / total_commits) * 100 if total_commits > 0 else 0
        commits_num = int(round(weight))
        color = lang_colors.get(name, "#858585")
        
        # Color dot / square
        svg.append(f'<rect x="20" y="{y-10}" width="10" height="10" rx="2" fill="{color}" />')
        # Language name
        svg.append(f'<text x="36" y="{y}" class="lang-label">{name}</text>')
        
        # Metric text (percentage + weighted commits)
        stat_str = f"{pct:.1f}% ({commits_num} commits)"
        svg.append(f'<text x="{width-20}" y="{y}" class="lang-stat" text-anchor="end">{stat_str}</text>')
        
        # Progress Bar
        bar_y = y + 4
        bar_max_width = width - 40
        bar_width = max(3, int((pct / 100) * bar_max_width))
        
        svg.append(f'<rect x="20" y="{bar_y}" width="{bar_max_width}" height="4" class="bar-bg" />')
        svg.append(f'<rect x="20" y="{bar_y}" width="{bar_width}" height="4" fill="{color}" class="bar-fill" />')
        
        y += item_height

    svg.append('</svg>')
    return '\n'.join(svg)

svg_content = build_svg(top_langs, total_weighted_commits, lang_colors)

# Write to profile-summary-card-output and repo root
output_paths = [
    "profile-summary-card-output/tokyonight/2-most-commit-language.svg",
    "top-languages-commits.svg"
]

for path in output_paths:
    dirname = os.path.dirname(path)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated {path} successfully!")
