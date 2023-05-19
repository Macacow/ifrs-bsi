from datetime import time
from musica import Musica
from album import Album
from tipos import Pais
from tipos import Genero
from playlist import Playlist
from artista import Artista


playlists= []

artista01 = Artista("Jaozim", True, Pais.BRAZIL, Genero.RAP)
musica01 = Musica("Vamo dale", time(minute=1, second=4))
album01 = Album("Furacão", "Tropinha")
playlist01 = Playlist("Trabalhando...")
musica01.tocar()

artista01.add_album(album01)
album01.add_artista(artista01)

artista01.add_musica(musica01)
musica01.add_artista(artista01)

musica01.add_album(album01)
album01.add_musica(musica01)

playlist01.add_musica(musica01)
musica01.add_playlist(playlist01)

playlists.append(f"{musica01}")


artista02 = Artista("Jhon", True, Pais.UK, Genero.FUNK)
musica02 = Musica("Funk do Jhon", time(minute= 3, second= 45))
album02 = Album("Só Funks", "GravaFunk")
musica02.tocar()
musica02.tocar()
musica02.tocar()

artista02.add_album(album02)
album02.add_artista(artista02)

artista02.add_musica(musica02)
musica02.add_artista(artista02)

musica02.add_album(album02)
album02.add_musica(musica02)

playlist01.add_musica(musica02)
musica02.add_playlist(playlist01)

playlists.append(f"{musica02}")

artista03 = Artista("Artista 3 sla", True, Pais.RU, Genero.PAGODE)
musica03 = Musica("Sambalaiê", time(minute= 10, second= 45))
album03 = Album("Churrasco", "Grava Churrasco")
playlist02 = Playlist("Músicas para Churrasco Vol. 1000")
musica03.tocar()

artista03.add_album(album03)
album03.add_artista(artista03)

artista03.add_musica(musica03)
musica03.add_artista(artista03)

musica03.add_album(album03)
album03.add_musica(musica03)

playlist02.add_musica(musica03)
musica03.add_playlist(playlist02)

playlists.append(f"{musica03}")

artista04 = Artista("O Rockeiro", True, Pais.USA, Genero.ROCK)
musica04 = Musica("A Paulada", time(minute= 2, second= 0))
album04 = Album("Músicas para paulada", "Grava Paulada")
musica04.tocar()
musica04.tocar()

artista04.add_album(album04)
album04.add_artista(artista04)

artista04.add_musica(musica04)
musica04.add_artista(artista04)

musica04.add_album(album04)
album04.add_musica(musica04)

playlist02.add_musica(musica04)
musica04.add_playlist(playlist02)

playlists.append(f"{musica02}")

artista05 = Artista("Bob", True, Pais.EU, Genero.REGGAE)
musica05 = Musica("Wanna Love Ya", time(minute= 20, second= 6))
album05 = Album("Mutch Love", "LoveLove")
musica05.tocar()
musica05.tocar()
musica05.tocar()
musica05.tocar()

artista05.add_album(album05)
album05.add_artista(artista05)

artista05.add_musica(musica05)
musica05.add_artista(artista05)

musica05.add_album(album05)
album05.add_musica(musica05)

playlist01.add_musica(musica05)
musica05.add_playlist(playlist01)

playlists.append(f"{musica05}")

print(f"========================== Playlist '{playlist01}' ========================== \n")
for p in playlists:
    print(p)

print(f"========================== Playlist '{playlist02}' ========================== \n")
for p in playlists:
    print(p)
