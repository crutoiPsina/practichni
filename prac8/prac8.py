import csv
import sqlite3
import redis
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

print("=== 1–2. Робота з файлами ===")

# 1
test1 = "This is a test of the emergency text system"
with open("test1.txt", "w") as f:
    f.write(test1)

# 2
with open("test1.txt", "r") as f:
    test2 = f.read()

print("Рядки однакові:", test1 == test2)


print("\n=== 3–5. CSV ===")

# створення CSV
with open("books.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["title", "author", "year"])
    writer.writerow(["The Weirdstone of Brisingamen", "Alan Garner", 1960])
    writer.writerow(["Perdido Street Station", "China Mieville", 2000])
    writer.writerow(["Thud!", "Terry Pratchett", 2005])
    writer.writerow(["The Spellman Files", "Lisa Lutz", 2007])
    writer.writerow(["Small Gods", "Terry Pratchett", 1992])

# читання CSV
with open("books.csv", "r") as f:
    reader = csv.DictReader(f)
    books = list(reader)

print("CSV прочитано:", books)


print("\n=== 6–7. SQLite ===")

conn = sqlite3.connect("books.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS books (
    title TEXT,
    author TEXT,
    year INTEGER
)
""")

# очистка (щоб не дублювались записи)
cur.execute("DELETE FROM books")

# додавання з CSV
for row in books:
    cur.execute("INSERT INTO books VALUES (?, ?, ?)",
                (row["title"], row["author"], row["year"]))

conn.commit()


print("\n=== 8. Title (алфавіт) ===")

for row in cur.execute("SELECT title FROM books ORDER BY title"):
    print(row[0])


print("\n=== 9. Всі книги (за роком) ===")

for row in cur.execute("SELECT * FROM books ORDER BY year"):
    print(row)


print("\n=== 10. SQLAlchemy ===")

engine = create_engine("sqlite:///books.db")
Base = declarative_base()

class Book(Base):
    __tablename__ = "books"
    title = Column(String, primary_key=True)
    author = Column(String)
    year = Column(Integer)

Session = sessionmaker(bind=engine)
session = Session()

books_sorted = session.query(Book).order_by(Book.title).all()

for b in books_sorted:
    print(b.title)


print("\n=== 11–12. Redis ===")

try:
    r = redis.Redis()

    r.hset("test", mapping={
        "count": 1,
        "name": "Fester Bestertester"
    })

    print("Було:", r.hgetall("test"))

    r.hincrby("test", "count", 1)

    print("Стало count:", r.hget("test", "count"))

except Exception as e:
    print("Redis не працює:", e)


# закриття БД
conn.close()
