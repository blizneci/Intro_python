import time
import csv
import sqlite3



"""
Упражнения главы 8
"""

"""

print("ex # 1")
test1 = 'This is a test of the emergency text system'
time.sleep(2)
print("String 'This is a test of the emergency text system' has been written into var test1")

with open("test_ex1.txt", "wt") as f:
    print(f"file {f.name} is opened for writing")
    time.sleep(2)
    f.write(test1)
    print(f"String from var test1 has been written into file {f.name}")
    time.sleep(2)

print('-' * 80)
print("ex # 2")
with open("test_ex1.txt", "rt") as f:
    print(f"file {f.name} is opened for reading")
    test2 = f.read()
    time.sleep(2)
    print(f"Content of file {f.name} has been written into var test2")
    time.sleep(2)

if test1 == test2:
    print(f"test1 == test2: {test1 == test2}")
else:
    print(f"test1 == test2: {test1 == test2}")
    print("Someting wrong")
    exit()
print("Next exercise? any or n")
ans = input().lower()
if ans == 'n':
    print("EXIT")
    time.sleep(2)
    exit()

"""
print('-' * 80)
print("ex # 3")
time.sleep(2)

in_books = """author,book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats, Shoots & Leaves"
"""
print(in_books)
with open("books_ex3.csv", "wt") as fin:
    print(f"file {fin.name} is opened for writing")
    fin.write(in_books)
    time.sleep(2)
    print(f"in_books has been written into file {fin.name}")

print("Next exercise? any or n")
ans = input().lower()
if ans == 'n':
    print("EXIT")
    time.sleep(2)
    exit()

print('-' * 80)
print("ex # 4")
time.sleep(2)

with open("books_ex3.csv", "rt") as fout:
    print(f"file {fout.name} is opened for reading")
    books = csv.DictReader(fout)
    time.sleep(2)
    print("Iterating for books with csv.DictReader")
    for book in books:
        print(book)
        time.sleep(1)

print("Next exercise? any or n")
ans = input().lower()
if ans == 'n':
    print("EXIT")
    time.sleep(2)
    exit()

print('-' * 80)
print("ex # 5")
time.sleep(2)

with open("books_ex5.csv", "wt") as fin:
    fin.write("""title,author,year
    The Weirdstone of Brisingamen,Alan Garner,1960
    Perdido Street Station,China Mieville,2000
    Thud!,Terry Pratchett,2005
    The Spellman Files,Lisa Lutz,2007
    Small Gods,Terry Pratchet,1992""")
    print(f"The file {fin.name} was opened and filled up with books")
    time.sleep(2)

print("Next exercise? any or n")
ans = input().lower()
if ans == 'n':
    print("EXIT")
    time.sleep(2)
    exit()

print('-' * 80)
print("ex # 6")
time.sleep(2)

conn = sqlite3.connect('books_ex5.db')
print("Database books_ex5.db is created")
curs = conn.cursor()
curs.execute('DROP TABLE books')
curs.execute('''CREATE TABLE books
        (title TEXT PRIMARY KEY, author TEXT, year INTEGER)''')
print("Table books is created")
conn.commit()

print("Next exercise? any or n")
ans = input().lower()
if ans == 'n':
    print("EXIT")
    time.sleep(2)
    exit()

print('-' * 80)
print("ex # 7")
time.sleep(2)

ins_str = 'INSERT INTO books VALUES(?, ?, ?)'
print(f"Insertion template is: {ins_str}")
with open('books_ex5.csv', 'rt') as f:
    books = csv.DictReader(f)
    for book in books:
        curs.execute(ins_str, (book['title'], book['author'], book['year']))
    print("Books added to database")
    conn.commit()

print("Next exercise? any or n")
ans = input().lower()
if ans == 'n':
    print("EXIT")
    time.sleep(2)
    exit()

print('-' * 80)
print("ex # 8")
time.sleep(2)

curs.execute('SELECT title FROM books ORDER BY title')
print("Command 'SELECT title FROM books ORDER BY' is in process")
rows = curs.fetchall()
for row in rows:
    print(row)

print("Next exercise? any or n")
ans = input().lower()
if ans == 'n':
    print("EXIT")
    time.sleep(2)
    exit()
