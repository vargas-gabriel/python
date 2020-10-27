import psycopg2 

#connect to db

con = psycopg2.connect(
    host = "127.0.0.1",
    database = "python",
    user = "gabrielvargas",
    password = "postgres",
    port = 5432
)
#cursor
cur = con.cursor()
#execute query
cur.execute("select id, name from things")

rows = cur.fetchall()

for r in rows:
    print(f"id {r[0]} name{r[1]}")

#close cursor
cur.close()
#close connection 
con.close()