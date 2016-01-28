import datetime

class Message():
	'''Encapsulates the message data used in the program internally'''
	def __init__(self, url = '', source = '', text = '', geocode = '', timestamp = datetime.datetime.now()):
		'''Constructor'''
		self.url = url
		self.source = source
		self.text = text
		self.geocode = geocode
		self.timestamp = timestamp
		self.decision = None
		self.confidence = None

	def __str__(self):
		'''Override str method'''
		seq = ('From ', self.url, ' (', self.source, ') at ', self.timestamp.strftime("%Y-%m-%d %H:%M:%S"), '.',
		' Location: ', self.geocode, '.\n', 'Message Body: ', self.text)
		return ''.join(seq)