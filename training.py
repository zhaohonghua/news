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

def word2vector():
	DBSession = sessionmaker(bind=sqliteEngine)
	session = DBSession()

	stopwords = load_chinese_stopwords()
	sentence_list = []

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
			if seg == "。" or seg == "！" or seg == "？":
				#print("/".join(sentence))
				for word in sentence:
					print("%s " % word, end='')
				if len(sentence) > 0:
					sentence_list.append(sentence)
				sentence = []
			else:
				if is_chinese_string(seg) and seg not in stopwords:
					sentence.append(seg)
	
	print('开启训练模型...')
	model = gensim.models.Word2Vec(sentence_list, min_count=1)
	model.save('wordvector.model')