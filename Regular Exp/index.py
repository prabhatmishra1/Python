import re

pattern = re.compile("a")

s = 'abaababa'

# matcher = pattern.finditer(s)
# cnt = 0
# for match in matcher:
#     cnt+=1
#     print(match.start(),"__", match.end(), "__", match.group())
# print(cnt)

# pass pattern directly to finiter method

# charcter classes
'''
1. [abc] == = > Either a or b or c
2. [ ^ abc] == = > Except a and b and c
3. [a-z] == >Any Lower case alphabet symbol
4. [A-Z] == = > Any upper case alphabet symbol
5. [a-zA-Z] == >Any alphabet symbol
6. [0-9] Any digit from 0 to 9
7. [a-zA-Z0-9] == >Any alphanumeric character
8. [^ a-zA-Z0-9] == >Except alphanumeric characters(Special Characters)
'''
# matcher = re.finditer('[^a-zA-Z0-4]', "a7b@k3zcZ")

# for match in matcher:
#     print(match.start(), match.group())

# Predefine character classes
'''
\s  Space character
\S  Any character except space character
\d  Any digit from 0 to 9
\D  Any character except digit
\w  Any word character[a-zA-Z0-9]
\W  Any character except word character(Special Characters)
.  Any character including special characters
'''

# matcher = re.finditer('\W', "a7b k@9z")

# print(matcher)
# for match in matcher:
#     print(f'{match.start()} {match.group()}')


# Quantifiers
'''
We can use quantifiers to specify the number of occurrences to match
'''

'''
a  Exactly one 'a'
a+  Atleast one 'a'
a*  Any number of a's including zero number
a?  Atmost one 'a' ie either zero number or one number
a{m}  Exactly m number of a's
a{m,n}  Minimum m number of a's and Maximum n number of a's

'''

# matcher = re.finditer('a{2,3}', "abaabaaab")
# for match in matcher:
#     print(f'{match.start()} {match.group()}')

#functions in re

#1......-> match(pattern, string)
''' It matches the pattern in the starting of the string'''

#synax-> match('pattern', 'string')

# match  = re.match('p', 'prabhat')
# # if no match then returns None else match object

# if match:
#     print("yeah it got match with string" ,match.start(), match.end())


#2..........->fullmatch(pattern, string)
'''#so here full pattern has to mtach with full string or we can say that it
matches the exact string'''

#If complete string matched then this function returns Match object otherwise it returns None
# fullmatch = re.fullmatch('prabhat', 'prabht')

# if fullmatch:
#     print("yeah it got matched", fullmatch)


#3...........serach(pattern, string)

#We can use search() function to search the given pattern in the target string
#If the match is available then it returns the Match object which represents first occurrence of the

# it matches the  first occurrence only

# search =  re.search("[a+]", "prabhat")

# print(search)

'''We can use ^ symbol to check whether the given target string starts with our provided pattern or
not.'''
# this we use in urls file of django
s = re.match('^/', '/lals')
print(s)

#4...............findall('regex', stirng)

#To find all occurrences of the match

# findall = re.findall('[a*bcAS0-9]', 'aAS09%32')

# print(findall)


#5...........sub(regex,replacement,tragetedstring)
'''
# so this is like find and repalcement thing, regex se jo bho value match hogi targeted string
vo replace vo jayigi replacment value se
'''

# s = re.sub("[a-zA-Z]","#", 'a#$1bsc23CD$')

# print(s)

#6..............split(regex,'string')

# normal split me regex nhi pass kr paynge but isme kar sakte hai

# s = re.split('[abc]', 'prabhat')

# print(s)


