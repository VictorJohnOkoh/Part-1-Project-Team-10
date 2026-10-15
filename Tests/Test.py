# Making post aspect of project
title =  str(input("Enter post title:"))
topics = str(input("Enter post topics:"))
body = str(input("Enter post body:"))
def create_post(title, body, topics):
    post = {
        topics: {
            "title": title,
            "body": body
        }
    }
    return post
post = create_post(title, body, topics)