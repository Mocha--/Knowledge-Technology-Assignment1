import os

class FilmTitle:
    def __init__(self, text):
        self.text = text
        self.words = self.text.split(' ')

class Review:
    def __init__(self, text, filmTitles):
        self.text = text
        self.words = self.text.split(' ')
        self.filmTitles = filmTitles
        self.matchedFilms = {}

    def findFilmTitle(self):
        for filmTitle in self.filmTitles:
            self._initMatrix(filmTitle.text)
            self._fillMatrix(filmTitle.text)
            minDistance = min(self.matrix[-1])
            if minDistance == 0:
                self.matchedFilms.update({filmTitle.text : self.matrix[-1].count(minDistance)})
        return self.matchedFilms

    def _initMatrix(self, filmTitle):
        self.matrix = []
        for i in range(len(filmTitle) + 1):
            row = []
            for j in range(len(self.text) + 1):
                row.append(0)
            self.matrix.append(row)

        for i in range(len(filmTitle) + 1):
            self.matrix[i][0] = i

        return self.matrix

    def _fillMatrix(self, filmTitle):
        for i in range(len(filmTitle)):
            for j in range(len(self.text)):
                upDown = self.matrix[i][j + 1] + 1
                leftRight = self.matrix[i + 1][j] + 1
                diagonal = self.matrix[i][j] if self.text[j] == filmTitle[i] else self.matrix[i][j] + 1
                self.matrix[i + 1][j + 1] = min(upDown, leftRight, diagonal)

if __name__ == '__main__':
    filmTitles = []
    f = open('film_titles.txt', 'r')
    while True:
        title = f.readline()
        if not title:
            break
        filmTitles.append(FilmTitle(title))
    f.close()
    print(len(filmTitles))

    reviewFileNames = os.listdir(os.getcwd() + '/revs')
    for fileName in reviewFileNames:
        f = open('revs/' + fileName)
        text = ''
        while True:
            line = f.readline()
            if not line:
                break
            text += line
        review = Review(text, filmTitles)
        res = review.findFilmTitle()
        print(res)
