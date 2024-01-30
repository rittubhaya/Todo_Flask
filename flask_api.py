from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__)

# Initialize task list
tasks = []

# API 1: View all tasks
@app.route('/tasks', methods=['GET'])
def view_tasks():
    return jsonify(tasks)

# API 2: Add a new task
@app.route('/add', methods=['POST'])
def add_task():
    task_description = request.form.get('task_description')
    if task_description:
        new_task = {'description': task_description, 'done': False}
        tasks.append(new_task)
    return redirect('/')

# API 3: Delete a task by its index
@app.route('/delete/<int:task_index>', methods=['GET'])
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
    return redirect('/')

# API 4: Update the status of a task and edit the task description
@app.route('/update/<int:task_index>', methods=['GET', 'POST'])
def update_task(task_index):
    if 0 <= task_index < len(tasks):
        if request.method == 'POST':
            if 'updated_description' in request.form:
                tasks[task_index]['description'] = request.form['updated_description']
            else:
                tasks[task_index]['done'] = not tasks[task_index]['done']
            return redirect('/')
        else:
            return render_template('edit.html', task=tasks[task_index], task_index=task_index)
    else:
        return "Task not found", 404

# Home page - HTML interface
@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
