# other_languages.py
import requests
import plotly.express as px

url = "https://api.github.com/search/repositories"
url += "?q=language:javascript+sort:stars+stars:>1000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()
repo_dicts = response_dict['items']

repo_names, star_counts = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    star_counts.append(repo_dict['stargazers_count'])

fig = px.bar(x=repo_names, y=star_counts,
    title="Most-Starred JavaScript Projects on GitHub",
    labels={'x': 'Repository', 'y': 'Stars'})
fig.show()