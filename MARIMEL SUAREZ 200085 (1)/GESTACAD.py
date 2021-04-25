print ("Bienvenido a Gestión Academica")

import mysql.connector

import random as RD



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="SUAREZ10",
  database="gestion_universitaria"
)

mycursor = mydb.cursor()
#Registro o inicio de sessión estudiantes y maestros

acc = int (input(" Selecione una opción 1) Registrarme / 2) iniciar sessión    " ))

if acc == 1:
	soy = int (input("¿Quien eres ?, ingrese una opcion 1) Estudiante / 2) Docente  "))
	if soy == 1:
		nom =input("Ingresa tu Nombre ")
		AP =input("Ingresa tu Apellido ")
		Corr =input("Ingresa tu Correo  ")
		Dir=input("Ingresa tu Direccion   ")
		CAR =input("Ingresa tu Carrera  ")
		tel =input("Ingresa tu Telefono  ")
		cla =input("Ingresa una CLAVE ")
		mat = int (input ("Ingresa tu matricula"))

		use = nom[0] + AP[0] + str(mat)
		print("Este es su nombre de Usuario  " , use)


		sql = "INSERT INTO Estudiantes (Nombre, Apellido, Matricula, Carrera, Telefon, Direccion, Correo, user, Clave) VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s)"
		val = (nom, AP, mat, CAR, tel, Dir, Corr, use, cla)
		mycursor.execute(sql, val)

		mydb.commit()

		print(mycursor.rowcount, "registro insertado")

		acc1 = int (input("Ingrese 0 para mostrar el menu principal"))

	elif soy == 2:


		no =input("Ingresa tu Nombre ")
		A =input("Ingresa tu Apellido ")
		Clavee=input("Ingresa tu Clave   ")
		maia = input ("Codigo de las materias que imparte  ")
		orden =["02","43", "67", "45", "76", "34", "09","54", "60", "40", "20", "12"]
		
		iu = RD.choice(orden)

		ID_M = iu + no[0] + A[0] 

		print ("Este es su nombre de usuario asignado   ", ID_M )

		sql = "INSERT INTO Docentes (Nombre, Apellido, Id_Maestro, Clave, Materias) VALUES (%s, %s,%s, %s, %s)"
		val = (no, A, ID_M, Clavee, maia)
		
		mycursor.execute(sql, val)

		mydb.commit()

		print(mycursor.rowcount, "registro insertado")

		acc = int (input("Ingrese 0 para mostrar el menu principal"))


elif acc ==2: #VALIDAR USUARIO

	si = int(input ("¿Iniciar session como 1)Docente / 2) Estudiantes ? , Seleccione una opción   "))
	if si == 1: 
		print ("Usted eligio  Inicar como Docente ")

		o = 0

		while o < 3:
			
			id = input ("Ingrese su nombre de usuario  ")
			mycursor.execute ("SELECT * FROM Docentes")
			
			cl = input ("Ingrese su clave")
			
			if mycursor.fetchall():
				print ("Bienvenido")
				o = o +1

				break 
			else:
				print ("Intentalo otra vez")
			if o == 3:
				print ("Intentos agotados")
		
		acc = int (input("Ingrese 0 para mostrar el menu principal"))

	elif si ==2:
		print ("Usted eligio iniciar seccion como estudiante")
		u = 0

		while u < 3:
			
			i = input ("Ingrese su nombre de usuario  ")
			mycursor.execute ("SELECT * FROM estudiantes")
			
			c = input ("Ingrese su clave")
			
			if mycursor.fetchall():
				print ("Bienvenido")
				u = u +1

				break 
			else:
				print ("Intentalo otra vez")
			if u == 3:
				print ("Intentos agotados")
		acc1 = int (input("Ingrese 0 para mostrar el menu principal"))






