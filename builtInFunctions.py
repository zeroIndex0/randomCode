#
#
#
# builtInFunctions.py

# Notes:    We will be covering some of pythons built-in functions
#
#			All:
#				Takes an iterable as an argument and returns true if all elements are truthy ( or if the iterable is empty )			
#
#
#			Any:
#				Return Ture if any element of the iterable is truthy.  If the iterable is empty return False
#
#
#			Sorted:
#				Returns a new sorted LIST from the items in iterable.  Works on anything thats iterable
#				it returns a sorted copy, DOES NOT change the item
#				You can even change the direction of the sort 'sorted(item, reverse=True)'
#				If you use sorted on a dictionary, you have to tell it how to sort since it ambigious without instructrion
#					so you would do sometihng like sorted(dictionary, key = 'how_you_want_to_sort_it')
#					you can even use a lambda for the key(dictionary, key = 'lambda function: to sort')
#
#
#
#			Max:
#				Return the largest item in an iterable or the largest of two or more arguments
#				Also takes a 'key' argument like Sorted and can have a lambda tossed in there
#
#			Min:
#				Return the smallest item in an iterable or the smallest of two or more arguments
#				Also takes a 'key' argument like Sorted and can have a lambda tossed in there
#
#			Reversed:
#				Return a reverse iterator ( so is that the 'end' then? like in iterator::end()
#				Can also be used with strings
#				So yeah, this is basically an iterator to the end of something like you would get in C++
#
#			Len:
#				Returns the lengt of an object ( the number of items in an object )
#				The argument can be a sequence (such as a string, tuple, list or range ) or a collection ( such as a dictionary, set )
#
#			Abs:
#				Returns the absolute value of a number. The argument may be an integer or a float only
#				side note: there is something called fabs() in 'import math' that will always return a float
#
#			Sum:
#				Takes an iterable and an optional start
#				Returns the sum of start and the items of an iterable from LEFT to RIGHT and returns the total
#				Start default to 0
#				side note: there is something called fsum() in 'import math' that will be more precise sum for floats
#
#			Round:
#				Return number rounded to ndigits percision after the deciaml point.
#				If ndigits is omitted or is None, it returns the nearest integer to its input
#
#			Zip:
#				Make an iterator that aggregates elements from each of the iterables.
#				Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument
#				sequences or iterables.
#				The iterator stops when the shortest input interable is exhausted
#					Image you have two lists of numbers of the exact same length. It pairs up the two and zips them together
#				Zips aren't really the best way to create what we have created, but its important to know it exists


#these examples are using comprehension which returns to us a list.  We dont often need a list taking up memeory
print("")
############################################# ALL #####################################################
print(all([0,1,2,3]))										#False
print(all([char for char in 'eio' if char in 'aeiou']))		#True
print(all([num for num in [4,2,10,6,8] if num % 2 == 0]))	#True
print("")

people = ['Charlie', 'Casey', 'Cody', 'Carly', 'Cristina']
print(all([name[0] == 'C' for name in people]))				#Do the names all start with C? True
nums = [2, 60, 26, 18]
#you have to do the conditional logic at the start of the function.  Too much back and forth kinda stuff, tbh its either start or end or middle
#depending on which type of comprehension youre attempting to use, not confusing at all, sure
print(all(num % 2 == 0 for num in nums))					#True
nums.append(17)
print(all(num % 2 == 0 for num in nums))					#False after append
print("")


############################################ ANY ######################################################
print(any([0,1,2,3]))
print(any([num % 2 == 0 for num in nums]))
print(any([num % 2 == 2 for num in nums]))
print("")


# we dont have to use the comprehension brackets
#this gives us something called a generator object, or something like that
#if we dont want a list on what we are checking and if we are just checking, then we dont need to return all that data
#so if we dont need to store it, there is no reason to have a list returned back to us
print(all(name[0] == 'C' for name in people))


#showing the different sizes in memory from the comprehension and the generator object
import sys
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp   = sys.getsizeof( x * 10 for x in range(1000) )

print("to do the same thing, it takes...")
print(f"List Comprehension:   {list_comp} bytes")		#4516 bytes
print(f"Generator Expression: {gen_exp} bytes")			#48   bytes  HUGE Difference
print("")
#end showing the difference in sizes of memeory




#implement a function that accepts a single iteraboe and returns true if it contains ONLY strings, otherwise return false
def is_all_strings(a_list):
	# return all(type(data) == 'str' for data in a_list)			#hmm, how do i check if something is a string or not?
	return all(type(data) == str for data in a_list)				#oh, right no '' around str... of course
	return all([type(data) == str for data in a_list])				#can also use comprehension to get a list back, but not really needed here

