# If the langs of 2 friends are same; what will happen to the program in problem 6 ?

d={}

# PERSON 1
name = input('name: ')
lang = input('lang: ')
d.update({name: lang})  #we use 'update' to fill in new data

# PERSON 2
name = input('name: ')
lang = input('lang: ')
d.update({name: lang})

# PERSON 3
name = input('name: ')
lang = input('lang: ')
d.update({name: lang})

# PERSON 4
name = input('name: ')
lang = input('lang: ')
d.update({name: lang})

print(d)

#if same "lang" value is entered, it will be displayed, no matter how many times.