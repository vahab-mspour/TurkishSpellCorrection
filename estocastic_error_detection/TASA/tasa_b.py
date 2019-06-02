

'''

class TASA(object):
    def __init__(self):
        self.V = ['a', 'e', 'o', 'ö', 'u', 'ü', 'i', 'ı']
        self.C = ['b', 'c', 'd', 'f', 'g', 'ğ', 'h', 'j', 'k', 'l', 'm', 'n', 'ç', 'p', 'r', 's', 'ş', 't', 'v', 'y', 'z']
        self.VC = [x + y for x in self.V for y in self.C]  # ab, ac, aç, ad, ..., az, eb, ec, eç, ...
        self.CV = [x + y for x in self.C for y in self.V]  # ba, be, bı, bi, ..., za, ze, zı, zi, …
        self.CVC = [x + y + z for x in self.C for y in self.V for z in self.C]  # bel, gel, köy, tır, ...
        self.VCC = [x + y + z for x in self.V for y in self.C for z in self.C]  # alt, üst, ırk, ...
        self.CCV = [x + y + z for x in self.C for y in self.C for z in self.V]  # bre
        self.CVCC = [x + y + z + w for x in self.C for y in self.V for z in self.C for w in self.C]  # kurt, yurt, renk, Türk, ...
        for x in self.VCC:
            if x[1] == x[2]:
                self.VCC.remove(x)  # remove abb add acc ...
        for x in self.CCV:
            if x[1] == x[0]:
                self.CCV.remove(x)  # remove bba dda ...
        for x in self.CVCC:
            if x[2] == x[3]:
                self.CVCC.remove(x)  # remove kabb daff
        print(self.CVCC)


def word2sylabes(V, word):
    """
            Step 4: If there are two vowels in the word side by side,
            the word is divided into subword units after the first vowel.
            """
    sylabes1 = ""
    sylabes2 = ""
    for i in range(len(word) - 1):
        if word[i] in V and word[i + 1] in V:  # two vowels in the word side by side,
            # divided into subword units after the first vowel
            sylabes1 = word2sylabes(word[:i + 1])
            print("sylabes1=", sylabes1)
            sylabes2 = word2sylabes(word[i + 1:])
            print("sylabes2=", sylabes2)
    return (sylabes1 + ", " + sylabes2)


ta = TASA()
word = 'eadeh'
sylabes = word2sylabes(ta.V, word)
print(sylabes)

'''


