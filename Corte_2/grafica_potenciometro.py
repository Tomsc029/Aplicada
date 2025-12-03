import serial
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# CONFIGURACIÓN
PUERTO_COM = 'COM3'         # Cambia según tu sistema
BAUDRATE = 115200           # Velocidad de comunicación
INTERVALO_MS = 200          # Intervalo de actualización gráfica (más rápido)
GUARDAR_CADA = 100          # Guardar CSV cada X muestras
ADC_MAX = 4095              # Resolución ADC ESP32
VREF = 3.3                  # Voltaje de referencia

# INICIALIZACIÓN
puerto = serial.Serial(PUERTO_COM, BAUDRATE)
datos = []

# FUNCIÓN DE ACTUALIZACIÓN
def actualizar(frame):
    global datos
    try:
        linea = puerto.readline().decode('utf-8').strip()
        if "," in linea:
            tiempo, voltaje = linea.split(",")
            datos.append({'Tiempo': float(tiempo), 'Voltaje': float(voltaje)})

        if len(datos) >= GUARDAR_CADA:
            df = pd.DataFrame(datos)
            df.to_csv('datos_potenciometro.csv', index=False)

        # Graficar
        if len(datos) > 5:
            df = pd.DataFrame(datos)
            df['VoltajeSuave'] = df['Voltaje'].rolling(window=5).mean()

            plt.cla()
            plt.plot(df['Tiempo'], df['VoltajeSuave'], color='green', label='Voltaje suavizado')
            plt.plot(df['Tiempo'], df['Voltaje'], color='lightgray', alpha=0.4, label='Voltaje crudo')
            plt.xlabel('Tiempo (s)')
            plt.ylabel('Voltaje (V)')
            plt.title('Voltaje del potenciómetro en tiempo real')
            plt.grid(True)
            plt.legend()
            plt.xlim(left=max(0, df['Tiempo'].iloc[-1] - 30))  # Últimos 30 segundos
            plt.ylim(0, VREF)

    except Exception as e:
        print(f"Error: {e}")

# INICIAR ANIMACIÓN
try:
    print("Iniciando lectura en tiempo real...")
    animacion = FuncAnimation(plt.gcf(), actualizar, interval=INTERVALO_MS)
    plt.tight_layout()
    plt.show()
except KeyboardInterrupt:
    print("Lectura detenida por el usuario.")
    puerto.close()