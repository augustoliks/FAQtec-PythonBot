import telepot
import json
from telepot.namedtuple import ForceReply, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

load = open("token.json")   # Lendo o Json que contém o token do bot
token = json.loads(load.read()) # Inserindo o token bot a variavel "token"
bot = telepot.Bot(token['token'])   # Inserindo o token no Bot

def condicoes(chatID, msg):
        #    tipoMsg, tipoChat, chatID = telepot.glance(msg) #Forma facilitada pela biblioteca do
            if(msg == '/start'):
                    inicio(chatID, bot)

########################### CURSOS
            elif(msg == 'Cursos'):
                    bot.sendMessage(
                        chatID,
                        "Cursos oferecidos pela Fatec Profº Jessen Vidal",
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Análise e Desenvolvimento de Sistemas", callback_data='ADS')],
                                [InlineKeyboardButton(text="Automação e Manufatura Digital", callback_data='ATM')],
                                [InlineKeyboardButton(text="Banco de Dados", callback_data='BD')],
                                [InlineKeyboardButton(text="Gestão da Produção Industrial", callback_data='GPI')],
                                [InlineKeyboardButton(text="Gestão Empresarial", callback_data='GE')],
                                [InlineKeyboardButton(text="Logística", callback_data='LOG')],
                                [InlineKeyboardButton(text="Manutenção de Aeronaves", callback_data='MA')],
                                [InlineKeyboardButton(text="Projetos de Estruturas Aeronáuticas", callback_data='PEA')]
                            ]
                        )
                    )
            elif(msg == 'ADS'):
                    txt = open('CursosOferecidos/ADS.md','r')
                    bot.sendMessage(
                        chatID,
                        txt.read(),
                        'Markdown',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Matriz Curricular", callback_data='matADS')]
                            ]
                        )
                    )
                    txt.close()

            elif(msg == 'matADS'):
                    bot.sendMessage(chatID, "Enviando Matriz Curricular...")
                    doc = open ("CursosOferecidos/matCurADS.pdf",'rb')
                    bot.sendDocument(chatID, doc)
                    doc.close()

            elif(msg == 'ATM'):
                    txt = open('CursosOferecidos/ATM.md','r')
                    bot.sendMessage(
                        chatID,
                        txt.read(),
                        'Markdown',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Matriz Curricular", callback_data='matATM')]
                            ]
                        )
                    )
                    txt.close()

            elif(msg == 'matATM'):
                    bot.sendMessage(chatID, "Enviando Matriz Curricular...")
                    doc = open ("CursosOferecidos/matCurATM.pdf",'rb')
                    bot.sendDocument(chatID, doc)
                    doc.close()

            elif(msg == 'BD'):
                    txt = open('CursosOferecidos/BD.md','r')
                    bot.sendMessage(
                        chatID,
                        txt.read(),
                        'Markdown',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Matriz Curricular", callback_data='matBD')]
                            ]
                        )
                    )
                    txt.close()

            elif(msg == 'matBD'):
                    bot.sendMessage(chatID, "Enviando Matriz Curricular...")
                    doc = open ("CursosOferecidos/matCurBD.pdf",'rb')
                    bot.sendDocument(chatID, doc)
                    doc.close()

            elif(msg == 'GPI'):
                    txt = open('CursosOferecidos/GPI.md','r')
                    bot.sendMessage(
                        chatID,
                        txt.read(),
                        'Markdown',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Matriz Curricular", callback_data='matGPI')]
                            ]
                        )
                    )
                    txt.close()

            elif(msg == 'matGPI'):
                    bot.sendMessage(chatID, "Enviando Matriz Curricular...")
                    doc = open ("CursosOferecidos/matCurGPI.pdf",'rb')
                    bot.sendDocument(chatID, doc)
                    doc.close()


            elif(msg == 'GE'):
                    txt = open('CursosOferecidos/GE.md','r')
                    bot.sendMessage(
                        chatID,
                        txt.read(),
                        'Markdown',
                    )
                    txt.close()

            elif(msg == 'LOG'):
                    txt = open('CursosOferecidos/LOG.md','r')
                    bot.sendMessage(
                        chatID,
                        txt.read(),
                        'Markdown',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Matriz Curricular", callback_data='matLOG')]
                            ]
                        )
                    )
                    txt.close()

            elif(msg == 'matLOG'):
                    bot.sendMessage(chatID, "Enviando Matriz Curricular...")
                    doc = open ("CursosOferecidos/matCurLOG.pdf",'rb')
                    bot.sendDocument(chatID, doc)
                    doc.close()


            elif(msg == 'MA'):
                    txt = open('CursosOferecidos/MA.md','r')
                    bot.sendMessage(
                        chatID,
                        txt.read(),
                        'Markdown',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Matriz Curricular", callback_data='matMA')]
                            ]
                        )
                    )
                    txt.close()

            elif(msg == 'matMA'):
                    bot.sendMessage(chatID, "Enviando Matriz Curricular...")
                    doc = open ("CursosOferecidos/matCurMA.pdf",'rb')
                    bot.sendDocument(chatID, doc)
                    doc.close()

            elif(msg == 'PEA'):
                    txt = open('CursosOferecidos/PEA.md','r')
                    bot.sendMessage(
                        chatID,
                        txt.read(),
                        'Markdown',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Matriz Curricular", callback_data='matPEA')]
                            ]
                        )
                    )
                    txt.close()

            elif(msg == 'matPEA'):
                    bot.sendMessage(chatID, "Enviando Matriz Curricular...")
                    doc = open ("CursosOferecidos/matCurPEA.pdf",'rb')
                    bot.sendDocument(chatID, doc)
                    doc.close()

