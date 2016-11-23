## 2. Authenticating with the API ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params = {"t": "day"}
response = requests.get("https://oauth.reddit.com/r/python/top", headers=headers, params=params)

python_top = response.json()

## 3. Getting the most upvoted article ##

print(python_top.keys())
python_top_articles = python_top["data"]["children"]
most_upvoted = ""
most_upvotes= 0

for i in python_top_articles:
    x = i["data"]
    if x["ups"] >= most_upvotes:
        most_upvoted = x["id"] 
        most_upvotes = x["ups"] 

## 4. Getting article comments ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params = {"t": "day"}
response = requests.get("https://oauth.reddit.com/r/python/comments/4b7w9u", headers=headers)

comments = response.json()

## 5. Getting the most upvoted comment ##

comments_list = comments[1]["data"]["children"]

most_upvoted_comment = ""
most_upvoted = 0 

for i in comments_list:
    co = i["data"]
    if co["ups"] >= most_upvoted:
        most_upvoted_comment = co["id"]
        most_upvoted = co["ups"]

## 6. Upvoting a comment ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params = {"dir":1,"id":"d16y4ry"}
response = requests.post("https://oauth.reddit.com/api/vote", headers=headers, json=params)
status = response.status_code