def getfile():
    filename = input('Enter A File Name: ')
    numberofwords = 0
    file1 = open(filename, 'r')
    for line in file1:
        words = line.split()
        numberofwords = numberofwords + len(words)
    print("Number Of Words: ")
    print(numberofwords)

getfile()
