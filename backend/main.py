from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = "mysql+pymysql://root:Happy87911%40%40@localhost/business_dashboard"

engine = create_engine(DATABASE_URL)


@app.get("/")
def home():
    return {"message": "FastAPI Backend Running"}


@app.get("/city-count")
def city_count():

    with engine.connect() as connection:

        result = connection.execute(text(
            "SELECT city, COUNT(*) as total FROM listing_master GROUP BY city"
        ))

        data = []

        for row in result:
            data.append({
                "city": row[0],
                "total": row[1]
            })

    return data


@app.get("/category-count")
def category_count():

    with engine.connect() as connection:

        result = connection.execute(text(
            "SELECT category, COUNT(*) as total FROM listing_master GROUP BY category"
        ))

        data = []

        for row in result:
            data.append({
                "category": row[0],
                "total": row[1]
            })

    return data


@app.get("/source-count")
def source_count():

    with engine.connect() as connection:

        result = connection.execute(text(
            "SELECT source, COUNT(*) as total FROM listing_master GROUP BY source"
        ))

        data = []

        for row in result:
            data.append({
                "source": row[0],
                "total": row[1]
            })

    return data