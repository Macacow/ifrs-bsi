from datetime import date
from datetime import time
from album import Album
from musica import Musica
from artista import Artista

artista01 = Artista("AC/DC")
artista02 = Artista("Jorge")

musica01 = Musica("Highway to Hell", time(minute=3, second=5), artista01, artista01)
musica02 = Musica("Amiga da Munha Mulher", time(minute=4), artista02, artista02)
musica03 = Musica("Hells Bells", time(second=55), artista01, artista01)
musica04 = Musica("Mina do Condomínio", time(minute=2, second=30), artista02, artista02)
musica05 = Musica("TNT", time(minute=3), artista01, artista01)

album01 = Album("Rock Pauleira", artista01, musica01)
album02 = Album("Músicas para Churrasco Vol. 2", artista02, musica02)
album03 = Album("Músicas para Churrasco Vol. 3", artista02, musica04)

album01.add_musica(musica03)
album01.add_musica(musica05)

musica01.add_album(album01)
musica02.add_album(album02)
musica03.add_album(album01)
musica04.add_album(album03)
musica05.add_album(album01)

album01.lancar(date(2023, 5, 19))
album02.lancar(date(2023, 4, 18))
album03.lancar(date(2023, 3, 17))

musica01.tocar()
musica01.tocar()
musica01.tocar()

musica02.tocar()
musica02.tocar()
musica02.tocar()

musica03.tocar()
musica03.tocar()
musica03.tocar()

musica04.tocar()
musica04.tocar()
musica04.tocar()

musica05.tocar()
musica05.tocar()
musica05.tocar()

print("==== Quantidade de Plays de Cada Artista ====\n")

plays01 = artista01.exibir_plays()
print(plays01)

plays02 = artista02.exibir_plays()
print(plays02)

print("\n==== Exibindo Albuns ====\n")

print(album01)
print()
print(album02)
print()
print(album03)