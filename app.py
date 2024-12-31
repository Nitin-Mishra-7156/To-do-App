from flask import Flask, jsonify, request, render_template
import sqlite3

app = Flask(__name__)

# Change Jinja2 delimiters to avoid conflict with AngularJS
app.jinja_env.block_start_string = '{%'
app.jinja_env.block_end_string = '%}'
app.jinja_env.variable_start_string = '[['
app.jinja_env.variable_end_string = ']]'

DATABASE = 'todo.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        # Create categories table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        ''')
        # Create todos table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                status INTEGER DEFAULT 0,
                category_id INTEGER,
                FOREIGN KEY (category_id) REFERENCES categories (id) ON DELETE CASCADE
            )
        ''')
    print("Database Initialized!")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/categories', methods=['GET'])
def get_categories():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM categories")
        categories = cursor.fetchall()
    return jsonify([{"id": row[0], "name": row[1]} for row in categories])

@app.route('/api/categories', methods=['POST'])
def add_category():
    data = request.get_json()
    name = data.get("name", "")
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))
            conn.commit()
        except sqlite3.IntegrityError:
            return jsonify({"message": "Category already exists!"}), 400
    return jsonify({"message": "Category added!"}), 201

@app.route('/api/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM categories WHERE id = ?", (category_id,))
        conn.commit()
    return jsonify({"message": "Category deleted!"})

@app.route('/api/todos', methods=['GET'])
def get_todos():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT todos.id, todos.task, todos.status, categories.name 
            FROM todos 
            LEFT JOIN categories ON todos.category_id = categories.id
        ''')
        todos = cursor.fetchall()
    return jsonify([
        {"id": row[0], "task": row[1], "status": row[2], "category": row[3]}
        for row in todos
    ])

@app.route('/api/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    task = data.get("task", "")
    category_id = data.get("category_id")
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO todos (task, category_id) VALUES (?, ?)", (task, category_id))
        conn.commit()
    return jsonify({"message": "Todo added!"}), 201

@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    status = data.get("status", 0)
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE todos SET status = ? WHERE id = ?", (status, todo_id))
        conn.commit()
    return jsonify({"message": "Todo updated!"})

@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
        conn.commit()
    return jsonify({"message": "Todo deleted!"})

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0',  port=5000, debug=True)