people = ['Charlie', 'Casey', 'Cody', 'Carly', 'Cristina']
print(is_all_strings(people))




######################################### SORTED ################################################
#not sort()

more_numbers = [6, 1, 8, 4]
print(sorted(more_numbers))
print(more_numbers)				#it returns a sorted copy, DOES NOT change the item, unlike sort() that changes the item
print("")


#You can even change the direction of the sort 'sorted(item, reverse=True)'
print(sorted(more_numbers, reverse = True))
print(more_numbers)				#again, its a copy of whats passed in and doesnt change whats passed in, important to know
print("")

#just to show its on more that just lists, here a tuple
a_tuple = (23, 654, 5, 2, 4)
print(sorted(a_tuple))			#but, do note that it returns a list, eventhough it was passed a tuple
print("")



#what about when you have a dictionary?
users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": [], "color": "orange"},
	{"username": "bob123", "tweets": [], "num": 69},
	{"username": "BobSAL", "tweets": ["I'm not comfortable with life"], "misses": "Time spent with Jane"},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": [], "loves": "penis", "hates": "Macho Men"}
]

#cannot do sorted(users)  sorted cant tell what is what in terms of sorting, you have to give it a paramter in order to sort
print(sorted(users, key = len))		#sort on length
print("")

print(sorted(users, key = lambda user: user["username"]))			#sort based on username
print("")

print(sorted(users, key = lambda active: len(active["tweets"])))					#sorts least amount of tweets to highests amount
print(sorted(users, key = lambda active: len(active["tweets"]), reverse = True))	#sorts highest amount of tweets to lowest amount
print("")


songs = [
	{"title": "city lights", "playcount": 46},
	{"title": "danger danger danger", "playcount": 100},
	{"title": "the less i know the better", "playcount": 34},
	{"title": "hold on let go", "playcount": 87},
]

print(sorted(songs, key = lambda plays: plays["playcount"]))
print("")
print(sorted(songs, key = lambda plays: plays["playcount"], reverse = True))
print("")



######################################### MAX and MIN ################################################

print(max(4, 55, 638, 343))
print(max('a', 'b', "A", 'F'))
# print(max(songs, users))     #hmm, says it cant work on dictionaries?
nums = [52, 25, 634, 26, 25, 56]
print(max(nums))
print("")

names = ["Arya", "Samson", "Dora", "Tim", "Ollivander"]
print(max(names))
print(min(names))			#its based off of the alphabet, so not length, if you want length you have to specify length
print(max(len(name) for name in names))
#you could return a list and then check that if you want
print([max(len(name) for name in names)])
print([min(len(name) for name in names)])	#but, if it only returns the min or max, why whould you want to do that? but you can
#but what if we want the actual name and not just a length?  Then we need a lambda
print(max(names, key = lambda name: len(name)))
print(min(names, key = lambda name: len(name)))
print("")


songs = [
	{"title": "city lights", "playcount": 46},
	{"title": "danger danger danger", "playcount": 100},
	{"title": "the less i know the better", "playcount": 34},
	{"title": "hold on let go", "playcount": 87},
]

print(min(songs, key = lambda song: song['playcount']))
print(max(songs, key = lambda song: song['playcount']))
#for this one you are passing title at the end to find the title.  If you think about when the return hits, is how this is pulled off
#its saying print( max(playcount)['title'] ) and the return of max playcout will be the entry "title": "song_name" so it works
print(max(songs, key = lambda song: song['playcount']) ['title'])
print(min(songs, key = lambda song: song['playcount']) ['title'])
print("")


#doing it without lambdas
the_max = 0
the_max_title = ""
for song in songs:
	if song["playcount"] > the_max:
		the_max = song['playcount']
		the_max_title = song["title"]
print(the_max, the_max_title)
print("")



#exercise:  write a function which accepts an iterable and returns a TUPLE with the min and max value
def extremes(an_iterable):
	top = max(an_iterable)
	bottom = min(an_iterable)
	return (bottom, top)
print(extremes([1,2,4,5,67]))



######################################### REVERSED ################################################
#not reverse()

#so yeah, this is basically an iterator to the end of the item, like you would get in C++
reversed_item = reversed("hello world")
reversed_item_finished = ""
for char in reversed_item:
	reversed_item_finished += char
print(reversed_item_finished)

#of course you could just use a slice
print("hello world"[::-1])
print("")

#or you could so something fancy like:
rev_list = list(reversed("hello"))
rev_string = ''.join(rev_list)
print(rev_string)
print("")

#can also be used in a range
for x in reversed(range(0, 10)):
	print(x)
print("")


########################################### LEN ######################################################

#we've used this a lot already
print(len("stuff"))
print(len(nums))
print(len(users))
print("")


