#https://techdevguide.withgoogle.com/paths/advanced/compress-decompression#!
The Challenge
#In this exercise, you're going to decompress a compressed string.

#Your input is a compressed string of the format number[string] and the decompressed output form should be the string written number times. For example:

#The input

#3[abc]4[ab]c

#Would be output as

#abcabcabcababababc

#Other rules
#Number can have more than one digit. For example, 10[a] is allowed, and just means aaaaaaaaaa

#One repetition can occur inside another. For example, 2[3[a]b] decompresses into aaabaaab

#Characters allowed as input include digits, small English letters and brackets [ ].

#Digits are only to represent amount of repetitions.

#Letters are just letters.

#Brackets are only part of syntax of writing repeated substring.

#Input is always valid, so no need to check its validity.

#Learning objectives
#This question gives you the chance to practice with strings, recursion, algorithm, compilers, automata, and loops. It’s also an opportunity to work on coding with better efficiency.


def split_num(a_str):
    """Split string like "ab2", "a" or "23"
    into ('ab', 2), ("a", 1) or ("", 23)"""
    idx = None
    for i in iter(a_str):
        if i.isdigit():
            idx = a_str.index(i)
            break
    if idx == None:
        return (a_str[:idx], int('1'))
    else:
        return (a_str[:idx], int(a_str[idx:]))

def parse_str(s):
    #print(f'received : {s}')
    buf = ''
    stack = []
    for i in range(len(s)):
        if s[i] == ']':
            _tmp = stack.pop()
            _h, _t = split_num(_tmp)
            buf = _h + buf * _t
        elif s[i] == '[':
            stack.append(buf)
            buf = ''
        else:
            buf += s[i]
    return buf

s = 'a2[b2[c2[x]z]d1[y]]edfg2[hi]'
g = parse_str(s)
print(g)
#abcxxzcxxzdybcxxzcxxzdyedfghihi
