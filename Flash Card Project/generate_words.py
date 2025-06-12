import random

class GenerateWords:
    def __init__(self):
        self.word=dict()
    def generate(self,data,word_list):
        available_words = [word for word in data if word['French'] not in word_list]
        if not available_words:
            return None
        self.word = random.choice(available_words)
        return self.word