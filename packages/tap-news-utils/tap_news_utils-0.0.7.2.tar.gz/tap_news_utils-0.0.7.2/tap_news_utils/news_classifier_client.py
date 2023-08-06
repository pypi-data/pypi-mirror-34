import jsonrpclib

URL = "http://{}:{}"

class NewsClassifierClient:
    def __init__(self, host='localhost', port=6060):
        self.client = jsonrpclib.ServerProxy(URL.format(host, port))

    def classify(self, text):
        topic = self.client.classify(text)
        return topic
