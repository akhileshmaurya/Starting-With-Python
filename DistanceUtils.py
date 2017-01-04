import math
import json


def manhatanDistance(x1, y1, x2, y2):
    distance = math.abs(x1 - x2) + math.abs(y1 - y2)
    return distance


def euclidianDistance(x1, y1, x2, y2):
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return distance


data = []
with open('data.txt') as json_data:
    data = json.load(json_data)
    #print(data)
    for key in data:
        print key
        print data[key]

'''Lets assume we have some Some rating based on user we have to
 read this and parse the json --
 {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0,
"Norah Jones": 4.5, "Phoenix": 5.0,
  "Slightly Stoopid": 1.5,
   "The Strokes": 2.5, "Vampire Weekend": 2.0},
  {"Blues Traveler": 2.0, "Broken Bells": 3.5,
   "Deadmau5": 4.0, "Phoenix": 2.0,
   "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
  {"Blues Traveler": 5.0, "Broken Bells": 1.0,
   "Deadmau5": 1.0, "Norah Jones": 3.0,
   "Phoenix": 5, "Slightly Stoopid": 1.0},
  {"Blues Traveler": 3.0, "Broken Bells": 4.0,
   "Deadmau5": 4.5, "Phoenix": 3.0,
   "Slightly Stoopid": 4.5, "The Strokes": 4.0,
   "Vampire Weekend": 2.0},
  {"Broken Bells": 4.0, "Deadmau5": 1.0,
   "Norah Jones": 4.0, "The Strokes": 4.0,
   "Vampire Weekend": 1.0},
  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0,
   "Phoenix": 5.0, "Slightly Stoopid": 4.5,
   "The Strokes": 4.0, "Vampire Weekend": 4.0},
  {"Blues Traveler": 5.0, "Broken Bells": 2.0,
   "Norah Jones": 3.0, "Phoenix": 5.0,
   "Slightly Stoopid": 4.0,  "The Strokes": 5.0},
"Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0,
             "Phoenix": 4.0,  "Slightly Stoopid": 2.5,
             "The Strokes": 3.0}}'''
