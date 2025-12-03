import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# Leer el archivo CSV
try:
    df = pd.read_csv('datos_velocidad.csv')

    # Verificar tipos y hacer cast si es necesario
    df['Tiempo'] = df['Tiempo'].astype(float)
    df['Velocidad'] = df['Velocidad'].astype(float)

    # Mostrar los primeros datos
    print("Datos cargados:")
    print(df.head())

    # Graficar
    plt.figure(figsize=(10, 5))
    plt.plot(df['Tiempo'], df['Velocidad'], marker='o', linestyle='-', color='blue', label='Velocidad')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Velocidad (m/s)')
    plt.title('Velocidad en función del tiempo')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    # Mostrar la figura si el backend es interactivo; si no, guardarla en archivo
    try:
        backend = mpl.get_backend().lower()
        if backend.startswith('agg'):
            out_file = 'grafica.png'
            plt.savefig(out_file)
            print(f"Figura guardada en '{out_file}' (backend no interactivo: {backend}).")
        else:
            plt.show()
    except Exception as e:
        print(f"Error al mostrar/guardar figura: {e}")

except FileNotFoundError:
    print("Error: El archivo CSV no fue encontrado.")
except ValueError as e:
    print(f"Error de conversión de datos: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")