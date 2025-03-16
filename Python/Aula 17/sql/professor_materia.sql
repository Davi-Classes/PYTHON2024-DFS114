USE escola;

-- Relacionamento Muitos para Muitos
CREATE TABLE professores_materias (
	id INT PRIMARY KEY AUTO_INCREMENT,
    professor_id INT NOT NULL,
    materia_id INT NOT NULL,
    FOREIGN KEY (professor_id) REFERENCES professores (id),
    FOREIGN KEY (materia_id) REFERENCES materias (id)
);

INSERT INTO professores_materias (professor_id, materia_id)
VALUES (1, 3),
		(1, 4),
		(1, 5);
        
INSERT INTO professores_materias (professor_id, materia_id)
VALUES (2, 1),
		(2, 2),
		(2, 5);

INSERT INTO professores_materias (professor_id, materia_id)
VALUES (5, 1),
		(5, 3),
		(5, 5);

-- Consultas
-- Quais são as materias vinculadas a um professor?
SELECT 
	m.id,
    m.nome,
    m.codigo sigla
FROM 
	materias m
    INNER JOIN professores_materias pm
		ON m.id = pm.materia_id
WHERE
	pm.professor_id = 5;