from flask import Flask, render_template, request
app = Flask(__name__)

questions = {
    'question1': {'text': 'Имеете ли Вы опыт в бессерверной разработке?', 'yes': 'question2', 'no': 'Chalice'},
    'question2': {'text': 'Важно ли Вам не быть привязанным к одному поставщику услуг?', 'yes': 'Serverless', 'no': 'question3'},
    'question3': {'text': 'Вы разрабатываете WSGI-приложение?', 'yes': 'question4', 'no': 'question5'},
    'question4': {'text': 'Хотите ли Вы перенести уже существующее WSGI-приложение в бессерверную среду?', 'yes': 'question6', 'no': 'question5'},
    'question5': {'text': 'Вы планируете большое приложение с широким функционалом?', 'yes': 'Serverless', 'no': 'Chalice'},
    'question6': {'text': 'Хотите ли вы использовать отечественную платформу?', 'yes': 'Yappa', 'no': 'Zappa'},
    'Chalice': {'text': 'Ваш выбор Chalice!'},
    'Serverless': {'text': 'Ваш выбор Serverless framework!'},
    'Zappa': {'text': 'Ваш выбор Zappa!'},
    'Yappa': {'text': 'Ваш выбор Yappa!'},
    'congratulations': {'text': 'Вы завершили тест!'}
}

@app.route('/')
def hello_page():
    return render_template('index.html')

@app.route('/platform')
def platform_page():
    return render_template('platform.html')

@app.route('/framework', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        answer = request.form['answer']
        current_question_key = request.form['current_question']
        next_question_key = get_next_question(answer, current_question_key)
        return render_template('framework.html', question=questions[next_question_key]['text'], current_question=next_question_key)
    else:
        return render_template('framework.html', question=questions['question1']['text'], current_question='question1')

def get_next_question(answer, current_question_key):
    current_question = questions[current_question_key]
    if answer.lower() in current_question:
        return current_question[answer.lower()]
    else:
        return 'congratulations'  

if __name__ == '__main__':
    app.run()
