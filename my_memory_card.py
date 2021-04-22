#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle

app = QApplication([])
window = QWidget ()
window.setWindowTitle('Memory Card')


class Question():
    def __init__(self, question, right_a, w1, w2, w3):
        self.question = question
        self.right_a = right_a
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3    

######################################################

question = QLabel('Какой национальности не существует?')
btnok = QPushButton('Ответить')
rbtn1 = QRadioButton('Энцы')
rbtn2 = QRadioButton('Смурфы')
rbtn3 = QRadioButton('Чулымцы')
rbtn4 = QRadioButton('Алеуты')
group = QGroupBox('Варианты ответов')
groupR = QButtonGroup()
groupR.addButton(rbtn1)
groupR.addButton(rbtn2)
groupR.addButton(rbtn3)
groupR.addButton(rbtn4)

rbg1 = QVBoxLayout()
rbg2 = QVBoxLayout()

rbg1.addWidget(rbtn1)
rbg1.addWidget(rbtn2)
rbg2.addWidget(rbtn3)
rbg2.addWidget(rbtn4)

rbgmain = QHBoxLayout()
rbgmain.addLayout(rbg1)
rbgmain.addLayout(rbg2)

group.setLayout(rbgmain)

groupok = QGroupBox('Результаты теста')
answer = QLabel('Неправильный ответ')
groupokline = QVBoxLayout()
groupokline.addWidget(answer, alignment=Qt.AlignCenter)
groupok.setLayout(groupokline)
groupok.hide()

linemain = QVBoxLayout()
linemain.addWidget(question, stretch=2, alignment=Qt.AlignCenter)
linemain.addWidget(group, stretch=8, alignment=Qt.AlignCenter)
linemain.addWidget(groupok, stretch=8, alignment=Qt.AlignCenter)
linemain.addWidget(btnok,stretch=2, alignment=Qt.AlignCenter)

window.setLayout(linemain)

def checkAnswer():
    if list_btns[0].isChecked():
        answer.setText('Правильный ответ')
        window.correct = window.correct + 1
    else:
        answer.setText('Неправильный ответ')
        window.incorrect = window.incorrect + 1
    group.hide()
    groupok.show()
    btnok.setText('Следующий вопрос')

def showQ():
    groupok.hide()
    group.show()
    btnok.setText('Ответить')
    groupR.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    groupR.setExclusive(True)

def btnclick():
    text = btnok.text()
    if text == 'Ответить':
        checkAnswer()

    else:
        qlist.remove(qlist[0])
        if len(qlist) > 0 :
            ask(qlist[0]) #здесь
        else:
            result = QLabel('Правильные ответы')
            quit()


list_btns = [rbtn1, rbtn2, rbtn3, rbtn4]
def ask(q):
    shuffle(list_btns)
    list_btns[0].setText(q.right_a)
    list_btns[1].setText(q.w1)
    list_btns[2].setText(q.w2)
    list_btns[3].setText(q.w3)
    question.setText(q.question)
    showQ()
    

btnok.clicked.connect(btnclick)

window.correct = 0
window.incorrect = 0


qlist = [
    Question('Какой сейчас век?', '21', '11', '20', '22'),
    Question('Самый новый iphone -', '12 ', '11', '5', '101'),
    Question('Виртуальный помощник на iphone', 'Siri', 'Alice', 'Google', 'Cartana'),
    Question('В каком году выпустли первый смартфон с сенсорным экраном?', '1994', '1982', '1978', '2001'),
    Question('Какой язык программирования был создан раньше?', 'Plankalkül', 'Python', 'Java', 'C++'),
    Question('В каком году выпустили первый айфон?', '2007', '2000', '2015', '1984')
]
shuffle(qlist)
ask(qlist[0])


###########################################################

window.show()
app.exec_()