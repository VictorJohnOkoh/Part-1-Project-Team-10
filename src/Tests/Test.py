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
    Inptopics = str(input("Enter post topics:"))
    Inptitle =  str(input("Enter post title:"))
    Inpbody = str(input("Enter post body:"))

    # Strips leading and starting white spaces
    strtopics = Inptopics.strip()
    strtitle = Inptitle.strip()
    strbody = Inpbody.strip()

    # Checks if topic is already in the list and if it is valid
    if strtopics not in topicsList and strtopics is not None:
        topicsList.append(strtopics)
    # After check creates post
    create_post(strtitle, strbody, strtopics)

def view_post():
    # Allows  user to search for specific topic they want to view
    singletopic = str(input("Enter the topics you want to view:"))
    for topics in topicsList:
        if singletopic == topics and singletopic in post:
            print("topic:", singletopic, post[singletopic])
