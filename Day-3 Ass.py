#Day-3 Ass

#1.question


level_1 = int(input("Enter level 1 score: "))

if level_1>7:
    print("Level 1 round is clear")

    level2 = int(input("Enter level 2 score :"))
    if level2>10:
        print("you are Selected")
    else:
        print("Rejected in level 2")

else:
    print("Rejected in level 2")


#2.Question


Marks =int(input("Enter the Mark :"))

if Marks>=90 and Marks<=100:
    print("Grade A")

elif Marks>=80 and Marks<=89:
    print("Grade B")

elif Marks>=70 and Marks<=79:
    print("Grade C")

else:
    print("Invalid mark")





