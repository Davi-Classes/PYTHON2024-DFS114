-- Categorias Comandos SQL
-- DDL (Data Definition Language)
-- Criar, Excluir e Atualizar a ESTRUTURA do Banco de Dados e suas tabelas
DROP DATABASE IF EXISTS escola;
CREATE DATABASE escola;

USE escola;

-- Criando Tabela
CREATE TABLE professores (
	-- <coluna> <tipo> <constraints...>
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    registro VARCHAR(5) NOT NULL UNIQUE,
    fl_ativo BOOL NOT NULL DEFAULT 1,
    criado_em TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE alunos (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    data_nascimento DATE NOT NULL,
    fl_ativo BOOL NOT NULL DEFAULT 1,
    criado_em TIMESTAMP NOT NULL DEFAULT NOW()
);
-- Excluindo Tabela
DROP TABLE alunos;

-- Alterando Tabela
-- ALTER TABLE alunos 
-- ADD email VARCHAR(255) NOT NULL;

ALTER TABLE alunos 
DROP COLUMN email;
-- ----------------------------------------
-- DQL (Data Query Language)

SELECT * FROM professores;
SELECT * FROM alunos;

-- ----------------------------------------
-- DML (Data Manipulation Language)
-- Inserindo Registros
INSERT INTO professores (nome, registro)
VALUES ('Davi', '00000');

INSERT INTO professores (nome, registro, fl_ativo)
VALUES ('Gabriel Silva', '00023', 1),
		('Henrique Souza', '00003', 0);

-- Atualizando Registros
UPDATE professores
SET nome = 'Davi Lucciola'
WHERE registro = '00000'; -- ATENÇÃO AO WHERE EM COMANDOS DE UPDATE

-- Excluindo Registros
DELETE FROM professores
WHERE id = 1; -- ATENÇÃO AO WHERE EM COMANDOS DE DELETE
