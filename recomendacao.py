avaliacoes = {
  'Ana': {
    'Freddy x Jason': 2.5,
    'O Ultimato Bourne': 3.5,
    'Star Trek': 3.0,
    'Exterminador do Futuro': 3.5,
    'Norbit': 2.5,
    'Star Wars': 3.0
  },
  'Marcos': {
    'Freddy x Jason': 3.0,
    'O Ultimato Bourne': 3.5,
    'Star Trek': 1.5,
    'Exterminador do Futuro': 5.0,
    'Star Wars': 3.0,
    'Norbit': 3.5
  },
  'Pedro': {
    'Freddy x Jason': 2.5,
    'O Ultimato Bourne': 3.0,
    'Exterminador do Futuro': 3.5,
    'Star Wars': 4.0
  },
  'Claudia': {
    'O Ultimato Bourne': 3.5,
    'Star Trek': 3.0,
    'Star Wars': 4.5,
    'Exterminador do Futuro': 4.0,
    'Norbit': 2.5
  },
  'Adriano': {
    'Freddy x Jason': 3.0,
    'O Ultimato Bourne': 4.0,
    'Star Trek': 2.0,
    'Exterminador do Futuro': 3.0,
    'Star Wars': 3.0,
    'Norbit': 2.0
  },
  'Janaina': {
    'Freddy x Jason': 3.0,
    'O Ultimato Bourne': 4.0,
    'Star Wars': 3.0,
    'Exterminador do Futuro': 5.0,
    'Norbit': 3.5
  },
  'Leonardo': {
    'O Ultimato Bourne': 4.5,
    'Norbit': 1.0,
    'Exterminador do Futuro': 4.0
  }
}

avaliacoes1 = {
  'Freddy x Jason': {
    'Ana': 2.5,
    'Marcos': 3.0,
    'Pedro': 2.5,
    'Adriano': 3.0,
    'Janaina': 3.0
  },
  'O Ultimato Bourne': {
    'Ana': 3.5,
    'Marcos': 3.5,
    'Pedro': 3.0,
    'Claudia': 3.5,
    'Adriano': 4.0,
    'Janaina': 4.0,
    'Leonardo': 4.5
  },
  'Star Trek': {
    'Ana': 3.0,
    'Marcos': 1.5,
    'Claudia': 3.0,
    'Adriano': 2.0
  },
  'Exterminador do Futuro': {
    'Ana': 3.5,
    'Marcos': 5.0,
    'Pedro': 3.5,
    'Claudia': 4.0,
    'Adriano': 3.0,
    'Janaina': 5.0,
    'Leonardo': 4.0
  },
  'Norbit': {
    'Ana': 2.5,
    'Marcos': 3.0,
    'Claudia': 2.5,
    'Adriano': 2.0,
    'Janaina': 3.5,
    'Leonardo': 1.0
  },
  'Star Wars': {
    'Ana': 3.0,
    'Marcos': 3.5,
    'Pedro': 4.0,
    'Claudia': 4.5,
    'Adriano': 3.0,
    'Janaina': 3.0
  }
}

from math import sqrt

def euclidiana(usuario1, usuario2):
  si = {}

  for item in avaliacoes[usuario1]:
    if item in avaliacoes[usuario2]:
      si[item] = 1  # pega somente as avaliacoes em comum

  if len(si) == 0:
    return 0

  soma = sum([pow(avaliacoes[usuario1][item] - avaliacoes[usuario2][item], 2)
              for item in avaliacoes[usuario1] if item in avaliacoes[usuario2]])  # calcula a distancia euclidiana para avaliacoes em comum

  return 1 / (1 + sqrt(soma))  # coloca em medida relativa 0 -> nao similar 1 -> totalmente similar

def getSimilares(usuario):
  similaridade = [(euclidiana(usuario, outro), outro) for outro in avaliacoes if outro != usuario]  # compara com outros usuarios
  similaridade.sort()  # ordena
  similaridade.reverse()  # reverte para mostrar o mais similar ate o menos similar
  return similaridade

