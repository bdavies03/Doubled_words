#A function that will filter out any words comprised of a string repeated twice from a list and outputting them in a seperate list

def filter_doubled(words):
    i = 0
    list_length = len(words)
    output = []
    while i < list_length:
        words[i] = words[i].lower()
        word_length = len(words[i])
        count = 0
        if word_length%2 == 0:
            j = 0
            while j < word_length/2:
                if words[i][j] == words[i][j+int(word_length/2)]:
                    count +=1
                j += 1
            if count == word_length/2:
              output.append(words[i])
        i += 1
    return(output)


words = ['bonbon', 'hello', 'pompom', 'hi', 'chicken', 'couscous', 'a', 'aa', 'aaa'] #the list of words to be checked
print(filter_doubled(words))
