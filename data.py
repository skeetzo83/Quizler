import requests
import html

response = requests.get(url="https://opentdb.com/api.php?amount=30&difficulty=hard&type=boolean")
response.raise_for_status()
questions = response.json()["results"]

question_data = [
    {"question": html.unescape(question["question"]),
     "correct_answer": question["correct_answer"]}
    for question in questions
]