##########################################################################################################

########################### COMO SER ALUNO
            elif (msg == 'Como ser Aluno'):
                    keyboard=ReplyKeyboardMarkup(
                        keyboard=[
                            [
                                KeyboardButton(text="Como se Inscrever"),
                                KeyboardButton(text="Provas Anteriores"),
                                KeyboardButton(text="Vestibular"),
                                KeyboardButton(text="Voltar")
                            ]
                        ],resize_keyboard=True
                    )
                    bot.sendMessage(chatID,"Todas as informações mais relevantes sobre a como se tornar aluno estão aqui...", reply_markup=keyboard)

            elif(msg == 'Como se Inscrever'):
                    txtHelp = open('ComoSerAluno\Textos\comoSeInscrever.md','r')	#Abre o arquivo Hello.md com o atributo leitura
                    bot.sendMessage(chatID,txtHelp.read(),'Markdown')	#Envia mensagem com o conteúdo do arquivo Help.txt
                    txtHelp.close()	#Fecha o arquivo

                    bot.sendMessage(chatID, "Enviando Manual do candidato...")
                    doc = open ("ComoSerAluno/manualCandidato.pdf",'rb')
                    bot.sendDocument(chatID, doc)
                    doc.close()


            elif(msg == 'Provas Anteriores'):
                    bot.sendMessage(chatID, "Enviando Prova do 1 semestre de 2017...")
                    doc = open ("ComoSerAluno/1semestre2017-PROVA.pdf",'rb')
                    bot.sendDocument(chatID, doc)
                    doc.close()

                    bot.sendMessage(chatID, "Enviando gabarito do 1 semestre de 2017...")
                    doc = open ("ComoSerAluno/1semestre2017-GABARITO.pdf",'rb')
                    bot.sendDocument(chatID, doc)
                    doc.close()

                    bot.sendMessage(chatID, "Enviando Prova do 2 semestre de 2017...")
                    doc = open ("ComoSerAluno/2semestre2017-PROVA.pdf",'rb')
                    bot.sendDocument(chatID, doc)
                    doc.close()

                    bot.sendMessage(chatID, "Enviando gabarito do 2 semestre de 2017...")
                    doc = open ("ComoSerAluno/2semestre2017-GABARITO.pdf",'rb')
                    bot.sendDocument(chatID, doc)
                    doc.close()

            elif(msg == 'Vestibular'):
                    txtHelp = open('ComoSerAluno/Textos/vestibular.md','r')	#Abre o arquivo Hello.md com o atributo leitura
                    bot.sendMessage(chatID,txtHelp.read(),'Markdown')	#Envia mensagem com o conteúdo do arquivo Help.txt
                    txtHelp.close()	#Fecha o arquivo

                    bot.sendMessage(chatID,'''Geralmente o vestibular ocorre nas escolas Estevam Ferri(Endereço: R. Cantídio Miragaia, 100 - Monte Castelo, São José dos Campos - SP, 12215-110)\nMarechal Rondon (Endereço: Praça Francisco Escobar, 165 - Monte Castelo, São José dos Campos - SP, 12215-170)\nambas em São José dos Campos''')

                    bot.sendMessage(chatID,"Enviando a localização da escola Estevam Ferri ...")
                    bot.sendLocation(chatID, -23.1829646,-45.8747777)

                    bot.sendMessage(chatID,"Enviando a localização da escola Marechal Rondon...")
                    bot.sendLocation(chatID, -23.183795, -45.874392)

