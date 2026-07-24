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
  print("Value : %d" % (value))
# Looping through the Keys in Order : 
for key in sorted(color.keys()):
  print(f"Color : {key}")
# For Getting only Unique Values (Duplicate Values are not Repeated) :
for value in set(color.values()):
  print("Value : %d" % (value))

# List of Dictionaries : 
color = {'black' : 1, 
        'blue' : 2, 
        'grey' : 3
        }
sub = {'phy' : 1, 
        'math' : 2, 
        'chem' : 3
        }
l = [color,sub]
print(l[0]['blue'])  #>>> 2

# Nested Dictionaries :
users = {
         'HB': {
                  'first': 'Homi',
                  'last': 'Bhabha',
         },
         'VS': {
                  'first': 'Vikram',
                  'last': 'Sarabhai',
         }
}
print(users['HB'])

