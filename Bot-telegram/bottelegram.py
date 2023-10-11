import telebot
import qrcode

CHAVE_API = "6487915515:AAGfwE6Z-C_rdFid8r9CSeWkQvBFINWGkk0"

bot = telebot.TeleBot(CHAVE_API) 

def generate_qr_code(mensagem):
    qr = qrcode.make(mensagem.text)
    qr.save('qrcode.png')
    with open('qrcode.png', 'rb') as photo:
        bot.send_photo(mensagem.chat.id, photo)

@bot.message_handler(commands=["conversao"])
def conversao(mensagem):
    texto = "Vamos começar a conversão. \n\nColoque o link para conversão."
    bot.send_message(mensagem.chat.id, texto)

    bot.register_next_step_handler(mensagem, generate_qr_code)


@bot.message_handler(commands=["help"])
def conversao(mensagem):
      print(mensagem)
      bot.send_message(mensagem.chat.id,"Você solicitou ajuda.\n\nO nosso bot é um conversor de um link web para um Qr code. Com o QrCode, você pode acessar links por meio da da camera do seu celular.\n\nPara fazer a conversão digite ou clique em \n/conversao para converter link em QrCode.")


def verificar(mensagem):
        return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = "Olá! \nAqui é o Bot Gerador de QrCode. \n\nEscolha alguma opção para continuar (Clique no item desejado). \n\nPara fazer a conversão, digite ou clique em  /conversao de link para QrCode. \n\nPara qualquer duvida, digite ou clique /help"
    bot.reply_to(mensagem,texto)

bot.polling()