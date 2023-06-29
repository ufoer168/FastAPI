from fastapi import FastAPI
from datetime import datetime
import sqlite3
from sqlite3 import Error
<<<<<<< HEAD
from sqlite3 import Connection

app = FastAPI()

def create_connection(db_file:str) -> Connection | None:
=======

app = FastAPI()

def create_connection(db_file):
>>>>>>> 34f309c044a254eac862307c006e7d81640b56f0
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

<<<<<<< HEAD
def create_table(conn:Connection):
=======
def create_table(conn):
>>>>>>> 34f309c044a254eac862307c006e7d81640b56f0
    sql_tasks = """
    CREATE TABLE IF NOT EXISTS iot1(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        light REAL NOT NULL,
        temperature REAL NOT NULL
    );
    """

    try:
        cursor = conn.cursor()
        cursor.execute(sql_tasks)
    except:
        print("error")

<<<<<<< HEAD
def insert_project(conn:Connection, project:tuple[str,float,float]):
=======
def insert_project(conn, project):
>>>>>>> 34f309c044a254eac862307c006e7d81640b56f0
    sql = """
    INSERT INTO iot1(date,light,temperature)
    VALUES(?,?,?)
    """
    cursor = conn.cursor()
    cursor.execute(sql,project)
    conn.commit()

@app.get("/")
def read_root():
    return {"Hello": "robert"}

@app.get("/items/{item_id}")
<<<<<<< HEAD
async def read_item1(item_id:int):
=======
async def read_item(item_id):
>>>>>>> 34f309c044a254eac862307c006e7d81640b56f0
    return {"item_id": item_id}

#query parameter
@app.get("/raspberry")
<<<<<<< HEAD
async def read_item(time:str = datetime.now().strftime("%Y%m%d %H:%M:%S"),light: float = 0.0, temperature: float = 0.0):
    conn = create_connection('data.db')
    if conn is not None:
        create_table(conn)
        insert_project(conn, (time,light,temperature))
        conn.close()
=======
async def read_item(time:str = datetime.now().strftime("%Y%m%d %H:%M:%S"), light: float = 0.0, temperature: float = 0.0):
    conn = create_connection('data.db')
    create_table(conn)
    insert_project(conn, (time,light,temperature))
    conn.close()
>>>>>>> 34f309c044a254eac862307c006e7d81640b56f0

    return {
        "時間":time,
        "光線":light,
        "溫度":temperature
<<<<<<< HEAD
    }
=======
    }
>>>>>>> 34f309c044a254eac862307c006e7d81640b56f0
