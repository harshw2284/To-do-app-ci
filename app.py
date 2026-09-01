import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple in-memory database suitable for CI testing environments
todos = [
    {"id": 1, "task": "Configure CI/CD Pipeline", "done": True},
    {"id": 2, "task": "Expose Port 5000 in Docker", "done": False},
    {"id": 3, "task": "Deploy Application", "done": False}
]

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    task = request.form.get('task')
    if task and task.strip():
        new_id = max([t['id'] for t in todos], default=0) + 1
        todos.append({"id": new_id, "task": task.strip(), "done": False})
    return redirect(url_for('index'))

@app.route('/toggle/<int:todo_id>')
def toggle_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['done'] = not todo['done']
            break
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Binds to 0.0.0.0 to enable port exposure across containers and external hosts
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)