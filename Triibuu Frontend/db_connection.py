import psycopg2

db_host = 'rionegro-server.postgres.database.azure.com'
db_user = 'julianegas'
db_pass = 'Julian58'
db_name = 'rionegro-db'
sslmode = 'require'

conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(db_host, db_user, db_name, db_pass, sslmode)
conn = psycopg2.connect(conn_string)