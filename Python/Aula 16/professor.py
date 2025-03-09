import db

def buscar_professores():
    # Criando Cursor
    with db.get_cursor() as cursor:
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

def cadastrar_professor(nome: str, registro: str, fl_ativo: bool = True):
    with db.get_cursor() as cursor:
        sql = '''
            INSERT INTO professores (nome, registro, fl_ativo)
            VALUES (%s, %s, %s)
        '''
        cursor.execute(sql, (nome, registro, fl_ativo))
    
    db.commit()

# cadastrar_professor('Vitor Prata', '21343')

professores = buscar_professores()
print(' Professores Cadastrados ')
for id, nome, registro, fl_ativo, criado_em in professores:
    print(id, nome, registro, bool(fl_ativo), criado_em)