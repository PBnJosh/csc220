#!/usr/local/bin/python3

def is_consonant(str):
    if ( len(str) > 1 ):
        raise Exception(f"function is_consonant parameter length exceeded. Expected: 1. Got: { len(str) }.")
    return str.isalpha() and (str != "a") and (str != "e") and (str != "i") and (str != "o") and (str != "u") and (str != "A") and (str != "E") and (str != "I") and (str != "O") and (str != "U")

def is_vowel(str):
    if ( len(str) > 1 ):
        raise Exception(f"function is_vowel parameter length exceeded. Expected: 1. Got: { len(str) }.")
    return str.isalpha() and not is_consonant(str)

def count_consonants(str):
    length = len(str)
    if (length == 0):
        return 0
    
    count = 0
    if ( is_consonant( str[0] ) ):
        count += 1

    return count + count_consonants( str[1 : length] )

def count_vowels(str):
    length = len(str)
    if (length == 0):
        return 0
    
    count = 0
    if ( is_vowel( str[0] ) ):
        count += 1

    return count + count_vowels( str[1 : length] )


while True:
    str_in = input("Enter a string: ")
    if ( len(str_in) != 0 ):
        break

num_vowels = count_vowels(str_in)
num_consonants = count_consonants(str_in)
if (num_consonants == 0 and num_vowels == 0):
    print("The string has no vowels or consonants")
elif (num_vowels < num_consonants):
    print("The string has more consonants")
elif (num_vowels > num_consonants):
    print("The string has more vowels")
else:
    print("The string has an equal number of vowels and consonants")



# print(f"is_consonant(f): {is_consonant("f")}")
# print(f"is_consonant(a): {is_consonant("a")}")
# print(f"is_consonant(E): {is_consonant("E")}")
# print(f"is_consonant(Z): {is_consonant("Z")}")
# print(f"is_consonant(?): {is_consonant("?")}")
# print()
# print(f"is_vowel(f): {is_vowel("f")}")
# print(f"is_vowel(a): {is_vowel("a")}")
# print(f"is_vowel(E): {is_vowel("E")}")
# print(f"is_vowel(Z): {is_vowel("Z")}")
# print(f"is_vowel(?): {is_vowel("?")}")
# print()
# print(f"count_consonants(abcd): {count_consonants("abcd")}")
# print(f"count_consonants(aeiouAEIOU Z!): {count_consonants("aeiouAEIOU Z!")}")
# print(f"count_consonants(zaaaaAaaaam): {count_consonants("zaaaaAaaaam")}")
# print()
# print(f"count_vowels(abcd): {count_vowels("abcd")}")
# print(f"count_vowels(aeiouAEIOU Z!): {count_vowels("aeiouAEIOU Z!")}")
# print(f"count_vowels(zaaaaAaaaam): {count_vowels("zaaaaAaaaam")}")