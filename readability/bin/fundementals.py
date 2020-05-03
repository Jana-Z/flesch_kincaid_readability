import re

def split_words(text):
    words = re.findall(r'\w+', text)
    return words

def split_sentences(text):
    text = text.strip()
    sentences = re.split(r'[.?!]+', text)
    sentences = [s.strip() for s in sentences]
    return sentences[:-1]

def count_words(text):
    words = re.findall(r'\w+', text)
    return len(words)

def count_sentences(text):
    text = text.strip()
    sentences = re.split(r'[.?!]+', text)
    if len(sentences) == 1 and text: return 1
    return len(sentences) - 1

def count_syllables(word, lang='en'):
    if lang == 'en':
        # algorithm from https://eayd.in/?p=232
        word = word.lower()
        exception_add = ['serious','crucial', 'being']
        exception_del = ['fortunately','unfortunately']
        co_one = ['cool','coach','coat','coal','count','coin','coarse','coup','coif','cook','coign','coiffe','coof','court']
        co_two = ['coapt','coed','coinci']
        pre_one = ['preach']
        syls = 0 #added syllable number
        disc = 0 #discarded syllable number
        if len(word) <= 3 :
            syls = 1
            return syls
        if word[-2:] == "es" or word[-2:] == "ed" :
            doubleAndtripple_1 = len(re.findall(r'[eaoui][eaoui]',word))
            if doubleAndtripple_1 > 1 or len(re.findall(r'[eaoui][^eaoui]',word)) > 1 :
                if word[-3:] == "ted" or word[-3:] == "tes" or word[-3:] == "ses" or word[-3:] == "ied" or word[-3:] == "ies" :
                    pass
                else :
                    disc+=1
        le_except = ['whole','mobile','pole','male','female','hale','pale','tale','sale','aisle','whale','while']
        if word[-1:] == "e" :
            if word[-2:] == "le" and word not in le_except :
                pass
            else :
                disc+=1
        doubleAndtripple = len(re.findall(r'[eaoui][eaoui]',word))
        tripple = len(re.findall(r'[eaoui][eaoui][eaoui]',word))
        disc+=doubleAndtripple + tripple
        numVowels = len(re.findall(r'[eaoui]',word))
        if word[:2] == "mc" :
            syls+=1
        if word[-1:] == "y" and word[-2] not in "aeoui" :
            syls +=1
        for i,j in enumerate(word) :
            if j == "y" :
                if (i != 0) and (i != len(word)-1) :
                    if word[i-1] not in "aeoui" and word[i+1] not in "aeoui" :
                        syls+=1

        if word[:3] == "tri" and word[3] in "aeoui" :
            syls+=1

        if word[:2] == "bi" and word[2] in "aeoui" :
            syls+=1

        if word[-3:] == "ian" : 
            if word[-4:] == "cian" or word[-4:] == "tian" :
                pass
            else :
                syls+=1

        if word[:2] == "co" and word[2] in 'eaoui' :

            if word[:4] in co_two or word[:5] in co_two or word[:6] in co_two :
                syls+=1
            elif word[:4] in co_one or word[:5] in co_one or word[:6] in co_one :
                pass
            else :
                syls+=1

        if word[:3] == "pre" and word[3] in 'eaoui' :
            if word[:6] in pre_one :
                pass
            else :
                syls+=1

        negative = ["doesn't", "isn't", "shouldn't", "couldn't","wouldn't"]

        if word[-3:] == "n't" :
            if word in negative :
                syls+=1
            else :
                pass   

        if word in exception_del :
            disc+=1

        if word in exception_add :
            syls+=1     

        return numVowels - disc + syls
    if lang == 'de':
        # every syllable either has a vowel or a diphtong (ai/au/ei/eu)
        num_syllables = 0
        last = ''
        word = word.lower()
        diphtongs = [
            'au',
            'ei',
            'ai',
            'eu',
            'äu',
            'ie',
            'aa',
            'ee',
            'ui'
        ]
        for char in word:
            if char in "aeiouäüö":
                num_syllables += 1
                if last:
                    if last+char in diphtongs:
                        num_syllables -= 1
                last = char
            else:
                last = ''
    return num_syllables