def get_syllabes_of_six(subword):
    """
        Case 6: The length of the subword unit is equal or greater than 6
    """
    V = ['a', 'e', 'o', 'ö', 'u', 'ü', 'i', 'ı']
    C = ['b', 'c', 'd', 'f', 'g', 'ğ', 'h', 'j', 'k', 'l', 'm', 'n', 'ç', 'p', 'r', 's', 'ş', 't', 'v', 'y',
         'z']
    syllabe1 = subword
    syllabe2 = ""
    if subword[0] in V: # If the first letter of the subword is vowel then,
        if subword [-1] in C and subword [-2] in C and subword [-3] in C : # last three are in C
            """
            If the last three letters are consonant then, The first letter is a syllable. 
            the next binary letters are syllables until the last five letters. The last five letters are a syllable. 
            """
            syllabe1 = subword [0] #firts letter
            syllabe2 = subword [-5:] #last five letter
            subword = subword [1:len(subword)-5] # remove first and last five
            i = 0
            if len(subword)%2 == 0:
                for i in range(len(subword)-2):
                    syllabe1 += ("_"+subword[i:i+2])
                else:
                    for i in range(len(subword)-3):
                        syllabe1 += ("_"+subword[i:i+2])
                    syllabe1 += ("_"+subword[-1])
            return syllabe1 +"_"+ syllabe2
        if subword[-1] in C and subword[-2] in C :  # last two are in C
            """
            ElseIf the last two letters are consonant then, The first letter is a syllable. 
            The next binary letters are syllables until the last four letters. The last four letters are a syllable.  
            """
            syllabe1 = subword [0] #firts letter
            syllabe2 = subword [-4:] #last four letter
            subword = subword [1:len(subword)-4] # remove first and last five
            i = 0
            if len(subword)%2 == 0:
                for i in range(len(subword)-2):
                    syllabe1 += ("_"+subword[i:i+2])
                else:
                    for i in range(len(subword)-3):
                        syllabe1 += ("_"+subword[i:i+2])
                    syllabe1 += ("_"+subword[-1])
            return syllabe1 +"_"+ syllabe2

        #ElseIf the last letter is vowel then, The first letter is a syllable.The next binary letters are syllables.
        if subword[-1] in V:
            syllabe1 = subword[0]  # firts letter
            subword = subword [1:]
            if len(subword)%2 == 0:
                for i in range(len(subword)-2):
                    syllabe1 += ("_"+subword[i:i+2])
                else:
                    for i in range(len(subword)-3):
                        syllabe1 += ("_"+subword[i:i+2])
                    syllabe1 += ("_"+subword[-1])
            return syllabe1 +"_"+ syllabe2
        else:
            """
                Else The first letter is a syllable. The next binary letters are syllables until the last three letters. The last three letters are a syllable. 
            """
            syllabe1 = subword[0]  # firts letter
            syllabe2 = subword[-3:]  # last three letter
            subword = subword[1:len(subword) - 3]  # remove first and last five
            i = 0
            if len(subword) % 2 == 0:
                for i in range(len(subword) - 2):
                    syllabe1 += ("_" + subword[i:i + 2])
                else:
                    for i in range(len(subword) - 3):
                        syllabe1 += ("_" + subword[i:i + 2])
                    syllabe1 += ("_" + subword[-1])
            return syllabe1 + "_" + syllabe2

    if subword[1] in V:  # If the second letter of the subword is vowel then,
        if subword[-1] in C and subword[-2] in C and subword[-3] in C:  # last three are in C
            syllabe1 = ""
            syllabe2 = subword[-5:]
            subword = subword[:len(subword) - 5] # remove last five
            if len(subword) % 2 == 0:
                for i in range(len(subword) - 2):
                    syllabe1 += ("_" + subword[i:i + 2])
                else:
                    for i in range(len(subword) - 3):
                        syllabe1 += ("_" + subword[i:i + 2])
                    syllabe1 += ("_" + subword[-1])
            return syllabe1 + "_" + syllabe2
        if subword[-1] in C and subword[-2] in C :  # last two are in C
            syllabe1 = ""
            syllabe2 = subword[-4:]
            subword = subword[:len(subword) - 4]  # remove last four
            if len(subword) % 2 == 0:
                for i in range(len(subword) - 2):
                    syllabe1 += ("_" + subword[i:i + 2])
                else:
                    for i in range(len(subword) - 3):
                        syllabe1 += ("_" + subword[i:i + 2])
                    syllabe1 += ("_" + subword[-1])
            return syllabe1 + "_" + syllabe2
        if subword[-1] in V:  # ElseIf the last letter is vowel then, The binary letters from the beginning are syllables.
            syllabe1 = ""
            if len(subword) % 2 == 0:
                for i in range(len(subword) - 2):
                    syllabe1 += ("_" + subword[i:i + 2])
                else:
                    for i in range(len(subword) - 3):
                        syllabe1 += ("_" + subword[i:i + 2])
                    syllabe1 += ("_" + subword[-1])
            return syllabe1
        if subword[-2] in V and subword[-1] in C: # XX..XVC :  the last two letters are vowel and consonant respectively
            syllabe1 = ""
            syllabe2 = subword[-3:]
            subword = subword[:len(subword) - 3]  # remove last three
            if len(subword) % 2 == 0:
                for i in range(len(subword) - 2):
                    syllabe1 += ("_" + subword[i:i + 2])
                else:
                    for i in range(len(subword) - 3):
                        syllabe1 += ("_" + subword[i:i + 2])
                    syllabe1 += ("_" + subword[-1])
            return syllabe1 + "_" + syllabe2
        else:
            """ Else If the third letter is vowel then, If the last three letters are consonant then, """
            if subword[2] in V: #third letter is vowel
                if subword[-1] in C and subword[-2] in C and subword[-3] in C:  # last three are in C
                    syllabe1 = subword[:3] # TODO sum are more than 6 ??
                    syllabe2 = subword[-5:]
                    subword = subword[3:len(subword) - 5]  # remove last three
                    if len(subword) % 2 == 0:
                        for i in range(len(subword) - 2):
                            syllabe1 += ("_" + subword[i:i + 2])
                        else:
                            for i in range(len(subword) - 3):
                                syllabe1 += ("_" + subword[i:i + 2])
                            syllabe1 += ("_" + subword[-1])
                    return syllabe1 + "_" + syllabe2
                if subword[-1] in C and subword[-2] in C :  # last two are in C
                    syllabe1 = subword[:3]  # TODO sum are more than 6 ??
                    syllabe2 = subword[-4:]
                    subword = subword[3:len(subword) - 4]  # remove last three
                    if len(subword) % 2 == 0:
                        for i in range(len(subword) - 2):
                            syllabe1 += ("_" + subword[i:i + 2])
                        else:
                            for i in range(len(subword) - 3):
                                syllabe1 += ("_" + subword[i:i + 2])
                            syllabe1 += ("_" + subword[-1])
                    return syllabe1 + "_" + syllabe2
                if subword[-2] in V and subword[-1] in C:  # XX..XVC :  the last two letters are vowel and consonant respectively
                    syllabe1 = subword[:3]
                    syllabe2 = subword[-3:]
                    subword = subword[3:len(subword) - 3]  # remove last three
                    if len(subword) % 2 == 0:
                        for i in range(len(subword) - 2):
                            syllabe1 += ("_" + subword[i:i + 2])
                        else:
                            for i in range(len(subword) - 3):
                                syllabe1 += ("_" + subword[i:i + 2])
                            syllabe1 += ("_" + subword[-1])
                    return syllabe1 + "_" + syllabe2
                if subword[-1] in V :  # XX..XV :  the last  letter is vowel
                    syllabe1 = subword[:3] # the first three is syllabe
                    subword = subword[3:]  # remove first three
                    if len(subword) % 2 == 0:
                        for i in range(len(subword) - 2):
                            syllabe1 += ("_" + subword[i:i + 2])
                        else:
                            for i in range(len(subword) - 3):
                                syllabe1 += ("_" + subword[i:i + 2])
                            syllabe1 += ("_" + subword[-1])
                    return syllabe1
                else: # Else If the last three letters are consonant then,
                    if subword[-1] in C and subword[-2] in C and subword[-3] in C:  # last three are in C
                        # first 4 and last 5 and binary between
                        syllabe1 = subword[:4]  # TODO sum are more than 6 ??
                        syllabe2 = subword[-5:]
                        subword = subword[4:len(subword) - 5]  # remove last three
                        if len(subword) % 2 == 0:
                            for i in range(len(subword) - 2):
                                syllabe1 += ("_" + subword[i:i + 2])
                            else:
                                for i in range(len(subword) - 3):
                                    syllabe1 += ("_" + subword[i:i + 2])
                                syllabe1 += ("_" + subword[-1])
                        return syllabe1 + "_" + syllabe2
                    if subword[-1] in C and subword[-2] in C:  # last two are in C
                        # first 4 and last 4 and binary between
                        syllabe1 = subword[:4]  # TODO sum are more than 6 ??
                        syllabe2 = subword[-4:]
                        subword = subword[4:len(subword) - 4]  # remove last three
                        if len(subword) % 2 == 0:
                            for i in range(len(subword) - 2):
                                syllabe1 += ("_" + subword[i:i + 2])
                            else:
                                for i in range(len(subword) - 3):
                                    syllabe1 += ("_" + subword[i:i + 2])
                                syllabe1 += ("_" + subword[-1])
                        return syllabe1 + "_" + syllabe2
                    if subword[-2] in V and subword[-1] in C:  # last two are in XXX..VC
                        # first 4 and last 3 and binary between
                        syllabe1 = subword[:4]  # TODO sum are more than 6 ??
                        syllabe2 = subword[-3:]
                        subword = subword[4:len(subword) - 3]  # remove last three
                        if len(subword) % 2 == 0:
                            for i in range(len(subword) - 2):
                                syllabe1 += ("_" + subword[i:i + 2])
                            else:
                                for i in range(len(subword) - 3):
                                    syllabe1 += ("_" + subword[i:i + 2])
                                syllabe1 += ("_" + subword[-1])
                        return syllabe1 + "_" + syllabe2
                    if subword[-1] in V :  # last letter are in V
                        # first 4 and all binaries
                        syllabe1 = subword[:4]  # TODO sum are more than 6 ??
                        subword = subword[4:len(subword) ]  # remove last three
                        if len(subword) % 2 == 0:
                            for i in range(len(subword) - 2):
                                syllabe1 += ("_" + subword[i:i + 2])
                            else:
                                for i in range(len(subword) - 3):
                                    syllabe1 += ("_" + subword[i:i + 2])
                                syllabe1 += ("_" + subword[-1])
                        return syllabe1 + "_" + syllabe2






    return syllabe1 + "_" + syllabe2
    pass


