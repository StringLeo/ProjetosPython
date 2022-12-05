from pytube import YouTube

def download(link):
    youtube = YouTube(link)

    try:
        print("Informações do vídeo:")
        print("Título:", youtube.title)
        print("Visualizações:", youtube.views)
        print(f"Tamanho: {youtube.length}MB")
        youtube = youtube.streams.get_highest_resolution()
        print("Resolução:", youtube.resolution)
        print("\nBaixando...")
        youtube.download()
    except TypeError as e:
        print(e)
    print("\nVideo baixado com sucesso")

link = input("Digite a URL do video: ")
download(link)
