import serial


class ArduinoWrapper:

    def __init__(self, port="/dev/ttyACM0", baudrate=9600, timeout=1, writeTimeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.writeTimeout = writeTimeout

    def send_msg(self, message):
        with serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout,
                writeTimeout=self.writeTimeout,
        ) as port_serie:
            port_serie.write(message.encode('ascii'))

