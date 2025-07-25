import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="drdlproject",      
        user="postgres",            
        password="drdl123",         
        host="localhost",           # your PC
        port="5432"                 # default PostgreSQL port
    )
