from flask import Flask, request
from faker import Faker
import csv
import requests

app = Flask(__name__)
fake = Faker()


@app.route('/')
def hello():
    return 'My homework number 7'


@app.route('/requirements')
def requirements():
    with open('story.txt', 'r') as f:
        story = str(f.read())
        return story


@app.route('/generate-users/')
def generate_users():
    amount = request.args.get('amount', 100)
    fake = Faker()
    resp_list = []
    for i in range(amount):
        resp_list.append(f'{fake.name()} {fake.email()}')

    response = "<br>".join(resp_list)
    return response


@app.route('/space')
def space():
    people = requests.get('http://api.open-notify.org/astros.json')
    numbers = people.json()['number']

    return f'Количество космонавтов в космосе: {str(numbers)}'


@app.route('/mean')
def mean():
    list_weight = []
    list_height = []
    with open('people_data.csv') as f:
        reader = csv.DictReader(f)
        for i in reader:
            weight = i[' "Weight(Pounds)"']
            height = i[' "Height(Inches)"']
            list_weight.append(float(weight.lstrip()))
            list_height.append(float(height.lstrip()))

    avg_heights = round((sum(list_height) / len(list_height)) * 2.54, 2)
    avg_weights = round((sum(list_weight) / len(list_weight)) / 2.205, 2)
    return f'Average height: {str(avg_heights)}, Average weight: {str(avg_weights)}'


if __name__ == '__main__':
    app.run(port=5000)
