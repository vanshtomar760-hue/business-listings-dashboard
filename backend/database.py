from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://root:@localhost/business_dashboard"

engine = create_engine(DATABASE_URL)

connection = engine.connect()

print("Database connected successfully!")