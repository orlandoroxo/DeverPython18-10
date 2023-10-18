-- Criação do banco de dados "meubanco", criação da tabela "dados e criação de usuário superuser, script compatível com PostgreSQL"

CREATE DATABASE meubanco;

USE meubanco;

CREATE USER orlando WITH SUPERUSER PASSWORD 'orlando2552';

CREATE TABLE dados (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    idade INT,
    cidade VARCHAR(255)
);
