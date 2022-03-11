import random
import time
import sys
# import cv2
from termcolor import colored , cprint
def crashcount ():
  global crashcounting
  # crashcounting += 1

value = ["moving speed", "training speed", "sea moving speed", "vessel building speed", "wepond durability", "wepond building speed", "buffs"]
default = [1,1,0,0,1,1,'null']
city = ['Ghufran', 'Mariln', 'Shae', 'Sae republic', 'Alibe', 'Naztmic', 'Nehc']
#0-3
def exp(x):
  x += wars//2
class seas:
  the_seas = [1,0,3,1,0,2,'']
  king_of_sea = [1,0,3,3,0,3,'tsanumi']
  sea_empire = [2,1,3,2,1,2,'rain']
class grassland:
  the_grass = [2,1,0,1,2,3,'']
  grass_explorer = [3,2,1,2,2,3,'speed']
  united_grasses = [2,2,1,3,2,3,'united']
class cliffs:
  the_mountainers = [1,1,2,3,1,2,'']
  the_minesquad = [3,2,0,3,3,3,'master']
  gold_empire = []
class caves:
  the_wepondaries = [1,2,0,3,2,3, 'iron age']
  the_originals = [3,3,0,3,3,3,'master']
  the_miners = [2,2,1,3,3,3,'vainemine']
class plateau:
  the_tribes = [1,1,0,1,1,1,'united']
  class the_peoples:
    the_humans = [2,2,1,2,2,2,'united']
    the_supremes = [3,2,2,3,3,2,'united']
  the_gods = [2,2,2,2,2,2,'united']
class arctics:
  the_northens = [2,1,1,1,1,1,'raid']
  ice_empire = [2,1,3,]
  vikings = [3,1,2,3,1,1,'raid']
class woods:
  the_spirits = [3,2,2,0,1,0,'']
class sky:
  the_aeros = [3,2,1,0,2,0,'quickcharge']
  aviacion_legend = [3,2,1,1,1,1,'total victory']
  the_wings = [3,3,3,0,0,0, 'air supremecy']
# tsanumi = damage 659
# rain = heal +20, enemy food supply - 10 (not in use for the sky)
# master = every slot +1, and slot with 3 +2
# speed = moving speed,training speed, sea moving speed, vessel building speed, wepond building speed +1
# united

imput = input("press enter to start ")
if imput == 0:
  debug = True
  print ("debug")
else:
  debug = False
  print (colored("starting the game..." , "blue" , attrs = ['blink']))
  time.sleep(1)
  print (colored("starting the system..." , "green" , attrs = ['blink']))
  time.sleep(1)
  print (colored("importing user service and setting ..." , "yellow" , attrs = ['reverse' , "blink"]))
  time.sleep(1)
  print (colored("inputting server data and debugging errors, adding errors. ..." , "red"))
  debug = False
  time.sleep(1)
  print (colored("initializing code..." , "cyan", attrs = ["reverse"]))
  wars = int()
  i = int(1)
  religion = str()
  text = str()
  print ("done")
logo = 'MCHIGM'
print (logo + "'" + 's' , "text game")
while i == 1:
  if debug == False:
    print (colored("Bought to you by B&B python" , "yellow", attrs = ["blink"]))
  else:
    print (title)
  print ("press 1 for the sea")
  print ("press 2 for the land")
  print ("press 3 for the mountins")
  print ("press 4 for the valleys")
  print ("press 5 for the deserts")
  print ("press 6 for the snows")
  print ("press 7 for the forests")
  print ("press 8 for the arrows")
  choose = int(input(colored("what is your choice", 'yellow', attrs=['blink','reverse'])+ ":_ "))
  if choose == int(0):
    if debug == False:
      print (colored("##debug mode ***" , "green"))
      debug = True
    else:
      i = 1
  elif choose == int(1) :
    choose = seas
    i = 0
  elif choose == int(2) :
    choose = grassland    
    i = int(0)
  elif choose == int(3) :
    choose = cliffs
    i = int(0)
  elif choose == int(4) :
    choose = caves
    i = int(0)
  elif choose == int(5) :
    choose = plateau
    i = int(0)
  elif choose == int(6) :
    choose = arctics
    i = int(0)
  elif choose == int(7) :
    choose = woods
    i = int(0)
  elif choose == int(8) :
    i = int(0)
    choose = sky
  elif choose == int(9) :
    if debug == true:
      debug = False
      print (colored("debug shutdown" , "red"))
    else: 
      cprint ("plese choose numbers between the above" , "blue")
  else:
    print ('plese choose numbers between the above')
    i = 1
if debug == False :
  print (colored(choose, "blue" , attrs=['blink']))
  place = random.choice(city)
  if place == 'Ghufran' :
    place = 'the mainland, Ghufran'
  elif place == 'Marlin' :
    place = 'the island, Marlin'
  elif place == 'Shae' :
    place = 'the ancient superpower, Shae'
  elif place == 'Sae republic' :
    place = 'the yongest and the richest country of Napolia, the Sae republic'
  elif place == 'Alibe' :
    place = 'the place where the most furious and most friendly humans live, Alibe'
  elif place == 'Naztmic':
    place = 'the militarized country, Naztmic'
  elif place == 'Nehc' :
    place = 'the start of culture, the country of Nehc'
  else:
    print (colored("server crashed :/ please restart the server", "blue", attrs=['blink']))
    # crashcount()
  if choose == seas :
    print ("The seas were born to be masters at swimming, they live in the costal area of" , place + ".")
  if choose == grassland:
    print ("The grasslanders were fast and good at building, they out standing construction skills can even use paper to defend a coannon. They live in the plain of" , place + ".")
  if choose == cliffs:
    print ("The cliffmans were good at mining. Low-education level didn't bother them for a strong civilization, they were the mountainers from" , place + ".")
  if choose == caves:
    print ("" , place + ".")
  if choose == plateau:
    print ("" , place + ".")
  if choose == arctics:
    print ("" , place + ".")
  if choose == woods:
    print ("" , place + ".")
  if choose == sky:
    print ("" , place + ".")
  if place = 
if debug == True:
  debug = False
  print (choose)
  # print (crashcounting)
  # crashcounting + 1
  text = ("<class ", "'" + "__main__." + random.choice(city) + "'>")
  print (colored(text, 'yellow',attrs=['reverse']))
  time.sleep(2)
  print (city)
  print (choose)
# x = input()
# for i in range (len(x), 0, -1):
#   print(x[i-1], end="")
# n = "Together, We Fight the Virus!"
# for i in range(1) :
#   n = len(n)
# print (n)
