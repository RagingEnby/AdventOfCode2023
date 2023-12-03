import os

def run_day(day_number):
  script_path = f'Day{day_number}/main.py'

  if os.path.exists(script_path):
    exec(open(script_path).read())
  else:
    print(f"{day_number} is not yet completed :(")

def main():
  try:
    to_run = int(input('Which day would you like to run? > '))

    if 1 <= to_run <= 25:
      run_day(to_run)
    else:
      exit("Not a valid integer between 1 and 25")

  except ValueError:
    exit("Invalid integer")

if __name__ == "__main__":
  main()