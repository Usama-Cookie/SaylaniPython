import random
def mimic_dict(filename):
    dic = {}
    file = open(filename).read()
    file_list = file.split(' ')
    global l
    l = file_list[0]
    for i in range(len(file_list)-1):
        if file_list[i] in dic.keys():
            dic[file_list[i]] += [file_list[i+1]]
        else:
            dic[file_list[i]] = [file_list[i+1]]
    return dic

a = mimic_dict('small.txt')
print(a)

def print_mimic(mimic_dict, word):
     for i in range(200):
         if word not in mimic_dict.keys():
            word = ''
         if word == '':
             mimic_dict[word] = [l]
             word = l
         else:
             word = random.choice(mimic_dict[word])
         print(word)

print_mimic(mimic_dict('small.txt'),word='are')