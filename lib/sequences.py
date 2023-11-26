#!/usr/bin/env python3

def print_fibonacci(length):
    container=[]
    x, y = 0, 1
    if length <= 0:
        print(container)
    elif length == 1:
        container.append(x)
        print(container)
    else:
        container.append(x)
        if length > 1:
            container.append(y)
            for i in range(2, length):
                x, y =y, x+y
                container.append(y)
        print(container)
      
#                 # CANVAS CODE ALONG
#                         # LISTS
#                     # using sort()
# # sorting numbers 
# my_list = [89,56,36,100,250,69,85]
# my_list.sort()
# print(my_list)

# # sorting strings 
# my_list_2 =['Cabbage', 'Apple', 'Banana', 'Potato']
# my_list_2.sort()
# print(my_list_2)

# # sorting parameters

# my_list_3 = ["This is a long sentence", "word", "z"]
# my_list_3.sort(key=len, reverse=True)
# print(my_list_3)

# my_list_4 = [('John', 2),('Steve', 1), ('Joe',3)]

# def sort_tuple(tuple_value):
#     return tuple_value[1]


# my_list_4.sort(key=sort_tuple)
# print(my_list_4)

#                     # using Sorted()
# # in this sorting method we pass the list as an argument to the sorted() method
# my_list_5 =[53,87,54,67,35]
# sorted_list = sorted(my_list_5)
# print(sorted_list)

# # we can also pass key and reverse parameters
# my_string_list = ['Abongoz', "Anguoz", "Wamaez", "Mkafwane"] #Taita vocabulary
# sorted_list_2 = sorted(my_string_list,key=len, reverse= True)
# print(sorted_list_2)

#                     # Adding to Lists
# # Modifying lists at indexes
# my_string_list[0] = "Aktambaa"
# print(my_string_list)

# # Adding new elements to lists
# # using list.append()
# my_string_list.append("Abongoz")
# print(my_string_list)

# # using list.insert()
# # takes two arguments an index and a value e.g list.insert(index, value)
# my_string_list.insert(3, "Aboo")
# print(my_string_list)

# # Removing from lists
# """
# There are four options for removing elements from a list
# """
# my_list_6 = [5000, 7895, 9201, 5058, 4413, 4114, 0.541]
# # 1. del() - removes elements from a list specified by an index or range of indices
# # Example
#         # Deleting from an index 
# # del(my_list_6[-1])
# # print(my_list_6)
#         # Deleting from a range of indices
# # del(my_list_6[2:5])
# # print(my_list_6)

# # 2. list.pop()- removes and returns the element at the index passed in as an argument
# # Example
# # my_list_6.pop(2)
# # print(my_list_6)

# 3. list.remove() -removes the element passed in as an argument N/B one of the few list methods that searches by valie unstead of index
# Example
# my_list_6.remove(5000)
# print(my_list_6)
# 4. list.clear()- erases all the values of the lists
# Example
# my_list_6.clear()
# print(my_list_6)


                            # TUPLES
# Tuples do not have exclusive methods like lists. the sequence that the are
# provided when created is maintained as long as the tuple object exists.
                            # Ranges
"""
Ranges are a very simple type of sequence that is most commonly used in for loops. Ranges can only contain integers in a fixed pattern.
You can build a range using the {range()} constructor method and loop through it as if it were a standard list.
The range constructor only requires one argument: the end of the range. 
"""
# Example
# for i in range(5):
#     print(i)
# There are two optional arguments that you can include when creating a range: a start value and a step size.
"""
range(4) gives us 0, 1, 2, 3
range(1, 4) gives us 1, 2, 3
range(0, 4, 2) gives us 0, 2
"""

# # A dynamic sequence of values that allows duplicates
# fibonacci_list = [0,1,1,2,3,5,8,13,21]
# print(fibonacci_list)

# An immutable, ordered sequence of months
# month_tuple=(
#     'January',
#     'February',
#     'March',
#     'April',
#     'May',
#     'June',
#     'July',
#     'August',
#     'September',
#     'October',
#     'November',
#     'December',
# )
# print(month_tuple[5])

# A simple pattern of numbers
# even_numbers_upto_1000 = range(0, 1001, 2)
# print(even_numbers_upto_1000)
# A grammatical sentence
# sentence_string = "I am a happy individual"
# print(sentence_string)

"""
x in s returns True if x is equal to at least one element of s.

s + s2 returns a single sequence of the elements of s followed by the elements of s2.

s * n returns a single sequence of s repeated n times.

s[i]returns the ith element of s (starting at 0).

NOTE: Python also supports negative indices. -1 represents the last element in a sequence.

s[i:j] returns a slice of s from index i up to (but not including!) index j.

s[i:j:k] returns a slice of s from i to j with steps of k in between.

len(s) returns the number of elements in s.

min(s) and max(s) return the minimum and maximum values in s, respectively. > NOTE: this requires the elements of s to be of the same data type, either str or numerical.

s.index(x) returns the index of the first x in s.

s.count(x) returns the number of instances of x in s.
"""