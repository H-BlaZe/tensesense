#tense sense

def output(outList):
    if len(outList) > 0:
        tenseAns = ''
        tenseAns += str(outList[-1])
        tenseAns += ' Tense'
        print(tenseAns)
    else:
        print('Looks like the format of your sentence is incorrect. Please check the input and rectify the mistake.')
        sentenceGet()

def brain():
    tenseType = []
    listSent = cleanSen
    storage = len(listSent)

    for triggers1 in listSent:
        if triggers1.find('ing') != -1:
            tenseType.append('continuous')

            if listSent[int(listSent.index(triggers1)) - 1] in ['is', 'are', 'am']:
                tenseType.append('Present Continuous')

            elif listSent[int(listSent.index(triggers1)) - 1] == 'be':
                if listSent[int(listSent.index(triggers1)) - 2] in ['will', 'shall']:
                    tenseType.append('Future continuous')
                else:
                    tenseType.append('xX102')

            elif listSent[int(listSent.index(triggers1)) - 1] in ['was', 'were']:
                tenseType.append('Past continuous')

            elif listSent[int(listSent.index(triggers1)) - 1] == 'been':
                if listSent[int(listSent.index(triggers1)) - 2] == 'has':
                    tenseType.append('Present Perfect Continuous')
                if listSent[int(listSent.index(triggers1)) - 2] == 'had':
                    tenseType.append('Past Perfect Continuous')
                if listSent[int(listSent.index(triggers1)) - 2] == 'have':
                    if listSent[int(listSent.index(triggers1)) - 3] == 'will':
                        tenseType.append('Future Perfect Continuous')
                    else:
                        tenseType.append('Present Perfect Continuous')

        elif triggers1 == 'had':
            if listSent[int(listSent.index(triggers1)) + 1] != 'been':
                tenseType.append('Past Perfect')

        elif triggers1 == "am" or triggers1 == "are":
            tenseType.append('Simple Present')


        elif triggers1.find('ed') != -1:
            if listSent[int(listSent.index(triggers1)) - 1] not in ['had', 'have', 'has']:
                tenseType.append('Simple Past')

        elif triggers1 in ['will', 'shall']:
            if listSent[int(listSent.index(triggers1)) + 1] not in ['have']:
                tenseType.append('Simple Future')

            elif listSent[int(listSent.index(triggers1)) + 1] == 'have':
                if listSent[int(listSent.index(triggers1)) + 2].find('ed') != -1 or listSent[int(listSent.index(triggers1)) + 2].find('en') != -1:
                    tenseType.append('Future Perfect')

        elif triggers1 in ['has', 'have']:
            if listSent[int(listSent.index(triggers1)) - 1] not in ['will', 'shall']:
                if listSent[int(listSent.index(triggers1)) + 1].find('ed') != -1 or listSent[int(listSent.index(triggers1)) + 1].find('en') != -1:
                    tenseType.append('Present Perfect')

    #print(tenseType)
    output(tenseType)


def sentenceGet():
    sentence = input('Enter your sentence:- ')
    sentence += ' '
    if len(sentence) == 0:
        print('The sentence provided has no character,')
        sentenceGet()
    global brokenSen
    brokenSen = []
    global cleanSen
    cleanSen = []
    temp_word = ''
    for charc in sentence:
        if ord(charc) != 32:
            temp_word += charc
        else:
            brokenSen.append(temp_word)
            temp_word = ''
    for space in brokenSen:
        if len(space) != 0:
            cleanSen.append(space)
    brain()
sentenceGet()
