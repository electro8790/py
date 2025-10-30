def match(words):

    ctr = 0

    lst = []

    for word in words:

        if word == word[::-1]:

            ctr += 1

            lst.append(word)

    print(lst)

    return ctr

counter = match(['level', 'world', 'radar', 'python', 'madam'])

print(counter)