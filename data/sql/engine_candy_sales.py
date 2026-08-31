from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:0000@localhost/ecommerce_project"
)

with engine.connect() as conn:
    print("Nice!")