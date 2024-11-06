import pyfirmata # type: ignore
import time
import math

# Configuração da porta e inicialização da placa Arduino
porta = 'COM3'
placa = pyfirmata.Arduino(porta)

# Configuração do pino analógico para leitura da temperatura
pino_temperatura = placa.get_pin('a:0:i')
iterator = pyfirmata.util.Iterator(placa)
iterator.start()
pino_temperatura.enable_reporting()

# Valores conhecidos
R_fixa = 10000  # Resistor fixo de 10kΩ utilizado no divisor de tensão
B_coefficient = 3950  # Coeficiente Beta do termistor NTC 103
T0 = 298.15  # Temperatura de referência (25°C em Kelvin)
R0 = 10000  # Resistência do termistor a 25°C (10kΩ)

# Função para calcular a temperatura em Celsius a partir da tensão medida
def calcular_temperatura_Celsius(V, R_fixa, B_coefficient, T0, R0):
    # Calcula a resistência do termistor (R_ntc) a partir da tensão medida (V)
    R_ntc = R_fixa * (5 / V - 1)
    
    # Aplica a equação de Steinhart-Hart para converter a resistência em temperatura Kelvin
    T_Kelvin = 1 / ((1 / T0) + (1 / B_coefficient) * math.log(R_ntc / R0))
    
    # Converte a temperatura de Kelvin para Celsius
    T_Celsius = T_Kelvin - 273.15
    return T_Celsius

# Loop principal para leitura da temperatura
try:
    while True:
        leitura = pino_temperatura.read()  # Lê o valor analógico do pino
        if leitura is not None and leitura > 0:
            V = leitura * 5  # Converte o valor lido para tensão (0V a 5V)
            T_Celsius = calcular_temperatura_Celsius(V, R_fixa, B_coefficient, T0, R0)
            print("Temperatura em Celsius:", round(T_Celsius, 2))  # Exibe a temperatura em Celsius
        time.sleep(1)  # Aguarda 1 segundo antes de fazer uma nova leitura

        if T_Celsius >= 25:
            placa.digital [2].write(1)
            time.sleep(1)

        else:
            placa.digital [2].write(0)
            
except:
    pino_temperatura.disable_reporting()  # Desabilita a leitura do pino
    placa.exit()  # Encerra a conexão com a placa Arduino