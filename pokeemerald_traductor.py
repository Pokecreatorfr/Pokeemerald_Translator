import csv

languages = {'jp' : 1, 'kr' : 3, 'cn' : 4 , 'fr' : 5 , 'de' : 6 , 'es' : 7 , 'it' : 8}
error_code = {1 : 'Unknown name ' , 2 : 'Name too long'}

chosen_language = 'fr'
Capitalized = True # Boolean
Capitalized_Desc = False # Boolean

Favorite_Version_For_Desc = 22 

Fav_version = 9
Fav_version2 = 14
Fav_version3 = 22

def open_all_csv():
    global pokemon_names
    global item_names
    global ability_names
    global move_names
    global nature_names
    global pokemon_desc
    pokemon_names = []
    item_names = []
    ability_names = []
    move_names = []
    nature_names = []
    pokemon_desc = []
    with open('csv/pokemon_species_names.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            pokemon_names.append(row)
        csvfile.close
    with open('csv/item_names.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            item_names.append(row)
        csvfile.close
    with open('csv/ability_names.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            ability_names.append(row)
        csvfile.close
    with open('csv/move_names.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            move_names.append(row)
        csvfile.close
    with open('csv/nature_names.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            nature_names.append(row)
        csvfile.close
    with open('csv/pokemon_species_flavor_text.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            pokemon_desc.append(row)
        csvfile.close

def linemaker(text , max_of_line , max_char_by_line):
    if text == 0 :
        return ''
    textsplit = text.split()
    list_line = ["" for a in range(max_of_line)]
    line = 0
    word = 0
    end = False
    valid_line = 0
    text_final = ''
    if len(text)/max_char_by_line > max_of_line:
        #print('error')
        return ''
    while end == False:

        if line == max_of_line:
            #print('error')
            return ''
        elif word == len(textsplit):
            end = True
        elif len(list_line[line]) + len(textsplit[word]) >= max_char_by_line:
            line += 1
        else :
            list_line[line] += textsplit[word] + ' '
            word += 1
    for i in range(max_of_line):
        if list_line[i] != '':
            valid_line += 1
    for i in range(valid_line):
            text_final += '    "' + list_line[i] + '\\n"'+ "\n"
    return text_final

def return_name(txt):
    for i in range(len(txt)):
        if txt[i] == '"':
            return txt[0: i]

def return_name_for_P_desc(txt):
    for i in range(len(txt)):
        if txt[i] == 'P' and i != 0:
            return txt[0: i]

def trad_name(english_name , data_list):
    specie_number = search_number(english_name , data_list)
    goodpoke = False
    i = 0
    while goodpoke == False:
        i += 1
        if i == len(data_list):
            return 0
        if int(data_list[i][0]) == specie_number:
            if int(data_list[i][1]) == languages[chosen_language]:
                if Capitalized == True :
                    return data_list[i][2].upper()
                else:
                    return data_list[i][2]

def trad_desc(english_name , data_list , data_list_for_name , version_id):
    specie_number = search_number(english_name , data_list_for_name)
    good_desc = False
    i = 0
    while good_desc == False:
        i += 1
        if i == len(data_list):
            return 0
        if int(data_list[i][0]) == specie_number:
            if int(data_list[i][2]) == languages[chosen_language] and int(data_list[i][1]) == version_id:
                if Capitalized_Desc == True :
                    return data_list[i][3].upper()
                else:
                    return data_list[i][3]

def check_trad_desc_existance(english_name , data_list , data_list_for_name):
    specie_number = search_number(english_name , data_list_for_name)
    good_desc = False
    i = 0
    while good_desc == False:
        i += 1
        if i == len(data_list):
            return False
        elif int(data_list[i][0]) == specie_number and int(data_list[i][2]) == languages[chosen_language]:
            return True

def search_number(english_name , list_number):
    gooditem = False
    i = 0
    while gooditem == False:
        i += 1
        if i == len(list_number):
            return 0
        if int(list_number[i][1]) == 9:
            if list_number[i][2].upper() == english_name.upper():
                return int(list_number[i][0])

open_all_csv()

#print(trad_desc('Pikachu' , pokemon_desc , pokemon_names , 9))

## Trad nom item
a_file = open("items.h" , encoding="UTF-8")
item_names_file = []
lines = a_file.readlines()
for line in lines:
    item_names_file.append(line)
a_file.close()
errorlist = []
for i in range(len(item_names_file)):
    if item_names_file[i].find(' _("') != -1 :
        start = item_names_file[i].find(' _("') + 4
        name = return_name(item_names_file[i][start:len(item_names_file[i])].replace("'", '’'))
        #print(trad_item__name(name) , name)
        if trad_name(name , item_names) != 0:
            item_names_file[i] = item_names_file[i][0:start] + trad_name(name , item_names) + '"),' + "\n"
        else:
            errorlist.append([name , i])
fichier = open("items_trad.h" , 'w' , encoding="UTF-8")
for line in item_names_file:
    fichier.write(line )
fichier.close()
fichier = open("error_item.txt" , 'w' , encoding="UTF-8")
for line in errorlist:
    fichier.write('Error with the name :  "'+ line[0] +'"  on line ' + str(line[1]) +  "\n")
## Trad nom pokémons
a_file = open("species_names.h" , encoding="UTF-8")
species_names_file = []
lines = a_file.readlines()
for line in lines:
    species_names_file.append(line)
a_file.close()
errorlist = []
for i in range(len(species_names_file)):
    if species_names_file[i].find(' _("') != -1 :
        start = species_names_file[i].find(' _("') + 4
        name = return_name(species_names_file[i][start:len(species_names_file[i])].replace("'", '’'))
        #print(trad_pokemon_name(name) , name)
        if trad_name(name , pokemon_names) != 0:
            species_names_file[i] = species_names_file[i][0:start] + trad_name(name , pokemon_names) + '"),'
        else:
            errorlist.append([name , i , error_code[1]])
fichier = open("species_names_trad.h" , 'w' , encoding="UTF-8")
for line in species_names_file:
    fichier.write((line + "\n"))
fichier.close()
fichier = open("error_pokémon.txt" , 'w' , encoding="UTF-8")
for line in errorlist:
    fichier.write('Error with the name :  "'+ line[0] +'"  on line ' + str(line[1]) + '   ' + line[2] + "\n")
#Trad noms ability
a_file = open("abilities.h" , encoding="UTF-8")
abilities_names_file = []
lines = a_file.readlines()
for line in lines:
    abilities_names_file.append(line)
a_file.close()
errorlist = []
for i in range(len(abilities_names_file)):
    if abilities_names_file[i].find('[ABILITY') != -1:
        if abilities_names_file[i].find(' _("') != -1 :
            start = abilities_names_file[i].find(' _("') + 4
            name = return_name(abilities_names_file[i][start:len(abilities_names_file[i])].replace("'", '’'))
            #print(trad_ability_name(name) , name)
            if trad_name(name , ability_names) != 0:
                abilities_names_file[i] = abilities_names_file[i][0:start] + trad_name(name , ability_names) + '"),' + "\n"
            else:
                errorlist.append([name , i])
fichier = open("abilities_trad.h" , 'w' , encoding="UTF-8")
for line in abilities_names_file:
    fichier.write((line ))
fichier.close()
fichier = open("error_abilities.txt" , 'w' , encoding="UTF-8")
for line in errorlist:
    fichier.write('Error with the name :  "'+ line[0] +'"  on line ' + str(line[1]) +  "\n")
#Trad move names
a_file = open("move_names.h" , encoding="UTF-8")
move_names_file = []
lines = a_file.readlines()
for line in lines:
    move_names_file.append(line)
a_file.close()
errorlist = []
for i in range(len(move_names_file)):
    if move_names_file[i].find(' _("') != -1 :
        start = move_names_file[i].find(' _("') + 4
        name = return_name(move_names_file[i][start:len(move_names_file[i])].replace("'", '’'))
        #print(trad_pokemon_name(name) , name)
        if trad_name(name , move_names) != 0:
            move_names_file[i] = move_names_file[i][0:start] + trad_name(name , move_names) + '"),'
        else:
            errorlist.append([name , i])
fichier = open("move_names_trad.h" , 'w' , encoding="UTF-8")
for line in move_names_file:
    fichier.write((line + "\n"))
fichier.close()
fichier = open("error_move.txt" , 'w' , encoding="UTF-8")
for line in errorlist:
    fichier.write('Error with the name :  "'+ line[0] +'"  on line ' + str(line[1]) +  "\n")
#Trad nature names 
a_file = open("nature_names.h" , encoding="UTF-8")
nature_names_file = []
lines = a_file.readlines()
for line in lines:
    nature_names_file.append(line)
a_file.close()
errorlist = []
for i in range(len(nature_names_file)):
    if nature_names_file[i].find(' _("') != -1 :
        start = nature_names_file[i].find(' _("') + 4
        name = return_name(nature_names_file[i][start:len(nature_names_file[i])].replace("'", '’'))
        #print(trad_item__name(name) , name)
        if trad_name(name , nature_names) != 0:
            nature_names_file[i] = nature_names_file[i][0:start] + trad_name(name , nature_names) + '"),'
        else:
            errorlist.append([name , i])
fichier = open("nature_names_trad.h" , 'w' , encoding="UTF-8")
for line in nature_names_file:
    fichier.write((line + "\n"))
fichier.close()
fichier = open("error_nature_name.txt" , 'w' , encoding="UTF-8")
for line in errorlist:
    fichier.write('Error with the name :  "'+ line[0] +'"  on line ' + str(line[1]) +  "\n")
# Trad Pokedex Texts
a_file = open("pokedex_text.h" , encoding="UTF-8")
pokedex_desc_file = []
pokedex_desc_file_Trad = []
lines = a_file.readlines()
for line in lines:
    pokedex_desc_file.append(line)
a_file.close()
errorlist = []
for i in range(len(pokedex_desc_file)):
    #print(pokedex_desc_file[i].find('const u8 g') != -1)
    if pokedex_desc_file[i].find('const u8 g') != -1 :
        start = pokedex_desc_file[i].find('const u8 g') + 10
        name = return_name_for_P_desc(pokedex_desc_file[i][start:len(pokedex_desc_file[i])].replace("'", '’').replace("HoOh", 'Ho-Oh').replace("Mrmime", 'MR. MIME').replace("Farfetchd", 'Farfetch’d').replace("NidoranM", 'Nidoran♂').replace("NidoranF", 'Nidoran♀'))
        if check_trad_desc_existance(name , pokemon_desc , pokemon_names) == True:
            if linemaker(trad_desc(name , pokemon_desc , pokemon_names, Favorite_Version_For_Desc), 4 , 40) != '':
                pokedex_desc_file_Trad.append(pokedex_desc_file[i] + linemaker(trad_desc(name , pokemon_desc , pokemon_names, Favorite_Version_For_Desc), 4 , 40) + ');')
            else:
                good_desc = False
                for x in range(34):
                    if good_desc == False:
                        if linemaker(trad_desc(name , pokemon_desc , pokemon_names, 34 - x), 4 , 40) != '':
                            pokedex_desc_file_Trad.append(pokedex_desc_file[i] + linemaker(trad_desc(name , pokemon_desc , pokemon_names, 24), 4 , 40) + ');')
                            good_desc = True
                        elif x == 33 and good_desc == False :
                            errorlist.append([name , i , error_code[1]])
        else:
            errorlist.append([name , i , error_code[1]])
fichier = open("pokedex_text_trad.h" , 'w' , encoding="UTF-8")
for line in pokedex_desc_file_Trad:
    fichier.write((line + '\n'))
fichier.close()
fichier = open("error_pokedex_desc.txt" , 'w' , encoding="UTF-8")
for line in errorlist:
    fichier.write('Error with the name :  "'+ line[0] +'"  on line ' + str(line[1]) + '   ' + line[2] + "\n")

# Trad item desc
# A faire , trouver les definition en français pour chaque gen , ou les scrapper 