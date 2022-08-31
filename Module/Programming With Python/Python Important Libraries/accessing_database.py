import sqlalchemy
import pymysql
import sqlalchemy as db


def main():

    # get sqlalchemy and pymysql vesion

    print("Sql alchemy: {}".format(sqlalchemy.__version__))
    print("pymysql: {}".format(pymysql.__version__))

    # get engine object using pymysql driver for mysql
    engine = db.create_engine(
        "mysql+pymysql://localhost:darshanpatel@localhost/actor")

    # get connection object
    connection = engine.connect()

    # get metadata object
    meta_data = db.MetaData()

    # set actor cration script table
    actor = db.Table(
        "actor", meta_data,
        db.Column("id", db.Integer, primary_key=True, autoincrement=True,
                  nullable=False),
        db.Column("first_name", db.String(50), nullable=False),
        db.Column("last_name", db.String(50), nullable=False),
        db.Column("age", db.Integer, nullable=False),
        db.Column("date_of_birth", db.Date, nullable=False),
        db.Column("active", db.Boolean, nullable=False)
    )

    # create actor table and store the information
    # in metadata

    meta_data.create_all(engine)

    # inserting data

    # get engine object using pymysql driver for mysql
    engine = db.create_engine(
        "mysql+pymysql: // username: password@localhost/movie")
    # get metadata object
    meta_data = db.MetaData()
    # get connection object
    connection = engine.connect()
    # get actor table definition
    actor_table = db.Table("actor", meta_data, autoload=True,
                           autoload_with=engine)
   # set the insert statement
    sql_query = db.insert(actor_table)
  # set data list
    data_list = [{"first_name": "John", "last_name": "Smith", "age": 50,
                  "date_of_birth": "1969-04-05", "active": True},
                 {"first_name": "Brian", "last_name": "Morgan", "age": 38,
                 "date_of_birth": "1981-02-11", "active": True},
                 {"first_name": "David", "last_name": "White", "age": 77,
                 "date_of_birth": "1942-06-30", "active": False}]

    # execute the insert statement
    result = connection.execute(sql_query, data_list)

    # select data

    # get engine object using pymysql driver for mysql
    engine = db.create_engine(
        "mysql+pymysql://username:password@localhost/movie")
    meta_data = db.MetaData()
    # get connection object
    connection = engine.connect()
    # get actor table definition
    actor_table = db.Table(
        "actor", meta_data, autoload=True, autoload_with=engine)
    # set the select statement
    select_actor = db.select([actor_table])
    # execute the select statement
    dataset = connection.execute(select_actor).fetchall()
    # print row by row
    for row in dataset:
        print(row)

   # Update Data
    engine = db.create_engine(
        "mysql+pymysql://username:password@localhost/movie")
    meta_data = db.MetaData()
   # get connection object
    connection = engine.connect()
    # get actor table definition
    actor_table = db.Table(
        "actor", meta_data, autoload=True, autoload_with=engine)

    # set update sql statement. update column 'active' to true
    # where id is equal to 4
    sql_query = db.update(actor_table).values(
        active=True).where(actor_table.columns.id == 4)
    results = connection.execute(sql_query)

    # Delete Data
    engine = db.create_engine(
        "mysql+pymysql://root:ana123!QAZ@localhost/movie")
    meta_data = db.MetaData()
    # get connection object
    connection = engine.connect()
    # get actor table definition
    actor_table = db.Table(
        "actor", meta_data, autoload=True, autoload_with=engine)
    # set delete sql statement. delete the record where id is equal to 1
    sql_query = db.delete(actor_table).where(actor_table.columns.id == 1)
    results = connection.execute(sql_query)


if __name__ == "__main__":
    main()
