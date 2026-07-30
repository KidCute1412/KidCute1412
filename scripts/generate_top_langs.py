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

# ==================== 1. GENERATE TOP LANGUAGES BY COMMIT ====================

query_years = """
query($username: String!) {
  user(login: $username) {
    contributionsCollection {
      contributionYears
    }
  }
}
"""

data_years = graphql_query(query_years, {"username": username})
years = data_years['data']['user']['contributionsCollection']['contributionYears']

lang_commits = {}
lang_colors_default = {
    "TypeScript": "#3178c6",
    "JavaScript": "#f1e05a",
    "C++": "#f34b7d",
    "HTML": "#e34c26",
    "Java": "#f59e0b",
    "Python": "#3572A5",
    "Jupyter Notebook": "#DA5B0B",
    "CSS": "#a855f7",
    "C": "#555555",
    "CMake": "#DA3434"
}
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
            l_color = edge['node']['color'] or lang_colors_default.get(l_name, "#858585")
            l_size = edge['size']
            weight = (l_size / total_size) * commits
            lang_commits[l_name] = lang_commits.get(l_name, 0.0) + weight
            lang_colors[l_name] = l_color

sorted_langs = sorted(lang_commits.items(), key=lambda x: x[1], reverse=True)
total_weighted_commits = sum(v for k, v in sorted_langs)
top_langs = sorted_langs[:8]

def build_top_langs_svg(top_langs, total_commits, lang_colors):
    width = 460
    item_height = 28
    header_height = 80
    padding_bottom = 35
    height = header_height + len(top_langs) * item_height + padding_bottom

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none">')
    svg.append('<defs>')
    svg.append('  <linearGradient id="cardBg" x1="0%" y1="0%" x2="100%" y2="100%">')
    svg.append('    <stop offset="0%" stop-color="#06080c" />')
    svg.append('    <stop offset="50%" stop-color="#0b0f19" />')
    svg.append('    <stop offset="100%" stop-color="#06080c" />')
    svg.append('  </linearGradient>')
    svg.append('  <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">')
    svg.append('    <stop offset="0%" stop-color="#00F0FF" />')
    svg.append('    <stop offset="50%" stop-color="#ff007b" />')
    svg.append('    <stop offset="100%" stop-color="#7000ff" />')
    svg.append('  </linearGradient>')
    svg.append('  <linearGradient id="barTrack" x1="0%" y1="0%" x2="100%" y2="0%">')
    svg.append('    <stop offset="0%" stop-color="#151d2a" />')
    svg.append('    <stop offset="100%" stop-color="#1e293b" />')
    svg.append('  </linearGradient>')
    svg.append('  <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">')
    svg.append('    <feGaussianBlur stdDeviation="3" result="blur" />')
    svg.append('    <feComposite in="SourceGraphic" in2="blur" operator="over" />')
    svg.append('  </filter>')
    
    for name, _ in top_langs:
        c = lang_colors.get(name, "#858585")
        safe_id = "".join([ch for ch in name if ch.isalnum()])
        svg.append(f'  <linearGradient id="grad_{safe_id}" x1="0%" y1="0%" x2="100%" y2="0%">')
        svg.append(f'    <stop offset="0%" stop-color="{c}" />')
        svg.append(f'    <stop offset="100%" stop-color="{c}" stop-opacity="0.7" />')
        svg.append(f'  </linearGradient>')

    svg.append('</defs>')
    svg.append('<style>')
    svg.append("  .bg-card { fill: url(#cardBg); stroke: url(#borderGrad); stroke-width: 1.5px; rx: 12px; }")
    svg.append("  .title-text { font-family: 'Fira Code', 'Segoe UI', monospace; font-size: 15px; font-weight: 700; fill: #00F0FF; letter-spacing: 0.05em; }")
    svg.append("  .badge-bg { fill: rgba(255, 0, 123, 0.15); stroke: #ff007b; stroke-width: 1px; rx: 10px; }")
    svg.append("  .badge-text { font-family: 'Fira Code', 'Segoe UI', monospace; font-size: 10px; font-weight: 700; fill: #ff007b; }")
    svg.append("  .lang-name { font-family: 'Segoe UI', -apple-system, sans-serif; font-size: 13px; font-weight: 600; fill: #f1f5f9; }")
    svg.append("  .lang-pct { font-family: 'Fira Code', monospace; font-size: 12px; font-weight: 700; fill: #38bdf8; }")
    svg.append("  .lang-count { font-family: 'Segoe UI', sans-serif; font-size: 11px; fill: #64748b; }")
    svg.append("  .footer-text { font-family: 'Fira Code', monospace; font-size: 10px; fill: #475569; }")
    svg.append('</style>')

    svg.append(f'<rect x="1" y="1" width="{width-2}" height="{height-2}" class="bg-card" />')
    svg.append('<g transform="translate(20, 22)">')
    svg.append('  <path d="M4 17l6-6-6-6M12 19h8" stroke="#00F0FF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />')
    svg.append('</g>')
    svg.append('<text x="48" y="36" class="title-text">TOP LANGUAGES BY COMMIT</text>')
    svg.append(f'<rect x="{width-145}" y="20" width="125" height="20" class="badge-bg" />')
    svg.append(f'<text x="{width-82}" y="34" class="badge-text" text-anchor="middle">ALL-TIME TELEMETRY</text>')

    bar_x = 20
    bar_y = 52
    total_bar_w = width - 40
    bar_h = 6

    svg.append(f'<rect x="{bar_x}" y="{bar_y}" width="{total_bar_w}" height="{bar_h}" rx="3" fill="url(#barTrack)" />')

    curr_x = bar_x
    for name, weight in top_langs:
        pct = (weight / total_commits) if total_commits > 0 else 0
        seg_w = max(2, int(pct * total_bar_w))
        c = lang_colors.get(name, "#858585")
        svg.append(f'<rect x="{curr_x}" y="{bar_y}" width="{seg_w}" height="{bar_h}" fill="{c}" />')
        curr_x += seg_w

    y = header_height + 12
    for name, weight in top_langs:
        pct = (weight / total_commits) * 100 if total_commits > 0 else 0
        commits_num = int(round(weight))
        c = lang_colors.get(name, "#858585")
        safe_id = "".join([ch for ch in name if ch.isalnum()])

        svg.append(f'<circle cx="26" cy="{y-4}" r="4.5" fill="{c}" filter="url(#glow)" />')
        svg.append(f'<text x="40" y="{y}" class="lang-name">{name}</text>')
        svg.append(f'<text x="{width-20}" y="{y}" text-anchor="end">')
        svg.append(f'  <tspan class="lang-pct">{pct:.1f}% </tspan>')
        svg.append(f'  <tspan class="lang-count">({commits_num} commits)</tspan>')
        svg.append('</text>')

        row_bar_y = y + 5
        row_bar_w = width - 40
        fill_w = max(4, int((pct / 100) * row_bar_w))

        svg.append(f'<rect x="20" y="{row_bar_y}" width="{row_bar_w}" height="4" rx="2" fill="url(#barTrack)" />')
        svg.append(f'<rect x="20" y="{row_bar_y}" width="{fill_w}" height="4" rx="2" fill="url(#grad_{safe_id})" />')

        y += item_height

    footer_y = height - 12
    svg.append(f'<circle cx="24" cy="{footer_y-3}" r="3" fill="#00ffaa" filter="url(#glow)" />')
    svg.append(f'<text x="34" y="{footer_y}" class="footer-text">Tracked across all owned, organization &amp; contributed repos</text>')
    svg.append('</svg>')
    return '\n'.join(svg)

