##配置
username = 'root'
password = '123456'
hostname = '127.0.0.1'
port = 3306
database = 'ram'
SQLALCHEMY_DATABASE_URI= f'mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}?charset=utf8'