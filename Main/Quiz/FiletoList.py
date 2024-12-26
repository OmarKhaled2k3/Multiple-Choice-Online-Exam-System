save_path = 'Main\\media\\'
completeName = save_path
def Savefile(f):
    global completeName
    completeName = save_path+f.name
    with open(completeName, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  

def Readfile():
    with open(completeName) as file:
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
    return questions_dict
    #print(questions_dict["Q7"]["Question Statement"])
    #print(questions_dict["Q1"]["A"])
    #print(answers_dict["Q1"])
    #print(questions_dict["Q1"]["Correct Answer"])


