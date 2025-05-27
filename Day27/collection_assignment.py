# Lists

"""
1.  List of Squares: Create a list of squares of numbers from 1 to 20
"""
squares = [i ** 2 for i in range(1, 21)]
print(squares)

"""
2. Second Largest Number: Find the second largest number in a list without using sort() 
"""
numbers = [20, 40, 10, 3, 4, 100, 678, 0, 1, 50]
first_largest = max(numbers)
second_largest = max(i for i in numbers if i != first_largest)
print(second_largest)

"""
3. Remove Duplicates: Write a program to remove all duplicate values from a list while preserving order.
"""
numbers = [1, 1, 3, 4, 5, 5 ,3, 6, 7, 9, 10, 11, 12, 11]
visited = set()
removed_duplicates = []

for i in numbers:
    if i not in visited:
        visited.add(i)
        removed_duplicates.append(i)
print(removed_duplicates)

"""
4. Rotate List: Rotate a list to the right by k steps. 
   Example: [1, 2, 3, 4, 5] rotated by 2 [4, 5, 1, 2, 3]
"""
element = [1, 2, 3, 4, 5]
k = 2
k = k % len(element)

element[:] = element[k+1:] + element[:k+1]
print(element)

"""
5. List Compression From a list of numbers, create a new list with only the even numbers doubled
"""
numbers =  [1, 1, 3, 4, 5, 5 ,3, 6, 7, 9, 10, 11, 12, 11]
even_numbers_doubled = []

for i in numbers:
    if i % 2 == 0:
        even_numbers_doubled.append(i * i)
print(even_numbers_doubled)

# Tuples

"""
6.  Swap Values: Write a function that accepts two tuples and swaps their contents. 
"""
def swap(tuple1, tuple2):
    return  tuple2, tuple1

a = (5, 3, 6)
b = (50, 30, 60)

print("Before Swapping")
print(f"First Tuple Value: {a}")
print(f"Second Tuple Value: {b}")

a, b = swap(a, b)

print("After Swapping")
print(f"First Tuple Value: {a}")
print(f"Second Tuple Value: {b}")

"""
7. Unpack Tuples: Unpack a tuple with student details: (name, age, branch, grade) and print them in a sentence.
"""
student_details = "Ashwin Harish", 22, "Computer Science", "O"
name, age, branch, grade = student_details

print(f"Name of the student: {name}")
print(f"Age: {age}")
print(f"Department: {branch}")
print(f"Grade Obtained: {grade}")

"""
8. Tuple to Dictionary Convert a tuple of key-value pairs into a dictionary.
   Example: (("a", 1), ("b", 2)) → {"a": 1, "b": 2}
"""
tuple_a = (("a", 1), ("b", 2), ("c", 3), ("d", 4))
dict_ele = {}
for key, value in tuple_a:
    dict_ele[key] = value
print(dict_ele)

# Sets

"""
9. Common Items: Find the common elements in two user-defined lists using sets
"""
list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 5, 7]

set_a = set(list_a)
set_b = set(list_b)

print(f"Common elements: {set_a.intersection(set_b)}")

"""
10.  Unique Words in Sentence: Take a sentence from the user and print all unique words
"""
sentence = input("Enter a sentence: ").split()
unique_words = list(set(sentence))
print(unique_words)

"""
11. Symmetric Difference: Given two sets of integers, print elements that are in one
    set or the other, but not both.
"""
set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set_b = {4, 5, 8, 9, 10, 11, 12, 13, 14}
print(f"Symmetric Difference of two sets: {set_a.symmetric_difference(set_b)}")

"""
12. Subset Checker: Check if one set is a subset of another.
"""
set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set_b = {1, 2, 3}

if set_b.issubset(set_a):
    print("Set B is a subset of Set A")
else:
    print("Set B is not a subset of Set A")

#DICTIONARIES

"""
13. Frequency Counter: Count the frequency of each character in a string using a
    dictionary.
"""
word = input("Enter a word: ")
frequency = {}

for i in word:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print(frequency)

"""
14. Student Grade Book: Ask for names and marks of 3 students. 
    Then ask for a name and display their grade (>=90: A , >=75: B , else C).
"""
student_details = {}
for i in range(3):
    print(f"\nFor student: {i+1}")
    name = input("Enter student name: ")
    mark = float(input("Enter student mark: "))

    if mark >= 90:
        student_details[name] = "A"
    elif mark >= 75:
        student_details[name] = "B"
    else:
        student_details[name] = "C"


print("\nStudent Info")
student_name = input("Enter student name: ")
print(f"Name of the student: {student_name}")
print(f"student grade: {student_details[student_name]}")

"""
15. Merge Two Dictionaries: Merge two dictionaries. If the same key exists, sum the values.
"""
merge_dict = {}
def merge(dict):
    for key, value in dict.items():
        if key in merge_dict:
            merge_dict[key] += value
        else:
            merge_dict[key] = value

dict_a = {
            "Pen": 10,
            "Notebook": 40,
            "Pencil": 5,
            "Eraser": 3,
            "Ruler": 15
        }

dict_b = {
            "Marker": 25,
            "Highlighter": 25,
            "Glue Stick": 15,
            "Scissors": 40,
            "Stapler": 40,
            "Pencil": 5,
            "Eraser": 3,
            "Ruler": 15
        }

merge(dict_a)
merge(dict_b)
print(merge_dict)

"""
16. Inverted Dictionary Invert a dictionary’s keys and values. 
    Input: {"a": 1, "b": 2} → Output: {1: "a", 2: "b"}
"""
dict_a = {"a": 1, "b": 2}
invert_dict = {}

for key, value in dict_a.items():
    invert_dict[value] = key
print(invert_dict)

"""
17.  Group Words by Length: Input a list of words. Create a dictionary where the key
     is word length and the value is a list of words of that length
"""

words = ["Marker", "Highlighter", "Glue Stick", "Scissors", "Stapler", "Pencil", "Eraser", "Ruler"]
grouped_words = {}

for word in words:
    length = len(word)
    if length in grouped_words:
        grouped_words[length].append(word)
    else:
        grouped_words[length] = [word]
print(grouped_words)

