/*
Exercicio Revisão.

a) Criem uma tabela "materias" que deve conter as seguintes
colunas:

- nome (obrigatorio)
- codigo (obrigatorio, Max 5 Letras)
- descricao (opcional, pode ser nulo)

b) Criem 5 registros para a tabela de "materias"
*/

CREATE TABLE materias (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    codigo VARCHAR(5) NOT NULL UNIQUE,
    descricao VARCHAR(255)
);

INSERT INTO materias (nome, codigo)
VALUES ('HTML e CSS', 'HC'),
		('Javascript', 'JS');
        
INSERT INTO materias (nome, codigo, descricao)
VALUES ('Banco de Dados Relacional', 'SQL', 'Banco de dados relacional utilizando SQL'),
		('Desenvolvimento de API', 'API', 'Desenvolvimento de API utilizando Pythone FastAPI'),
        ('Python', 'PY', NULL);
	
SELECT id, nome, codigo, descricao FROM materias;