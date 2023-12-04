import os

def run(day, part):
  script_path = f'Day{day}'

  os.chdir(script_path)
  os.system(f'python3 part_{part}.py')

def main():
  try:
    day = int(input('Which day would you like to run? > '))
    part = int(input('Which part would you like to run? > '))
    run(day, part)

  except ValueError:
    exit("Invalid integer")

if __name__ == "__main__":
  main()