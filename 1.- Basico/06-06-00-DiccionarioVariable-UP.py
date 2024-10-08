def listarTerminos(**terminos):
    for x, y in terminos.items():
        print(f'{x}: {y}')

listarTerminos(IDE='Integrated Developement Environment', PK='Primary Key')
listarTerminos(DBMS='Database Management System')