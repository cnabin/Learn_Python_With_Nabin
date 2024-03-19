#Tuple -> (), Immutable, does not support re-aasignment
fruits=('apple',
'apple'
'banana',
'grapes')
print(type(fruits))
fruits[0]="Mango"
print(fruits[0])
