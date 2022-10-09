class Filme:
  def __init__(self, nome, ano, duracao, likes):
    self.__nome = nome.title()
    self.ano = ano
    self.duracao = duracao
    self.__likes = likes

  @property
  def likes(self):
    return self.__likes
  def dar_like(self):
    self.__likes += 1

  @property
  def nome(self):
    return self.__nome
  
  @nome.setter
  def nome(self, novo_nome):
    self.__nome = novo_nome.title()

vingadores = Filme('Vingadores - guerra infinita', 2018, 160, 10)

print(f'Nome: {vingadores.nome} \nAno: {vingadores.ano} \nTemporadas: {vingadores.duracao} \nLikes: {vingadores.likes}')

