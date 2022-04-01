import sqlite3

conn = sqlite3.connect('data/echo.db')
c = conn.cursor()

def create(table_name):
    c.execute(f'''  
    CREATE TABLE IF NOT EXISTS {table_name}
    ([rno_no] INTERGER,[stduent_name] TEXT,[grade_year] TEXT) 
    ''')

def st_insert(r_no, st_name, yr):
    query = f'''
    INSERT INTO students(rno_no,student_name,grade_year)
    VALUES ({r_no}, {st_name}, {yr})
    '''
    return 0