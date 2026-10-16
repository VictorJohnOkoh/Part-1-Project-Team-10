# Making post aspect of project

# Stores all posts in dictionary and list of topics to find specific posts
topicsList = []
post = {}

def create_post(Inptitle, Inpbody, Inptopics):
    post[Inptopics] = {
        "title": Inptitle,
        "body": Inpbody
    }

def make_post():
    Inptopics = str(input("Enter post topics:"))
    Inptitle =  str(input("Enter post title:"))
    Inpbody = str(input("Enter post body:"))

    strtopics = Inptopics.strip()
    strtitle = Inptitle.strip()
    strbody = Inpbody.strip()
    if strtopics not in topicsList and strtopics is not None:
        topicsList.append(strtopics)
    create_post(strtitle, strbody, strtopics)

def view_post():
    singletopic = str(input("Enter the topics you want to view:"))
    for topics in topicsList:
        if singletopic == topics and singletopic in post:
            print("topic:", singletopic, post[singletopic])