#!/usr/bin/python3

# for i in range(1, 10):
#     if i <= 5:
#         print("THE VALUE OF I IS LESS THAN OR EQUAL TO 5")
#     elif i >= 6 and i <= 8:
#         print("THE VALUE IS BETWEEN 6 AND 8")
#     else:
#         print("PYTHON IS COOL!")

# if, elif, else
# x = int(input("Please enter an integer: "))
# if x < 0:
#     x = 0
#     print("Negative changed to zero")
# elif x == 0:
#     print("Zero")
# elif x == 1:
#     print("Single")
# else:
#     print("More...")

#  for statement
words = ['cat', 'window', 'computer', 'Chair', 'Chocolate']
# for w in words:
#     print(w, len(w))

# Create a sample collection
# users = {'Joseph': 'Active', 'Emma': 'Active', 'Afande Ojok': 'Active', 'Elisa': 'Inactive', 'Mark': 'Inactive', 'Caroline': 'Inactive'}

# Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'Inactive':
#         del users[user]
#         # print(users)
#     print(user)

# Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'Active':
#         active_users[user] = status
#     print(active_users)

# The range() Function
# for i in range(5, 15, 5):
#     print(i)

for word in range(len(words)):
    print(word, words[word])

for index, word in enumerate(words):
    print(index, word)