# Flet
# frontend design do site
# backend logica por tras do site

# todo programa que iniciar com flet, fazer 3 coisas:
# importar flet
import flet as ft

#criar funcao principal do seu app
def main(pag):
    # criar todas as funcionalidades
    # criar elemento
#tela inicial
    # titulo: chatzap
    titulo = ft.Text('chatzap')

    def iniciar_chat(evento):
        pag.dialog = popup
        popup.open= True
        pag.update()
     # botao de iniciar chat 
        # "add uma acao ao botao, ao clicar vai fazer a funcao "iniciar chat""
    botiniciar = ft.ElevatedButton('entrar', on_click=iniciar_chat)


    # pop up
         # "bem vindo ao chatzap"
    titpopup = ft.Text('bem vindo ao chatzap')

         # campo de texto "escreva seu nome"
    campo_nome_usuario = ft.TextField(label='escreva seu nome no chat')
    chat=ft.Column()

    def entrar_chat(evento):  
        # sumir com o titulo chatzap
        pag.remove(titulo)
        # remover botiniciar
        pag.remove(botiniciar)
        # fechar pop up
        popup.open=False
        # add a coluna 'chat'
        pag.add(chat)
        # add a linha_msg
        pag.add(linha_msg)
        #valor que esta em nome de usuario
        nome_usuario=campo_nome_usuario.value
        #f= formatar, vai formatar o texto do seu jeito
        mensagem= f'{nome_usuario}: entrou no chat'
        pag.pubsub.send_all(mensagem)
        # carregar o chat
        pag.update()
        # add ao botao entrar a funcao de 'entrar_chat' ao clicar
    botentrarchat = ft.ElevatedButton('entrar no chat', on_click=entrar_chat)
    popup = ft.AlertDialog(
        title=titpopup, 
        content=campo_nome_usuario, 
        actions=[botentrarchat])
    
                                     
# socket e websocket fazem a conexao entre os computadores
    def conexao_msg(mensagem):
        texto_chat= ft.Text(mensagem)
        # add ao final do 'chat'
        chat.controls.append(texto_chat)

        pag.update()
    pag.pubsub.subscribe(conexao_msg)
                # mensagens que ja foram enviadas (chat)
            # "pessoa" entrou no chat     
            # campo de texto "digite sua mensagem"
            # botao "enviar"
    def enviar_msg(evento):
        nome_usuario=campo_nome_usuario.value
        texto_msg=campo_msg.value
        mensagem=f'{nome_usuario}: {texto_msg}'
        pag.pubsub.send_all(mensagem)
        campo_msg.value=''
        pag.update()

    botao_msg= ft.ElevatedButton('enviar', on_click=enviar_msg)
    campo_msg= ft.TextField(label='escreva sua mensagem', on_submit=enviar_msg)
    linha_msg=ft.Row([campo_msg,botao_msg])
    

    # add na pag
    pag.add(titulo)
    pag.add(botiniciar)


# rodar app
# para rodar como site, add: view=ft.WEB_BROWSER
ft.app(main, view=ft.WEB_BROWSER)