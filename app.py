import sqlite3

def insert_poems():
    # Create a connection to the database (or create it if it doesn't exist)
    connection = sqlite3.connect('poems.db')

    # Create a cursor object to execute SQL commands
    cursor = connection.cursor()

    # Define the SQL commands to create the table and insert data
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS poems (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        text TEXT
    );
    '''

    insert_poems_sql = '''
    INSERT INTO poems (title, author, text)
    VALUES
        ('The Road Not Taken', 'Robert Frost', 'Two roads diverged in a yellow wood, And sorry I could not travel both...'),
        ('Ozymandias', 'Percy Bysshe Shelley', 'I met a traveller from an antique land Who said: Two vast and trunkless legs of stone...'),
        ('Daffodils', 'William Wordsworth', 'I wandered lonely as a cloud That floats on high o''er vales and hills...'),
        ('Sonnet 18', 'William Shakespeare', 'Shall I compare thee to a summer''s day? Thou art more lovely and more temperate...'),
        ('The Raven', 'Edgar Allan Poe', 'Once upon a midnight dreary, while I pondered, weak and weary...');
    '''

    # Execute the SQL commands
    cursor.execute(create_table_sql)
    cursor.execute(insert_poems_sql)

    # Commit the changes and close the connection
    connection.commit()
    connection.close()

    print("poems.db created and populated successfully.")
    
def main():
    insert_poems()
    
if __name__ == '__main__':
    main()
