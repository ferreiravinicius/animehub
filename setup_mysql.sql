-- Testado no Mysql57

-- Cria o user para o app do flask
-- Warning: garante todos os privilegios (use apenas em ambiente de testes) 
CREATE USER IF NOT EXISTS 'flask'@'localhost' IDENTIFIED BY 'flask123';
GRANT ALL PRIVILEGES ON * . * TO 'flask'@'localhost';
FLUSH PRIVILEGES;

-- Cria o banco de dados
CREATE DATABASE IF NOT EXISTS animehub;


