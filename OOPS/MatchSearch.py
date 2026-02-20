# match - match the exact sequence
# match - beginning only - validate the formats

import re

# o/p match object - matched sequence and span() - start and end index
# checks for the match only at the beginning
# Returns a match object if found, else None.

text = "hello world"
result = re.match("hello", text)
print(result)

# using pattern
test_str = "12345678cfabcgafgdhhdgdgabcABC"
pattern = re.compile("abc")

# re.finditer() finds all non-overlapping matches of a pattern in a string
# returns an iterator of match objects (not a list)

matches = pattern.finditer(test_str)
for match in matches:
    print(match)

# search operation searches the entire string
# returns the first occurrence

text = "python is powerful maths powerful"
result = re.search("powerful", text)
print(result)

# search - search the entire string - to find the occurrences

# raw string
a = r"\tHello"
print(a)

# match() - Determine if the RE matches at the beginning of the string
# search() - Scan through a string, looking for any location where the RE matches
# finditer() - Find all substrings where the RE matches, and return them as an iterator
# findall() - Find all the strings where the RE matches and return a list

my_string = "abc123ABC123abc"
pattern = re.compile(r"123")
matches = pattern.findall(my_string)

for match in matches:
    print(match)

# Methods on match
# group() - return the string matched by the RE
# start() - return the starting position of the match
# end() - return the ending position of the match
# span() - return a tuple containing the (start, end) position of the match

test_str = "12345678cfabcgafgdhhdgdgabcABC"
pattern = re.compile("abc")
matches = pattern.finditer(test_str)

for match in matches:
    print(match)
    print(match.span(), match.start(), match.end())
    print(match.group())  # returns the substring that was matched

# special characters
# meta characters
# regular expressions
# pattern meaning

# abc - matches exact text
# [abc] - a or b or c
# [a-z] - lowercase letters
# [0-9] - digits
# a|b - OR operator

text = "I like abc and abcde"
result = re.findall("abc", text)
print(result)

# [abc] - matches single characters: a OR b OR c
text = "apple banana cat"
result = re.findall("[abc]", text)
print(result)

# [a-z] lowercase letters
text = "I like abc and ABCGHJHJH"
result = re.findall("[a-z]", text)
print(result)

# [0-9] digits
text = "I like abc and 12345BCGHJHJH"
result = re.findall("[0-9]", text)
print(result)

# matches either "cat" OR "bat"
text = "cat,bat,rat,mat"
result = re.findall("cat|bat", text)
print(result)

# any single character
text = "cat bat rat bob"
result = re.findall("c.t", text)
print(result)

# special sequences
'''
Special sequences begin with a backslash \

Sequence    Meaning                          Example

\\d          Digit (0-9)                       \\d\\d
\D          Non-digit                         \D
\w          Word char (a-z, A-Z, 0-9, _)      \w+
\W          Non-word char                     \W
\s          Whitespace                        \s
\S          Non-whitespace                    \S
\b          Word boundary                     \bcat\b
\B          Not a word boundary               \Bcat
'''

# \d Digit (0-9)
print(re.findall(r"\d", "Order 123 costs 450"))

# \D Non-digit
print(re.findall(r"\D", "Order 123 costs 450"))

# \w Word char (a-z, A-Z, 0-9, _)
text = "Python_3 version!"
result = re.findall(r"\w", text)
print(result)

# \W Non-word char
# Matches anything that is NOT a word character
text = "Hello@123!"
result = re.findall(r"\W", text)
print(result)

# \s Whitespace (spaces, tabs and newline)
text = "Hello World\nPython"
result = re.findall(r"\s", text)
print(result)

# \S Non-whitespace
text = "Hello World\nPython"
result = re.findall(r"\S", text)
print(result)

# \b Word boundary
text = "cat scatter catalog"
result = re.findall(r"\bcat\b", text)
print(result)

# \B Not a word boundary
text = "cat catalog scatter"
result = re.findall(r"cat\B", text)
print(result)

