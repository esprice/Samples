from flask import Flask, request, render_template_string

app = Flask(__name__)

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index] += " - Completed"

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]

    def get_tasks(self):
        return self.tasks

todo_list = ToDoList()

HTML = '''
<!doctype html>
<html>
<head><title>To-Do List</title></head>
<body>
    <h1>To-Do List</h1>
    <form action="/add" method="post">
        <input type="text" name="task" />
        <input type="submit" value="Add Task" />
    </form>
    <ul>
        {% for task in tasks %}
        <li>{{ task }}</li>
        {% endfor %}
    </ul>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML, tasks=todo_list.get_tasks())

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    todo_list.add_task(task)
    return home()

if __name__ == '__main__':
    app.run(debug=True)
