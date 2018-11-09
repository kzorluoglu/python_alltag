import re


sentence = "Ich habe 30 Hunde, die jeweils 4 Liter Wasser brauchen und 2 kg Nahrung"

finded = re.findall("[0-9]+", sentence)

print(finded)


print(re.search("der?", "Hallo de Hallo"))
print(re.search("der?", "Hallo der Hallo"))
print(re.search("der?", "Hallo derrrrrr Hallo"))
print('####')
print(re.search("der*", "Hallo de Hallo"))
print(re.search("der*", "Hallo der Hallo"))
print(re.search("der*", "Hallo derrrrrr Hallo"))
print('####')
print(re.search("der+", "Hallo de Hallo"))
print(re.search("der+", "Hallo der Hallo"))
print(re.search("der+", "Hallo derrrrrr Hallo"))
print('####')
print(re.search("[0123456789]", "Hallo 123 Hallo"))
print(re.search("[0123456789]+", "Hallo 123 Hallo"))
print(re.search("[0-9]+", "Hallo 123 Hallo"))
print('####')
print(re.findall("[0-9]+", "Hallo 123 Hallo 321"))

