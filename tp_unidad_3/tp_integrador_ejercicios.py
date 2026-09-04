
#Modesto Domingo Titirico Mamani


#Ejercicio 1:Ejercicio 1— “Caja del Kiosco” 
while True:
    cliente = input("Ingrese su nombre: ")
    if cliente.isalpha():
        print(f"Bienvenido, {cliente}!")
        break
    else:
        print("Nombre inválido. Debe contener solo letras y no puede estar vacío.")

while True:
    can_producto = input("Ingrese la cantidad de productos que desea comprar: ")
    if can_producto.isdigit() and 1 <= int(can_producto) <= 3:
        can_producto = int(can_producto)
        suma_total = 0
        total_con_descuento = 0
        total_ahorrado = 0
        for producto in range(can_producto):
            producto += 1
            while True:
                precio_producto = input(f"Ingrese el precio del producto {producto}: ")
                if precio_producto.isdigit():
                    precio_producto = int(precio_producto)
                    #print(f"Producto {producto}: {precio_producto}")
                    while True:
                        descuento = input(f"Consultar si tiene Descuento el {producto} (s/n): ")
                        descuento = descuento.lower()
                        if descuento == "s":
                            descuento_producto = precio_producto * 0.10
                            precio_producto = precio_producto - descuento_producto
                            #print(f"El precio con descuento del producto {producto} es: {precio_producto}")
                            break
                        elif descuento == "n":
                            descuento_producto = 0
                            break
                        else:
                            print("Debe ingresar 's' o 'n'" )
                    break
                else:
                    print("Debe contener Número y no puede estar vacío.")
            total_con_descuento += precio_producto
            total_ahorrado += descuento_producto
        total_sin_descuento = total_con_descuento + total_ahorrado
        break
    else:
        print("Cantidad inválida. Debe ser un número entre 1 y 3.")



print(f"=" * 45)
print(f"El total sin descuento es: {total_sin_descuento:.2f}")
print(f"El total con descuento es: {total_con_descuento:.2f}")
print(f"El total ahorrado es: {total_ahorrado:.2f}")
print(f"=" * 45)

#=====================================================================
#Ejercicio 2 - "Acceso al Campsus y Menú Seguro"
#objetivo: Login con intentos + menú de acciones con validacion estricta
usuario = "alumno"
clave = "python123"

intentos = 3
cuenta_conectada = False
for i in range(intentos):
    print(f"intentos para ingresar usuario: {intentos - i}/3")
    usuario_login = input("Ingrese su usuario: ")
    if usuario_login == usuario:
        intentos_clave = 3
        for j in range(intentos_clave):
            print(f"intentos para ingresar la clave: {intentos_clave - j}/3")
            clave_login = input("Ingrese su clave: ")
            if clave_login == clave:
                cuenta_conectada = True
                while True:
                    print(f"Bienvenido al Campus: {usuario_login} ")
                    print(f"=" * 45)
                    print("Menú")
                    print("1. Ver estado de Inscripción")
                    print("2. Cambiar clave")
                    print("3. Mostrar mensaje motivacional")
                    print("4. Salir")
                    print(f"=" * 45)
                    opcion = input("Ingrese una opción (1-4): ")
                    if opcion.isdigit() and 1 <= int(opcion) <= 4:
                        opcion = int(opcion)
                        if opcion == 1:
                            print("=" *20)
                            print("Estado de Inscripción: Activo")
                            print("=" *20)
                        elif opcion == 2:
                            nueva_clave = input("Ingrese su nueva clave: ")
                            clave = nueva_clave
                            while True:
                                confirmar_clave = input("Confirme su nueva clave: ")
                                if confirmar_clave == clave:
                                    print("=" *20)
                                    print("Clave cambiada exitosamente.")
                                    print("=" *20)
                                    break
                                else:
                                    print("=" *20)
                                    print("Las claves no coinciden. Intente nuevamente.")
                                    print("=" *20)
                        elif opcion == 3:
                            print("=" *20)
                            print("Qué bueno es tener un amigo que te ayude a estudiar y a crecer. ¡Sigue adelante!")
                            print("=" *20)
                        elif opcion == 4:
                            print("=" *20)
                            print("Saliendo del menú. ¡Hasta luego!")
                            print("=" *20)
                            break
                    else:
                        print("Opcion no disponible, intente de nuevo. ")
                break
            else:
                print(f"Clave incorrecta.")
        if not cuenta_conectada:
            print(f"intentos para ingresar la clave: 0/3")
            if intentos - i - 1 == 0:
                print(f"=" * 45)
                print(f"Cuenta bloqueada, intente mas tarde.")
                print(f"=" * 45)
                break
            else:
                continue
        if cuenta_conectada:
            break
    else:
        if intentos - i - 1 == 0:
            print(f"=" * 45)
            print(f"Cuenta bloqueada, intente mas tarde.")
            print(f"=" * 45)
        else:
            print(f"Usuario incorrecto.")

#Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)” 
lunes_1 = ""
lunes_2 = "Jose"
lunes_3 = ""
lunes_4 = "Erwin"

martes_1 = "Modesto"
martes_2 = ""
martes_3 = "Daniel"

nombre_operador = input("Ingrese su Nombre de operador: ")
while not nombre_operador.isalpha():
    print("x" * 30)
    print("Ingrese un nombre Valido.")
    print("x" * 30)
    nombre_operador = input("Ingrese su Nombre de operador: ")

while True:
    print("=" * 38)
    print(f"Bienvenido/a {nombre_operador} al sistema de turnos")
    print("-" * 38)
    print("Menu:")
    print("1. Reservar Turno")
    print("2. Cancelar Turno (por nombre)")
    print("3. Ver agenda del dia")
    print("4. Ver resumen general")
    print("5. Cerrar Sistema")
    print("=" * 38)
    opcion = input("Ingrese una opción del menú: ")
    if opcion.isdigit():
        opcion = int(opcion)
        #Reservar Turno
        if opcion == 1:
            print("-" * 25)
            print(f"Reservar Turno: ")
            print(f"1. Lunes")
            print(f"2. Martes")
            print("-" * 25)
            reservar_turno = input("Opcion de reserva de Turno:  ")
            if reservar_turno.isalpha():
                print("x" * 50)
                print("Error: Ingrese un número de opción válido.")
                print("x" * 50)
            elif reservar_turno.isdigit():
                reservar_turno = int(reservar_turno)
                if reservar_turno == 1 or reservar_turno == 2:
                    nombre_cliente = input("Ingrese el nombre del cliente: ")
                    while not nombre_cliente.isalpha():
                        print("x" * 30)
                        print("Ingrese un nombre Valido.")
                        print("x" * 30)
                        nombre_cliente = input("Ingrese el nombre del cliente: ")
                    if nombre_cliente == lunes_1 or nombre_cliente == lunes_2 or nombre_cliente == lunes_3 or nombre_cliente == lunes_4:
                        print("x" * 50)
                        print("Error: El cliente ya tiene un turno reservado para el Lunes.")
                        print("x" * 50)
                    elif nombre_cliente == martes_1 or nombre_cliente == martes_2 or nombre_cliente == martes_3:
                        print("x" * 50)
                        print("Error: El cliente ya tiene un turno reservado para el Martes.")
                        print("x" * 50)   
                    else:
                        if reservar_turno == 1:
                            if lunes_1 == "":
                                lunes_1 = nombre_cliente
                                print(f"Turno reservado para {nombre_cliente} el Lunes 1")
                            elif lunes_2 == "":
                                lunes_2 = nombre_cliente
                                print(f"Turno reservado para {nombre_cliente} el Lunes 2")
                            elif lunes_3 == "":
                                lunes_3 = nombre_cliente
                                print(f"Turno reservado para {nombre_cliente} el Lunes 3")
                            elif lunes_4 == "":
                                lunes_4 = nombre_cliente
                                print(f"Turno reservado para {nombre_cliente} el Lunes 4")
                            else:
                                print("x" * 60)
                                print("Error: No hay más turnos disponibles para el Lunes.")
                                print("x" * 60)     
                        elif reservar_turno == 2:
                            if martes_1 == "":
                                martes_1 = nombre_cliente
                                print(f"Turno reservado para {nombre_cliente} el Martes 1")
                            elif martes_2 == "":
                                martes_2 = nombre_cliente
                                print(f"Turno reservado para {nombre_cliente} el Martes 2")
                            elif martes_3 == "":
                                martes_3 = nombre_cliente
                                print(f"Turno reservado para {nombre_cliente} el Martes 3")
                            else:
                                print("x" * 60)
                                print("Error: No hay más turnos disponibles para el Martes.")
                                print("x" * 60)    
                    print("_" * 30)
                    print(lunes_1, lunes_2, lunes_3, lunes_4)
                    print(martes_1, martes_2, martes_3)    
                    print("‾" * 30)
        #Cancelar Turnno
        elif opcion == 2:
            print("-" * 25)
            print(f"Cancelar Turno: ")
            print(f"1. Lunes")
            print(f"2. Martes")
            print("-" * 25)
            cancelar_turno = input("Seleccione el dia del turno a cancelar:  ")
            if cancelar_turno.isalpha():
                print("x" * 50)
                print("Error: Ingrese un número de opción válido.")
                print("x" * 50)
            elif cancelar_turno.isdigit():
                cancelar_turno = int(cancelar_turno)
                if cancelar_turno == 1 or cancelar_turno == 2:
                    nombre_cliente = input("Ingrese el nombre del cliente: ")
                    while not nombre_cliente.isalpha():
                        print("x" * 30)
                        print("Ingrese un nombre Valido.")
                        print("x" * 30)
                        nombre_cliente = input("Ingrese el nombre del cliente: ")
                    if cancelar_turno == 1:
                        if nombre_cliente == lunes_1:
                            lunes_1 = ""
                            print(f"Turno cancelado para {nombre_cliente} el lunes 1.")
                        elif nombre_cliente == lunes_2:
                            lunes_2 = ""
                            print(f"Turno cancelado para {nombre_cliente} el lunes 2.")
                        elif nombre_cliente == lunes_3:
                            lunes_3 = ""
                            print(f"Turno cancelado para {nombre_cliente} el lunes 3.")
                        elif nombre_cliente == lunes_4:
                            lunes_4 = ""
                            print(f"Turno cancelado para {nombre_cliente} el lunes 4.")
                        else:
                            print("x" * 50)
                            print("Error: El cliente no tiene turno")
                            print("x" * 50)   
                    elif cancelar_turno == 2:
                        if nombre_cliente == martes_1:
                            martes_1 = ""
                            print(f"Turno cancelado para {nombre_cliente} el martes 1.")
                        elif nombre_cliente == martes_2:
                            martes_2 = ""
                            print(f"Turno cancelado para {nombre_cliente} el martes 2.")
                        elif nombre_cliente == martes_3:
                            martes_3 = ""
                            print(f"Turno cancelado para {nombre_cliente} el martes 3.")
                        else:
                            print("x" * 50)
                            print("Error: El cliente no tiene turno")
                            print("x" * 50)                 
                    
                    print("_" * 30)
                    print(lunes_1, lunes_2, lunes_3, lunes_4)
                    print(martes_1, martes_2, martes_3)    
                    print("‾" * 30)

        #Ver agenda del dia
        elif opcion == 3:
            print("-" * 25)
            print(f"Agenda del Lunes: ")
            print("-" * 25)
            print(f"Turno 1: {lunes_1 or 'Disponible'}")
            print(f"Turno 2: {lunes_2 or 'Disponible'}")
            print(f"Turno 3: {lunes_3 or 'Disponible'}")
            print(f"Turno 4: {lunes_4 or 'Disponible'}")
            print("-" * 25)
            print(f"Agenda del Martes: ")
            print("-" * 25)
            print(f"Turno 1: {martes_1 or 'Disponible'}")
            print(f"Turno 2: {martes_2 or 'Disponible'}")
            print(f"Turno 3: {martes_3 or 'Disponible'}")
        #Ver resumen general
        elif opcion == 4:
            disponibles_lunes = 0
            ocupados_lunes = 0

            disponibles_martes = 0
            ocupados_martes = 0
            if lunes_1 == "":
                disponibles_lunes += 1
            else:
                ocupados_lunes += 1
            if lunes_2 == "":
                disponibles_lunes += 1
            else:
                ocupados_lunes += 1
            if lunes_3 == "":
                disponibles_lunes += 1
            else:
                ocupados_lunes += 1
            if lunes_4 == "":
                disponibles_lunes += 1 
            else:
                ocupados_lunes += 1
            if martes_1 == "":
                disponibles_martes += 1
            else:
                ocupados_martes += 1
            if martes_2 == "":
                disponibles_martes += 1
            else:
                ocupados_martes += 1
            if martes_3 == "":
                disponibles_martes += 1
            else:
                ocupados_martes += 1
            if ocupados_lunes < ocupados_martes:
                dia_turno = "Martes"
            elif ocupados_lunes > ocupados_martes:
                dia_turno = "Lunes"
            elif ocupados_lunes == ocupados_martes:
                dia_turno = "Empate"
            
            
            print("_" * 38)
            print(f"Resumen General: ")
            print("‾" * 38)
            print(f"Lunes: Disponibles = {disponibles_lunes} | Ocupados = {ocupados_lunes}")
            print(f"Martes: Disponibles = {disponibles_martes} | Ocupados = {ocupados_martes}")
            print(f"Dia con más turnos ocupados: {dia_turno}")
            print("‾" * 38)
        #Salir del sistema
        elif opcion == 5:
            print("Cerrando el sistema...")
            break
        else:
            print("-" * 50)
            print("Error: Ingrese una opción válida del 1 al 5.")
            print("-" * 50)
    elif opcion.isalpha() or not opcion.isdigit():
        print("x" * 50)
        print("Error: Ingrese un número de opción válido.")
        print("x" * 50)

