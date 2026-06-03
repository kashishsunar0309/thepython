import requests
import plotly.express as px
#Make an API call and check the response
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}

r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
#Process overall results
response_dict = r.json()
print(response_dict.keys())

print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

#Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")
repo_names, stars = [], []
#Examine the first repository.
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    
#Make visualization.
fig = px.bar(x=repo_names, y= stars)
fig.show()