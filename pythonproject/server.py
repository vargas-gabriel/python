from flask import Flask
import psycopg2 
api = Flask(__name__)

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




api = Flask(__name__)


@api.route('/')
def get_result():
  return 'Hello World'


@api.route('/db')
def get_OtherResult():
  return '(data!)'

