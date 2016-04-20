import os
import operator
import editdistance

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

    #find film title based on the given film title list
    def findFilmTitle(self):
        for filmTitle in self.filmTitles:
            # print(filmTitle.text)
            self.wordsCompare(filmTitle)

        # one review may match multiple film titles
        # let the film title appearing the most times in the review be the matched film title
        if len(self.matchedFilms.keys()) > 0:
            return max(self.matchedFilms.iteritems(), key=operator.itemgetter(1))[0]
        else:
            return 'No matched film title.'

    # text broken into separate words
    # film title broken into separate words as well
    # compare each word in review text and film title
    # edit distance threshold I set is the number of film title words
    def wordsCompare(self, filmTitle):
        curPos = 0
        count = 0
        while True:
            if curPos + len(filmTitle.words) > len(self.words):
                break
            penalty = 0
            for i in range(len(filmTitle.words)):
                dis = editdistance.eval(filmTitle.words[i], self.words[curPos + i])
                penalty += dis
            if penalty <= len(filmTitle.words):
                count += 1
            curPos += 1
        self.matchedFilms.update({filmTitle.text : count})

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
    resultFile = open('result-global.txt', 'w')

    # get all reviews files
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
        print(fileName + ' film title : ' + str(res))
        resultFile.write(fileName + ' film title : ' + str(res))
    resultFile.close()
