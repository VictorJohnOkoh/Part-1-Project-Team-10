Projects = {"Project_A": 
            {"teamLead": "Alice",
            "Deadline": "24/10/26",
            "Estimated_hours": 100,
            "tasks": [{
                    "taskName": "TempTest",
                    "Employee": "Bob",
                    "Deadline": "02/30/2020", 
                    "Status": "In Progress", 
                    "Estimated_hours": 5}]},

            "Project_B": 
            {"teamLead": "Tracy", 
             "Deadline": "12/05/29", 
             "Estimated_hours": 300, 
             "tasks": [{
                    "taskName": "Test2",
                    "Employee": "John", 
                    "Deadline": "02/30/2050", 
                    "Status": "In Progress", 
                    "Estimated_hours": 6},

                    {"taskName": "TestTask2",
                    "Employee": "Mikolaj", 
                    "Deadline": "02/30/2028", 
                    "Status": "Complete", 
                    "Estimated_hours": 10
}]}}

#Note for actual function simply return details found and use the loop below in the gui to show visually
def Search_Project_Details():
    ProjectName = str(input("Enter Project Name"))
    StrProjectName = ProjectName.strip()

    if StrProjectName not in Projects:
        print("No such project found")

    Details_Found = Projects[StrProjectName]
    print("Team Leader:", Details_Found["teamLead"])
    print("Deadline:", Details_Found["Deadline"])
    print("Estimated hours:", Details_Found["Estimated_hours"])

    print("Project:", StrProjectName)
    for task in Details_Found["tasks"]:
        print("Task Name:", task["taskName"])
        print("Employee:", task["Employee"])
        print("Deadline:", task["Deadline"])
        print("Status:", task["Status"])
        print("Estimated hours:", task["Estimated_hours"])
