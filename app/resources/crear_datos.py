import random
from datetime import datetime, timedelta
import mysql.connector

# Configuración de la base de datos (si decides insertar directamente)
config = {
    "user": "root",
    "password": "",
    "host": "localhost",
    "database": "Cafe",
    "raise_on_warnings": True,
}

# Conexión a la base de datos (si decides insertar directamente)
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Lista de productos predefinidos
productos = [
    {"nombre": "Café Americano", "categoria": "Café", "precio": 2.50},
    {"nombre": "Café Latte", "categoria": "Café", "precio": 3.00},
    {"nombre": "Café Mocha", "categoria": "Café", "precio": 3.50},
    {"nombre": "Tarta de Manzana", "categoria": "Postre", "precio": 4.00},
    {"nombre": "Brownie", "categoria": "Postre", "precio": 3.00},
    {"nombre": "Galletas", "categoria": "Snack", "precio": 2.00},
    {"nombre": "Sandwich", "categoria": "Snack", "precio": 5.00},
]


# Función para generar una fecha aleatoria en 2024
def generar_fecha():
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    random_date = start_date + timedelta(
        days=random.randint(0, (end_date - start_date).days)
    )
    return random_date.strftime("%Y-%m-%d %H:%M:%S")


# Generar datos para la tabla Producto
def generar_productos():
    inserts = []
    for producto in productos:
        insert = f"INSERT INTO Producto (nombre, categoria, precio) VALUES ('{producto['nombre']}', '{producto['categoria']}', {producto['precio']});"
        inserts.append(insert)
    return inserts


# Generar datos para la tabla Inventario
def generar_inventario():
    inserts = []
    for idProducto in range(1, len(productos) + 1):
        cantidad = random.randint(10, 100)
        insert = f"INSERT INTO Inventario (idProducto, cantidad) VALUES ({idProducto}, {cantidad});"
        inserts.append(insert)
    return inserts


# Generar datos para la tabla Venta y DetalleVenta
def generar_ventas():
    ventas_inserts = []
    detalles_inserts = []
    for idVenta in range(1, 1001):  # 365 días del año
        fecha = generar_fecha()
        total = 0
        for _ in range(random.randint(1, 10)):  # Entre 1 y 10 productos por venta
            idProducto = random.randint(1, len(productos))
            cantidad = random.randint(1, 5)
            subtotal = productos[idProducto - 1]["precio"] * cantidad
            total += subtotal
            detalles_inserts.append(
                f"INSERT INTO DetalleVenta (idVenta, idProducto, cantidad, subtotal) VALUES ({idVenta}, {idProducto}, {cantidad}, {subtotal});"
            )
        ventas_inserts.append(
            f"INSERT INTO Venta (fecha, total) VALUES ('{fecha}', {total});"
        )
    return ventas_inserts, detalles_inserts


def generar_reportes():
    inserts = []
    for mes in range(1, 13):
        fecha_generacion = datetime(2024, mes, 1).strftime("%Y-%m-%d %H:%M:%S")
        total_ventas = round(
            random.uniform(1000.00, 5000.00), 2
        )  # Redondea a 2 decimales
        inserts.append(
            f"INSERT INTO ReportesVentas (tipoReporte, fechaGeneracion, totalVentas) VALUES ('Mensual', '{fecha_generacion}', {total_ventas});"
        )
    return inserts


# Generar todos los inserts
def generar_inserts():
    productos_inserts = generar_productos()
    inventario_inserts = generar_inventario()
    ventas_inserts, detalles_inserts = generar_ventas()
    reportes_inserts = generar_reportes()

    all_inserts = (
        productos_inserts
        + inventario_inserts
        + ventas_inserts
        + detalles_inserts
        + reportes_inserts
    )
    return all_inserts


# Escribir los inserts en un archivo .sql
def escribir_a_archivo(inserts, filename="datos_cafeteria.sql"):
    with open(filename, "w") as file:
        for insert in inserts:
            file.write(insert + "\n")


# Insertar directamente en la base de datos
def insertar_en_bd(inserts):
    for insert in inserts:
        cursor.execute(insert)
    conn.commit()


# Ejecutar el programa
if __name__ == "__main__":
    inserts = generar_inserts()

    # Elegir una de las dos opciones:
    # 1. Escribir los inserts en un archivo .sql
    # escribir_a_archivo(inserts)

    # 2. Insertar directamente en la base de datos
    insertar_en_bd(inserts)

    print("Datos generados exitosamente.")
