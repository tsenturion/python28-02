def connect(host, port=5432):
    print("Хост:", host)
    print("Порт:", port)

#connect()
connect("192.168.0.10")
connect("192.168.0.10", 5433)
connect("192.168.0.10", port=5433)