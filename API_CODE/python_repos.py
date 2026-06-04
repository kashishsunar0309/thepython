# Import required libraries
import requests
import plotly.express as px

# Make an API call and check the response
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}

# Send GET request to GitHub API
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process overall results
response_dict = r.json()
print(response_dict.keys())

# Print total and completeness info
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# Explore information about the repositories
repo_dicts = response_dict['items']
repo_names, stars, hover_texts = [], [], []

# Examine each repository in the results
for repo_dict in repo_dicts:
    # Collect repository name
    repo_names.append(repo_dict['name'])
    # Collect star count
    stars.append(repo_dict['stargazers_count'])

    # Build hover texts with owner and description
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# Make visualization
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}

# Create bar chart with hover data (fixed: hover_data instead of hover_name)
fig = px.bar(x=repo_names, y=stars, title=title, labels=labels, hover_data=[hover_texts])

# Update font sizes for title and axes
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)

# Display the chart
fig.show()