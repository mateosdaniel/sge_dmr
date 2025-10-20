#2. Contar elementos en un diccionario

productos = {
    "Electrónica": ["Smartphone", "Laptop", "Tablet", "Auriculares", "Smartwatch"],
    "Hogar": ["Aspiradora", "Microondas", "Lámpara", "Sofá", "Cafetera"],
    "Ropa": ["Camisa", "Pantalones", "Chaqueta", "Zapatos", "Bufanda"],
    "Deportes": ["Pelota de fútbol", "Raqueta de tenis", "Bicicleta", "Pesas", "Cuerda de saltar"],
    "Juguetes": ["Muñeca", "Bloques de construcción", "Peluche", "Rompecabezas", "Coche de juguete"],
}

total_cat = len(productos.keys())
total_productos_cat = {}
total_productos = 0

for cat in productos:
    total_productos_cat[cat] = len(productos.get(cat))
    total_productos += len(productos.get(cat))

print(f"Hay un total de {total_cat} categorias")
print(total_productos_cat)
print(f"Hay un total de {total_productos} productos")