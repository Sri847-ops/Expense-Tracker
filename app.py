from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production
DB_NAME = 'expenses.db'

# Initialize DB
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  amount REAL NOT NULL,
                  category TEXT NOT NULL,
                  date TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

init_db()

@app.route('/')
def index():
    conn = get_db_connection()
    expenses = conn.execute("SELECT * FROM expenses ORDER BY date DESC").fetchall()
    total = conn.execute("SELECT SUM(amount) FROM expenses").fetchone()[0] or 0
    conn.close()
    return render_template('index.html', expenses=expenses, total=total)

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        amount = request.form.get('amount', '').strip()
        category = request.form.get('category', '').strip()
        date = request.form.get('date', '').strip()
        
        # Validation
        if not title or not amount or not category or not date:
            flash('All fields are required!', 'error')
            return render_template('add.html')
        
        try:
            amount = float(amount)
            if amount <= 0:
                flash('Amount must be greater than 0!', 'error')
                return render_template('add.html')
        except ValueError:
            flash('Please enter a valid amount!', 'error')
            return render_template('add.html')
        
        try:
            # Validate date format
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            flash('Please enter a valid date!', 'error')
            return render_template('add.html')
        
        conn = get_db_connection()
        conn.execute("INSERT INTO expenses (title, amount, category, date) VALUES (?, ?, ?, ?)",
                    (title, amount, category, date))
        conn.commit()
        conn.close()
        flash('Expense added successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add.html')

@app.route('/delete/<int:expense_id>')
def delete_expense(expense_id):
    conn = get_db_connection()
    expense = conn.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,)).fetchone()
    if expense:
        conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        conn.commit()
        flash('Expense deleted successfully!', 'success')
    else:
        flash('Expense not found!', 'error')
    conn.close()
    return redirect(url_for('index'))

@app.route('/report')
def report():
    conn = get_db_connection()
    data = conn.execute("SELECT category, SUM(amount) as total FROM expenses GROUP BY category").fetchall()
    total_expenses = conn.execute("SELECT SUM(amount) FROM expenses").fetchone()[0] or 0
    conn.close()
    
    categories = [row['category'] for row in data]
    amounts = [row['total'] for row in data]
    
    return render_template('report.html', categories=categories, amounts=amounts, total=total_expenses)

if __name__ == '__main__':
    app.run(debug=True)
