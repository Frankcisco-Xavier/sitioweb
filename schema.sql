create database turismo;
use turismo;

CREATE TABLE contactos (
    id_contacto INT AUTO_INCREMENT primary key,
    nombre varchar(50),
    telefono varchar(50),
    email varchar(50),
    fecha_actuliz datetime,
    sitio_web longtext,
    informacion longtext,
    guia_turistico varchar(50),
    telefono_guia varchar(10));
