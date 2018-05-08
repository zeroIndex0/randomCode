#
#
#
# exercises.py

# Notes:	Testing some exercises
#
#



def sum_pairs(a_list, a_number):
	counter = 0
	for number in a_list:
		print(f"Number: {number}  |  Counter: {counter}  |  A_List Len: {len(a_list)}    |  A_List Contents: {a_list}")
		if counter + 1 < len(a_list):
			if number + a_list[counter+1] == a_number:
				return [number, a_list[counter + 1]]
			counter += 1
	return []


print(sum_pairs([4,2,10,5,1], 6))
print(sum_pairs([11,20,4,2,1,5], 100))
print("")


# semi falied code here
data = {}
text = "awesome"
for letter in text:
	count = 0
	if letter in "aeiou":
		count += 1
		print(letter, count)

count = 0
# a simple call to a built in function called count..... worked... heh
data = {letter: text.count(letter) for letter in "aeiou"}
print(data)

#the code that actually worked that was borrowed failry heavly from the instructor
# the above code doesnt work becuase it also retuns blanks for the vowel's that arent in the string
# so the added 'if letter in "aeiou"' is needed to make sure that wont be an issue.  That and making sure the string is .lower()-ed
def vowel_count(a_string):
	return {letter: a_string.lower().count(letter) for letter in a_string if letter in "aeiou"}

print(vowel_count("awesome"))
print("")


# Write a function called titleize which accepts a string of words and resturns a new string with the first letter of every word in teh string capitalized.
# This seems fairly harmless at first, but its enough to have almost killed me.
# I'm sure there is a much cleaner and neater way to do this, but this is what I have

# I feel like there has to be a better way than to create a different list that pushes the values from the one list into the other list, since the one list
# cant have its values chaged.  Just seems like if it wont work for one list then it shouldnt work for another list, but whatever, I used splicing and
# got the job done
def titleize(a_string):
	temp = a_string.split(" ")
	new_list = temp
	print(temp)
	#just need to get this working, but I can't get item[0].upper() to stick... :'(  ( I actually get it to stick by pushing it into a different list )
	#It's just part of the languge, it doesnt work like C++
	count = 0
	for item in temp:
		# item[0] = item[0].upper()   # You would think works.... BUT IT DOESN'T  ( sorry spoilers )
		new_list[count] = item[0].upper() + item[1::]
		count += 1
	print(new_list)
	#sets the list back to a string
	temp = " ".join(new_list)
	return temp

print(titleize("this is awesome"))
print(titleize("oNLy cAPITALIZe fIRSt"))
print("")





# write a function which accepts a collection, a value, and an optinal starting index.  The function should return True if the value exists in the collection
# when we search starting from the starting index. Otherwise, it should return False
# The collection can be a string, a list, or a dictionary. If the collection is a string or array, the thrid parameter is a starting index for where to search
# from.  If the collection is a dictionary, the function searches for the value among values in the dictionary; since objects have no sort order, the thrid
# parameter is ignored

def includes(collection, find_value, pos = 0):
	if type(collection) == list or type(collection) == str:
		count = 0
		for value in collection:
			if count >= pos:
				if value == find_value:
					return True
	else:
		for value in collection:
			if collection[value] == find_value:
				return True
	return False

print(includes([1, 2, 3], 1)) # True 
print(includes([1, 2, 3], 1, 2)) # False 
print(includes({ 'a': 1, 'b': 2 }, 1)) # True 
print(includes({ 'a': 1, 'b': 2 }, 'a')) # False
print(includes('abcd', 'b')) # True
print(includes('abcd', 'e')) # False
print("")



# write a function that takes in two lists and returns a dictionary. The first list is the keys and the second list is the values
# If there are not enough values, the remaining keys should have a value null, if there not enough keys, just ignore the remaining values

# This works for me, but the problem is that keys are not in any sort of order
# This is actually really dangerous since its working here, but could fail later, kinda thing
def two_list_dictionary(list1, list2):
	# item = {}.fromkeys(list1, None)
	item = {key: None for key in list1}
	count = 0
	for key in item:
		if count < len(list2):
			item[key] = list2[count]
		count += 1 

	return item


print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])) # {'a': 1, 'b': 2, 'c': 3, 'd': null}
print(two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4])) # {'a': 1, 'b': 2, 'c': 3}
print(two_list_dictionary(['x', 'y', 'z']  , [1,2])) # {'x': 1, 'y': 2, 'z': null}





