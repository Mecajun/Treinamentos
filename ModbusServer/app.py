from fastapi import FastAPI
import psycopg2


app = FastAPI()


def get_max_reading(slave_id):
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="example",
                                    host="0.0.0.0",
                                    port="5432")
        cursor = connection.cursor()
        postgres_insert_query = """ select max(value) from readings where modbus_id = %s group by modbus_id """

        record_to_insert = ((slave_id,))    
        cursor.execute(postgres_insert_query, record_to_insert)

        value = cursor.fetchone()
        connection.close()
        return value[0]
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)


@app.get("/")
def read_root():
    return {"Message" : "OK"}

@app.post("/")
def read_post():
    return {"dado":"enviado"}

@app.get("/slave/")
def read_slave(slave_id:int):
    base = get_max_reading(slave_id)

    return {"slave_id": slave_id, "max_value": base}