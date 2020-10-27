from twilio.rest import Client 

mensagem = "Obrigado por contratar nosso serviço, aguarde que seu contato já foi redirecionado para um dos nossos vendedores"

f = open("/Users/Patrick F/Desktop/projeto/ambienteVirtual/credenciais.txt")
account = f.readline().split("=")[1]
token = f.readline().split("=")[1]

def enviarMensagem(telefone,mensagem):
    account_sid = '{}'.format(account) 
    auth_token = '{}'.format(token) 
    client = Client(account_sid, auth_token) 
    body=("'{}'".format(mensagem))
    print(body)
    
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='{}'.format(mensagem),      
                                to='{}'.format(telefone) 
                            ) 
    
    print(message.sid)