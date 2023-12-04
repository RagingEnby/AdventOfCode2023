max_red = 12
max_green = 13
max_blue = 14

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
    

def is_possible(r, g, b):
  return r <= max_red and g <= max_green and b <= max_blue


def main():
  games = read_games()

  final_answer = 0
  for game in games:
    game_data = games[game]
    game_possible = True
    for round in game_data:
      r, g, b = (round['red'], round['green'], round['blue'])
      if not is_possible(r, g, b):
        game_possible = False
        break
    if game_possible: final_answer += game

  print('Final answer:', final_answer)
  

main()