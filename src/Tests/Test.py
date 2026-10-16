# Making post aspect of project
topicsList = []
post = {}

def create_post(Inptitle, Inpbody, Inptopics):
    post[Inptopics] = {
        "title": Inptitle,
        "body": Inpbody
    }
def make_post():
    for i in range(2):
        Inptopics = str(input("Enter post topics:"))
        Inptitle =  str(input("Enter post title:"))
        Inpbody = str(input("Enter post body:"))
        if Inptopics not in topicsList:
            topicsList.append(Inptopics)
        create_post(Inptitle, Inpbody, Inptopics)

def view_post():
    singletopic = str(input("Enter the topics you want to view:"))
    for topics in topicsList:
        if singletopic == topics and singletopic in post:
            print(singletopic, post[singletopic])
        else:
            print("Not found")