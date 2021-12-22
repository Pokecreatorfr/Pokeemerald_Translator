def linemaker(text , max_of_line , max_char_by_line):
    textsplit = text.split()
    list_line = ["" for a in range(max_of_line)]
    line = 0
    word = 0
    end = False
    valid_line = 0
    text_final = ''
    if len(text)/max_char_by_line > max_of_line:
        print('error')
        return ''
    while end == False:
        if line > max_of_line:
            print('error')
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
        if i == valid_line - 1: 
            text_final += list_line[i]
        else:
            text_final += list_line[i] + "\n"
    return list_line
print(linemaker("Its fur is the ultimate in luxuriousness. Sleeping alongside a WIGGLYTUFF is simply divine. Its body expands seemingly without end when it inhales.", 4, 44))