from pytube import YouTube
from os import listdir
from os.path import isfile, join

#Mettre le chemin du dossier où vous souhaitez mettre vos musiques
path="C:/Users/emmao/OneDrive/Documents/pytube/"
fichiers = [f for f in listdir(path) if isfile(join(path, f))]
qualities = ["360p","480p","720p","1080p"]

while True :
    try:
        url = input("URL de la vidéo Youtube :\n")
        yt_object=YouTube(url)
        break
    except:
        print("ERREUR : URL invalide\n")

while True:
    try:
        choice = input("Tapez 1 pour convertir en .mp3\nTapez 2 pour convertir en .mp4\n")
        if choice == "1" or choice == "2":
            break
    except:
        print("ERREUR : La saisie n'est pas valide\n")



if choice == "1":
    while True:
        try:
            file_name = input("\nNom du fichier ? (Sans le .mp3) :\n")
            if file_name+".mp3" not in fichiers:
                break
        except:
            print("ERREUR : Ce fichier existe déjà")

    print("Début du téléchargement...")
    audio = yt_object.streams.filter(only_audio = True).first()
    print("Téléchargement en cours...")
    audio.download(output_path=path,filename=file_name+".mp3")
    print("Téléchargement terminé ! \nLe fichier " + file_name+".mp3 est téléchargé dans le dossier :\n" + path)


elif choice =="2":
    while True:
        try:
            file_name = input("\nNom du fichier ? (Sans le .mp4) :\n")
            if file_name+".mp4" not in fichiers:
                break
        except:
            print("ERREUR : Ce fichier existe déjà\n")

    while True:
        try:
            quality = input('Entrez la qualité de la vidéo (360p / 480p / 720p / 1080p) :\n')
            if quality in qualities:
                break
        except:
            print("ERREUR : Cette qualité n'est pas conforme\n") 

    print("Début du téléchargement...")
    video = yt_object.streams.filter(res=quality, file_extension='mp4').first()
    print("Téléchargement en cours...")
    video.download(output_path=path,filename=file_name+".mp4")
    print("Téléchargement terminé ! \nLe fichier " + file_name+".mp4 est téléchargé dans le dossier :\n" + path)
else:
    print("ERREUR")