########################################### ABS - SUM - ROUND   ################################################

print(abs(5))
print(abs(-5))
print(abs(3.5))
print(abs(-3.5))
print("")

print(sum([1,2,3]))
#with a starting points, basically adds values starting with 'starting point'
print(sum([1,2,3], 10))
print(sum([1,2,3], -6))
print(sum((1.5, 2, 3.7)))
# print(sum([1,4,5,6], [4,5,2,6])) cannot do two lists
print("")


print(round(10.2))
print(round(10.8))
print(round(10.8, None))
print(round(10.8, 10))			#not really sure what the ndigits is at this point ( the 2nd entry here )
print(round(10.89857345, 4))	#the second value is how many decimal places to round to
print(round(1.212121, 2))		#not really sure what the ndigits is at this point... OOHHH its decimmal places to round to
print("")



#exercise: write a function that accepts a single list full of numbers.  It should return the magintude of the number
#with the largest magnitude ( the number that is furthest away from zero )
def max_magnitude(a_list):
	return max(abs(num) for num in a_list)
print(max_magnitude([300, 20, -900]))
print("")


#write a function that accepts a number of inputs and returns the sum of all the even values that were input
def sum_even_values(*args):
	return sum(v for v in args if v % 2 == 0)
print(sum_even_values(1,2,3,4,5,6))
print("")



########################################### ZIP ############################################################

first_zip = zip([1,2,3], [4,5,6])
print(list(first_zip))

first_zip = zip([1,2,3], [4,5,6])
print(dict(first_zip))
print("")

nums1 = [1,2,3,4,5]
nums2 = [6,7,8,9,10,11,12]		#its stops when the shortest one is finished and it will cut off 11 and 12 in this example
z = zip(nums1, nums2)			#Notice its a list of TUPLES
print(list(z))
print("")

words = ['hi', 'lol', 'haha', ':)']
z = zip(words, nums1, nums2)
print(list(z))
print("")

#you can unpack in list using the * operator
#the first item of each is matched with each other and the second item of each are matched with each other
five_by_two = [(0,1), (1,2), (2,3), (3,4), (4,5)]
print(list(zip(*five_by_two)))
print("")


############### More complext zip examples
midterms = [80, 91, 78]
finals   = [98, 89, 53]
students = ['dan', 'ang', 'Jane']

# final_grades = {'dan': 98, 'ang': 91, 'Jane': 78}   #this is the end result were looking for

# using zip with dictionary comprehension
final_grades = {pair[0]: max(pair[1], pair[2]) for pair in zip(students, midterms, finals)}
# print(list(zip(max(midterms, finals))))    #the above is the same things as doing this line of code however its all different now

print(final_grades)
print("")

#this gives the highest scores
scores = dict( zip( students, map( lambda pair: max(pair), zip(midterms, finals) ) ) )
print(scores)
print("")

#changing the lambda to get an average grade
average_grades = scores = dict( zip( students, map( lambda pair: (pair[0] + pair[1]) / 2, zip(midterms, finals) ) ) )
print(average_grades)
print("")



#Exercise:  write a function that interleaves to strings 'hi', 'ha' returns 'hhia'
def interleave(string1, string2):
	result = []
	result = list(zip(string1, string2))
	result = [''.join(item) for item in result]
	result = ''.join(item for item in result)
	return result

print(interleave('hi', 'ha'))
print(interleave('aaa', 'zzz'))
print(interleave('lzr', 'iad'))
print("")

#or just ONE LINE IT XD  this looks so strange  This one was all me too, baby!
def interleave(string1, string2):
	return ''.join(item for item in [''.join(item) for item in list(zip(string1, string2))])
print(interleave('hi', 'ha'))
print(interleave('aaa', 'zzz'))
print(interleave('lzr', 'iad'))
print("")



#exercise:  write a function that takes a list of strings and returns a list that filters our any number not divisible by 4 and
#			then tripples each remaining number

def triple_and_filter(a_list):
	return [num * 3 for num in filter(lambda n: n % 4 == 0, a_list)]

print(triple_and_filter([1,2,3,4]))
print(triple_and_filter([6,8,10,12]))
print("")


#exercise:  write a function that accepts a list of dictionaries and retusn a new list of strings with the first and last name keys in each
#			dictionary concatenated
def extract_full_name(a_list):
	#this works just fine, but i feel like he wasnt wanting this type of solution
	return [name['first'] + ' ' + name['last'] for name in a_list]
	

names = [{'first': 'Jane', 'last': 'Doe'}, {'first': 'Guy', 'last': 'Lewis'}, {'first': 'Bob', 'last': 'Smith'}]
print(extract_full_name(names))
print("")