########################### COMO CHEGAR
            elif (msg == 'Como Chegar'):
                    txtHelp = open('ComoChegar/Textos/txt01.md','r')	#Abre o arquivo Hello.md com o atributo leitura

                    keyboard=ReplyKeyboardMarkup(
                        keyboard=[
                            [
                                KeyboardButton(text="Fatec no Mapa"),
                                KeyboardButton(text="Imagens"),
                                KeyboardButton(text="Voltar")
                            ]
                        ],
                        resize_keyboard=True
                    )

                    bot.sendMessage(chatID,	txtHelp.read(),'Markdown', reply_markup=keyboard)

                    txtHelp.close()	#Fecha o arquivo

            elif(msg == 'Fatec no Mapa'):
                    bot.sendMessage(chatID,"Enviando localização...")
                    bot.sendLocation(chatID, -23.162578,-45.7967319)

            elif (msg == 'Imagens'):
                    bot.sendMessage(chatID, "Enviando imagem...")
                    imgFatec = open("ComoChegar/Imagens/VistaFatec01.jpg","rb")
                    bot.sendPhoto(chatID, imgFatec)
                    imgFatec.close()
##########################################################################################################

########################### SOBRE A FATEC
            elif (msg == 'Sobre a Fatec'):
                    txtHelp = open('SobreFatecSjc/Textos/introducaoSobreAFatec.md','r')	#Abre o arquivo Hello.md com o atributo leitura
                    keyboard=ReplyKeyboardMarkup(
                        keyboard=[
                            [
                                KeyboardButton(text="+ Sobre Fatec"),
                                KeyboardButton(text="Projetos"),
                                KeyboardButton(text="Regulamento Interno"),
                                KeyboardButton(text="Voltar")
                            ]
                        ],resize_keyboard=True
                    )
                    bot.sendMessage(chatID, txtHelp.read(), 'Markdown', reply_markup=keyboard)
                    txtHelp.close()

            elif (msg == '+ Sobre Fatec'):
                    txtHelp = open('SobreFatecSjc/Textos/sobreFatec.md','r')
                    bot.sendMessage(chatID, txtHelp.read(), 'Markdown')
                    txtHelp.close()
                    bot.sendContact(chatID, "551239054979", "FatecSJC", "01")
                    bot.sendContact(chatID, "551239052423", "FatecSJC", "02")
                    bot.sendContact(chatID, "551239054699", "FatecSJC", "03")

            elif (msg == 'Regulamento Interno'):
                    bot.sendMessage(chatID, "Enviando regulamento...")
                    doc = open ("RegulamentoInterno/regulamentoGeral.pdf",'rb')
                    bot.sendDocument(chatID, doc)
                    doc.close()

