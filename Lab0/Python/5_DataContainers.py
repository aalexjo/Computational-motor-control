#!/usr/bin/env python3

"""This script explains the different ways in Python to store and group data.
The three major ways in which you store data are
1. Lists
2. Tuple
3. Dictionaries"""

import cmc_pylog as pylog  # Import pylog to log messages

# Lists
# properties: ordered, iterable, mutable, can contain multiple data types
pylog.info(3*'\t' + 20*'#' + ' LISTS ' + 20*'#' + 3*'\n')

# create an empty list (two ways)
empty_list = []
empty_list = list()

# create a list
course = ['computational', 'motor', 'control']

# examine a list
pylog.info("Examine the first element of the course : {}".format(
    course[0]))     # print element 0 ('homer')

pylog.warning('Indexing in Python starts from 0 and not 1')

pylog.info("Print the length of the list : {}".format(
    len(course)))   # returns the length (3)

# modify a list (does not return the list)
course.append('I')                 # append element to end
pylog.info(".append : {}".format(course))

course.extend(['love', 'Python'])  # append multiple elements to end
pylog.info(".extend : {}".format(course))

# insert element at index 0 (shifts everything right)
course.insert(0, '2019 : ')
pylog.info(".insert : {}".format(course))

# search for first instance and remove it
course.remove('Python')
pylog.info(".remove : {}".format(course))

course.pop(0)                         # remove element 0 and return it
pylog.info(".pop : {}".format(course))

del course[0]                         # remove element 0 (does not return it)
pylog.info("del element [0] : {}".format(course))

course[0] = '?????????????'                  # replace element 0
pylog.info("replace element [0] : {}".format(course))

# concatenate lists
students = course + ['student1', 'student2', 'student3']
pylog.warning("This method is slower than \'.extend\' method")

# find elements in a list
course.count('motor')      # counts the number of instances
pylog.info('Number of instances of motor in the list : {}'.format(
    course.count('motor')))

# list slicing [start:end:step]
pylog.info('Indexing or slicing in Python [start:end:step]')
weekdays = ['mon', 'tues', 'wed', 'thurs', 'fri']
weekdays[0]         # element 0
weekdays[0:3]       # elements 0, 1, 2
weekdays[:3]        # elements 0, 1, 2
weekdays[3:]        # elements 3, 4
weekdays[-1]        # last element (element 4)
weekdays[::2]       # every 2nd element (0, 2, 4)
weekdays[::-1]      # backwards (4, 3, 2, 1, 0)

pylog.info('Try to see if there are other methods to reverse a list')

# sort a list in place (modifies but does not return the list)
course.sort()
course.sort(reverse=True)     # sort in

# create a second reference to the same list
pylog.info('Copying lists only creates a new reference and not a new list')

same_course = course
same_course[0] = 0         # modifies both 'course' and 'same_course'

pylog.info(
    'Element 0 in course : {}\nElement 0 in same_course : {}'.format(
        course[0],
        same_course[0]
    )
)

# copy a list (two ways)
new_course = course[:]
pylog.info('To make a new copy of a list use slicing methods')

# examine objects
# returns True (checks whether they are the same object)
course is same_course
course is new_course          # returns False
# returns True (checks whether they have the same contents)
course == same_course
course == new_course          # returns True


# TUPLES
pylog.info(3*'\t' + 20*'#' + ' TUPLES ' + 20*'#' + 3*'\n')

pylog.info('Tuples are like lists but don\'t change in size')

# Create a tuple
pylog.info('Tuples are created with \'(...)\' or using the keyword tuple')

digits = (0, 1, 'two')  # Create a tuple directly
digits = tuple([0, 1, 'two'])  # Create a tuple from list
pylog.warning('A trailing comma is required to indicate its a tuple')
zero = (0,)

# examine a tuple
digits[2]           # returns 'two'
len(digits)         # returns 3
digits.count(0)     # counts the number of instances of that value (1)
digits.index(1)     # returns the index of the first instance of that value (1)

# elements of a tuple cannot be modified
try:
    digits[2] = 2       # throws an error
except BaseException:
    pylog.error('Tuples cannot be edited once initialized')

# concatenate tuples
digits = digits + (3, 4)

# create a single tuple with elements repeated (also works with lists)
(3, 4) * 2          # returns (3, 4, 3, 4)

# sort a list of tuples
tens = [(20, 60), (10, 40), (20, 30)]
sorted(tens)        # sorts by first element in tuple, then second element
#   returns [(10, 40), (20, 30), (20, 60)]

# tuple unpacking
bart = ('male', 10, 'simpson')  # create a tuple
(sex, age, surname) = bart      # assign three values at once


# DICTIONARY
pylog.info(3*'\t' + 20*'#' + ' DICTIONARY ' + 20*'#' + 3*'\n')

# properties: unordered, iterable, mutable, can contain multiple data types
# made of key-value pairs
# keys must be unique, and can be strings, numbers, or tuples
# values can be any type

# create an empty dictionary (two ways)
pylog.info(
    'Dictionaries are created with \'{...}\' or using the keyword dict')

empty_dict = {}
empty_dict = dict()

# create a dictionary (two ways)
family = {'dad': 'homer', 'mom': 'marge', 'size': 6}
family = dict(dad='homer', mom='marge', size=6)

# convert a list of tuples into a dictionary
list_of_tuples = [('dad', 'homer'), ('mom', 'marge'), ('size', 6)]
family = dict(list_of_tuples)

# examine a dictionary
family['dad']       # returns 'homer'
len(family)         # returns 3
'mom' in family     # returns True
'marge' in family   # returns False (only checks keys)

# returns a list (Python 2) or an iterable view (Python 3)
list(family.keys())       # keys: ['dad', 'mom', 'size']
list(family.values())     # values: ['homer', 'marge', 6]
# key-value pairs: [('dad', 'homer'), ('mom', 'marge'), ('size', 6)]
list(family.items())

# modify a dictionary (does not return the dictionary)
family['cat'] = 'snowball'              # add a new entry
family['cat'] = 'snowball ii'           # edit an existing entry
del family['cat']                       # delete an entry
family['kids'] = ['bart', 'lisa']       # dictionary value can be a list
# remove an entry and return the value ('homer')
family.pop('dad')
family.update({'baby': 'maggie', 'grandpa': 'abe'})   # add multiple entries

# access values more safely with 'get'
family['mom']                       # returns 'marge'
family.get('mom')                   # equivalent

try:
    # throws an error since the key does not exist
    family['grandma']
except BaseException:
    pylog.error(
        'Key grandma does not exist. Try using get method instead to check the keys')

family.get('grandma')               # returns None instead

family.get('grandma', 'not found')  # returns 'not found' (the default)

# access a list element within a dictionary
family['kids'][0]                   # returns 'bart'
family['kids'].remove('lisa')       # removes 'lisa'

# string substitution using a dictionary
'youngest child is %(baby)s' % family   # returns 'youngest child is maggie'

