# To-Do Application

This project is a simple **To-Do Application** built using **Flask** (backend), **AngularJS** (frontend), and **SQLite** (database). The app supports creating categories, adding tasks, and marking them as completed.

---

## Features
1. **Category Management**: Create, view, and delete categories.
2. **Task Management**: Add, view, update, and delete tasks.
3. **Task Completion**: Mark tasks as completed.
4. **Simple UI**: Responsive design using **Bootstrap**.

---

## Prerequisites
- Python 3.x
- Flask
- SQLite3
- AngularJS (included via CDN)
- Bootstrap (included via CDN)

---

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Nitin-Mishra-7156/To-do-App.git
cd To-Do-App
```

### 2. Install Required Python Packages

#### Using `requirements.txt`:
A `requirements.txt` file is included to simplify package installation. Run the following command:
```bash
pip install -r requirements.txt
```

The file contains:
```
flask
```

This installs Flask and its dependencies automatically.

### 3. Set Up the Database
1. **Initialize Database**: The database tables will automatically be created when you run the app for the first time.
2. **Manual SQLite Setup (if needed)**:
   - Open a terminal and navigate to the project directory.
   - Launch the SQLite shell:
     ```bash
     sqlite3 todo.db
     ```
   - Create tables manually (optional):
     ```sql
     CREATE TABLE categories (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL UNIQUE
     );

     CREATE TABLE todos (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         task TEXT NOT NULL,
         status INTEGER DEFAULT 0,
         category_id INTEGER,
         FOREIGN KEY (category_id) REFERENCES categories (id) ON DELETE CASCADE
     );
     ```
 3. **Manual SQLite Modification for `category_id`**

     If you initially created the `todos` table without the `category_id` column, follow these steps to add the column manually using the SQLite terminal:

     1. **Open the SQLite terminal**:
        ```bash
        C:\sqlite\sqlite3.exe todo.db
        ```
     2. **Check the current schema of the `todos` table**:
        ```sql
        .schema todos
        ```
        Output:
        ```sql
        CREATE TABLE todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            status INTEGER DEFAULT 0
        );
        ```
     3. **Add the `category_id` column**:
        ```sql
        ALTER TABLE todos ADD COLUMN category_id INTEGER;
        ```

     4. **Verify the updated schema**:
        ```sql
        .schema todos
        ```
        Output:
        ```sql
        CREATE TABLE todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            status INTEGER DEFAULT 0,
            category_id INTEGER
        );
        ```
     This modification ensures that tasks can now be associated with categories using the `category_id` column.

---

### 4. Run the Flask Application
```bash
python app.py
```
- Open your browser and navigate to: `http://127.0.0.1:5000/`

---

## Application Structure
```plaintext
.
├── app.py          # Backend code with Flask routes
├── todo.db         # SQLite database file (auto-created)
├── templates/
│   └── index.html  # Main HTML file
└── static/
    └── js/       
        └── app.js          # AngularJS controller for the frontend
```

---

## Usage

### Adding Categories
1. Go to the **Categories** section.
2. Enter a category name and click "Add Category."

### Adding Tasks
1. Select a category.
2. Enter the task description.
3. Click "Add Task."

### Managing Tasks
- Mark tasks as completed by checking the checkbox.
- Delete tasks using the "Delete" button.

---

## SQLite Note for `category_id`
When creating tasks, ensure that `category_id` in the **todos** table matches a valid ID from the **categories** table. This can be verified or manually updated using the SQLite terminal:
```sql
SELECT * FROM categories;  -- To view available categories and their IDs.
```

---

## Demo
Here’s what you can expect:
- A responsive and functional to-do app.
- Full CRUD operations for tasks and categories.
- Smooth interaction between the frontend and backend using RESTful APIs.

---


