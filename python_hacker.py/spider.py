import requests
from bs4 import BeautifulSoup

def spider_urls(url, keyword):
    try:
        response = requests.get(url)
    except Exception as e:
        print(f"Request Failed: {url} ({e})")
        return []   # return empty list if request fails

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        urls = []
        # find all <a> tags with href attribute
        for tag in soup.find_all("a", href=True):
            href = tag["href"]
            # filter only links that contain the keyword
            if keyword.lower() in href.lower():
                urls.append(href)

        return urls   # return the list of matching links

    return []   # if status code not 200, return empty list


# main program
url = input("Enter the URL you want to scrap: ")
keyword = input("Enter the keyword: ")
print(spider_urls(url, keyword))
