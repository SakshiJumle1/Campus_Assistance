import sqlite3

# Connect to SQLite database (creates campus.db if it doesn't exist)
conn = sqlite3.connect('database/campus.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS faqs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        answer TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS locations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL
    )
''')

# Insert or update FAQs with new and updated questions
faqs = [
    # Updated existing questions with new answers
    ('What are the library hours?', 'The library is open from 8.30 AM to 9 PM daily.'),
    ('Where is the cafeteria?', 'The cafeteria is on ground floor in library building.'),
    ('When is the next exam?', 'Exams are scheduled for the last week of April.'),
    
    # New questions
    ('What is the wifi-password of campus area?', 'The password is Campus@123.'),
    ('Where is library?', 'The library is above cafeteria.'),
    ('Where is research center?', 'Research center is in PPCRC building.'),
    ('How many departments are there in college?', 'There are 3 departments in college.')
]

# Insert or replace FAQs (updates answers for existing questions)
for question, answer in faqs:
    cursor.execute('''
        INSERT OR REPLACE INTO faqs (id, question, answer)
        VALUES ((SELECT id FROM faqs WHERE question = ?), ?, ?)
    ''', (question, question, answer))

# Insert locations (unchanged from your original, with OR IGNORE for safety)
cursor.executemany('''
    INSERT OR IGNORE INTO locations (name, description) VALUES (?, ?)
''', [
    ('library', 'Building A, 2nd floor'),
    ('cafeteria', 'Building B, ground floor'),
    ('admin office', 'Building C, 1st floor')
])

# Commit and close
conn.commit()
conn.close()

print("Database created and populated successfully!")
