
"""
This is our first Py4Sudan python basic course. created by Mohamed Ishag

"""

# the first programme we will write is print('Hello, World)
print('Hello, World')


#======== variable =======================================
# we will discuss the concept of variable

# variable = value

song = "song.mp3"
image = "image.png"
text = 'Mohamed Ishag Adam Yahya in Ombada 1950'
num = 1555251655265

print(song)
print(image)
print(text)
print(num)


#========  Data Type  =====================================
# here we will see the basic data type in python

## 1- Numbers:-
# 1-1 int or integer
my_int = 100
my_int_1 = 50

add = my_int + my_int_1
sub = my_int - my_int_1
div = my_int / my_int_1
mul = my_int * my_int_1

print(add)
print(sub)
print(div)
print(mul)


# 1-2 Float
my_float = 12.25
my_float_1 = 4.75

add = my_float + my_float_1
sub = my_float - my_float_1
div = my_float / my_float_1
mul = my_float * my_float_1

print(add)
print(sub)
print(div)
print(mul)


# 1-3 complex
my_complex = 1+2j
my_complex_1 = 2+5j

add = my_complex + my_complex_1
sub = my_complex - my_complex_1
div = my_complex / my_complex_1
mul = my_complex * my_complex_1

print(add)
print(sub)
print(div)
print(mul)


## 2- String:-

my_str = 'Mohamed '
my_str_1 = "Ishag "

my_str_2 = """The most common mistake involving articles is using "an" instead of "a"(or vice versa). This mistake
occurs because writers believe "an" is used before a vowel and "a" before a consonant. That is not entirely accurate.
"An" is used before a vowel sound, and "a" is used before a consonant sound. The word sound is important because
consonants can create vowel sounds, and vowels can create consonant sounds. Therefore, the use of "an" or "a" is
determined by the sound not the letter.
"""

print(my_str)
print(my_str_1)
print(my_str_2)

##======  Slicing  =========================================================
# variable[start:stop:step]

name = 'Mohamed Ishag Adam'
print(name[3:20])


##======= 3-  List:-   ======================================================

my_list = ['Py4sudan', 1, 5.25, 'Mo']
my_list_1 = [['family_index', 'father','mather','childern'],
            [1,'Adam','Asha',['Ahmed', 'Ali', 'Amany']],
            [2,'Taha','Mona',['Usama', 'Areg']],
            [3,'Mukhtar','Yasmin',['Yahya', 'Fatima', 'Ashraf']]]

print(my_list)
print(my_list_1)


##======= 4- Dictionary:-    ===============================================

my_dic = {'key_a': 100,'key_b':'Py4sudan deserve to follow','key_c': 1.5}
my_dic_1 = {'families':    {1: ['Adam', 'Asha', ['Ahmed', 'Ali', 'Amany']],
                           2: {'father': 'Taha', 'mother': 'Mona', 'children':['Osama', 'Areg']}},
           'brst_page':    'Py4sudan',
           'flolt_number': 10.15}

print(my_dic)
print(my_dic_1)


##======= 5- Set:- =====================================================

my_set = {5, 5, 5,'Py4sudan', 1.5, 'AA', 'AA'}
my_set1 = {(1, 2, 'Py4sudan', 'AA', 1.5), 'Py4sudan', 10.5, 100}
my_fro_set = frozenset(my_set1)

print(my_set)
print(my_set1)
print(my_fro_set)


##======= 6- Tuple:-  ==================================================

tuple_ = (1, 'Py4sudan', 1.5, 'AA')
my_tuple = ({5, 'Py4sudan', 1.5}, 'Py4sudan', 5.5, 50)
my_tuple_1 = ({'Py4sudan', 1.5, 'AA'}, {'key': 'Py4sudan', 'num': 10}, (1, 2, 3), [9, 8, 7], 1.5)

print(tuple_)
print(my_tuple)
print(my_tuple_1)


##======== Logical operators ===========================================

# not, or, and
my_logic = 1
my_logic1 = 2

my_logic2 = my_logic or not my_logic1
my_logic3 = my_logic and not my_logic1
my_logic4 = my_logic or my_logic1
my_logic5 = my_logic and my_logic1

print(my_logic2)
print(my_logic3)
print(my_logic4)
print(my_logic5)


##====== Comparison operators ==========================================

# # <=, <, >, >=, !=, ==
comp = 3
comp1 = 4
my_com2 = comp < comp1
my_com3 = comp > comp1
my_com4 = comp <= comp1
my_com5 = comp != comp1
my_com6 = comp >= comp1
my_com7 = comp == comp1

print(my_com2)
print(my_com3)
print(my_com4)
print(my_com5)
print(my_com6)
print(my_com7)


##======== obj Members =================================================

# in , not in
my_list = [1, 'Mohamed', 2, 'ok']

my_checking = 'Mohamed' in my_list
my_checking1 = 3 not in my_list

print(my_checking)
print(my_checking1)


##========== Identical ================================================

# is, is not
obj  = 6
obj1 = obj
obj2 = 6

my_obj = obj is not obj1
my_obj1 = obj is obj1
my_obj2 = obj is obj2

print(my_obj)
print(my_obj1)
print(my_obj2)


##================ Mathematics Priorities ============================

# ( ) , ** , [ * / ] , [ + - ]
x = (1 + 2) ** (3 * 1) + 5 - 2
x = 3 ** 3 + 5 - 2
x = 27 + 5 - 2
x = 32 - 2
x = 30
print(x)


##=================  Flow Control =====================================

num = 2
my_num = 0

if num == 5:
    my_num = 50
    print('my_num =', my_num)
elif num < 1:
    my_num = 10
    print('my_num =', my_num)
else:
    my_num = 15
    print('my_num =', my_num)


##============== for loop =============================================

names = ['Ombada', 'Mohamed', 'Ishag', 'py4sudan']
for name in names:
    print(name)


##============== while loop =============================================

names = ['Ombada', 'Mohamed', 'Ishag', 'py4sudan']
index = 0

while True:
    print(names[index])
    if index == len(names) - 1:
        break
    index = index + 1


