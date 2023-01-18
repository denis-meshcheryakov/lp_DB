from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('postgresql://wgqiunub:JYIg61oZx7ORK6RqQz8uflkpdHgJRmyl@hattie.db.elephantsql.com/wgqiunub')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
