# hn_discussions.py
from operator import itemgetter
import requests
import plotly.express as px

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:30]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    response_dict = r.json()

    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': int(response_dict.get('descendants', 0)),
        }
    except KeyError:
        continue
    else:
        submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts,
    key=itemgetter('comments'), reverse=True)

titles, comments, links = [], [], []
for sd in submission_dicts[:10]:
    titles.append(sd['title'])
    comments.append(sd['comments'])
    links.append(sd['hn_link'])

fig = px.bar(x=comments, y=titles, orientation='h',
    title="Most Active Discussions on Hacker News",
    labels={'x': 'Comments', 'y': 'Submission'})

# Make each bar label a clickable link
fig.update_traces(customdata=links,
    hovertemplate="<a href='%{customdata}'>%{y}</a><br>Comments: %{x}<extra></extra>")

fig.show()