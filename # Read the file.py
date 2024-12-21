# Read the file
with open('Networks.txt') as file:
    lines = file.readlines()

# Initialize variables
questions = []
answers = []

# Process lines
for i in range(0, len(lines), 7):  # Each question block has 7 lines
    question_block = lines[i:i+7]
    
    # Extract question components
    question_number = question_block[0].split(":")[0].strip()  # Q1, Q2, etc.
    question_statement = question_block[0].split(":")[1].strip()  # Question text
    options = {chr(65 + j): question_block[j + 1].strip()[3:] for j in range(4)}  # A, B, C, D options
    correct_letter = question_block[5].strip().split(":")[1].strip()  # Correct Answer letter (A, B, etc.)
    correct_statement = options[correct_letter]  # Map letter to the statement

    # Append to questions and answers
    questions.append({
        "Question Number": question_number,
        "Question Statement": question_statement,
        "Options": options
    })
    answers.append({
        "Question Number": question_number,
        "Correct Answer": correct_statement
    })

# Output results
print("Questions Dictionary:")
print(questions)
print("\nAnswers Dictionary:")
print(answers)
