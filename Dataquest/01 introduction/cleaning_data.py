#%%
# lectura del archivo de trabajo
from csv import reader
opened_file = open('artworks.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# muestra las primeras cinco filas
for row in moma[:5]:
    print(row)

#%%
# Reemplazar substrings con el método replace
age1 = "I am thirty-one years old"
age2 = age1.replace("thirty-one", "thirty-two")
print(age2)


#%%
for row in moma[1:5]:
    nationality = row[2]
    print(nationality)

for row in moma:
    nationality = row[2]
    nationality = nationality.replace("(","")
    nationality = nationality.replace(")", "")
    row[2] = nationality


for row in moma[1:5]:
    nationality = row[2]
    print(nationality)