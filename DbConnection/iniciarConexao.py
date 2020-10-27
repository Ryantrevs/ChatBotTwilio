import mysql.connector 
from mysql.connector import errorcode

def iniciar():
	try:
		dbConnection = mysql.connector.connect(host='localhost',user='root',password='12345678',database='chatbotdb')
		return dbConnection
	except mysql.connector.Error as error:
		if error.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database doesn't exist")
		elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("User name or password is wrong")
		else:
			print(error)
	else:
		dbConnection.close()
	return

def selectTelefone(telefone,db):
	cursor = db.cursor()
	sql = ("SELECT * FROM cliente where numero='{}'".format(telefone))
	cursor.execute(sql)
	resultado = cursor.fetchone()
	cursor.close()
	return resultado

def InsertTelefone(telefone,db):
	cursor = db.cursor()
	sql = ("INSERT INTO chatbotdb.cliente (numero,etapa) VALUES ('{}',1)".format(telefone))
	cursor.execute(sql)
	db.commit()
	result = cursor.rowcount
	cursor.close()
	return result

def InsertInfo(telefone,mensagem,db,campo,etapa):
	cursor = db.cursor()
	sql = ("UPDATE chatbotdb.cliente SET {} = '{}',etapa = {} where numero='{}'".format(campo,mensagem,etapa,telefone))
	print (sql)
	cursor.execute(sql)
	db.commit()
	result = cursor.rowcount
	cursor.close()
	return result

def InsertMensagem(telefone,mensagemEnviada,db):
	cursor = db.cursor()
	sql = ("UPDATE chatbotdb.cliente SET {} = '{}' where numero='{}'".format("mensagemEnviada",mensagemEnviada,telefone))
	cursor.execute(sql)
	db.commit()
	cursor.close()
	return

def InsertEtapa(telefone,etapa,db):
	cursor = db.cursor()
	sql = ("UPDATE chatbotdb.cliente SET etapa = {} where numero='{}'".format(etapa,telefone))
	cursor.execute(sql)
	db.commit()
	cursor.close()
	return

def InsertTitulo(telefone,mensagem,db,etapa):
	cursor = db.cursor()
	sql = ("INSERT INTO chatbotdb.trabalho (numeroCliente,Assunto) VALUES ('{}','{}')".format(telefone,mensagem))
	cursor.execute(sql)
	db.commit()
	InsertEtapa(telefone,etapa,db)
	cursor.close()
	return

def InsertTrabalho(telefone,mensagem,db,contexto,etapa):
	cursor = db.cursor()
	sql = ("UPDATE chatbotdb.trabalho SET {} = '{}' where numeroCliente='{}'".format(contexto,mensagem,telefone))
	cursor.execute(sql)
	db.commit()
	InsertEtapa(telefone,etapa,db)
	cursor.close()
	return