def subword_controller(subword):
    """
    :param subword:
    :return: syllabs
    """
    V = ['a', 'e', 'o', 'ö', 'u', 'ü', 'i', 'ı']
    C = ['b', 'c', 'd', 'f', 'g', 'ğ', 'h', 'j', 'k', 'l', 'm', 'n', 'ç', 'p', 'r', 's', 'ş', 't', 'v', 'y',
         'z']
    """
        Case 1: The length of the subword unit is 1
        If the subword unit has only one letter then, It is only a syllable.
        and
        Case 2: The length of the subword unit is 2; If the subword unit has two letters then,
        It is only a syllable.
    """
    syllabe1 = subword
    syllabe2 =""

    if len(subword)<=2:
        return subword

    """

        Case 3: The length of the subword unit is 3
        If the three letters of the subword unit VCV respectively then,
        There are two syllables. The first vowel is the first syllable and the other two letters are the second syllable.
        ElseIf vowel and consonant forms are VCC, CVC and CCV then, The subword unit is only one syllable. 
    """
    if len(subword)== 3:
        if subword[0] in V and subword[1] in C and subword[2] in V:
            syllabe1 = subword[0]
            syllabe2 = subword[1:3]
            return syllabe1 + "_" + syllabe2
        return subword # if in the form of VCC, CVC and CCV then, then the unit is only one syllable

    """
        Case 4: The length of the subword unit is 4
        If the first two letters or the last two letters of the subword unit are consonant then, The subword unit is a syllable.
        Else If the first letter is vowel then, The first letter is the first syllable and the
        other three letters are the second syllable.
        Else  The first two letters are the first syllable and the other two letters are the second syllable. 
    """
    if len(subword)== 4:
        if (subword[0] in C and subword[1] in C) or (subword[2] in C and subword[3] in C):#CCXX or XXCC then only one syllabe
            return subword
        if subword[0] in V: # first letter is vowel then, The first letter is the first syllable VCXX-> V + CXX
            syllabe1 = subword [0]
            syllabe2 = subword [1:]
            return syllabe1 + "_" + syllabe2
        syllabe1 = subword[0:2] #first two letters are the first syllable
        syllabe2 = subword[2:4]
        return syllabe1 + "_" + syllabe2
    """
    Case 5: The length of the subword unit is 5
        If the first 'or' the last three letters of the subword unit are consonants then, It is only a syllable.
        ElseIf the first 'and' the last two letters of the subword unit are consonants then, It is only a syllable.
        
        Else If the first letter is vowel then, If the last two letters are consonants then,
            The first letter is the first syllable, and theother letters are the second syllable.
            Else The first letter is the first syllable. The next two letters are the second syllable. The last two letters are the third syllable.
Else
If the second letter of the subword unit is
consonant then,
The first three letters are the first syllable,
and the other two letters are the second
syllable.
 Else
The first two letters are the first syllable,
and the other three letters are the second
syllable.
    """
    if len(subword) == 5:
        if (subword[0] in C and subword[1] in C and subword[2] in C) or (subword[2] in C and subword[3] in C and subword[4] in C):#CCCXX or XXCCC then only one sylla
            return subword
        if (subword[0] in C and subword[1] in C ) and (subword[3] in C and subword[4] in C):#CCXXCC then only one sylla such as SPORT
            return subword
        if subword[0]in V:
            if subword[3] in C and subword[4] in C:
                syllabe1 = subword[0]
                syllabe2 = subword[1:]
                return syllabe1 + "_" + syllabe2
            else:
                syllabe1 = subword[0]
                syllabe2 = subword[1:3]
                return syllabe1 + "_" + syllabe2 + "_" + subword[3:]
        if subword[1] in C: # first and second letter are consonant
            syllabe1 = subword[0:3] # first three are first syllabe
            syllabe2 = subword[3:]
            return syllabe1 + "_" + syllabe2

        else:
            syllabe1 = subword[0:2]  # first two are first syllabe
            syllabe2 = subword[2:]
            return syllabe1 + "_" + syllabe2
        return syllabe1 + "_" + syllabe2

    if len(subword)>5 :
        return get_syllabes_of_six(subword)







print(subword_controller("su"))
print(subword_controller("iyi"))
print(subword_controller("kötü"))


print(subword_controller("Çekoslovakyalılaştıramadıklarımızdanmışsınızcasına"))
print(subword_controller('tıramadık'))

