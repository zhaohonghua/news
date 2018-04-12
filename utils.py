def is_chinese_character(c):
	if '\u4e00' <= c and c <= '\u9fff':
		return True
	else:
		return False

def is_chinese_punctuation(c):
	pass

def is_alphabet(c):
	if '\u0041' <= c and c <= '\u005a':
		return True
	elif '\u0061' <= c and c <= '\u007a':
		return True
	else:
		return False

def is_english_punctuation(c):
	pass

def is_number(c):
	if '\u0030' <= c and c < '\u0039':
		return True
	else:
		return False

def is_chinese_string(s):
	for c in s:
		if is_chinese_character(c):
			continue
		else:
			return False
	return True

def load_chinese_stopwords():
	#从文件导入停用词表
	stpwrdpath = "stop_words.txt"
	stpwrd_dic = open(stpwrdpath, 'r')
	stpwrd_content = stpwrd_dic.read()
	#将停用词表转换为list  
	stpwrdlst = stpwrd_content.splitlines()
	stpwrd_dic.close()
	return  stpwrdlst