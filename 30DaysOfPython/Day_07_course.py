# Empty Set creation:
st = set()

# Set with items creation:
st = {'item1', 'item2', 'item3', 'item4'}

#  Will I learn how this is different from a list...

fruits = {'banana', 'orange', 'mango', 'lemon'}

# len() is length, as expected
print(len(fruits))
# 4

# Checking for an item in a set, using "in" membership operator
print("Does set fruits contain an orange?", 'orange' in fruits)
# Does set fruits ... orange? True

# Add an item using "add()"

fruits.add('lime')
print(fruits)
# {lemon', 'orange', 'mango', 'lime', 'banana'}
# wait huh? they're out of order. inchresting. wonder why... 

# add multiple items using update() but the items need to be formatted as a list. Again. How is this different than a list. 
st.update(['item5', 'item6', 'item7'])
print(st)
#{'item3', 'item6', item2', 'item1', 'item4', 'item5', 'item7'}
# different because it's out of order??!??!?!?!??!?

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
fruits.update(vegetables)
print(fruits)
# {'banana', 'tomato', 'lemon', 'potato', 'carrot', onion', 'mango', 'cabbage', 'orange'}

# Removing items with remove(), but if it's not there, there will be an error. Discard will try to remove but will not error out.abs

st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
print(st)
# {'item3', 'item4', 'item1'}

# pop() removes a random item from a set and returns the removed item. Neat
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()
print(f"{fruits}; no longer has {removed_item}!!!")

# to empty out a set, use clear(), the result is "set()"
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
print(st)
# set()

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) 
# set()

# Deleting a set with del
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits

# Swapping between List and Set: Removes duplicates and only keeps unique items
lst = ['item1', 'item2', 'item3', 'item4', 'item1', 'item3']
st = set(lst)
print(st) # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered

fruits = ['banana', 'orange', 'mango,' 'lemon', 'orange', 'banana']
fruits = set(fruits) # {'mango, 'lemon', 'banana', 'orange'}

# Joining Sets: union() or update() or |

# Union returns a new set
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2) #st3 = st1 | st2

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'otato', 'cabbage', 'onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', carrot', tomato', banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
# can also use: print(fruits | vegetables)

# Update inserts a set into a given set
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # (will contain item1 to item8)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

# Intersection, aka items that are in both sets. use intersection() or &
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {}'item3, 'item2'}
# or st1 & st2

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 3, 4 ,6, 8, 10}
whole_numbers.intersection(even_numbers) # {this is just even numbers....?}
# whole_numbers & even_numbers

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.intersection(dragon)) # {'o', 'n'}
# python & dragon

# Checking Subset and Super Set

# a set can be a subset or super set of other sets. What does this mean
# Subset: issubset()
# Super set: issuperset()

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) #True
st1. issuperset(st2) #True

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False

# Checking the Difference between two sets

# returns the differences between two sets, using difference() or -
stl = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.difference(st1)) # set() : st2 - st1 retuns empty because "negative"? removes 1, 2, 3, 4 from 2 & 3.
print(st1.difference(st2)) # {'item1', 'item4'} => st1\st2 : st2 - st1 removes 2 & 3 from 1, 2, 3, 4. 

# Finding Symmetric Difference Between Two Sets
# what the everloving
# contains all items from both sets, except items that are in both sets.abs
# whatever this is mathematically: A\B) ∪ (B\A)

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'} : st2 ^ st1
# it's what I thought difference was going to be?
# all items that are unique to each set

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
# both have 'o' and 'n' so it's the total of both sets but no 'o' and 'n'

# Disjoint Sets

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) #False

even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}

