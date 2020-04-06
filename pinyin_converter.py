import pandas as pd

word_beginnings = ['b','p','m','f','d','t','n','l','g','k','h','z','c','s','zh','ch','sh','r','j','q','w','x','y']
word_endings = ['a','o','e','i','er','ai','ei','ao','ou','an','en','ang','eng','ong','ia','iao','ie','iu','ian','in','iang','ing','iong','u','ua','uo','uai','ui','uan','un','uang','ueng','ü','üe','üan','ün']

# input 
# the script will read the input starting from the
# END of the string to the BEGINNING of the string

# identify the word ending that has the longest len()
# it then looks for the first instance of a beginning 
# of a word and then repeat process until it reaches
# the very beginning of the string

words_constructed = []
pinyin_converts = input("What pinyin do you want to convert?\n")


#For loop to identify longest possible ending in pinyin input. 
#The longest possible ending in Chinese is four letters hence why we start at -4.

def PinyinParser(pinyin_converts):
	if len(pinyin_converts) == 0:
		return
	for i in range(-4,0):
		# print(pinyin_converts[i:])
		pinyin_end_substring = pinyin_converts[i:]
		if pinyin_end_substring in word_endings:
			ending_index = len(pinyin_converts) + i
			# print(pinyin_end_substring)
			# For loop inside first If statement identifying the beginning of the word.
			# It does this by starting two index positions in front of the ending_index 
			# (which is the value of the first index of the identified word ending) until
			# it identifies the beginning of the word (which will either be 1 or 2 letters long).
			for j in range(ending_index-2, ending_index):
				# print(pinyin_converts[i:])
				pinyin_beg_substring = pinyin_converts[j:ending_index]
				# print(pinyin_beg_substring)
				if pinyin_beg_substring in word_beginnings:
					pinyin_combined_substring = pinyin_beg_substring + pinyin_end_substring
					words_constructed.insert(0, pinyin_combined_substring)
					pinyin_converts = pinyin_converts[:j]
					PinyinParser(pinyin_converts)
					# print(pinyin_beg_substring)
					# print(pinyin_converts)
					break
				else:
					continue		
			break
		else:
			continue
# print(ending_index)		
PinyinParser(pinyin_converts)
print(words_constructed)







