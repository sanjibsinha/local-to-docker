# Creating a task manager application
import sqlite3

def connect_db():
    conn = sqlite3.connect('tasks.db')
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            completed INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def add_task(title, description):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (title, description) VALUES (?, ?)', (title, description))
    conn.commit()
    conn.close()
    print(f"Task '{title}' added successfully.")

def get_tasks():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    if tasks:
        for task in tasks:
            print(f"ID: {task[0]}, Title: {task[1]}, Description: {task[2]}, Completed: {task[3]}")
    else:
        print("No tasks found.")    

def update_task(task_id, title, description):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET title = ?, description = ? WHERE id = ?', (title, description, task_id))
    conn.commit()
    conn.close()
    print(f"Task '{title}' updated successfully.")

def delete_task(task_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    print("Task deleted successfully.")

def mark_task_completed(task_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    print("Task marked as completed.")

def mark_task_incomplete(task_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET completed = 0 WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    print("Task marked as incomplete.")

def main():
    create_table()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Get Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Mark Task as Incomplete")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(title, description)
        elif choice == "2":
            get_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID: "))
            title = input("Enter new task title: ")
            description = input("Enter new task description: ")
            update_task(task_id, title, description)
        elif choice == "4":
            task_id = int(input("Enter task ID: "))
            delete_task(task_id)
        elif choice == "5":
            task_id = int(input("Enter task ID: "))
            mark_task_completed(task_id)
        elif choice == "6":
            task_id = int(input("Enter task ID: "))
            mark_task_incomplete(task_id)
        elif choice == "7":
            print("Exiting the task manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
