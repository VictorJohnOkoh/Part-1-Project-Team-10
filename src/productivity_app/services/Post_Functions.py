# Stores all posts in dictionary
post = {}
RestrictedTopics = {}

def RestrictTopics():
    # Allows user to input topic to restrict access to that topic
    InpRestrictedTopic = str(input("Enter the topics you want to restrict:"))
    strRestrictedTopic = InpRestrictedTopic.strip().lower()

    # Checks to ensure topic is not empty
    if not strRestrictedTopic:
        print("Please enter a valid topic.")
        return

    # Adds the restricted topic to the RestrictedTopics dictionary
    RestrictedTopics[strRestrictedTopic] = True
    print("Access to this topic has been restricted.")

def create_post(Inptitle, Inpbody, Inptopics):
    # Creates fresh list for new topics and uses the new topic as a key
    if Inptopics not in post:
        post[Inptopics] = []

    # Adds title and body as element to list of posts for the given topic
    post[Inptopics].append({
        "title": Inptitle,
        "body": Inpbody,
        "comments": [] 
    })

def make_post():
    # Allows users to input post information
    # Strips leading and starting white spaces and checks if user input is valid
    Inptopics = str(input("Enter post topics:"))
    strtopics = Inptopics.strip().lower()
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

def make_comment():
    # Allows user to input topic to comment on
    Inpcommenttopic = str(input("Enter the topic you want to comment on:"))
    strcommenttopic = Inpcommenttopic.strip().lower()

    # Checks to ensure topic is not empty
    if not strcommenttopic:
        print("Please enter a valid topic.")
        return

    # Checks if topic exists within the dictionary of posts
    if strcommenttopic not in post:
        print("No posts about this topic have been found.")
        return

    Inptitle = str(input("Enter the title of the post you want to comment on:"))
    strtitle = Inptitle.strip().lower()

    post_found = False
    for single_posts in post[strcommenttopic]:
        if single_posts["title"].lower() == strtitle:
            Inpcomment = str(input("Enter your comment:"))
            strcomment = Inpcomment.strip()

            if not strcomment:
                print("Please enter a valid comment.")
                return
            
            single_posts["comments"].append(strcomment)
            post_found = True
            print("Comment added successfully!")
            break

    if post_found == False:
        print("No post with the given title has been found.")

def view_post():
    # Allows user to input topic to view the posts related to that topic
    singletopic = str(input("Enter the topics you want to view:"))
    strsingletopic = singletopic.strip()
    
    # Checks to ensure topic is not empty
    if not strsingletopic:
        print("Please enter a valid topic.")
        return

    LowerTopic = strsingletopic.lower()
    if LowerTopic in RestrictedTopics:
        print("Access to this topic is restricted. Please choose another topic.")
        return

    # Checks if topic exists within the dictionary of posts
    if LowerTopic not in post:
        print("No posts about this topic have been found.")
        return

    # Creates list of the title and body of all posts related to the topic and counts the number of posts found
    posts_found = post[LowerTopic]
    Postcount = len(posts_found)

    print("\n")
    print("Posts found for topic:", strsingletopic)
    print("Number of posts found:", Postcount)
    print("--------------------------")
    
    # Loops through each post in the list and prints the title and body of each post
    for single_posts in posts_found:
        print("Title:", single_posts["title"])
        print("Body:", single_posts["body"])

        if single_posts["comments"]:
            print("Comments:")
            for comment in single_posts["comments"]:
                print("-", comment)
        else:
            print("Comments:")
            print("No comments for this post.")
        print("--------------------------")

