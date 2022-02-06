CREATE DATABASE IF NOT EXISTS proyecto_consola;

use proyecto_consola;

CREATE TABLE usuario(

    id int(25) auto_increment not null,
    nombre varchar(100) ,
    apellidos varchar(200),
    email varchar(150) not null,
    password varchar(200) not null,
    fecha date not null,
    CONSTRAINT pk_usuario PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
) ENGINE = InnoDb; 

CREATE TABLE notas(
    id int(25) auto_increment not null,
    usuario_id int(25) not  null,
    titulo varchar(200) not null,
    descripcion MEDIUMTEXT, 
    fecha date not null,
    CONSTRAINT pk_notas PRIMARY KEY(id),
    CONSTRAINT fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuario(id)
)ENGINE = InnoDb;