from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Function to fetch poems from the database
def get_poems():
    connection = sqlite3.connect('poems.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM poems')
    poems = cursor.fetchall()
    connection.close()
    return poems

def insert_poems():
    # Create a connection to the database (or create it if it doesn't exist)
    connection = sqlite3.connect('poems.db')

    # Create a cursor object to execute SQL commands
    cursor = connection.cursor()
    
    # Define the SQL commands to create the table and insert data
    sql_statement = '''
        DROP TABLE IF EXISTS poems;
        CREATE TABLE poems (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            text TEXT
        );

        INSERT INTO poems (title, author, text)
        VALUES
            ('The Road Not Taken', 'Robert Frost', 'Two roads diverged in a yellow wood, And sorry I could not travel both...'),
            ('Ozymandias', 'Percy Bysshe Shelley', 'I met a traveller from an antique land Who said: Two vast and trunkless legs of stone...'),
            ('Daffodils', 'William Wordsworth', 'I wandered lonely as a cloud That floats on high o''er vales and hills...'),
            ('Sonnet 18', 'William Shakespeare', 'Shall I compare thee to a summer''s day? Thou art more lovely and more temperate...'),
            ('The Raven', 'Edgar Allan Poe', 'Once upon a midnight dreary, while I pondered, weak and weary...');
    '''
    
    # Execute the SQL commands
    cursor.execute(sql_statement)

    # Commit the changes and close the connection
    connection.commit()
    connection.close()

    print("poems.db created and populated successfully.")


# Route to render the page with poems
@app.route('/')
def index():
    poems = get_poems()
    return render_template('index.html', poems=poems)

if __name__ == '__main__':
    
    app.run(debug=True)