# ==================== 2. GENERATE STREAK STATS CARD ====================

query_calendar = """
query($username: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $username) {
    contributionsCollection(from: $from, to: $to) {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            date
            contributionCount
          }
        }
      }
    }
  }
}
"""

now = datetime.datetime.now(datetime.timezone.utc)
from_date = (now - datetime.timedelta(days=365)).strftime("%Y-%m-%dT%H:%M:%SZ")
to_date = now.strftime("%Y-%m-%dT%H:%M:%SZ")

res_cal = graphql_query(query_calendar, {"username": username, "from": from_date, "to": to_date})
cal = res_cal['data']['user']['contributionsCollection']['contributionCalendar']

total_contribs = cal['totalContributions']
days = []
for w in cal['weeks']:
    for d in w['contributionDays']:
        days.append(d)

days.sort(key=lambda x: x['date'])

longest_streak = 0
temp_streak = 0
today_str = now.strftime("%Y-%m-%d")

for d in days:
    cnt = d['contributionCount']
    if cnt > 0:
        temp_streak += 1
        if temp_streak > longest_streak:
            longest_streak = temp_streak
    else:
        temp_streak = 0

curr_temp = 0
for d in reversed(days):
    d_date = d['date']
    cnt = d['contributionCount']
    if d_date > today_str:
        continue
    if cnt > 0:
        curr_temp += 1
    else:
        if d_date == today_str:
            continue
        else:
            break

current_streak = curr_temp

