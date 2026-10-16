# Stores all posts in dictionary
post = {}

def create_post(Inptitle, Inpbody, Inptopics):
    # Creates fresh list for new topics and uses the new topic as a key
    if Inptopics not in post:
        post[Inptopics] = []

    # Adds title and body as element to list of posts for the given topic
    post[Inptopics].append({
        "title": Inptitle,
        "body": Inpbody
    })

def make_post():
    # Allows users to input post information
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

    create_post(strtitle, strbody, strtopics)
    print("Post created successfully!")

def view_post():
    # Allows user to input topic to view the posts related to that topic
    singletopic = str(input("Enter the topics you want to view:"))
    strsingletopic = singletopic.strip()

    # Checks to ensure topic is not empty
    if not strsingletopic:
        print("Please enter a valid topic.")
        return

    # Checks if topic exists within the dictionary of posts
    if strsingletopic not in post:
        print("No posts about this topic have been found.")
        return

    # Creates list of the title and body of all posts related to the topic and counts the number of posts found
    posts_found = post[strsingletopic]
    Postcount = len(posts_found)

    print("\n")
    print("Posts found for topic:", strsingletopic)
    print("Number of posts found:", Postcount)
    print("--------------------------")
    
    # Loops through each post in the list and prints the title and body of each post
    for single_posts in posts_found:
        print("Title:", single_posts["title"])
        print("Body:", single_posts["body"])
        print("--------------------------")

