
from flask import Flask
import sqlite3

app = Flask(__name__)

def init_db():
  with sqlite3.connect('todo.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS todos(
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      title TEXT NOT NULL,
                      completed BOOLEAN NOT NULL CHECK (completed IN (0,1))
                      )''')
    conn.commit()

init_db()

# POST /todo - lägga till en uppgift
@app.route('/todo', methods=['POST'])
def create_todo():
  return "None"

# GET /todo - hämta alla uppgifter
# GET /todo/1 - hämtar en specifik uppgift
# PUT /todo/1 - markera som klar
# DELETE /todo/1 - radera en uppgift



if __name__ == '__main__':
  app.run(debug=True)



