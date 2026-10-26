import random

#TASK 1

def brute_force(text,p):
    positions = []
    for i in range(len(text) - len(p) + 1):
        if text[i:i+len(p)] == p:
            positions.append(i)
    return positions

#print(brute_force("AAAA", "AA"))

def suffix_array(text):
    sorted_text = sorted(range(len(text)), key=lambda i: text[i:])
    return sorted_text
#print(suffix_array("AAAA"))

def find_block(text, sa, p):
    n = len(sa)
    lo = 0
    hi = n
    while lo < hi:
        mid = (lo + hi) // 2
        prefix = text[sa[mid]:sa[mid] + len(p)]

        if prefix < p:
            lo = mid + 1
        else:
            hi = mid


    a = lo
    lo = a
    hi = n
    while lo < hi:
        mid = (lo + hi) // 2
        prefix = text[sa[mid]:sa[mid] + len(p)]

        if prefix < p:
            lo = mid + 1

        else:
            hi = mid

    b = lo
    return a, b

text_test = "AAGGCGGCTTCA$"
sa_test = suffix_array(text_test)

# Check1
if sorted(sa_test) == list(range(len(text_test))):
    print("Check1 OK")
else:
    print("Check1 failed")

# Check2
for i in range(len(sa_test) - 1):
    if text_test[sa_test[i]:] >= text_test[sa_test[i + 1]:]:
        print("Check2 failed")
        break
else:
    print("Check2 OK")

#TASK 2

def bwt(text, sa):
    result = ""
    for i in sa:
        result += text[i - 1]
    return result

#print(bwt(text_test, sa_test))
BTW = bwt(text_test, sa_test)

def first_occurrence(letters):
    result = {}
    sorted_letters = sorted(letters)
    for i in range(len(sorted_letters)):
        char = sorted_letters[i]
        if char not in result:
            result[char] = i
    return result

print(first_occurrence(BTW))

def inverse_bwt(bwt):
    first = first_occurrence(BTW)
    counts = {}
    occurrences = []

    for char in bwt:
        counts[char] =counts.get(char, 0) + 1
        occurrences.append(counts[char])
    row = 0
    result = ""
    for i in range(len(bwt)-1):
        char = bwt[row]
        result += char
        row = first[char] + occurrences[row] - 1
        result_final = result[::-1] + "$"
    return result_final

#check
for i in range(100):
    t = "".join(random.choice("ACGT") for _ in range(20)) + "$"

    if inverse_bwt(bwt(t, suffix_array(t))) != t:
        print("Check failed")
        break
else:
    print("All checks passed")

#TASK3
class FMIndex:
    def __init__(self, text, s):
        sa = suffix_array(text)
        self.bwt = bwt(text, sa)
        self.first_occurrence = first_occurrence(self.bwt)
        self.s = s
        self.counts = {}

        for char in self.bwt:
            self.counts[char]





