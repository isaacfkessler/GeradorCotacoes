# -----> PASSO 1 - IMPORTAR O TKINTER

from tkinter import *    # Biblioteca utilizada para as janelas, sempre importar dessa maneira
import requests  # Para a API

# -----> PASSO 2 - JOGAR O CÓDIGO PARA DENTRO DE UMA FUNÇÃO

def pegar_cotacoes():   # Função Lógica do aplicativo
    requisicao = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']   # DOLAR X REAL
    cotacao_euro = requisicao_dic['EURBRL']['bid']    # EURO X REAL
    cotacao_btc = requisicao_dic['BTCBRL']['bid']     # BITCOIN X REAL

    texto = f'''        
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BitCoin: {cotacao_btc}'''       # TEXTO A SER EXIBIDO

    texto_cotacoes['text'] = texto      # Após a função ser chamada, passa o novo valor de Texto para a váriavel

# -----> PASSO 3 - CRIAR JANELA USANDO TKINTER

janela = Tk()  # Inicializando a janela
janela.title('Cotação atual das Moedas')   # Título da Janela
#janela.geometry('400x400') ## Para regular tamanho da janela, NÃO utilizada no projeto.
texto_orientacao = Label(janela, text='Clique no botão para ver as cotações das moedas.')  # Cria textos
texto_orientacao.grid(column=0, row=0, padx=10, pady=20)   # Posicionamento do texto

botao = Button(janela, text='Gerar cotações DÓLAR/EURO/BTC', command=pegar_cotacoes)  # Criar botão
botao.grid(column=0, row=1)  # Posicionamento do botão

texto_cotacoes = Label(janela, text='')   # Cria texto vazio, sendo modificado após o clique para mostrar cotações.
texto_cotacoes.grid(column=0, row=2, pady=10)  # Posicionamento do texto


janela.mainloop()  # Essencial no fim do código para manter a janela aberta.