def getRecomendacoes(usuario):
  totais = {}
  somaSimilaridade = {}
  for outro in avaliacoes:
    if outro == usuario:
      continue  # elimina comparação do usuário com ele mesmo
    similaridade = euclidiana(usuario, outro)  # procura a similaridade entre os usuários, pelo cálculo da distancia euclidiana

    if similaridade <= 0:
      continue  # elimina computação se não houver filmes avaliados em comum, ou similaridade

    for item in avaliacoes[outro]:  # percorre todos os filmes avaliados
      if item not in avaliacoes[usuario]:  # pega filmes que não foram assistidos pelo usuário alvo
        totais.setdefault(item, 0)
        totais[item] += avaliacoes[outro][item] * similaridade  # media ponderada
        somaSimilaridade.setdefault(item, 0)
        somaSimilaridade[item] += similaridade
  rankings = [(total / somaSimilaridade[item], item) for item, total in totais.items()]
  rankings.sort()
  rankings.reverse()
  return rankings

def mostrarFilmes(usuarios, filmes):
  if filmes == 'todos':
    for i in usuarios:
      print(f'Avaliação dos filmes pelo usuário {i}')
      for j in avaliacoes1:
        if i in avaliacoes1[j]:
          print(f'Filme {j}: {avaliacoes1[j][i]}')
        else:
          print(f'Filme {j}: sem avaliação')
      print('\n')
  else:
    for i in usuarios:
      print(f'Avaliação do filme {filmes} pelo usuário {i}: {avaliacoes1[filmes][i]}\n')

def filmesUsuarios(filme):
  for i in avaliacoes1[filme]:
    print(i)
  print('\n')

# Mostrar todos os filmes/notas avaliados pelos usuários: Ana e Marcos.
mostrarFilmes(['Ana', 'Marcos'], 'todos')

# Mostrar os filmes/notas com avaliação por Pedro e Leonardo.
mostrarFilmes(['Leonardo', 'Pedro'], 'todos')

# Qual nota foi data pelo Adriano para o filme Norbit?
mostrarFilmes(['Adriano'], 'Norbit')

# Quais usuários avaliaram o filme “Freddy x Jason”?
filme = 'Freddy x Jason'
print(f'Os usuários que avaliaram o filme {filme} foram: {filmesUsuarios(filme)}')

# Quais usuários avaliaram o filme “Star Trek” e o filme “Star Wars”?
filmes_interesse = ["Star Trek", "Star Wars"]

usuarios_star_trek = []
usuarios_star_wars = []

for usuario, avaliacoes_usuario in avaliacoes.items():
  if filmes_interesse[0] in avaliacoes_usuario:
    usuarios_star_trek.append(usuario)
  if filmes_interesse[1] in avaliacoes_usuario:
    usuarios_star_wars.append(usuario)

usuarios_comuns = list(set(usuarios_star_trek) & set(usuarios_star_wars))

if usuarios_comuns:
  print(f"Usuários que avaliaram ambos os filmes '{filmes_interesse[0]}' e '{filmes_interesse[1]}':")
  for usuario in usuarios_comuns:
    print(usuario)
else:
  print("Nenhum usuário avaliou ambos os filmes.")

# Quais as similaridades dos usuários “Janaina”, “Claudia” e “Pedro”?
usuarios_interesse = ["Janaina", "Claudia", "Pedro"]

# Calcular e mostrar as similaridades para cada usuário de interesse
for usuario in usuarios_interesse:
  similaridades = getSimilares(usuario)
  print(f"Similaridades para o usuário {usuario}:")

  for similaridade, outro_usuario in similaridades:
    print(f"Usuário: {outro_usuario}, Similaridade: {similaridade}")

  print("\n")

# Quais as recomendações para os usuários “Pedro”, “Leonardo” e “Ana”?
usuarios_interesse = ["Pedro", "Leonardo", "Ana"]

numero_recomendacoes = 5

for usuario in usuarios_interesse:
  recomendacoes = getRecomendacoes(usuario)
  print(f"Recomendações para o usuário {usuario}:")

  if not recomendacoes:
    print("O usuário já viu todos os filmes.\n")
  else:
    for pontuacao, filme in recomendacoes[:numero_recomendacoes]:
      print(f"Filme: {filme}, Pontuação: {pontuacao}")

  print("\n")
