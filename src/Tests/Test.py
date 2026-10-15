# Making post aspect of project
topicslist = []
post = {}
def create_post(title, body, topics):
    post[topics] = {
        "title": title,
        "body": body
    }

for i in range(2):
    title =  str(input("Enter post title:"))
    topics = str(input("Enter post topics:"))
    topicslist.append(topics)
    body = str(input("Enter post body:"))
    create_post(title, body, topics)

for singletopics in topicslist:
    if singletopics in post:
        print(post[singletopics])
    else:
        print("Not found")