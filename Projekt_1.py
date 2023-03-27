# Projekt_1.py: První projekt Engeto
# author: Tomas Kupka
# Email: tomaskupka93@gmail.com
# Discord: Tomas K.

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# users= ("bob","ann", "mike"," liz ")
# password= ("123","pass123","password123","pass123")
separator = "-" * 50
sep_long = '=' * 70

user_database = {'Bob': "123", 'Ann': "pass123", 'Mike': "password123", 'Liz': "pass123"}
username = input( "username: ")
password = input("password: ")
if password == user_database.get(username):
    print("Welcome in paradise of the text analyzer ♥ .")
else:    
    print("Wrong username or password. You are TERMINATED!!!")
    quit()
print(separator)

select = input(f'Select text which you want to analyze - enter number from 1 to {len(TEXTS)}: ')
if not (select.isnumeric() and int(select) in range(1, len(TEXTS) + 1)):
    print("Wrong choice of the number. You are TERMINATED!!!")
    quit()
else:
    t_select = TEXTS[int(select) - 1]
print(separator, '\nSELECTED TEXT:\n', t_select)

clean_words = [
    word.strip(".,") for word in t_select.split() if word.strip(".,")
]

word_count = len(clean_words)

titlecases = [word for word in clean_words if word.istitle()]
titlecases_count = len(titlecases)

upppercases = [word for word in clean_words
               if word.isupper()]
upppercases_count = len(upppercases)

lowercases = [word for word in clean_words
              if word.islower()]
lowercases_count = len(lowercases) 

numbers = [int(word) for word in clean_words if word.isdigit()]
numbers_count = len(numbers)

sum_of_numbers = sum(numbers)

word_lenghts = [len(word) for word in clean_words]
max_lenght = max(word_lenghts)

list = {}
for number in range(1, (max_lenght + 1)):
    list[number] = word_lenghts.count(number)

print(f'{separator}\nYour informations about selected text:')
print("There is/are:\n")
print(f'{word_count}\tword(s)')
print(f'{titlecases_count}\ttitlecase word(s)')
print(f'{upppercases_count}\tuppercase word(s)')
print(f'{lowercases_count}\tlowercase word(s)')
print(f'{numbers_count}\tnumber(s)')
print(f'The sum of all numbers is {sum_of_numbers}.')
print(separator)
for key in list:
    print((str(key).rjust(8)), ('*' * int(list.get(key))).ljust(20),
          str(list.get(key)).ljust(5), sep='|')
print(separator)