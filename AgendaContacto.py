import csv

if __name__ == "__main__":
    print('AGENDA DE CONTACTOS')

    opcion = 0

    # La condicion del while tiene que ser: ejecuta el ciclo mientras la opcion no sea el numero 5, es mas sencillo
    # de entender para el programador y para el codigo una condicion sencilla que validar un rango.
    # while 0 < opcion <= 5: - COMENTARIO JOY

    while opcion != 5:
        print()
        print('AGENDA DE CONTACOS')
        print('******************')
        print('1. Consultar')
        print('2. Anadir')
        print('3. Modificar')
        print('4. Borrar')
        print('5. Salir')
        print('******************')

        # Cambie el input a un entero, si quieres manejarlo como numero. COMENTARIO JOY
        opcion = int(input('Ingrese una opcion: '))

        if opcion == 1:
            # Generar lista de contactos a partir del archivo CSV (csvfile)
            # contactos = list(csv.DictReader(csvfile))
            # Utilizar for para recorrer la lista de contactos
            # ejemplo: for contacto in contactos:
            #               if contacto['phone'] == telefono
            #                   print(contacto)contacto['nombre']
            telefono = input('Ingrese su telefono: ')
            csvfile = open('lista_contactos.csv')
            contactos = list(csv.DictReader(csvfile))
            for contacto in contactos:
                if contacto['phone'] == telefono:
                    print('Nombre del Contacto:', contacto['nombre'])
                    print('Numero de telefono:', contacto['phone'])
                    break
            csvfile.close()

        elif opcion == 2:
            # nuevoContacto = {'phone': numero_telefono, 'nombre': nombre_contacto}
            # csvfile = open('lista_contactos.csv', 'w', newline='')
            # header = ['phone','nombre']
            # writer = csv.DictWriter(csvfile, fieldnames=header)
            # writer.writeheader()
            # writer.writerow(nuevoContacto)
            nuevo_contacto = {}
            nuevo_contacto['phone'] = input('Ingrese su telefono: ')
            nuevo_contacto['nombre'] = input('Ingrese su nombre: ')

            with open('lista_contactos.csv', 'r') as csvfile:
                file_has_data = csvfile.read(1)

            with open('lista_contactos.csv', 'a', newline='') as csvfile:
                headers = ['phone', 'nombre']
                writer = csv.DictWriter(csvfile, fieldnames=headers)

                if not file_has_data:
                    writer.writeheader()

                writer.writerow(nuevo_contacto)
                csvfile.close()

            print('El contacto fue añadido.')
            
        elif opcion == 3:
            telefono = input('Ingrese su telefono: ')
            csvfile = open('lista_contactos.csv')
            contactos = list(csv.DictReader(csvfile))
            for contacto in contactos:
                if contacto['phone'] == telefono:
                    telefono_modificado = input('Ingrese el nuevo numero: ')
                    contacto['phone'] = telefono_modificado
                    print('Modificado')
                    break
            csvfile.close()
    # Este ELSE no va, si la opcion es 5, sale del while y se muestra el mensaje de 'Hasta la proxima'
    # else:
    #     print('Hasta la proxima.') - COMENTARIO JOY
    print('Hasta la proxima.')
