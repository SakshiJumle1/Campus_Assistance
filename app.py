from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database/campus.db')  # Matches create_database.py path
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.json.get('question', '').strip()
    if not user_question:
        return jsonify({'answer': 'Please enter a question!'})

    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Query the faqs table with case-insensitive matching
    cursor.execute("SELECT answer FROM faqs WHERE LOWER(question) LIKE ?", ('%' + user_question.lower() + '%',))
    result = cursor.fetchone()
    
    conn.close()
    
    if result:
        return jsonify({'answer': result['answer']})
    else:
        return jsonify({'answer': 'Sorry, I don’t have an answer for that. Try something else!'})

if __name__ == '__main__':
    app.run(debug=True)