#### Projetos
            elif (msg== 'Projetos'):
                    bot.sendMessage(
                        chatID,
                        "Projetos atuais da Fatec Profº Jessen Vidal",
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Agencia Inova CPS", callback_data='Agencia Inova')],
                                [InlineKeyboardButton(text="BAJA", callback_data='BAJA')],
                                [InlineKeyboardButton(text="Relações Internacionais", callback_data='Relações Internacionais')],
                                [InlineKeyboardButton(text="Cimatech", callback_data='Cimatech')],
                                [InlineKeyboardButton(text="Escola de Inovadores", callback_data='Escola de Inovadores')],
                                [InlineKeyboardButton(text="Escritório de Carreiras", callback_data='Escritório de Carreiras')],
                                [InlineKeyboardButton(text="Fatec Business Mentoring", callback_data='FBM')],
                                [InlineKeyboardButton(text="Projeto IBM HACKaTruck", callback_data='Projeto IBM HACKaTruck')],
                                [InlineKeyboardButton(text="Vestec", callback_data='Vestec')],
                                [InlineKeyboardButton(text="Megazord", callback_data='Megazord')],
                            ]
                        )
                    )

            elif (msg=="Agencia Inova"):
                    bot.sendMessage(chatID, "Aguarde um instante...")

                    txt = open('SobreFatecSjc/Textos/Projetos/agenciaInovaPaulaSouza.md','r')
                    img = open("SobreFatecSjc/imgProjetosInternos/imgAgenciaInovaPaulaSouza.jpg","rb")
                    bot.sendPhoto(chatID, img, txt.read())
                    txt.close()
                    img.close()

                    txtPP = open('SobreFatecSjc/Textos/Projetos/agenciaInovaPaulaSouzaPP.md','r')
                    bot.sendMessage(chatID,txtPP.read(),'Markdown')
                    txtPP.close()

                    bot.sendContact(chatID, "5512987456578", "Renato", "Galvão")

            elif (msg=="BAJA"):
                    bot.sendMessage(chatID, "Aguarde um instante...")

                    txt = open('SobreFatecSjc/Textos/Projetos/baja.md','r')
                    img = open("SobreFatecSjc/imgProjetosInternos/imgBajaSaeBrasil.png","rb")
                    bot.sendPhoto(chatID, img, txt.read())
                    txt.close()
                    img.close()

                    txtPP = open('SobreFatecSjc/Textos/Projetos/bajaPP.md','r')
                    bot.sendMessage(chatID,txtPP.read(),'Markdown')
                    txtPP.close()

                    bot.sendMessage(chatID, "Aguarde um momento, estamos carregando a foto do projeto...")

                    imgPP = open("SobreFatecSjc/imgProjetosInternos/imgBaja01.jpg","rb")
                    bot.sendPhoto(chatID, imgPP, "Foto do projeto em 2015")
                    imgPP.close()

            elif (msg=="Relações Internacionais"):
                    bot.sendMessage(chatID, "Aguarde um instante...")

                    txt = open('SobreFatecSjc/Textos/Projetos/nucleoDeRelacoesInternacionais.md','r')
                    img = open("SobreFatecSjc/imgProjetosInternos/imgNucleoDeRelacoesInternacionais.jpg","rb")
                    bot.sendPhoto(chatID, img, txt.read())
                    txt.close()
                    img.close()

                    txt = open('SobreFatecSjc/Textos/Projetos/nucleoDeRelacoesInternacionaisPP.md','r')
                    bot.sendMessage(chatID,txt.read(),'Markdown')
                    txt.close()

            elif (msg=="Escola de Inovadores"):
                    bot.sendMessage(chatID, "Aguarde um instante...")
                    bot.sendSticker(chatID, "CAADAQADNQYAAjN-VQp9fRoNVhK8sQI")

                    txt = open('SobreFatecSjc/Textos/Projetos/escolaDeInovadores.md','r')
                    img = open("SobreFatecSjc/imgProjetosInternos/imgEscoladeInovadores.png","rb")
                    bot.sendPhoto(chatID, img, txt.read())
                    txt.close()
                    img.close()

                    txt = open('SobreFatecSjc/Textos/Projetos/escolaDeInovadoresPP.md','r')
                    bot.sendMessage(chatID,txt.read(),'Markdown')
                    txt.close()

            elif (msg=="Escritório de Carreiras"):
                    bot.sendMessage(chatID, "Aguarde um instante...")

                    txt = open('SobreFatecSjc/Textos/Projetos/escritorioDeCarreiras.md','r')
                    img = open("SobreFatecSjc/imgProjetosInternos/imgEscritorioDeCarreiras.png","rb")
                    bot.sendPhoto(chatID, img, txt.read())
                    txt.close()
                    img.close()

                    txt = open('SobreFatecSjc/Textos/Projetos/escritorioDeCarreirasPP.md','r')
                    bot.sendMessage(chatID,txt.read(),'Markdown')
                    txt.close()

            elif (msg=="FBM"):
                    bot.sendMessage(chatID, "Aguarde um instante...")

                    txt = open('SobreFatecSjc/Textos/Projetos/fbm.md','r')
                    img = open("SobreFatecSjc/imgProjetosInternos/imgFBM.png","rb")
                    bot.sendPhoto(chatID, img, txt.read())
                    txt.close()
                    img.close()

                    txt = open('SobreFatecSjc/Textos/Projetos/fbmPP.md','r')
                    bot.sendMessage(chatID,txt.read(),'Markdown')
                    txt.close()

                    bot.sendContact(chatID, "551239054979", "ContatoFBM", "01")
                    bot.sendContact(chatID, "551239052423", "ContatoFBM", "02")
                    bot.sendContact(chatID, "551239054699", "ContatoFBM", "03")


            elif (msg=="Projeto IBM HACKaTruck"):
                    bot.sendMessage(chatID, "Aguarde um instante...")

                    txt = open('SobreFatecSjc/Textos/Projetos/projetoIBMHACKaTruck.md','r')
                    img = open("SobreFatecSjc/imgProjetosInternos/imgHackTruck03.jpg","rb")
                    bot.sendPhoto(chatID, img, txt.read())
                    txt.close()
                    img.close()

                    txt = open('SobreFatecSjc/Textos/Projetos/projetoIBMHACKaTruckPP.md','r')
                    bot.sendMessage(chatID,txt.read(),'Markdown')
                    txt.close()

                    txt = open('SobreFatecSjc/Textos/Projetos/projetoIBMHACKaTruckLink.md','r')
                    bot.sendMessage(chatID,txt.read(),'Markdown')
                    txt.close()

                    txt = open('SobreFatecSjc/Textos/Projetos/projetoIBMHACKaTruckYT.md','r')
                    bot.sendMessage(chatID,txt.read(),'Markdown')
                    txt.close()

            elif (msg=="Vestec"):
                    bot.sendMessage(chatID, "Aguarde um instante...")

                    txt = open('SobreFatecSjc/Textos/Projetos/vestec.md','r')
                    img = open("SobreFatecSjc/imgProjetosInternos/imgVestec.png","rb")
                    bot.sendPhoto(chatID, img, txt.read())
                    txt.close()
                    img.close()

                    txt = open('SobreFatecSjc/Textos/Projetos/vestecPP.md','r')
                    bot.sendMessage(chatID,txt.read(),'Markdown')
                    txt.close()

            elif (msg=="Megazord"):
                    bot.sendMessage(chatID, "Aguarde um instante...")

                    txt = open('SobreFatecSjc/Textos/Projetos/megazord.md','r')
                    img = open("SobreFatecSjc/imgProjetosInternos/imgMegazord.png","rb")
                    bot.sendPhoto(chatID, img, txt.read())
                    img.close()
                    txt.close()

                    txt = open('SobreFatecSjc/Textos/Projetos/megazordPP.md','r')
                    bot.sendMessage(chatID,txt.read(),'Markdown')
                    txt.close()

                    img = open("SobreFatecSjc/imgProjetosInternos/imgMegazord01.jpg","rb")
                    bot.sendPhoto(chatID, img)
                    img.close()

                    img = open("SobreFatecSjc/imgProjetosInternos/imgMegazord02.jpg","rb")
                    bot.sendPhoto(chatID, img)
                    img.close()

                    bot.sendMessage(chatID,"https://www.youtube.com/user/MegazordAerodesign")
                    bot.sendMessage(chatID,"https://www.facebook.com/megazordaerodesign?hc_ref=ARTOOGrhjaoVa14Y36pTJtl6rInOIgA928tr-YknVHuiL2RRHBKKQwji2kGgggUb89o")
                    bot.sendMessage(chatID,"Para mais informações entre em contato com: Carlos ou Murilo")

                    bot.sendContact(chatID, "5512988281517", "Carlos", "Megazord")
                    bot.sendContact(chatID, "5512997527525", "Murilo", "Megazord")

##########################################################################################################

            elif (msg == 'Voltar'):
                    inicio(chatID, bot)


def callback(msg):
            query_id, from_id, query_data = telepot.glance(msg, flavor="callback_query")
            chatID = from_id
            texto = query_data
            print(chatID)
            bot.answerCallbackQuery(query_id, text="Só um instante")
            print("callback query", query_id, from_id, query_data)
            condicoes(chatID, texto)

def ir(msg):
            tipoMsg, tipoChat, chatID = telepot.glance(msg)

            texto = msg['text']
            condicoes(chatID, texto)


def inicio(chatID, bot):
            keyboard=ReplyKeyboardMarkup(
                        keyboard=[
                            [
                                KeyboardButton(text="Como ser Aluno"),
                                KeyboardButton(text="Como Chegar"),
                                KeyboardButton(text="Cursos"),
                                KeyboardButton(text="Sobre a Fatec"),
                            ]
                        ],resize_keyboard=True
                    )

            txt = open('Inicializacao/Hello.md','r')
            bot.sendMessage(chatID,txt.read(),'Markdown',reply_markup=keyboard)
            txt.close()

bot.message_loop(
    {
        'chat': ir,
        'callback_query': callback,
    }
)

while True:
            pass
