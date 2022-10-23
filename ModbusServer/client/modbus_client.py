from pyModbusTCP.client import ModbusClient
import time
import psycopg2

c = ModbusClient(host="localhost", port=8002, auto_open=True, auto_close=True)

while c.open():
    connection = psycopg2.connect(user="postgres",
                        password="example",
                        host="0.0.0.0",
                        port="5432")
    try:

        regs_list_1 = c.read_holding_registers(0, 1)

        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO readings (modbus_id, value, sensor) VALUES (%s,%s,%s)"""
        record_to_insert = (4, regs_list_1[0], 0 )
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()   
        print(regs_list_1)

    except:
        pass
    time.sleep(1)
    connection.close()