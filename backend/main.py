from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app=FastAPI()

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT"),
        )
        return conn
    except Exception as e:
        print("Database connection failed:", e)
        raise



class Nums(BaseModel):
  num:int

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/submit")
def find_sum(element:Nums):
  conn=get_db_connection()
  curr=conn.cursor()
  curr.execute('''INSERT INTO public."NUMBERS"(number) VALUES (%s) ''',(element.num,))
  conn.commit()
  curr.execute('''SELECT SUM(number) FROM public."NUMBERS"''')
  result=curr.fetchone()[0]
  curr.close()
  conn.close()
  return {"sum":result}