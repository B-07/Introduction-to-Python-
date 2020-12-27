# Homework1
# This program will show you how to introduce yourself in English.

print('\nBu program, kendinizi İngilizce olarak nasıl tanıtacağınızı size gösterecek.\n\nÖncelikle istenilen bilgileri giriniz.')

Name=input('\nPlease enter your name: ')
Surname=input('Please enter your surname: ')
Age=input('Please enter your age: ')
Country=input('Please enter your country: ')
Nationality=input('Please enter nationality: ')

# If we use the print command, the type of values is always a string. Because we don't use int(input()) command or something else.
print(type(Name))
print(type(Surname))
print(type(Age))
print(type(Country))
print(type(Nationality))

print('\nKendinizi kısaca aşağıdaki cümledeki gibi tanıtabilirsiniz.')
print(f"\nMy name is {Name} {Surname}. I'm {Age} years old. I'm from {Country} and I'm {Nationality}.")