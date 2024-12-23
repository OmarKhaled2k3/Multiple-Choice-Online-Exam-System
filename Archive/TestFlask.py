from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# A pool of multiple-choice questions
QUESTIONS_POOL = [
    {"question": "What is the capital of France?", "choices": ["Paris", "London", "Berlin", "Madrid"], "answer": 1},
    {"question": "What is 5 + 7?", "choices": ["10", "11", "12", "13"], "answer": 3},
    {"question": "What is the color of the sky?", "choices": ["Blue", "Green", "Red", "Yellow"], "answer": 1},
    {"question": "Which programming language is this?", "choices": ["Python", "Java", "C++", "Ruby"], "answer": 1},
    {"question": "What is 10 / 2?", "choices": ["2", "3", "4", "5"], "answer": 4},
    # Add more questions as needed
]

# Generate a random quiz of 5 questions
def generate_quiz():
    return random.sample(QUESTIONS_POOL, 5)

@app.route("/")
def home():
    # Generate a random quiz for the student
    quiz = generate_quiz()
    return render_template("quiz.html", quiz=quiz)

@app.route("/submit", methods=["POST"])
def submit_quiz():
    # Retrieve answers from the student
    student_answers = request.json.get("answers")
    quiz = request.json.get("quiz")

    # Grade the quiz
    score = sum(1 for q, a in zip(quiz, student_answers) if q["answer"] == a)
    result = {"score": score, "total": len(quiz)}

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=12345)
