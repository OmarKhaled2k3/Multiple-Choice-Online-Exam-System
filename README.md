# Online Quiz Application

## Overview
The Online Quiz Application is a Django-based web application that allows an examiner to create and manage multiple-choice quizzes for students. The application features a web-based interface for students to attempt quizzes with a real-time timer, dynamic question loading, and instant feedback upon submission.

---

## Features
- **Dynamic Quiz Generation:** Randomized multiple-choice questions for each session.
- **Real-Time Timer:** Tracks quiz duration and auto-submits when time is up.
- **Instant Feedback:** Grades are calculated and displayed immediately after submission.
- **Admin Interface:** Manage questions, options, and correct answers.
- **User Authentication:** Secure login and session management.

---

## Tech Stack
- **Backend:** Django
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite
- **Protocols:** HTTP with CSRF protection

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/OmarKhaled2k3/Multiple-Choice-Online-Exam-System.git
   cd quiz-app
   ```

2. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser for the admin panel:
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application:
   - Admin Panel: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
   - Quiz Application: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Usage

### Admin:
1. Log in to the admin panel.
2. Add questions with options and mark the correct answers.
3. Assign quizzes to students if required.

### Students:
1. Log in to the application.
2. Start the quiz and complete it within the allotted time.
3. View your grade immediately upon submission.

---

## Folder Structure

```
DjangoProject/
├── quiz/               # Core application folder
│   ├── migrations/     # Database migrations
│   ├── templates/      # HTML templates
│   ├── static/         # Static files (CSS, JS, images)
│   ├── admin.py        # Admin panel configuration
│   ├── apps.py         # App configuration
│   ├── models.py       # Database models
│   ├── views.py        # Core application logic
│   ├── urls.py         # URL routing
│   └── tests.py        # Test cases
├── manage.py           # Django management script
└── requirements.txt    # Project dependencies
```
---
## Snapshots
<img src="https://github.com/user-attachments/assets/e3c907f4-bc93-4d81-ac1e-5fc0210d19d4" width="400">
<img src="https://github.com/user-attachments/assets/2a07fb02-e565-4d4e-bd0b-9a6ff539cd7b" width="400">
<img src="https://github.com/user-attachments/assets/068424d5-7798-4a94-b695-4489232d4de9" width="400">
<img src="https://github.com/user-attachments/assets/19fc41f1-31fc-4640-aa44-b6b4ea04e537" width="400">
<img src="https://github.com/user-attachments/assets/010fec11-4177-465b-b957-fae5f20d96d2" width="400">
<img src="https://github.com/user-attachments/assets/226e44ae-bed2-447d-a16a-5c6b7f195b87" width="400">

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature/fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of your changes"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact
For any inquiries or support, please contact [omarkhaled2k3@gmail.com](mailto:omarkhaled2k3@gmail.com).

---

