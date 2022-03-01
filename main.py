import random
wars = int()
i = int(1)
religion = str()
debug = False
value = ["moving speed", "training speed", "sea moving speed", "vessel building spped", "wepond durability", "wepond building speed", "buffs"]
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
  the_mountainers = []
  the_minesquad = [3,2,0,3,3,3,'master']
  gold_empire = []
class caves:
  the_originals = [3,3,3,3,3,3,'master']
class plateau:
  the_tribes = []
class arctics:
  the_northens = []
  ice_empire = []
  vikings = []
class woods:
  the_spirits = []
class sky:
  the_aeros = [3,2,1,0,2,0,'quickcharge']
  aviacion_legend = [3,2,1,1,1,1,'total victory']
  the_wings = [3,3,3,0,0,0, 'air supremecy']
tsanumi = damage 50
rain = heal +20, enemy food supply - 10 (not in use for the sky)

logo = 'MCHIGM'
print (logo + "'" + 's' , "text game")
while i == 1:
  print ("press 1 for the sea")
  print ("press 2 for the land")
  print ("press 3 for the mountins")
  print ("press 4 for the valleys")
  print ("press 5 for the deserts")
  print ("press 6 for the snows")
  print ("press 7 for the forests")
  print ("press 8 for the arrows")
  choose = int(input("what is your choice:_ "))
  if choose == 0:
    print ("##debug mode ***")
    debug = True
  elif choose == (1) :
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
  else:
    print ('plese choose numbers between the above')
    i = 1
if debug == False :
  print (choose)
  place = random.choice(city)
  print ("<class ", "'" + "__main__." + place + "'>")
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
    print ("server crashed :/ please restart the server")
  if choose == seas :
    print ("The seas were born to be masters at swimming, they live in the costal area of" , place , end = ".")
  if choose == grassland:
    print ("The grasslanders were fast and good at building, they out standing construction skills can even use paper to defend a coannon. They live in the plain of" , place , end = ".")
  if choose == cliffs:
    print ("The cliffmans were good at mining. Low-education level didn't bother them ")
    