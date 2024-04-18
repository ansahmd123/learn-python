# main.py
from secrets import secrets

secret_key = secrets.get('SECRET_KEY')

# gives default value if the credential is absent
db_user = secrets.get('DATABASE_USER')
db_pass = secrets.get('DATABASE_PASSWORD')
db_port = secrets.get('DATABASE_PORT')

print('secret_key :', secret_key)
print('db_user :', db_user)
print('db_pass :', db_pass)
print('db_port :', db_port)
