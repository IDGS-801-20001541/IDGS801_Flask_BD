from db import get_connection

try:
    connection= get_connection()
    with connection.cursor() as curso:
        curso.execute('call insertar(%s, %s, %s)',('Diana','Dominguez', 'diana@gmail.com'))
        """resulset = curso.fetchall()
        for row in resulset:
            print(row)"""
    connection.commit()
    connection.close()
except Exception as e:
    print(e)
    pass