from editora import Editora
from livro import Livro
from autor import Autor
from datetime import date

editora01 = Editora("0000000001", "João Minella", "Editora Legal 01", "editoralegal1@legal.com")
editora02 = Editora("0000000002", "João Minella", "Editora Legal 02", "editoralegal2@legal.com")
editora03 = Editora("0000000003", "João Minella", "Editora Legal 03", "editoralegal3@legal.com")
editora04 = Editora("0000000004", "João Minella", "Editora Legal 04", "editoralegal4@legal.com")
editora05 = Editora("0000000005", "João Minella", "Editora Legal 05", "editoralegal5@legal.com")

livro01 = Livro("1111111111", "1234567890123")
livro02 = Livro("1111111112", "1234567890124")
livro03 = Livro("1111111113", "1234567890125")
livro04 = Livro("1111111114", "1234567890126")
livro05 = Livro("1111111115", "1234567890127")

autor01 = Autor("Vitor", date(2001, 12, 31), "Chefinho")
autor02 = Autor("João", date(2001, 12, 31), "Minas")
autor03 = Autor("Moisés", date(2001, 12, 31), "Moisa")
autor04 = Autor("Ricardo", date(2001, 12, 31), "Cara de Porto")
autor05 = Autor("Luciano", date(2001, 12, 31), "Gebler")

livro01.add_autor(autor01)
livro01.add_autor(autor02)
livro01.add_autor(autor03)
livro01.remove_autor(autor02)
livro02.add_autor(autor05)

editora01.publicar(livro01)
editora02.publicar(livro02)
editora03.publicar(livro03)
editora04.publicar(livro04)
editora05.publicar(livro05)

autor04.adicionar_livro(livro03)
autor04.adicionar_livro(livro04)

print(livro01.listar_autores())
print(livro02.listar_autores())
print(livro03.listar_autores())
print(livro04.listar_autores())
print(livro05.listar_autores())

print(editora01.listar_livros())
print(editora02.listar_livros())