# write a function which accepts an NxN list of lists and sums the two main diagonals in the array: the one from
# the upper left to the lower right, and the one from the upper right to the lower left.

def sum_up_diagonals(a_list):
	# So, this changes depending on size. How can i account for the size difference?
	# It's NxN so N will be the size.  Whats some math to account for that
	# N = 2 sum all
	# N = 3 sum edges - middle twice - edges
	# N = 4 sum edges - two middle twice - edges
	# N = 5 sum edges - two from edge - middle twice - two from edge - edges
	# left most corner and right most corner
	# cannot work for a 5x5... so i have to cheese this?
	# len(list) = what to do
	# count = 0
	# while count < len(list):
	# list[0] + list[len(list)]
	# list[1] + list[len(list)-1] # will handle middle being counted twice if thats the case
	#
	#
	# oh, wait a minute...
	# I really really overthought this one, solution is super simple
	count = 0
	total = 0
	while count < len(a_list):
		#Keep pushing in the matrix as you advance rows, as the rows grow larger
		#then the value checking the length becomes smaller and will grab the left value
		total += a_list[count][count] + a_list[count][len(a_list[count])-1-count]
		count += 1
	print(total)
	return total


list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
];
 
sum_up_diagonals(list1); # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
];
 
sum_up_diagonals(list2); # 30
 
list3 = [
  [  4,  1, 0],
  [ -1, -1, 0],
  [  0,  0, 9]
];

sum_up_diagonals(list3); # 11

list4 = [
  [ 1,  2,  3, 4 ],
  [ 5,  6,  7, 8 ],
  [ 9, 10, 11, 12],
  [ 13,14, 15, 16]
];
 
sum_up_diagonals(list4); # 68
print("")
# list5 = [
# 	[1, 2, 3, 4, 5],
# 	[6, 7, 8, 9, 10],
# 	[11,12,13,14,15],
# 	[16,17,18,19,20]
# ] Cannot work for a 5x5

# list6 = [
# 	[1, 2, 3,  4, 5, 6],
# 	[7, 8, 9, 10,11,12],
# 	[13,14,15,16,17,18],
# 	[19,20,21,22,23,24]
# ] Cannot work for a 6x6 either... of course




# write a function that accepts a list and returns the number of times a number is followed by a larger number across the entire list.
# take the example find_greater_numers([6,1,2,7]) # 4 there are 4 times where a number is followed by a greater number:
#	2 > 1
#	7 > 6
#	7 > 1
#	7 > 2

def find_greater_numbers(a_list):
	index = 0
	total = 0
	for num in a_list:
		if index > 0:
			if num > a_list[index - 1]:
				for value in a_list[:index+1:]:
					if num > value:
						total += 1
		index += 1
	return total


print(find_greater_numbers([1,2,3])) # 3 
print(find_greater_numbers([6,1,2,7])) # 4
print(find_greater_numbers([5,4,3,2,1])) # 0
print(find_greater_numbers([])) # 0
print(find_greater_numbers([1,2,3,4,5,6,7])) # 21
print("")



# I needed a character counter, fast. This has nothing to do with the exercises
count = "Hello"
total = 0
for char in count:
	total += 1
print(total)
print("")



# take each number of a passed in number and add a power to it that increases starting at a passed in power
# then if such a number exists that the passed in number * i is equal to the result, return i, otherwise return -1
def dig_pow(number, power):
	increasing_pow = power
	num_list = list(str(number))
	result = 0
	for num in num_list:
		result += pow(int(num), increasing_pow)
		increasing_pow += 1

	print("Result mod number " + str(result % number), "\n")
	if result % number == 0:
		for i in range(1, result):
			if i * number == result:
				return i
	return -1

print(dig_pow(22,    2))	# -1
print(dig_pow(89,    1))	# 1
print(dig_pow(92,    1))	# -1
print(dig_pow(695,   2))	# 2
print(dig_pow(46288, 3))	# 51
print("")



#what are the divisors of a number
def divisors(number):
	result = []
	for i in range(2, number):
		if number % i == 0:
			result.append(i)
	if not result:
		return f"{number} is prime"
	return result

print(divisors(12))
print(divisors(25))
print(divisors(13))
print("")