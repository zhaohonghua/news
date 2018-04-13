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

def load_training_sentence_array():
	word_array_list = []
	f = open("wordarray.txt")
	while 1:
		line = f.readline()
		if line == "":
			break
		else:
			word_array_list.append(line.split())
	return word_array_list

def load_training_article_array():
	word_array_list = []
	f = open("articlearray.txt")
	while 1:
		line = f.readline()
		if line == "":
			break
		else:
			word_array_list.append(line.split())
	return word_array_list

article2 = """
近期，中美贸易战消息持续轰炸市场，中美双方针锋相对，互不退让。为应对美国的500亿美元关税清单，上周中国方面也宣布对美国大豆、飞机等500亿美元商品加征25%的关税。随后，特朗普又表态，称将继续对中国追加1000亿美元商品的关税计划。中美贸易战有愈演愈烈之势头。

　　中国作为全球第一大铜消费国，国产铜远不能满足国内需求，铜原料极度依赖于国外进口。考虑到，中国已经终止了来自于美国的废铝减税政策，那么如果后市中美贸易战继续升级，那么铜原料的进口很可能也会受到不小的钳制。

　　据海关数据显示，2017年，中国自美国进口精炼铜0.21万吨，占总进口量的0.06%；自美国进口废铜53.5万吨，占总进口量的15.1%；自美国进口铜矿43.3万吨，占总进口量的2.5%。

　　从数据上可以看出，中国自美国进口的精炼铜数量微乎其微，铜矿进口量也不大，废铜进口量占比却达到了15.1%，这还不包括一部分经过香港地区流入国内市场的美国废铜。据估计，2017年全年，中国自美国直接及间接的进口量应该在57万吨左右，要远远高于其他国家（如图1所示）。


　　图：中国废铜进口分布图对比


　　再来看，今年海关方面公布的数据：在国内对于进口固体废弃物把控力度日益增强的背景下，2018年，中国前两个月废铜进口数据大幅下滑39.91%，然而主要的进口下滑地区为中国香港、菲律宾、泰国、韩国、澳大利亚等地区，来自美国和德国的废铜进口量仍在继续增长。其中，前两个月来自于美国的废铜进口量同比增长5.78%，为7.8万吨，占前两个月中国废铜进口总量的24%，这一比例也高于今年1月份的22%。可见，相较于往年而言，由于今年限制了亚洲、澳洲等地区废铜货源的流入，国内废铜市场货源更加依赖于欧美等国家。


　　表：2018年前二月废铜进口国别数据


　　综上我们可以得出结论，中国废铜进口极度依赖于美国，而且未来进口自美国的废铜占比可能会继续加大。一旦后市中美贸易战继续升温，从而影响到废铜进口的话，那么必然会使得国内废铜市场货源更加紧张。

　　可能有人会说，中国废铜货源这么依赖于美国，不太可能会在这上面去动刀子。实际上我们反过来考虑也一样，美国每年出口的废铜有七成左右都流入了中国市场，如果失去了中国这个全球第一大铜消费国，美国自然也不会好受。另外，虽然国内废铜市场一直处于供不应求状态，但是去年，国家依然出台了废七类进口禁令，可见国内市场的供需矛盾并不会对国家政策面产生决定性的影响。
（富宝铜研究小组）

喜讯：由富宝资讯、中国再生资源回收利用协会主办的《中国首届再生金属产业链峰会》将于5月3-4日在上海新国际博览中心举行，目前报名通道已开启，会员单元前50名报名免费 》点击进入报名。http://laohu.f139.com/v1/meet/shanghai.do?from=timeline
"""
article1 = """
SMM网讯：中美贸易战消息持续轰炸市场，中美双方针锋相对，互不退让，有愈演愈烈之势头。 中国作为全球第一大铜消费国，国产铜远不能满足国内需求，铜原料极度依赖于国外进口。考虑到，中国已经终止了来自于美国的废铝减税政策，那么如果后市中美贸易战继续升级，那么铜原料的进口很可能也会受到不小的钳制。 据海关数据显示，2017年，中国自美国进口精炼铜0.21万吨，占总进口量的0.06%;自美国进口废铜53.5万吨，占总进口量的15.1%;自美国进口铜矿43.3万吨，占总进口量的2.5%。 从数据上可以看出，中国自美国进口的精炼铜数量微乎其微，铜矿进口量也不大，废铜进口量占比却达到了15.1%，这还不包括一部分经过香港地区流入国内市场的美国废铜。据估计，2017年全年，中国自美国直接及间接的进口量应该在57万吨左右，要远远高于其他国家。 今年海关方面公布的数据：在国内对于进口固体废弃物把控力度日益增强的背景下，2018年，中国前两个月废铜进口数据大幅下滑39.91%，然而来自美国和德国的废铜进口量仍在继续增长。其中，前两个月来自于美国的废铜进口量同比增长5.78%，为7.8万吨，占前两个月中国废铜进口总量的24%，这一比例也高于今年1月份的22%。 综上，中国废铜进口极度依赖于美国，而且未来进口自美国的废铜占比可能会继续加大。一旦后市中美贸易战继续升温，从而影响到废铜进口的话，那么必然会使得国内废铜市场货源更加紧张。 另外，虽然国内废铜市场一直处于供不应求状态，但是去年，国家依然出台了废七类进口禁令，可见国内市场的供需矛盾并不会对国家政策面产生决定性的影响。
[转载需保留出处 - 上海有色网] 中美贸易战恐冲击国内废铜市场 https://news.smm.cn/news/100791876
"""