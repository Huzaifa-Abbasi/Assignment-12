'''Create a program that asks the user for their scores in different subjects and calculates their 
overall grade based on a grading scale stored in a dictionary.'''

grade = {
    "A1": 90,
    "A": 80,
    "B": 70,
    "C": 60,
    "D": 50,
    "Fail": 1,
}

user_input = int(input("Enter Your score "))
if any(value <= user_input for value in grade.values()):
    for key, value in grade.items():
        if user_input >= value:
            print(f"Your grade is: {key}")
            break
else:
    print("Invalid input")