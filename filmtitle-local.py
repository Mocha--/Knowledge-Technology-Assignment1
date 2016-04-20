import os
import operator

# film title class
class FilmTitle:
    def __init__(self, text):
        self.text = text
        self.words = self.text.split(' ')

#review class
class Review:
    def __init__(self, text, filmTitles):
        self.text = text
        self.words = self.text.split(' ')
        self.filmTitles = filmTitles
        self.matchedFilms = {}

    # find film title
    def findFilmTitle(self):
        for filmTitle in self.filmTitles:
            print(filmTitle.text)
            self._initMatrix(filmTitle.text)
            self._fillMatrix(filmTitle.text)
            minDistance = min(self.matrix[-1])
            #allow 1 mistake in every 10 letters
            if (len(filmTitle.text) / minDistance >= 10):
                self.matchedFilms.update({filmTitle.text : self.matrix[-1].count(minDistance)})

        # one review may match multiple film titles
        # let the film title appearing the most times in the review be the matched film title
        if len(self.matchedFilms.keys()) > 0:
            return max(self.matchedFilms.iteritems(), key=operator.itemgetter(1))[0]
        else:
            return 'No matched film title.'

    # init matrix which is used for dynamical programing
    # first row, all 0
    # first colum, 1,2,3....n
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

    # fill the matrix based on 'modified Needleman-wunsch algorithm'
    def _fillMatrix(self, filmTitle):
        for i in range(len(filmTitle)):
            for j in range(len(self.text)):
                upDown = self.matrix[i][j + 1] + 1
                leftRight = self.matrix[i + 1][j] + 1
                diagonal = self.matrix[i][j] if self.text[j].lower() == filmTitle[i].lower() else self.matrix[i][j] + 1
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

    #output file
    resultFile = open('result-local.txt', 'w')

    # get review files
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
        resultFile.write(fileName + ' film title : ' + str(res))
    resultFile.close()
