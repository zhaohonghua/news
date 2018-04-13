import gensim

import datasource

def train_word2vector_model():
	sentence_list = datasource.load_training_sentence_array()
	print('开始训练模型...')
	model = gensim.models.Word2Vec(sentence_list, min_count=1)
	model.save('wordvector.model')

def load_word2vector_model():
	model = gensim.models.Word2Vec.load('wordvector.model')
	return model

def train_tfidf_model():
	corpora_documents = datasource.load_training_article_array()

	# get dictionary from corpora_documents
	dictionary = gensim.corpora.Dictionary(corpora_documents)
	print(dictionary.token2id)

	bow_corpus = [dictionary.doc2bow(text) for text in corpora_documents]

	# train the tfidf model
	tfidf_model = gensim.models.TfidfModel(bow_corpus)
	tfidf_model.save("tfidf.model")

def load_tfidf_model():
	tfidf = gensim.models.TfidfModel.load("tfidf.model")
	return tfidf