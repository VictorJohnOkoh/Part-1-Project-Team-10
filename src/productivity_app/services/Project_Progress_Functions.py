Projects = {"Project_A": 
            {"teamLead": "John Smith",
            "Deadline": "24/10/26",
            "Estimated_hours": 100,
            "tasks": [{
                    "taskName": "TestTask1",
                    "Employee": "Bilbo Baggins",
                    "Deadline": "02/30/2020", 
                    "Status": "In Progress", 
                    "Estimated_hours": 100}]},

            "Project_B": 
            {"teamLead": "John Smith", 
             "Deadline": "12/05/29", 
             "Estimated_hours": 300, 
             "tasks": [{
                    "taskName": "TestTask1",
                    "Employee": "Bilbo Baggins", 
                    "Deadline": "02/30/2050", 
                    "Status": "In Progress", 
                    "Estimated_hours": 225},

                    {"taskName": "TestTask2",
                    "Employee": "Sherlock Holmes", 
                    "Deadline": "02/30/2028", 
                    "Status": "Complete", 
                    "Estimated_hours": 75}]},
            "Project_C": 
            {"teamLead": "Michael Scott", 
             "Deadline": "12/05/29", 
             "Estimated_hours": 50, 
             "tasks": [{
                    "taskName": "TestTask1",
                    "Employee": "Qui-gon Jinn", 
                    "Deadline": "02/30/2050", 
                    "Status": "In Progress", 
                    "Estimated_hours": 10},

                    {"taskName": "TestTask2",
                    "Employee": "Randy Marsh", 
                    "Deadline": "02/30/2099", 
                    "Status": "Complete", 
                    "Estimated_hours": 5},

                    {"taskName": "TestTask3",
                    "Employee": "Anakin Skywalker", 
                    "Deadline": "02/30/2099", 
                    "Status": "Complete", 
                    "Estimated_hours": 3},

                    {"taskName": "TestTask4",
                    "Employee": "Jake Peralta", 
                    "Deadline": "02/30/2099", 
                    "Status": "Complete", 
                    "Estimated_hours": 2},

                    {"taskName": "TestTask5",
                    "Employee": "Jim Halpert", 
                    "Deadline": "02/30/2099", 
                    "Status": "Complete", 
                    "Estimated_hours": 30}
                    ]},

            "Project_D": 
            {"teamLead": "Michael Scott", 
             "Deadline": "12/05/29", 
             "Estimated_hours": 90, 
             "tasks": [{
                    "taskName": "TestTask1",
                    "Employee": "Jake Peralta", 
                    "Deadline": "02/30/2050", 
                    "Status": "In Progress", 
                    "Estimated_hours": 10},

                    {"taskName": "TestTask2",
                    "Employee": "Anakin Skywalker", 
                    "Deadline": "02/30/2099", 
                    "Status": "Complete", 
                    "Estimated_hours": 40},

                    {"taskName": "TestTask3",
                    "Employee": "Jim Halpert", 
                    "Deadline": "02/30/2099", 
                    "Status": "Complete", 
                    "Estimated_hours": 2},

                    {"taskName": "TestTask4",
                    "Employee": "Qui-gon Jinn", 
                    "Deadline": "02/30/2099", 
                    "Status": "Complete", 
                    "Estimated_hours": 5},

                    {"taskName": "TestTask5",
                    "Employee": "Randy Marsh", 
                    "Deadline": "02/30/2099", 
                    "Status": "Complete", 
                    "Estimated_hours": 33}
                    ]}
}

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
