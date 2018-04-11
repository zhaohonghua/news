import jieba
import jieba.analyse
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from bs4 import BeautifulSoup

from datasource import sqliteEngine, News


DBSession = sessionmaker(bind=sqliteEngine)

def test():
	pass

if __name__ == "__main__":
	session = DBSession()
	news = session.query(News).filter(News.id == 100762591).first()
	bs = BeautifulSoup(news.content, "html.parser")
	text = bs.get_text()

	# 分词
	seg_list = jieba.cut(text, cut_all=False)
	print("/ ".join(seg_list))

	# 按句子形式输出，去除英文
	sentence = []
	for seg in seg_list:
		if seg == "。" or seg == "！":


	# TextRank关键词提取
	'''
	keywords = jieba.analyse.textrank(text, withWeight=True)
	for x,w in keywords:
		print('%s %s' % (x, w))
	
	print('-'*40)
	for x, w in jieba.analyse.extract_tags(text, withWeight=True):
		print('%s %s' % (x, w))
	'''
