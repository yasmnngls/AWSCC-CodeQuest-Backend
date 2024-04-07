import json
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['DATABASE'] = 'password_manager.db'

def get_db():
    db = sqlite3.connect(app.config["DATABASE"])
    return db

conn = get_db()
cursor = conn.cursor()
cursor.execute('''
                CREATE TABLE IF NOT EXISTS passwords (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    website TEXT,
                    email TEXT,
                    password TEXT
                    )
                ''')
conn.commit()
conn.close()

def add(website, email, password):
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('''
                        INSERT INTO passwords (website, email, password)
                        VALUES (?, ?, ?)
                        ''', (website, email, password))
        conn.commit()

    except sqlite3.Error as e:
        print("SQLite error:", e)

    finally:
        conn.close()

def view():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
                    SELECT * FROM passwords
                    ''')
    entries = cursor.fetchall()
    conn.close()
    return entries

def delete(entry_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
                    DELETE FROM passwords WHERE id = ?
                    ''', (entry_id,))
    conn.commit()
    conn.close()

def update(entry_id, email, password):
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('''
                        UPDATE passwords SET email = ?, password = ? WHERE id = ?
                        ''', (email, password, entry_id))
        conn.commit()

    except sqlite3.Error as e:
        print("SQLite error:", e)

    finally:
        conn.close()

@app.route('/')
def index():
    entries = view()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    website = request.form['website']
    email = request.form['email']
    password = request.form['password']
    
    add(website, email, password)
    return redirect(url_for('index'))

@app.route('/delete/<int:entry_id>')
def delete_entry(entry_id):
    delete(entry_id)
    return redirect(url_for('index'))

@app.route('/update/<int:entry_id>', methods=['POST'])
def update_entry(entry_id):
    email = request.form.get('email')
    password = request.form.get('password')
    update(entry_id, email, password)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()