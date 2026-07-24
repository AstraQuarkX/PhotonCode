# Tuples are immutable
numbers = (2,3,4,5)

# Creating a Tuple : 
  # Normal Method :
     squares = ()
     for i in range(1,10):
         squares += (i**2,)
  # Generator Method :
     squares = tuple(i**2 for i in range(1,10))
  # Normal Method : 
     numbers = (2,4,6,8)
  # Generator Method :
     numbers = tuple(range(2,9,2))

# Slicing and Indexing are same as lists
# Values can be added only by concatenation and typing a ',' at the end
# Tuple elements can't be deleted or updated 
