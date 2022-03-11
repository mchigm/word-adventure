worldborder_width = 61
worldborder_height = 3*worldborder_width-31
worldborder_width_space = str(" ") * 61
i = int()
j = int()
i = int(0)
j = int(0)
# for i in range (0,worldborder_height):
#   for j in range (0,worldborder_width):
#     print ("*", end = "")
for i in range (0,worldborder_width):
  print ("*", end = "")
for i in range (0,worldborder_height):
  print ("*", end = worldborder_width_space)
## print (worldborder_width_space)