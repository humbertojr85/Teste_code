CREATE DATABASE sistema_hospitalar;

use sistema_hospitalar;

CREATE TABLE paciente(
    ID INT PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    nome VARCHAR(128) NOT NULL,
    cpf VARCHAR(14) NOT NULL UNIQUE,
    data_nascimento DATE TIME NOT NULL,
    tipo_sanguineo VARCHAR(3),
    telefone VARCHAR(17) NOT NULL,
    endeteco VARCHAR(64) NOT NULL,
    genero VARCHAR(10) NOT NULL,
    PRIMARY KEY(ID)
);