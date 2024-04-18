from secrets import secrets

secret_key = secrets.get('SECRET_KEY')
adminId = secrets.get('ADMIN_ID')
adminPwd = secrets.get('ADMIN_PWD')

print(adminId)
print(adminPwd)