# I got part 1 done pretty easily. However, I got stuck on part 2 and decided to move on to day 2 and continue solving this later on.

text_numbers = {
  "one": "1",
  "two": "2",
  "three": "3",
  "four": "4",
  "five": "5",
  "six": "6",
  "seven": "7",
  "eight": "8",
  "nine": "9"
}

def get_last_num(char_list):
  last_num = None
  for char in char_list:
    try:
      last_num = int(char)
    
    except ValueError:
      continue
      
  return last_num if last_num else 0

def get_first_num(char_list):
  return get_last_num(reversed(char_list))


def get_num(og_value):
  value = replace_text_nums(og_value)
  char_list = list(value)
  
  first_num = get_first_num(char_list)
  last_num = get_last_num(char_list)
  combined_num = int(f"{first_num}{last_num}")
  print(f"{og_value} - {value} - {combined_num}")
  return combined_num

def replace_text_nums(value):
  index = 0
  while index < len(value):
    for text_num in text_numbers:
      if value[index:].startswith(text_num):
        value = value[:index] + text_numbers[text_num] + value[index + len(text_num):]
        break
    index += 1
  return value

def main():
  sum = 0
  with open('input.txt', 'r') as file:
    for line in file:
      value = line.strip().lower()        
      sum += get_num(value)
  print(f"Found sum (yipee!): {sum}")

main()