import db
from mysql.connector import MySQLConnection


class ProfessorRepository:
    def __init__(self, db: MySQLConnection):
        self.db = db

    def listar(self):
        # Criando Cursor
        with self.db.cursor() as cursor:
            # Executando Consulta
            sql = '''
                SELECT 
                    id, nome, registro, 
                    fl_ativo, criado_em 
                FROM professores
            '''
            cursor.execute(sql)

            # Buscando Dados Retornados
            dados = cursor.fetchall()

        return dados

    def cadastrar(self, nome: str, registro: str, fl_ativo: bool = True):
        with self.db.cursor() as cursor:
            sql = '''
                INSERT INTO professores (nome, registro, fl_ativo)
                VALUES (%s, %s, %s)
            '''
            cursor.execute(sql, (nome, registro, fl_ativo))
        
        self.db.commit()

    def listar_materias(self, professor_id: int):
        with self.db.cursor() as cursor:
            sql = '''
                SELECT 
                    m.id,
                    m.nome,
                    m.codigo sigla
                FROM 
                    materias m
                    INNER JOIN professores_materias pm
                        ON m.id = pm.materia_id
                WHERE
                    pm.professor_id = %s
            '''

            cursor.execute(sql, (professor_id,))
            dados = cursor.fetchall()
        
        return dados


professor_repository = ProfessorRepository(db.conn)
