# Read the file
with open("Networks.txt") as file:
    lines = file.readlines()
questions_dict = {}
answers_dict = {}

for i in range(0, len(lines), 7):
    question_block = lines[i:i+7]
    question_number = question_block[0].split(":")[0].strip()
    question_statement = question_block[0].split(":")[1].strip()
    options = {chr(65 + j): question_block[j + 1].strip()[3:] for j in range(4)}
    correct_letter = question_block[5].strip().split(":")[1].strip()
    correct_statement = options[correct_letter]

    questions_dict[question_number] = {
        "Question Statement": question_statement,
        "A": options["A"],
        "B": options["B"],
        "C": options["C"],
        "D": options["D"],
        "Correct Answer": correct_statement
    }
    answers_dict[question_number] = correct_statement

<<<<<<< HEAD
print(questions_dict["Q1"]["Question Statement"])
print(questions_dict["Q1"]["A"])
print(answers_dict["Q1"])
print(questions_dict["Q1"]["Correct Answer"])
=======
# Output results
print("Questions Dictionary:")
print(questions)
print("\nAnswers Dictionary:")
print(answers)
#print(answers["Q1"])
<<<<<<< Updated upstream
=======
>>>>>>> c068471dabd1c005c0a79767a0c7298c769795f4
>>>>>>> Stashed changes
