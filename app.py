from rich import print
import os

# Constantes
VOTOS_BOLSONARO = 0
VOTOS_LULA = 0

# Rodar eternamente
while True:
  print('*'*20)
  # Apresentar os candidatos
  print(f'[on blue]TOTAL BOLSONARO:[/] {VOTOS_BOLSONARO}{os.linesep}[on red]TOTAL LULA:[/] {VOTOS_LULA}')
  print('*'*20)

  # Permita votar
  voto = int(input(f'Para quem gostaria de votar?{os.linesep}1 - Bolsonaro{os.linesep}2 - Lula{os.linesep}Seu voto: '))
  try:
    if voto == 1:
      VOTOS_BOLSONARO += 1
    elif voto == 2:
      VOTOS_LULA += 1
    else:
      pass
  except:
    print('Digite apenas 1 ou 2')
    os.system('pause')
  
  os.system('cls')