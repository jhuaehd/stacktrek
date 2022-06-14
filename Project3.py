from time import sleep
import sys

string = "The Battle Cats For Life" # Whatever string you want

for letter in string:
  sleep(0.15) # In seconds
  sys.stdout.write(letter)
  sys.stdout.flush()
