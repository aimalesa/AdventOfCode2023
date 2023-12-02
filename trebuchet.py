f = open("trebuchetInput.txt", "r")
total = 0
values = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}

valuesFlipped = {
    "eno" : 1,
    "owt" : 2,
    "eerht" : 3,
    "ruof" : 4,
    "evif" : 5,
    "xis" : 6,
    "neves" : 7,
    "thgie" : 8,
    "enin" : 9
}

for x in f:
    f = x
    wordsofar = ""
    for y in x:
        if not y.isdigit():
            wordsofar += y
        else:
            wordsofar = ""
        if wordsofar in values.keys():
            x = x.replace(wordsofar, str(values.get(wordsofar)), 1)

        for i in values.keys():
            if i in wordsofar:
                x = x.replace(i, str(values.get(i)), 1)

    num1 = ""
    for y in x:
        if y.isdigit():
            num1 += str(y)

    wordsofar = ""

    z = f[::-1]
    for y in z:
        if not y.isdigit():
            wordsofar += y
        else:
            wordsofar = ""
        if wordsofar in valuesFlipped.keys():
            z = z.replace(wordsofar, str(valuesFlipped.get(wordsofar)), 1)

        for i in valuesFlipped.keys():
            if i in wordsofar:
                z = z.replace(i, str(valuesFlipped.get(i)), 1)

    num2 = ""
    for y in z:
        if y.isdigit():
            num2 += str(y)

    total += int(num1[0] + num2[0]) 

print(total)
