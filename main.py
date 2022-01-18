#pip install pytube
#pip install PyQt5


from pytube import YouTube
import os
from PyQt5 import uic,QtWidgets

def baixarMp4():

    url = telaInicial.labelUrl.text()
    try:
        telaInicial.labelAlerta.setText('')
        urlVideo = YouTube(url)
        video = urlVideo.streams.get_highest_resolution()
        video.download(output_path='C:/Users/Usu/Downloads')
        telaInicial.labelAlerta.setStyleSheet('color:gray')
        telaInicial.labelAlerta.setText('Vídeo salvo na pasta download')
    except:
        telaInicial.labelAlerta.setStyleSheet('color:red')
        telaInicial.labelAlerta.setText('Erro ao tentar baixar Arquivo')


def baixarAudio():

    url = telaInicial.labelUrl.text()
    try:
        urlAudio = YouTube(url)
        audio = urlAudio.streams.filter(only_audio=True)[0]
        audio.download(output_path='./audio')
        converterMp3()
    except Exception:
        telaInicial.labelAlerta.setStyleSheet('color:red')
        telaInicial.labelAlerta.setText('Erro ao tentar baixar Arquivo')


def converterMp3():

    telaInicial.labelAlerta.setText('')
    nomeMusica = os.listdir('audio')
    nomeMusica = str(nomeMusica)
    nomeMusica = nomeMusica.replace("['","")
    nomeMusica = nomeMusica.replace("']","")
    nomeMusicaMp3 = nomeMusica.replace('mp4','mp3')
    try:
        os.rename(f'audio/{nomeMusica}',
                  f'C:/Users/Usu/Downloads/{nomeMusicaMp3}')
        telaInicial.labelAlerta.setStyleSheet('color:gray')
        telaInicial.labelAlerta.setText('Áudio salvo na pasta download')
    except:
        telaInicial.labelAlerta.setStyleSheet('color:red')
        telaInicial.labelAlerta.setText('Erro ao Baixar: Arquivo já existe')
        os.remove(f'audio/{nomeMusica}')


# Interface Gráfica
tela = QtWidgets.QApplication([])
telaInicial = uic.loadUi('tela_inicial.ui')
telaInicial.show()
telaInicial.botaoMp3.clicked.connect(baixarAudio)
telaInicial.botaoMp4.clicked.connect(baixarMp4)
tela.exec()






