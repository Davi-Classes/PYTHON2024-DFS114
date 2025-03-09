import db


def buscar_materias():
    with db.get_cursor() as cursor:
        sql = '''
            SELECT id, nome, codigo, descricao 
            FROM materias
        '''
        cursor.execute(sql)
        dados = cursor.fetchall()
    
    return dados


materias = buscar_materias()

print('Materias Cadastradas:')
for id, nome, codigo, _ in materias:
    print(id, nome, codigo)