from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = []

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)


@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.json
    task_text = data.get("task", "").strip()
    if task_text:
        tasks.append({"id": len(tasks) + 1, "task": task_text})
    return jsonify({"message": "Task added"}), 201

@app.route('/api/tasks/<int:tid>', methods=['DELETE'])
def delete_task(tid):
    global tasks
    tasks = [t for t in tasks if t['id'] != tid]
    for i, t in enumerate(tasks): t['id'] = i + 1
    return jsonify({"message": "Task deleted"})
