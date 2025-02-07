DROP DATABASE IF EXISTS Cafe;
CREATE DATABASE IF NOT EXISTS Cafe;

USE Cafe;

CREATE TABLE Producto (
    idProducto INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    categoria ENUM('Café', 'Postre', 'Snack') NOT NULL,
    precio DECIMAL(10,2) NOT NULL
);


CREATE TABLE Inventario (
    idInventario INT PRIMARY KEY AUTO_INCREMENT,
    idProducto INT NOT NULL,
    cantidad INT NOT NULL,
    fechaActualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (idProducto) REFERENCES Producto(idProducto)
);

CREATE TABLE Venta (
    idVenta INT PRIMARY KEY AUTO_INCREMENT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10,2) NOT NULL
);

CREATE TABLE DetalleVenta (
    idDetalle INT PRIMARY KEY AUTO_INCREMENT,
    idVenta INT NOT NULL,
    idProducto INT NOT NULL,
    cantidad INT NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (idVenta) REFERENCES Venta(idVenta),
    FOREIGN KEY (idProducto) REFERENCES Producto(idProducto)
);

CREATE TABLE ReportesVentas (
    idReporte INT PRIMARY KEY AUTO_INCREMENT,
    tipoReporte ENUM('Diario', 'Semanal', 'Mensual') NOT NULL,
    fechaGeneracion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    totalVentas DECIMAL(10,2) NOT NULL
);


