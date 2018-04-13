import jieba
import jieba.analyse
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from bs4 import BeautifulSoup
import gensim

from datasource import sqliteEngine, News
from utils import is_chinese_string, load_chinese_stopwords

def article2wordarray(article):
	stopwords = load_chinese_stopwords()

	# 分词
	seg_list = jieba.cut(article, cut_all=False)
	
	# 按句子形式输出，去除英文
	word_list = []
	for seg in seg_list:
		if is_chinese_string(seg) and seg not in stopwords:
			word_list.append(seg)
	return word_list

def articles2sentence():
	DBSession = sessionmaker(bind=sqliteEngine)
	session = DBSession()

	stopwords = load_chinese_stopwords()

	out_put_file = "wordarray.txt"
	f = open(out_put_file, "w")
		
	news_list = session.query(News).all()#.limit(1)
	
	for news in news_list:
		sentence_count = 0

		bs = BeautifulSoup(news.content, "html.parser")
		text = bs.get_text()

		# 分词
		seg_list = jieba.cut(text, cut_all=False)
		#print("/ ".join(seg_list))

		# 按句子形式输出，去除英文
		sentence = []
		for seg in seg_list:
			if seg == "。" or seg == "！" or seg == "？":
				sentence_count = sentence_count + 1
				#print("/".join(sentence))
				#for word in sentence:
				#	print("%s " % word, end='')
				if len(sentence) > 0:
					f.writelines(" ".join(sentence))
					f.write("\n")
				sentence = []
			else:
				if is_chinese_string(seg) and seg not in stopwords:
					sentence.append(seg)
		print("news id: %d, sentence_count: %d" % (news.id, sentence_count))
	f.close()

def articles2array():
	DBSession = sessionmaker(bind=sqliteEngine)
	session = DBSession()

	stopwords = load_chinese_stopwords()

	out_put_file = "articlearray.txt"
	f = open(out_put_file, "w")
		
	news_list = session.query(News).all()#.limit(1)
	
	for news in news_list:
		bs = BeautifulSoup(news.content, "html.parser")
		text = bs.get_text()

		# 分词
		seg_list = jieba.cut(text, cut_all=False)
		#print("/ ".join(seg_list))

		# 按句子形式输出，去除英文
		sentence = []

		for seg in seg_list:
			if is_chinese_string(seg) and seg not in stopwords:
				sentence.append(seg)
		if len(sentence) > 0:
			f.writelines(" ".join(sentence))
		f.write("\n")
		print("news id: %d" % (news.id))
	f.close()
