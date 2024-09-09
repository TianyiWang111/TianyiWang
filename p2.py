
str1 = "Howl's Moving Castle"

for index, char in enumerate(str1):
    print(f"Index: {index}, Character: {char}")


some_list = ['Baa', 'baa', 'black', 'sheep']

result = ' '.join(some_list)
print(result)  # Output: Baa baa black sheep


import random

random_number = random.random()
print(random_number)


import random

some_list = ['Baa', 'baa', 'black', 'sheep']
random_element = random.choice(some_list)
print(random_element)
