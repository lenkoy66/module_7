#Найдет везде
from itertools import count
from operator import index

from module_3.module_3_5 import result


class WordsFinder:

    def __init__(self, *args):
        self.file_names = list(args)

    def get_all_words(self):
        all_words = {}
        punct = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for files in self.file_names:
            with open(files, encoding='utf-8') as file:
                key = file.name
                text = file.read().lower()
                for char in punct:
                    text = text.replace(char, "")
                all_words[key] = text.split()
        return all_words

    def find(self, word):
        data = self.get_all_words()
        word = word.lower()
        result = {}
        for key, value in data.items():
            if word in value:
                index = value.index(word)
                result[key] = index + 1
        return result

    def count(self, word):
        data = self.get_all_words()
        word = word.lower()
        result = {}
        for key, value in data.items():
            if word in value:
                count = value.count(word)
                result[key] = count
        return result


finder2 = WordsFinder('test_file.txt', 'sampe2.txt')
print(finder2.get_all_words())
print(finder2.find('teXT'))
print(finder2.count('teXT'))


