from sqlalchemy import create_engine, text
import os

db_engine_string = os.environ["DB_CONNECTION_STRING"]

engine = create_engine(db_engine_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem",
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    result_list = result.all()
    jobs = []
  for t in result_list:
    jobs.append(t._asdict())
  return jobs
