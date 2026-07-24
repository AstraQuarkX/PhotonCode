# Adding Items to  List :
brand = ['Quark']
brand.append('X')
brand.insert(0,'Astra')  # list.insert(index,value)
brand.extend([3,4,5])    # brand = ['Astra','Quark','X',3,4,5]
brand.extend('xy')       # brand = ['Astra','Quark','X',3,4,5,'x','y']

# Deleting Items from List :
del brand[1]  # del list[index]
     # brand = ['Astra','X',3,4,5,'x','y']
popped_value = brand.pop(1)   # popped_val = list.pop(index) {pop() returns the popped value}
     # brand = ['Astra',3,4,5,'x','y']
     # popped_value = 'X'
brand.remove('x')  # list.remove(value)
     # brand = ['Astra',3,4,5,'y']
     # It removes only the first occurrence of the value

# Sorting a List : 
num = [3,4,2,8,1,9] 
num.sort()  # num = [1,2,3,4,8,9] 
            # Sorts permanently 
            # Numbers in increasing order and words in alphabetical order
num.sort(reverse = True)  # num = [9,8,4,3,2,1]
num2 = sorted(num)  # sorted(list) returns the sorted list, doesn't change the original one
num3 = sorted(num, reverse = True)

# Reversing a List : 
num.reverse()  # Reverses the original list
num4 = num[::-1]  # Creates a new list num4 with elements of list num in reverse order 

print(len(num))  # len(list) returns the number of elements in the list

# Simple Statistics with a List of Numbers :
digits = [1,3,5,7,8,9,100]
Min_Value = min(digits)         # Min_Value = 1
Max_Value = max(digits)         # Max_Value = 100
Sum_of_Values = sum(digits)     # Sum_of_Values = 133

# List Comprehensions : 
  # Normal Method :
     squares = []
     for i in range(1,10):
         squares.append(i**2)
  # List Comprehension Method (One Line) :
     squares = [i**2 for i in range(1,10)]
  # Normal Method : 
     numbers = [2,4,6,8]
  # List Comprehension Method :
     numbers = list(range(2,9,2))

# Slicing a List : 
 # Creates a new list
 # Last value is not taken
  list2 = list1[start:stop:step]
 # Default values : 
   # Start - 0
   # Stop - End of the list
   # Step - -1

# Copying a List
 # Assignment (No Copy) :
  # Both variables refer to the same list.
  # Changes made through one variable are reflected in the other.
   list2 = list1
 # Shallow Copy : 
  # Creates a new outer list.
  # Changes to the outer list do not affect the original list.
  # Nested mutable objects are still shared.
   list2 = list1[:]       # By Slicing
   list2 = list1.copy()   # By copy() Method
   list2 = list(list1)    # By list() Constructor 