#4Ejercicio 4  — “Escape Room: La Bóveda” 
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

forzados = 0

agente = input("Ingrese su nombre de Agente: ")
while not agente.isalpha():
    print("Por favor, Ingrese solo letras.")
    agente = input("Ingrese su nombre de Agente: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    print("Menu: ")
    print("1. Forzar cerradura")
    print("2. Hackear Panel")
    print("3. Descansar")
    opcion = input("Ingrese una opción (1, 2 o 3): ")
    while not opcion.isdigit() or not (1 <= int(opcion) <= 3):
        print("Por favor, ingrese una opción válida (1, 2 o 3).")
        opcion = input("Ingrese una opción (1, 2 o 3): ")
    opcion = int(opcion)
    if opcion == 1:
        energia -= 20
        tiempo -= 2
        forzados += 1
        if energia < 0:
            energia = 0
        if tiempo < 0:
            tiempo = 0
        if forzados == 3:
            alarma = True
            print("Alarma activada, no puedes forzar más cerraduras.")
        elif energia < 40:
            print("Riesgo de alarma.")
            peligro = input("Elija un numero entre 1 a 3: ")
            while not peligro.isdigit() or not (1 <= int(peligro) <= 3):
                print("Por favor, ingrese un número válido entre 1 y 3.")
                peligro = input("Elija un numero entre 1 a 3: ")
            peligro = int(peligro)
            if peligro == 3:
                alarma = True
                print("Alarma activada, no puedes forzar más cerraduras.")
            else:
                print("Cerradura forzada con éxito.")
                cerraduras_abiertas += 1
        else:
            cerraduras_abiertas += 1
            if cerraduras_abiertas == 3:
                print("Cerradura forzada con exito")
            else:
                print(f"Cerradura forzada {cerraduras_abiertas}/3")
    if opcion == 2:
        forzados = 0
        energia -= 10
        tiempo -= 3
        for i in range(4):
            codigo_parcial += "A"
            print(f"Desencriptando... {i + 1}/4")
        if len(codigo_parcial) >= 8:
            cerraduras_abiertas += 1
            codigo_parcial = ""
        if cerraduras_abiertas == 3:
            print("Cerradura hackeada con exito")
        else:
            print(f"Cerradura hackeada: {cerraduras_abiertas}/3")
    if opcion == 3:
        forzados = 0
        tiempo -= 1
        if alarma == True:
            print("Alarma activada, Descansando... -10 de Energia.")
            energia -= 10
        elif alarma == False:
            print("Descansando... +15 de Energia.")
            energia += 15
        if energia < 0:
            energia = 0
        if energia > 100:
            energia = 100
        if tiempo < 0:
            tiempo = 0
    print("_" *40)
    print("Energia restante: ", energia)
    print("Tiempo restante: ", tiempo)
    print("Cerraduras abiertas: ", cerraduras_abiertas)
    print("Codigo parcial: ", codigo_parcial)
    print("Alarma activada: ", alarma)
    print(f"Forzar cerraduras: {forzados}")
    print("‾" *40)
    
    if cerraduras_abiertas == 3:
        print("¡Felicidades! Has abierto todas las cerraduras.")
        break
    if energia <= 0 or tiempo <= 0:
        print("¡Has fallado! No tienes suficiente energía o tiempo.")
        break
    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        print("¡Has fallado! La alarma se ha activado, kabum kabum...")
        break



#5 Ejercicio 5  — “Escape Room:"La Arena del Gladiador"
vida_del_gladiador = 100
vida_del_enemigo = 100
pociones_de_vida = 3
daño_base_ataque_pesado = 15
daño_base_del_enemigo = 12

Turno_gladiador = True

print(f"====== BIENVENIDO A LA ARENA DE COMBATE ======")
nombre_gladiador = ""
nombre_gladiador = input("Ingrese el nombre del gladiador: ")

while not nombre_gladiador.isalpha():
    print("Error: SOlo se permiten letras")
    nombre_gladiador = input("Ingrese el nombre del gladiador: ")

while vida_del_gladiador > 0 and vida_del_enemigo > 0:
    print("_" * 80)
    print(f"Turno del gladiador: {nombre_gladiador}")
    print(f"Vida del gladiador: {vida_del_gladiador} | Vida del enemigo: {vida_del_enemigo} | Pociones Restantes: {pociones_de_vida}")
    print("‾" * 80)
    print("Accion del Gladiador: ")
    print(f"1. Ataque Pesado {daño_base_ataque_pesado} de daño")
    print(f"2. Ráfaga Veloz ")
    print(f"3. Curar (Pociones de vida restantes: {pociones_de_vida})")
    print("‾" *80)
    opcion = input("Ingrese una opcion: ")
    while not opcion.isdigit() or not 1 <= int(opcion) <= 3:
        print("Error: Ingrese una opcion valida (1, 2 o 3)")
        opcion = input("Ingrese una opcion: ")
    opcion = int(opcion)
    if opcion == 1:
        if vida_del_enemigo < 20:
            golpe_critico = daño_base_ataque_pesado * 1.5
            golpe_critico = float(golpe_critico)
            vida_del_enemigo -= golpe_critico
            print(f"Has infligido un golpe critico de {golpe_critico} de daño al enemigo")
        if vida_del_enemigo >= 20:
            vida_del_enemigo -= daño_base_ataque_pesado
            print(f"¡Atacaste al enemigo por {daño_base_ataque_pesado} de daño!")
    elif opcion == 2:
        for i in range(1,4, 1):
            vida_del_enemigo -= 5
            print(f"Rafaga veloz: {i}/3")
            print(f"¡Atacaste al enemigo - 5 daño!")
            print(f"Daño total infligido: {i * 5}")
    elif opcion == 3:
        if pociones_de_vida > 0:
            vida_del_gladiador += 30
            pociones_de_vida -= 1
            print(f"¡Has usado una pocion de vida! Vida actual: {vida_del_gladiador}")
        elif pociones_de_vida == 0:
            print(f"?No quedan pociones!")

        if vida_del_gladiador > 100:
            vida_del_gladiador = 100
            
    if opcion == 1 or opcion == 2:
            vida_del_gladiador -= daño_base_del_enemigo
            if vida_del_enemigo <= 0:
                print(f"¡El enemigo ha sido derrotado!")
                pass
            elif vida_del_enemigo > 0:
                print("_" * 50)
                print(f"¡El enemigo te atacó por {daño_base_del_enemigo} de daño!")
                print("‾" * 50)
    if vida_del_gladiador > 0 and vida_del_enemigo < 0:
        print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla")
    if vida_del_gladiador <= 0:
        print(f"DERROTA. Has caído en combate.")