if acc ==0:

	print ("_______Menú Principal_______")
	print("1) Consultar Materias" )
	print("2) Actualizar Mis Datos" )
	print("3) Consultar estudiantes" )
	print("4) Registrar  Materias" )
	print("5) Eliminar  Materias" )
	print("6) Salir " )

	opc = int(input ("Seleccione una opción"))

	if opc <1 or opc <6 :
		print ("Ingrese nuevamente...")
	
	elif opc == 6:
		print ("¡Gracias por incresar al sistema! ")
	if opc == 1:
		mycursor = mydb.cursor()
		print ()
		print ("Nombre______ Codigo_____")
		mycursor.execute("SELECT Nombre, Codigo FROM Materias")



		myresult = mycursor.fetchall()

		for datos  in myresult:
			 
			print (datos) 
			print ()
	if opc == 2:

		act = int( input ("Ingrese el campo que desea actualizar, Ej: 1.Nombre, 2.Apellido, 3.Clave  "))

		if act == 1:
			print ( "Usted selecciono actualizar su Nombre")

			DS=  input (" Nombre actual")

			dd = input("Nuevo Nombre ")

			mycursor = mydb.cursor()

			sql= ("UPDATE Docentes SET Nombre =  %s WHERE Nombre = %s ")
			val = ( 'DS', 'dd')
			mycursor.execute ( sql, val)

			mydb.commit()

			print (mycursor.rowcount, "Registro Actualizado")

		if act ==2:
			
			print ( "Usted selecciono actualizar su Apellido")

			DS=  input (" Apellido actual ")

			dd = input(" Apellido Nuevo  ")

			mycursor = mydb.cursor()

			sql= ("UPDATE Docentes SET Apellido =  %s WHERE Apellido = %s ")
			val = ( 'DS', 'dd')
			mycursor.execute ( sql, val)

			mydb.commit()

			print (mycursor.rowcount, "Registro Actualizado")
		
		if act == 3:
			
			print ( "Usted selecciono actualizar su Clave")

			DS=  input (" Clave actual ")

			dd = input(" Clave Nueva  ")

			mycursor = mydb.cursor()

			sql= ("UPDATE Docentes SET Clave =  %s WHERE Clave = %s ")
			val = ( 'DS', 'dd')
			mycursor.execute ( sql, val)

			mydb.commit()

			print (mycursor.rowcount, "Registro Actualizado")

	if opc ==3:

		print ("Usted eligio Consultar estudiantes")
		mycursor = mydb.cursor()
		print ()
		print ("Nombre______  , Apellido_____, Matricula_______, Carrera")
		mycursor.execute("SELECT Nombre, Apellido, Matricula, Carrera FROM Estudiantes")

		myresult = mycursor.fetchall()

		for datos  in myresult:
			 
			print (datos) 
			print ()
	if opc ==4:

		print ("Useted eligio Registrar materias ")

		nm = input ("Ingrese el nombre de la materia ")
		P = input ("Ingrese codigo ")
		cr = int (input("Ingrese el numero de creditos "))
		ho = input ("Ingrese el Horario")

		mycursor = mydb.cursor()

		sql = "INSERT INTO Materias (Nombre, Codigo, Creditos, Horarios) VALUES (%s, %s,%s, %s)"
		val = (nm, P, cr, ho)
		
		mycursor.execute(sql, val)

		mydb.commit()

		print(mycursor.rowcount, "registro insertado")
	if opc == 5:

		print ("Usted ha elegido eliminanr materias")

		i = int ( input ("Seguro que desea elimiar el registro  1. si / 2. no"))
		if i == 1:


			mycursor = mydb.cursor()

			MJ = input ("Ingrese el nombre de la materia a eliminar  ")

			sql = "DELETE FROM Materias WHERE Nombre = 'MJ' "

			mycursor.execute(sql)

			mydb.commit()

			print(mycursor.rowcount, "Registro eliminado ")
		elif i == 2:

			print (" Ok, No se elimino ningun registro ")
	if opc == 6:
		print ("Gracias por usar el sistema")

if acc1 == 0 :

	print ("_______Menú Principal_______")
	print("1) Actualizar Mis Datos" )
	print("2) ver profesores " )
	print("3) Ver horario de  Materias" )
	print("4) Consultar  indice" )
	print("5) Salir " )

	ui = int (input("¿Que opcion desea realizar "))

	if ui <1 or ui >5:
		print ("Opnción incorrecta, ingrese nuevamente...")
	elif ui == 5:
		print ("¡Gracias por incresar al sistema! ")

	if ui == 1:
		act = int( input ("Ingrese el campo que desea actualizar, Ej: 1.Nombre, 2.Apellido, 3.Clave, 4. Direccion  "))

		if act == 1:
			print ( "Usted selecciono actualizar su Nombre")

			DS=  input (" Nombre actual")

			dd = input("Nuevo Nombre ")

			mycursor = mydb.cursor()

			sql= ("UPDATE Estudiantes SET Nombre =  %s WHERE Nombre = %s ")
			val = ( 'DS', 'dd')
			mycursor.execute ( sql, val)

			mydb.commit()

			print (mycursor.rowcount, "Registro Actualizado")

		if act ==2:
			
			print ( "Usted selecciono actualizar su Apellido")

			DS=  input (" Apellido actual ")

			dd = input(" Apellido Nuevo  ")

			mycursor = mydb.cursor()

			sql= ("UPDATE Estudiantes SET Apellido =  %s WHERE Apellido = %s ")
			val = ( 'DS', 'dd')
			mycursor.execute ( sql, val)

			mydb.commit()

			print (mycursor.rowcount, "Registro Actualizado")
		
		if act == 3:
			
			print ( "Usted selecciono actualizar su Clave")

			DS=  input (" Clave actual ")

			dd = input(" Clave Nueva  ")

			mycursor = mydb.cursor()

			sql= ("UPDATE Estudiantes SET Clave =  %s WHERE Clave = %s ")
			val = ( 'DS', 'dd')
			mycursor.execute ( sql, val)

			mydb.commit()

			print (mycursor.rowcount, "Registro Actualizado")

		if act == 4:
			
			print ( "Usted selecciono actualizar su Direccion")

			DS=  input (" Direcccion  actual ")

			dd = input(" Direccion  Nueva  ")

			mycursor = mydb.cursor()

			sql= ("UPDATE Estudiantes SET Direccion =  %s WHERE Direccion = %s ")
			val = ( 'DS', 'dd')
			mycursor.execute ( sql, val)

			mydb.commit()

			print (mycursor.rowcount, "Registro Actualizado")

	if ui == 2:

		print ("Ver profesores")
		mycursor = mydb.cursor()
		print ()
		print ("Nombre______  , Apellido_____ , Materias _________")
		mycursor.execute("SELECT Nombre, Apellido, Materias FROM  Docentes")

		myresult = mycursor.fetchall()

		for datos  in myresult:
			 
			print (datos) 
			print ()

	if ui == 3:

		print ("Ver Horario de materias ")
		mycursor = mydb.cursor()
		print ()
		print ("Nombre______  , Codigo_________ , Horario_______ ")
		mycursor.execute("SELECT Nombre, Codigo, Horarios FROM  Materias ")

		myresult = mycursor.fetchall()

		for datos  in myresult:
			 
			print (datos) 
			print ()

	if ui ==4:
		print ("Ver indice ")
		mycursor = mydb.cursor()



		print ()
		print ("Indice ")
		mycursor.execute("SELECT Nombre, Indice FROM  Estudiantes  ")

		myresult = mycursor.fetchall()

		for datos  in myresult:
			 
			print (datos) 
			print ()






















	







