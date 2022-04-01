import sqlite3

conn = sqlite3.connect('/data/echo.db')
c = conn.cursor()

def create(table_name):
    c.execute('''  
    CREATE TABLE IF NOT EXISTS students
    ([rno_no] INTERGER) 
    ''')




def 