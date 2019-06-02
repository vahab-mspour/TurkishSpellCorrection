
"""
this code is am implementation of
"http://www.akademik.adu.edu.tr/bolum/fef/matematik/webfolders/File/personel/a1005/inista2005_paperid_141.pdf"
"""

def word2sylabes(word):
    V = ['a', 'e', 'o', 'ö', 'u', 'ü', 'i', 'ı']
    C = ['b', 'c', 'd', 'f', 'g', 'ğ', 'h', 'j', 'k', 'l', 'm', 'n', 'ç', 'p', 'r', 's', 'ş', 't', 'v', 'y',
              'z']
    if len(word)<2: # vc cv cc atleast 3 consonants must be
        return word

    sylabes = word
    sylabes1 = word
    sylabes2 = ""
    print(word)
    """
                step 4: if four consonants in the word side by side, 
                and if these consonants are not at the beginning or end of the word, 
                the word is divided into subword units 'after the second consonant'.
    """

    if len(word)> 4 :
        i = 1  # not at the beginning of the word,
        while i < len(word) - 3:
            if word[i] in C and word[i + 1] in C and word[i + 2] in C and word[
                        i + 3] in C:  # 'four' consonants in the word side by side,
                # divided into subword units after the 'second' consonant
                sylabes1 = word[:i + 2]
                sylabes1 = word2sylabes(sylabes1)
                sylabes2 = "_" + word[i + 2:]
                sylabes2 = word2sylabes(sylabes2)
                i += 1
                return sylabes1 + sylabes2
            i += 1
    #state 2
    """
            Step 2: If there are 'three consonants' in the word side by side,
            and if these consonants are not at the beginning or end of the word,
            the word is divided into subword units 'after' the 'second' consonant.
    """
    if len(word) > 3:
        i = 1 #not at the beginning of the word,
        while i < len(word)-2:
            if word[i] in C and word[i + 1] in C and word[i + 2] in C:  # 'three' consonants in the word side by side,
                # divided into subword units after the 'second' consonant
                sylabes1 = word[:i + 2]
                sylabes1 = word2sylabes(sylabes1)
                sylabes2 = "_" + word[i + 2:]
                sylabes2 = word2sylabes(sylabes2)
                i += 1
                return sylabes1 + sylabes2
            i += 1

    # state 3
    """
            step 3: two consonants in the word side by side, 
            and if these consonants are not at the beginning or end of the word, 
            the word is divided into subword units 'after' the 'first consonant'.
    """
    # two consonant in the word side by side, not at the beginning of the word,
    i = 1
    while i < len(word)-2:
        if word[i] in C and word[i + 1] in C:  # two consonant in the word side by side,
            # divided into subword units after the 'first' consonant
            sylabes1 = word[:i + 1]
            sylabes1 = word2sylabes(sylabes1)
            sylabes2 = "_" +word[i + 1:]
            sylabes2 = word2sylabes(sylabes2)
            i += 1
            sylabes = sylabes1 + sylabes2
            print(sylabes)
            return sylabes1 + sylabes2
        i += 1

    # state 4 :
    """
            step 4: two vowels in the word side by side, 
            the word is divided into subword units 'after' the 'first vowel'.
    """
    i = 0
    while i < len(word)-1:
        if word[i] in V and word[i + 1] in V:  # two vowels in the word side by side,
            # divided into subword units after the first vowel
            sylabes1 = word[:i + 1]
            sylabes2 = "_" +word[i + 1:]
            sylabes2 = word2sylabes(sylabes2)
            i += 1
            sylabes = sylabes1 + sylabes2
            print(sylabes)
            return sylabes1 + sylabes2
        i += 1
    sylabes = sylabes1 +  sylabes2
    print(sylabes)
    return sylabes1 +  sylabes2

def get_word_sylabes(word):
    word_sylabes = word2sylabes(word)
    return word_sylabes.split("_")

word = 'muvaffakiyetsizleştiricileştir'
syllabes = get_word_sylabes(word)
print(syllabes)
print(get_word_sylabes('kitaplık'))
print(get_word_sylabes('Çekoslovakyalılaştıramadıklarımızdanmışsınızcasına'))
# word4 = 'eadeeh'
# word3= 'muhakkan'
# word2 = 'aktpe'
# print(word2[:3])
# # print(word[:2])
# # print(tasa.V)
# word = 'muvaffakiyetsizleştiricileştir'
# word2= '_tiricileştir'
# word_sylabes = word2sylabes(word)
# print("... word_sylabes=", word_sylabes)
# # (tasa.C, word2)
# # sylabes = word2sylabesrule3(tasa.C, word3)
# # sylabes = word2sylabesrule4(tasa.V, word4)
# # print("word_sylabes= %s" %(word2sylabes(word)))