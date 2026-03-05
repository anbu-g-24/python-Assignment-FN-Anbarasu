
students = [
    {"name": "Arun", "marks": [78, 82, 90]},
    {"name": "Bala", "marks": [65, 70, 60]},
    {"name": "Chitra", "marks": [88, 92, 95]}
]

# 1.calculate average for each student:

for student in students:
    total =0
    for mark in student["marks"]:
        total = total+mark
    average = total/ len(student["marks"])
    print(student["name"], "average mark is:",average)
    

#2.find highest average


highest_average = 0
name = ""

for student in students:
    average = sum(student["marks"]) / len(student["marks"])
    
    if average > highest_average:
        highest_average = average
        name = student["name"]

print("Highest average:", name, "=", highest_average)



#3.list students with average above 80

for student in students:
    if average>80:
        print(student['name'])


 #output:
             #students above 80 average
                #1.Arun
                #2.Chitra

