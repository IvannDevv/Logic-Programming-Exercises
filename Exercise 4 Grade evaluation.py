print(" #############GRADE CALCULATOR############ ")

#input of dates
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
woman = input("You are a woman or man?: ").lower()

def greet(name, last):
    print(f"Welcome {name} {last}")
    
greet(first_name, last_name)

#Grade
grade_user = float(input(("Enter your math grade: ")))

#Condicional of genre
if woman == "woman" and grade_user == 10.5:
    grade_user = 11

#Condicionals of grades
if grade_user < 11:
    print("i'm sorry, you failed")
elif 11 <= grade_user <= 13:
    print("You passed with the minimum required")
elif 14 <= grade_user <= 17:
    print("Good joob!")
elif 18 <= grade_user <= 20:
    print("Perfect!")
else:
    print("Out")