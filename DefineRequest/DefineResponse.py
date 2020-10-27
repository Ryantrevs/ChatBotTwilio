from DbConnection import iniciarConexao
import mysql.connector 
from Response import response
from Entity import Cliente

campo=["Bem vindo ao Chat do Atenas Consultoria\n\n\nGostariamos de agradecer pela oportunidade",
"Gostariamos de saber seu curso,\n\n digite por favor",
"Digite Agora o titulo do seu trabalho",
"Gostariamos de saber seu e-mail,\n\n digite por favor",
"Descreva mais sobre seu projeto\n\nTodos os detalhes de data de entrega,Assunto a ser desenvolvido, Detalhes de procedimento\n\n Todo detalhe faz diferença para o atendimento personalizado.",
"Agradecemos sua prefência, Logo um dos nossos vendedores entrará em contato para dar seguimento ao seu atendimento"]

def Definir(telefone,mensagem):
    db = iniciarConexao.iniciar()
    info = constroiCliente(telefone,db)
    if(info!=None):
        print(info.etapa)
        if info.etapa == 1:
            if info.mensagemEnviada==None:
                enviarMensagem = "Gostariamos de saber seu curso,\n\n digite por favor"
                response.enviarMensagem(telefone,enviarMensagem)
                iniciarConexao.InsertMensagem(telefone,enviarMensagem,db)
                return 
            else:
                iniciarConexao.InsertInfo(telefone,mensagem,db,"curso",2)
                info = constroiCliente(telefone,db)
                print("a etapa é: {}".format(info.etapa))
        if info.etapa == 2:
            if "titulo" in info.mensagemEnviada:
                iniciarConexao.InsertTitulo(telefone,mensagem,db,3)
                info = constroiCliente(telefone,db)
            else:
                enviarMensagem = "Digite Agora o titulo do seu trabalho"
                response.enviarMensagem(telefone,enviarMensagem)
                iniciarConexao.InsertMensagem(telefone,enviarMensagem,db)
                return 
        if info.etapa == 3:
            if "Descreva" in info.mensagemEnviada:
                iniciarConexao.InsertTrabalho(telefone,mensagem,db,"descricao",4)
                info = constroiCliente(telefone,db)
            else:
                enviarMensagem = "Descreva mais sobre seu projeto\n\nTodos os detalhes de data de entrega,Assunto a ser desenvolvido, Detalhes de procedimento\n\n Todo detalhe faz diferença para o atendimento personalizado."
                response.enviarMensagem(telefone,enviarMensagem)
                iniciarConexao.InsertMensagem(telefone,enviarMensagem,db)
                '''
        if info.etapa == 3:
            if "e-mail" in info.mensagemEnviada:
                iniciarConexao.InsertInfo(telefone,mensagem,db,"email",4)
                info = constroiCliente(telefone,db)
            else:
                enviarMensagem = "Gostariamos de saber seu e-mail,\n\n digite por favor"
                response.enviarMensagem(telefone,enviarMensagem)
                iniciarConexao.InsertMensagem(telefone,enviarMensagem,db)
                return 

        if info.etapa == 4:
            if "Descreva" in info.mensagemEnviada:
                iniciarConexao.InsertTrabalho(telefone,mensagem,db)
                info = constroiCliente(telefone,db)
            else:
                enviarMensagem = "Descreva mais sobre seu projeto\n\nTodos os detalhes de data de entrega,Assunto a ser desenvolvido, Detalhes de procedimento\n\n Todo detalhe faz diferença para o atendimento personalizado."
                response.enviarMensagem(telefone,enviarMensagem)
                iniciarConexao.InsertMensagem(telefone,enviarMensagem,db)
                return 
        if info.etapa == 5:
            if "projeto" in info.mensagemEnviada:
                iniciarConexao.InsertTrabalho(telefone,mensagem,db,"descricao")
                info = constroiCliente(telefone,db)
            else:
                enviarMensagem = "Agradecemos sua prefência, Logo um dos nossos vendedores entrará em contato para dar seguimento ao seu atendimento"
                response.enviarMensagem(telefone,enviarMensagem)
                iniciarConexao.InsertMensagem(telefone,enviarMensagem,db)
                return
                '''
    else:
        enviarMensagem = "Bem vindo ao Chat do Atenas Consultoria\n\n\nGostariamos de agradecer pela oportunidade"
        iniciarConexao.InsertTelefone(telefone,db)
        response.enviarMensagem(telefone,enviarMensagem)
        return Definir(telefone,mensagem=" ")


def constroiCliente(telefone,db):
    dadosCliente = iniciarConexao.selectTelefone(telefone,db)
    if(dadosCliente!=None):
        info = Cliente.DadosCliente(dadosCliente[0],dadosCliente[1],dadosCliente[2],dadosCliente[3],dadosCliente[4],dadosCliente[5],dadosCliente[6])
        return info
    else:
        return None
#def selectEtapa(mensagem,telefone,cliente):
 #   if (mensagem[cliente.etapa] == cliente.mensagemEnviada):
  #      campo[cliente.etapa] = 0