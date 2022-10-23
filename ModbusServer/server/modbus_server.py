from pyModbusTCP.server import ModbusServer
from random import uniform
import time
server = ModbusServer(host="localhost", port = 8002, no_block=True)

try:
    print("Servidor iniciando")
    server.start()
    print("Servidor Pronto")
    val = [0]
    while True:
        val1 = int(uniform(0,100))
        server.data_bank.set_holding_registers(0, [val1])
        time.sleep(1)
except:
    print("deu erro")