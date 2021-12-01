# # try,except and finally in Python
# try:
# 	f = open("simple.txt", 'r')
# 	f.write("Hello World") #this will give error as we are trying to write in a read only file
#     # except will take care of a certain type of error if no error is specified then all error are considered
# except IOError:
# 	print("2) Couldn't interact with a file!")
# # finally will always get executed
# finally:
# 	print("Will be executed in any way")
#     f.close()



# # regular ecpressions
# import re
#
# # search function
# patterns = ['term1', 'term2']
#
# text = "This is the text with term1 and nothing else"
#
# for pattern in patterns:
# 	print("Searching for a "+pattern)
#
# 	if re.search(pattern,text):
# 		print("MATCH")
# 	else:
# 		print("NO MATCH")
#
#
# match = re.search('term1',text)
# print(type(match))
# print(match.start())
#
#
# # split function
# split_term = '@'
#
# email = 'user@gmail.com'
#
# print(re.split(split_term,email))
#
#
# # findall function
# print(re.findall('term1', text))
#
#
# # Medich character syntax
# def multi_re_find(patterns, phrase):
#
# 	for pattern in patterns:
# 		print("Searching for pattern {}".format(pattern))
# 		print(re.findall(pattern,phrase))
# 		print('\n')
#
# test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'
#
# ### Repetition Syntax
#
# # * means 0 or more 'd'
# # + means 1 or more 'd'
# # ? means 0 or 1 'd'
# # {3} means exactly 3 'd'
# # {1,3} means 1 or 3 'd'
# test_patterns = ['sd*',
# 				 'sd+',
# 				 'sd?',
# 				 'sd{3}',
# 				 'sd{1,3}',
# 				 ]
#
# multi_re_find(test_patterns, test_phrase)
#
# ### Character Sets
#
# # [sd] means 's' or 'd'
# # s[sd]+ means s followed by 1 or more 's' or 'd'
# test_patterns = ['[sd]',
# 				 's[sd]+',
# 				 ]
#
# multi_re_find(test_patterns, test_phrase)
#
# ### Exclusion and Character Ranges
#
# test_phrase = "It's a string! Moreover it has punctuation. Should we remove it?"
#
# # [^!?.]+ means that all after '^' all characters will be used as separator to split the text
# # [a-z]+ searches for all sequences of small letters
# # [A-Z]+ searches for all sequences of big letters
# # [a-zA-Z]+ searches for all sequences of small and big letters
# # [A-Z][a-z]+ searches for one big letter and sequences of small letters after all
# # (words which start with uppercase letter)
# test_patterns = ["[^!?.]+",
# 				 '[a-z]+',
# 				 '[A-Z]+',
# 				 '[a-zA-Z]+',
#                  '[A-Z][a-z]+'
# 				 ]
#
# multi_re_find(test_patterns, test_phrase)
#
# # Escape Codes
#
# test_phrase = "That's a string with 43132 number, and some #hashtag is here"
#
# # \d+ searches for digits (numbers)
# # \D+ searches for non digits
# # \s+ searches for whitespaces
# # \S+ searches for non whitespaces
# # \w+ searches for alpha-numeric chars
# # \W+ searches for non alpha-numeric chars
# test_patterns = [r'\d+',
#                  r'\D+',
#                  r'\s+',
#                  r'\S+',
#                  r'\w+',
#                  r'\W+',
#                  ]
#
# multi_re_find(test_patterns, test_phrase)

# # modules in Python
# import myModule
# # or use import myModule as mm, now we can use mm instead of myModule
# # or use:
# # from myModule import func_in_module
# myModule.func_in_module()


# name and main
# note that the below code is just an example(we need two files one.py and two.py for it to work)
# import one
# print("Top level two.py")
#
# one.func()
#
# if __name__ == '__main__':
# 	print("Two.py being run directly")
# else:
# 	print("Two.py is being imported")
