import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from main import capitalize

# Casos básicos
assert capitalize('hello') == 'Hello'

assert capitalize('Hello') == 'Hello' 

# Casos límite
assert capitalize('') == '' 

print("✅ Todas las pruebas pasaron correctamente.")