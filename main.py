import telepot
import json

class telebot(): #Classe do Bot
    def __init__(self, token):
        self.bot = telepot.Bot(token) #Conexão com o Bot no Telegram
        self.loadData()

        self.bot.message_loop(self.receiveMessages) #Estabelecimento do loop de mensagens
    def loadData(self): #Carrega os Dados (Frases) do bot
        try:
            with open('data/database.json', 'r') as db:
                self.database = json.load(db)
        except FileNotFoundError:
            with open('data/database.json', 'w') as db:
                      database = {} #Os dados estão guardados como um dicionário
                      json.dump(database, db)
            self.loadData()
    def updateData(self): #Atualiza os Dados
        with open('data/database.json', 'w') as db:
            json.dump(self.database, db)
    def create(self, msg): #Cria novas Frases
        msg = msg.replace('cr ', '')
        print(msg)
        try:
            command = msg.split(' r ')[0]
            print(command)
            answer = msg.split(' r ')[1]
            print(answer)
            self.database[command] = answer
            print(command)
            self.bot.sendMessage(self.neoId, 'okay...')
        except:
            self.bot.sendMessage(self.neoId, 'Erro.')
        self.updateData()
    def receiveMessages(self, message): #Trata as Mensagens recebidas
        content_type, chat_type, chat_id = telepot.glance(message)
        print(content_type, chat_type, chat_id)
        self.neoId = chat_id

        if content_type == 'text': #Caso Text
            print('Usuário:', message['text'])
            if message['text'].lower() == 'data reset': #Deleta os dados
                self.database = {}
                self.updateData()
            elif 'cr ' in message['text'].lower(): #Cria frases
                self.create(message['text'].lower())
            elif message['text'].lower() in self.database: #Caso a frase seja reconhecida
                self.bot.sendMessage(chat_id, self.database[message['text'].lower()]) #Frases são convertidas em Minúsculas
            else:
                self.bot.sendMessage(chat_id, 'Não compreendo.') #Caso a frase não seja reconhecida

        else:
            self.bot.sendMessage(chat_id, 'Não consigo compreeender. Lamento.') #Caso não seja do tipo Text


magexp = telebot('473347105:AAGZz6C1GuTaaX-mlm5g9S5I08LlveLyMvs') #Chave do Bot
while True:
    pass
