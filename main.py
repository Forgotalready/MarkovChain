import random


class MarkovChain:
    def __init__(self, text):
        corpus = text.split()
        pairs = []
        for i in range(len(corpus) - 1):
            pairs.append((corpus[i], corpus[i + 1]))

        self.words = {}
        for firstWord, secondWord in pairs:
            if firstWord in self.words.keys():
                self.words[firstWord].append(secondWord)
            else:
                self.words[firstWord] = [secondWord]

    def generate(self, text, n: int) -> str:
        corpus = text.split()

        firstWord = random.choice(corpus)
        while firstWord.islower():
            firstWord = random.choice(corpus)

        genStr = [firstWord]

        for i in range(n - 1):
            if genStr[-1] not in self.words.keys():
                genStr.append(random.choice(self.words[random.choice(self.words.keys())]))
            else:
                genStr.append(random.choice(self.words[genStr[-1]]))

        return " ".join(genStr)


def main():
    text = open('hamlet.txt', encoding='utf8').read()
    markov = MarkovChain(text)
    print(markov.generate(text, 10))


if __name__ == "__main__":
    main()