# Meta-characters have special meaning in regex.

# Meta-character    Meaning
# .                 Any character
# ^                 Start of string
# $                 End of string
# *                 0 or more
# +                 1 or more
# ?                 0 or 1
# {n}               Exactly n times
# {n,}              n or more
# {n,m}             Between n and m
# []                Character set
# ()                Grouping
# ^ Start of string
text = "Python is easy"
print(re.findall(r"^Python", text))

# $ End of string
text = "Python is easy"
print(re.findall(r"easy", text))

# * 0 or more
text = "ab abb abbb a"
print(re.findall(r"ab*", text))

# + 1 or more
text = "ab abb abbb a"
print(re.findall(r"ab+", text))

# ? 0 or 1
text = "color colour colr"
print(re.findall(r"colou?r", text))

# {n} Exactly n times
text = "111 22 3333 68777"
print(re.findall(r"\d{3}", text))

# {n,} n or more
text = "1 22 333 4444"
print(re.findall(r"\d{3,}", text))

# {n,m} Between n and m
text = "1 22 333 4444"
print(re.findall(r"\d{2,3}", text))

# [] Character set
text = "apple banana cat"
print(re.findall(r"[abc]", text))

# () Grouping
text = "2026-02-11"
result = re.findall(r"(\d{4})-(\d{2})-(\d{2})", text)
print(result)

#Regular expression modifiers
# Regular expression modifiers

'''
Modifier        Short     Purpose
re.IGNORECASE   re.I      Case-insensitive matching
re.MULTILINE    re.M      ^ and $ match each line
re.DOTALL       re.S      . matches newline
re.VERBOSE      re.X      Write readable regex with comments
re.ASCII        re.A      ASCII-only matching
re.DEBUG        ---       Debug pattern
'''
# re.IGNORECASE   re.I   Case-insensitive matching
text = "Python"
print(re.search(r"python", text, re.I))

# re.MULTILINE    re.M   ^ and $ match each line
text = "Hello\nPython"
print(re.findall(r"^Python", text, re.M))

# re.DOTALL  re.S  - . matches newline

text = "Hello\nWorld"
print(re.search(r"Hello.*World", text, re.S))

# re.VERBOSE  re.X   Write readable regex with comments - make it more readable

pattern = re.compile(r"""
    789nbgjklksdgdsksl..^^&*&89
""", re.X)

print(pattern)

# re.ASCII  re.A  - ASCII-only matching

text = "Python123"
print(re.findall(r"\w+", text, re.A))
# re.DEBUG  -  Debug pattern
pattern = re.compile(r"""
    789nbgjklksdgdsksl..^^&*&89
""", re.DEBUG)

print(pattern)

#assertions-validating the output or checking certain condition
'''
^  - Start of string
$  - End of string
\b - Word boundary
\B - Not word boundary
(?=...)  - Positive Lookahead
(?!...)  - Negative Lookahead
(?<=...) - Positive Lookbehind
(?<!...) - Negative Lookbehind
'''
# ^  - Start of string
text = "Python is easy"
print(re.findall(r"^Python", text))


# $  - End of string
text = "Python is easy"
print(re.findall(r"easy$", text))


# \b  - Word boundary
text = "cat scatter catalog"
print(re.findall(r"\bcat\b", text))


# \B  - Not word boundary
text = "cat scatter catalog"
print(re.findall(r"cat\B", text))

# (?=...)  - Positive Lookahead  = match only if followed by something
text = "user1 admin2 test"
print(re.findall(r"\w+(?=\d)", text))


# (?!...)  - Negative Lookahead
text = "user1 admin test2"
print(re.findall(r"\w+(?!\d)", text))

# (?<=...) → Positive Lookbehind - match only if preceded by something
text = "Price ₹500"
print(re.findall(r"(?<=₹)\d+", text))


# (?<!...) → Negative Lookbehind
text = "Price ₹500 and 300"
print(re.findall(r"(?<!₹)\d+", text))
