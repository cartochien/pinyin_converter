import pandas as pd
from pinyin_converter import pinyin_converter

file_to_convert = pd.read_excel('example_pinyin_list.xlsx')
pinyin_num_list = []

def selection(index):
	term = file_to_convert.iloc[index]
	return term['Pinyin']

size = len(file_to_convert)
selection_indices = list(range(size))

for index in selection_indices:
	pinyin = selection(index)
	pinyin_num_converted = pinyin_converter(pinyin)
	pinyin_num_list.append(pinyin_num_converted)

print("Finished converting pinyin!")
df = pd.DataFrame(pinyin_num_list, columns=['PinyinNum'])

df.to_excel("pinyin_num_converted.xlsx", index=False)