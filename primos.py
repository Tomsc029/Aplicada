# 9/09/2025 9:36
def primo(n):
    """Verifica si un número es primo usando while"""
    if n < 2:
        return False
    
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# Programa principal con bucle while
while True:
    try:
        num = int(input("Ingresa un número (0 para salir): "))
        
        if num == 0:
            print("¡Programa terminado!")
            break
            
        if primo(num):
            print(f"{num} es PRIMO")
        else:
            print(f"{num} NO es primo")
            
    except ValueError:
        print("Error: Ingresa un número válido")
