import datetime
now = datetime.datetime.now()
name = input('Enter your name: ')
age = int(input('Enter your age: '))
ageWhen100 = int((100 - age + now.year))
print('You are %s, and you are %d years old\nand you will be 100 years old in '
       'year %d' % (name, age, ageWhen100) )