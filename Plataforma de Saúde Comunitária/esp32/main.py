import machine
import network
import time
import urequests

# Configuração da rede Wi-Fi
ssid = 'YOUR_SSID'
password = 'YOUR_PASSWORD'

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while not station.isconnected():
    pass

print('Connected to', ssid)

# Configuração dos pinos para os sensores
pressure_sensor = machine.ADC(machine.Pin(34))  # GPIO 34
glucose_sensor = machine.ADC(machine.Pin(35))   # GPIO 35

url = 'http://YOUR_SERVER_IP:5000/data'

while True:
    pressure_value = pressure_sensor.read()  # Valor bruto do ADC
    glucose_value = glucose_sensor.read()    # Valor bruto do ADC
    
    pressure = (pressure_value / 4095.0) * 300  # Simulando pressão em mmHg
    glucose = (glucose_value / 4095.0) * 200    # Simulando glicemia em mg/dL
    
    data = {
        'pressure': pressure,
        'glucose': glucose
    }
    
    response = urequests.post(url, json=data)
    print(response.text)
    response.close()
    
    time.sleep(10)  # Enviar dados a cada 10 segundos
