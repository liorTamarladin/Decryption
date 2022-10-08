import urllib
import urllib.request


class CorpusReader:

    def __init__(self, url):
        with urllib.request.urlopen(url) as response:
            self.corpus = response.read().decode('utf-8')
            response.close()
        self.clean_up()

    def clean_up(self):
        sigma = (',', '.', ':', '\n', '#', '(', ')', '!', '?', '\'', '\"', " ")
        self.corpus = self.corpus.lower()
        for char in self.corpus:
            if char not in sigma:
                if ord(char) < 97 or ord(char) > 122:
                    self.corpus = self.corpus.replace(char, "")


class LanguageModel:

    def __init__(self, filteredCorpus):
        self.sigma = self.sigma()
        self.unigramCount = self.unigramCount(filteredCorpus)
        self.unigramProb = self.unigramProb(filteredCorpus)
        self.bigramCount = self.bigramCount(filteredCorpus)
        self.bigramProb = self.bigramProb()

    def sigma(self):
        alpha = "abcdefghijklmnopqrstuvwxyz"
        sigma = [',', '.', ':', '\n', '#', '(', ')', '!', '?', '\'', '\"', " "]
        for char in alpha:
            sigma.append(char)
        return sigma

    def unigramCount(self, filteredCorpus):
        d = {}
        for i in range(len(self.sigma)):
            d[self.sigma[i]] = 0
        for char in filteredCorpus.corpus:
            d[char] += 1
        return d

    def unigramProb(self, filteredCorpus):
        d = {}
        for i in range(len(self.sigma)):
            C_wi = self.unigramCount[self.sigma[i]]+1
            N = len(filteredCorpus.corpus)
            V = len(self.sigma)
            d[self.sigma[i]] = C_wi/(N+V)

        return d

    def bigramCount(self, filteredCorpus):
        d = {}
        for i in range(len(self.sigma)):
            for j in range(len(self.sigma)):
                d[(self.sigma[i], self.sigma[j])] = 0
        for i in range(1, len(filteredCorpus.corpus)):
            d[(filteredCorpus.corpus[i-1], filteredCorpus.corpus[i])] += 1
        return d

    def bigramProb(self):
        d = {}
        for i in range(len(self.sigma)):
            for j in range(len(self.sigma)):
                C_wiwj = self.bigramCount[(self.sigma[i], self.sigma[j])]+1
                C_wi = self.unigramCount[(self.sigma[i])]
                V = len(self.sigma)
                d[self.sigma[i], self.sigma[j]] = C_wiwj/(C_wi + V)
        return d
