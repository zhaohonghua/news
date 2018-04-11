from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker

mysqlEngine = create_engine("mysql+mysqldb://root:smmdb2016@182.254.211.181:3306/test")
sqliteEngine = create_engine("sqlite:///data.sqlite")

Base = declarative_base()

class News(Base):
	def __init__(self, id, title, content, profile, refer, typeid, keywords, date):
		self.id = id
		self.title = title
		self.content = content
		self.profile = profile
		self.refer = refer
		self.typeid = typeid
		self.keywords = keywords
		self.date = date

	__tablename__ = "news"

	id = Column('news_id', Integer, primary_key = True)
	title = Column('title_name', String)
	content = Column('news_content', String)
	profile = Column('news_profile', String)
	refer = Column('come_from', String)
	typeid = Column('news_type_id', String)
	keywords = Column('keywords', String)
	date = Column('renew_date', DateTime)




def loadDataFromMySQL():
	Session = sessionmaker(bind=mysqlEngine)
	session = Session()

	Session2 = sessionmaker(bind=sqliteEngine)
	session2 = Session2()

	news = session.query(News).all()
	for n in news:
		n2 = News(n.id, n.title, n.content, n.profile, n.refer, n.typeid, n.keywords, n.date)
		session2.add(n2)
	session2.commit()

	session.close()
