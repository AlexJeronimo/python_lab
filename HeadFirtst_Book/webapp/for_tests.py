from DBcm import UseDatabase

config = {'host': '127.0.0.1',
          'user': 'vsearch',
          'password': 'vsearchpasswd',
          'database': 'vsearchlogDB', }

with UseDatabase(config) as cursor:
    _SQL = """show tables"""
    cursor.execute(_SQL)
    data = cursor.fetchall()

print(data)
