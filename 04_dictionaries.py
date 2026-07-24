# Creating a Dictionary :
color = {'black' : 1, 
         'blue' : 2, 
         'grey' : 3
        }
color['white'] = 4  # Adding a key-value pair
color['grey'] = 5  # Changing a value
del color['blue']  # Removing a key value pair

# Accessing Key-Value Pairs from Dictionary using Loop :
for key, value in color.items():
  print("{} : {}".format(key,value))
for key in color.keys():
  print(f"Color : {key}")
for value in color.values():
  print("Value : %d",value)
