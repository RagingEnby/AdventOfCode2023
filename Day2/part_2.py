with open('input.txt', 'r') as file:
  input = [line.strip() for line in file]

def get_rounds(game):
  game = game.replace('Game ', '')
  game_split = game.split(': ')
  game_num = int(game_split[0])
  rounds = game_split[1].split('; ')
  rounds = [round.split(', ') for round in rounds]
  return game_num, rounds

colors = ['red', 'green', 'blue']
def process_round(round):
  #[
  #  "4 red",
  #  "9 green",
  #  "4 blue"
  #]
  processed_round = {color: 0 for color in colors}
  for color in colors:
    for round_color in round:
      if color in round_color:
        processed_round[color] = int(round_color.split(' ')[0])
  return processed_round

def read_games():
  game_data = {}
  for game in input:
    game_num, rounds = get_rounds(game)
    game_data[game_num] = [process_round(round) for round in rounds]
  return game_data

def get_mins(game):
  mins = {color: 0 for color in colors}
  for round in game:
    for color in round:
      if round[color] > mins[color]: mins[color] = round[color]
  return mins['red'], mins['green'], mins['blue']
      

def main():
  games = read_games()

  powers = []
  for game in games:
    min_r, min_g, min_b = get_mins(games[game])
    print(f'Game {game}: {min_r, min_g, min_b}')
    powers.append(min_r * min_g * min_b)
  final_answer = 0
  for power in powers:
    final_answer += power
  print('Final answer:', final_answer)
  

main()