def build_streak_svg(total_contribs, current_streak, longest_streak):
    width = 460
    height = 195
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none">')
    svg.append('<defs>')
    svg.append('  <linearGradient id="streakBg" x1="0%" y1="0%" x2="100%" y2="100%">')
    svg.append('    <stop offset="0%" stop-color="#06080c" />')
    svg.append('    <stop offset="100%" stop-color="#0d111a" />')
    svg.append('  </linearGradient>')
    svg.append('  <linearGradient id="streakBorder" x1="0%" y1="0%" x2="100%" y2="100%">')
    svg.append('    <stop offset="0%" stop-color="#ff007b" />')
    svg.append('    <stop offset="100%" stop-color="#00F0FF" />')
    svg.append('  </linearGradient>')
    svg.append('  <filter id="neonGlow" x="-20%" y="-20%" width="140%" height="140%">')
    svg.append('    <feGaussianBlur stdDeviation="4" result="blur" />')
    svg.append('    <feComposite in="SourceGraphic" in2="blur" operator="over" />')
    svg.append('  </filter>')
    svg.append('</defs>')
    svg.append('<style>')
    svg.append("  .bg-card { fill: url(#streakBg); stroke: url(#streakBorder); stroke-width: 1.5px; rx: 12px; }")
    svg.append("  .stat-val { font-family: 'Fira Code', 'Segoe UI', monospace; font-size: 26px; font-weight: 800; fill: #00F0FF; }")
    svg.append("  .stat-label { font-family: 'Segoe UI', sans-serif; font-size: 12px; font-weight: 600; fill: #94a3b8; letter-spacing: 0.05em; }")
    svg.append("  .fire-val { fill: #ff007b; }")
    svg.append("  .divider { stroke: #1e293b; stroke-width: 1px; stroke-dasharray: 4; }")
    svg.append('</style>')

    svg.append(f'<rect x="1" y="1" width="{width-2}" height="{height-2}" class="bg-card" />')

    # 3 Columns Layout
    col_w = (width - 40) / 3
    centers = [20 + col_w * 0.5, 20 + col_w * 1.5, 20 + col_w * 2.5]

    # Col 1: Total Contributions
    svg.append(f'<g transform="translate({centers[0]}, 60)">')
    svg.append('  <path d="M-12 -25h24v4h-24zM-12 -15h24v4h-24zM-12 -5h24v4h-24z" fill="#00F0FF" opacity="0.6" />')
    svg.append(f'  <text x="0" y="30" text-anchor="middle" class="stat-val">{total_contribs}</text>')
    svg.append('  <text x="0" y="55" text-anchor="middle" class="stat-label">TOTAL COMMITS</text>')
    svg.append('  <text x="0" y="70" text-anchor="middle" style="font-family: sans-serif; font-size: 10px; fill: #475569;">Past 365 Days</text>')
    svg.append('</g>')

    # Divider 1
    svg.append(f'<line x1="{20+col_w}" y1="35" x2="{20+col_w}" y2="{height-35}" class="divider" />')

    # Col 2: Current Streak (Fire Glowing Accent)
    svg.append(f'<g transform="translate({centers[1]}, 60)">')
    svg.append('  <path d="M0 -30 C5 -20 12 -15 12 -5 C12 8 -12 8 -12 -5 C-12 -18 0 -22 0 -30 Z" fill="#ff007b" filter="url(#neonGlow)" />')
    svg.append(f'  <text x="0" y="30" text-anchor="middle" class="stat-val fire-val">{current_streak} <tspan font-size="14">days</tspan></text>')
    svg.append('  <text x="0" y="55" text-anchor="middle" class="stat-label" style="fill: #ff007b;">CURRENT STREAK</text>')
    svg.append('  <text x="0" y="70" text-anchor="middle" style="font-family: sans-serif; font-size: 10px; fill: #ff007b; opacity: 0.8;">Active Streak</text>')
    svg.append('</g>')

    # Divider 2
    svg.append(f'<line x1="{20+col_w*2}" y1="35" x2="{20+col_w*2}" y2="{height-35}" class="divider" />')

    # Col 3: Longest Streak
    svg.append(f'<g transform="translate({centers[2]}, 60)">')
    svg.append('  <path d="M0 -30 L8 -14 L24 -12 L12 0 L15 16 L0 8 L-15 16 L-12 0 L-24 -12 L-8 -14 Z" fill="#38bdf8" opacity="0.8" />')
    svg.append(f'  <text x="0" y="30" text-anchor="middle" class="stat-val">{longest_streak} <tspan font-size="14">days</tspan></text>')
    svg.append('  <text x="0" y="55" text-anchor="middle" class="stat-label">LONGEST STREAK</text>')
    svg.append('  <text x="0" y="70" text-anchor="middle" style="font-family: sans-serif; font-size: 10px; fill: #475569;">All-time Record</text>')
    svg.append('</g>')

    svg.append('</svg>')
    return '\n'.join(svg)

# Write all outputs
top_langs_svg = build_top_langs_svg(top_langs, total_weighted_commits, lang_colors)
streak_svg = build_streak_svg(total_contribs, current_streak, longest_streak)

outputs = {
    "profile-summary-card-output/tokyonight/2-most-commit-language.svg": top_langs_svg,
    "top-languages-commits.svg": top_langs_svg,
    "github-streak-stats.svg": streak_svg
}

for path, content in outputs.items():
    dirname = os.path.dirname(path)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {path} successfully!")
