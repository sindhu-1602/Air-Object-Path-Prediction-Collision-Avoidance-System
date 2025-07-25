import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="drdlproject",
        user="postgres",
        password="drdl123",  
        host="localhost",
        port="5432"
    )

def insert_data_from_file(filename):
    conn = get_connection()
    cur = conn.cursor()

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue 
            values = list(map(float, line.split()))
            cur.execute("""
                INSERT INTO aircraft_data
                (time, pos_x, pos_y, pos_z, acc_x, acc_y, acc_z, vel_x, vel_y, vel_z)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """, values)

    conn.commit()
    cur.close()
    conn.close()
    print("Aircraft data inserted into PostgreSQL!")

if __name__ == "__main__":
    insert_data_from_file("AirCraft.txt")
