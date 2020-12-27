# Homework2
# Identification Program for Covid-19

print('\nThis program gets your information for Covid-19.\nIf any restrictions affect you, it will notify you.\nPlease enter the requested information.')

Name= input('\nPlease enter your name: ')
Surname= input('Please enter your surname: ')
Age= int(input('Please enter your age: '))                # Burada değeri 'if' komutunun çalışması için integer olarak aldık.
Birth= input('Please enter your year of birth: ')         

list=[Name, Surname, Age, Birth]

for i in list:
    print(i)
    
if Age >= 18:
    print("\n*You can go out to the street.*")
elif Age < 0:
    print("\n*Please enter a number greater than zero.*")
elif Age < 18: 
    print("\n*You can't go out because it's too dangerous.*") # Oluşturduğum programa göre sebebin kısıtlama olması gerekiyordu fakat cümleyi ödevde istenilen şekilde yazmak istedim. 