import jieba
import jieba.analyse
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from bs4 import BeautifulSoup

from datasource import sqliteEngine, News
from utils import is_chinese_string


def test():
	pass

if __name__ == "__main__":
	


	# TextRank关键词提取
	'''
	keywords = jieba.analyse.textrank(text, withWeight=True)
	for x,w in keywords:
		print('%s %s' % (x, w))
	
	print('-'*40)
	for x, w in jieba.analyse.extract_tags(text, withWeight=True):
		print('%s %s' % (x, w))
	'''
