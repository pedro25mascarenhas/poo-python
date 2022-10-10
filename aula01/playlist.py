from modelo import Filme, Serie

class Playlist(list):
  def __init__(self, nome, programas):
    self.nome = nome
    self._programas = programas
  
  @property
  def listagem(self):
    return self._programas

  @property
  def tamanho(self):
    return len(self._programas)


vingadores = Filme('Vingadores', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo Mundo em panico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_like()
atlanta.dar_like()
tmep.dar_like()
demolidor.dar_like()
vingadores.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

print(f'Tamanho da Playlist: {len(playlist_fim_de_semana)}')
for programa in playlist_fim_de_semana.listagem:
  print(programa)

print(f'Ta ou nao ta: {demolidor in playlist_fim_de_semana}')