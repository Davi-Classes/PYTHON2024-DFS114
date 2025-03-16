/*
Ex01.

a) Criem uma tabela chamada "Turmas" que deve conter as seguintes colunas:

- id: INT
- materia_id: INT
- professor_id: INT
- data_inicio: DATE
- data_fim: DATE
- horario: TIME
- duracao: TIME
- dia_da_semana: VARCHAR

Os dias da semana podem ser: DOM, SEG, TER, QUA, QUI, SEX, SAB
OBS: Lembrem-se que "materia_id" e "professor_id" são "Foreign Keys"

b) Cadastrem 2 turmas utilizando o INSERT

c) Façam uma consulta que traga as seguintes informações:

- id da turma
- nome do professor
- nome da materia
- codigo da materia
- data de inicio
- data de fim
- horario
- dia da semana
*/

CREATE TABLE turmas (
	id INT PRIMARY KEY AUTO_INCREMENT,
	materia_id INT NOT NULL,
	professor_id INT NOT NULL,
	data_inicio DATE NOT NULL,
	data_fim DATE NOT NULL,
	horario TIME NOT NULL,
	duracao TIME NOT NULL,
	dia_da_semana VARCHAR(3) NOT NULL,
    FOREIGN KEY (materia_id) REFERENCES materias (id),
    FOREIGN KEY (professor_id) REFERENCES professores (id)
);

SELECT * FROM materias;
SELECT * FROM turmas;

INSERT INTO turmas (materia_id, professor_id, data_inicio, data_fim, horario, duracao, dia_da_semana)
VALUES (3, 1, '2025-02-23', '2025-03-23', '14:00', '03:00', 'DOM');

INSERT INTO turmas (materia_id, professor_id, data_inicio, data_fim, horario, duracao, dia_da_semana)
VALUES (1, 1, '2025-01-23', '2025-03-20', '19:00', '03:00', 'QUI');

SELECT * FROM professores;

INSERT INTO turmas (materia_id, professor_id, data_inicio, data_fim, horario, duracao, dia_da_semana)
VALUES (5, 2, '2025-03-11', '2025-05-06', '15:00', '03:00', 'TER');

-- Listagem de Turmas
SELECT
	t.id,
    p.nome as professor,
    m.nome as materia,
    m.codigo as sigla,
    t.data_inicio,
    t.data_fim,
    t.horario as horario_inicio,
    ADDTIME(t.horario, t.duracao) as horario_fim,
    t.dia_da_semana
FROM
	turmas t
    INNER JOIN professores p
		ON t.professor_id = p.id
    INNER JOIN materias m
		ON t.materia_id = m.id;