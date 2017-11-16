def make_dict(filename):
    with open(filename) as file:
        content = file.read()
        dic = {}
        word = content.split()
        for w in word:
            w = w.lower()
            if w in dic:
                dic[w] +=1
            else:
                dic[w] = 1
    file.close()
    return dic
def print_words(filename):
    dicti = make_dict(filename)
    for word in sorted(dicti.keys()):
        print(word,dicti[word])

a = print_words('alice.txt')

def sort_by_value(item):
    return item[-1]

def print_top(filename):
    count = make_dict(filename)
    items = sorted(count.items(),key=sort_by_value,reverse=True)
    for item in items[:20]:
        print(item[0] + ': ' + str(item[1]) + ' times')

a = print_top('alice.txt')
print(a)