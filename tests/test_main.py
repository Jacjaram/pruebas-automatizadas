import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from main import capitalize

# Casos básicos
if capitalize('hello') != 'Hello':
    raise Exception("Error: no convierte la primera letra en mayúscula")

if capitalize('Hello') != 'Hello':
    raise Exception("Error: ya estaba capitalizada")

# Casos límite
if capitalize('') != '':
    raise Exception("Error: no maneja cadena vacía")

if capitalize('123abc') != '123abc':
    raise Exception("Error: no debería cambiar nada si empieza por un número")

print("✅ Todas las pruebas pasaron correctamente.")