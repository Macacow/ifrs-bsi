from datetime import time
from artista import Artista
from tipos import Pais, Genero
from musica import Musica
from playlist import Playlist

mc_gebler = Artista("MC Gebler")
mc_gebler.pais = Pais.BRAZIL
mc_gebler.genero = Genero.FUNK
musica_gebler01 = Musica("Música Boa Part. I", time(0, 3, 30))
musica_gebler02 = Musica("Música Boa Part. II", time(0,20, 20))

print(mc_gebler)

playlist_funk = Playlist("Playlist de Funk")
playlist_funk.add_musica(musica_gebler01)
playlist_funk.add_musica(musica_gebler02)

playlist_funk.remove_musica(musica_gebler01)
