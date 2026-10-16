# Making post aspect of project

# Stores all posts in dictionary and has a list of topics to find specific posts
topicsList = []
post = {}

def create_post(Inptitle, Inpbody, Inptopics):
    # Adds new posts into posts dictionary
    post[Inptopics] = {
        "title": Inptitle,
        "body": Inpbody
    }

def make_post():
    # Allows users to input various post information 
    # Strips leading and starting white spaces and checks if user input is valid

    Inptopics = str(input("Enter post topics:"))
    strtopics = Inptopics.strip()
    if not strtopics:
        print("Please enter a valid topic.")
        return
    
    Inptitle =  str(input("Enter post title:"))
    strtitle = Inptitle.strip()
    if not strtitle:
        print("Please enter a valid title.")
        return
    
    Inpbody = str(input("Enter post body:"))
    strbody = Inpbody.strip()
    if not strbody:
        print("Please enter a valid body.")
        return

    # Checks if topic is already in the list and if it is valid
    if strtopics not in topicsList:
        topicsList.append(strtopics)
    
    # After check creates post
    create_post(strtitle, strbody, strtopics)
    print("Post created successfully!")

def view_post():
    Postcount = 0
    singletopic = str(input("Enter the topics you want to view:"))
    strsingletopic = singletopic.strip()

    if not strsingletopic:
        print("Please enter a valid topic.")
        return
    
    if strsingletopic not in topicsList:
        print("No posts about this topic have been found.")
        return
    
    # Loops through the topics list and checks if the topic is in the list of topics and prints all posts with that topic
    for topics in topicsList:
        if strsingletopic == topics and strsingletopic in post:
            print("topic:", strsingletopic, post[strsingletopic])
            Postcount += 1
    print("Number of posts found:", Postcount)
