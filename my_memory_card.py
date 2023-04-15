from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup
from random import *

listof = 0

class Question():
    def __init__(self, right_answer, wrong, wrong1, wrong2, question):
        self.right_answer = right_answer
        self.wrong = wrong
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.question = question

prilozh = QApplication([])
all_list = list()
all_list.append(Question('Португальский', 'Бразильский', 'Испанский', 'Английский', 'Государственный язык Бразилии'))
all_list.append(Question('Правильно', 'Неправильно 1', 'Неправильно 2', 'Неправильно 3', 'Самый сложный вопрос в мире!'))
all_list.append(Question('В России', 'В Великобритании', 'В США', 'В Греции', 'Где находится населённый пункт Свиридоново(это может быть перевод!)'))
all_list.append(Question('Зелёный', 'Красный', 'Синий', 'Белый', 'Какого цвета нет на флаге России?'))
all_list.append(Question('Джава', 'Питон', 'Гадюка', 'Удав', 'Какой змеи нет?'))
konst = QWidget()
konst.setWindowTitle('Memory Card')
konst.resize(400, 200)
knop = QRadioButton()
knop1 = QRadioButton()
knop2 = QRadioButton()
knop3 = QRadioButton()
text = QLabel()
text2 = QLabel()
text3 = QLabel()
answers = [knop, knop1, knop2, knop3]
knop5 = QPushButton('Ответить')

box = QGroupBox('Варианты ответов')
prav = 0
clicked1 = 0
box1 = QGroupBox('Результат теста')
group = QButtonGroup()
group.addButton(knop)
group.addButton(knop1)
group.addButton(knop2)
group.addButton(knop3)

lin4 = QHBoxLayout()
lin4.addWidget(text, alignment = Qt.AlignCenter) #вопрос

lin5 = QHBoxLayout()
lin5.addStretch(1)
lin5.addWidget(knop5, stretch = 2) #ответить
lin5.addStretch(1)

lin2 = QVBoxLayout()
lin2.addWidget(knop, alignment = Qt.AlignCenter) #кнопка
lin2.addWidget(knop1, alignment = Qt.AlignCenter) #кнопка

lin3 = QVBoxLayout()
lin3.addWidget(knop2, alignment = Qt.AlignCenter) #кнопка
lin3.addWidget(knop3, alignment = Qt.AlignCenter) #кнопка

lin = QHBoxLayout()
lin.addLayout(lin2)
lin.addLayout(lin3)

box.setLayout(lin)

lin7 = QHBoxLayout()
lin8 = QHBoxLayout()
lin9 = QVBoxLayout()

lin7.addWidget(text2, alignment = Qt.AlignLeft) #правильно или неправильно
lin8.addWidget(text3, alignment = Qt.AlignHCenter) #правильный ли ответ
lin9.addLayout(lin7)
lin9.addLayout(lin8)

box1.setLayout(lin9)

lin6 = QVBoxLayout()
lin6.addLayout(lin4)
lin6.addWidget(box)
lin6.addWidget(box1)
lin6.addLayout(lin5)

konst.setLayout(lin6)

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong)
    answers[2].setText(q.wrong1)
    answers[3].setText(q.wrong2)
    text.setText(q.question)
    show_question()

def show_result():
    box.hide()
    box1.show()
    knop5.setText('Следующий вопрос')

def show_question():
    box1.hide()
    group.setExclusive(False)
    knop.setChecked(False)
    knop1.setChecked(False)
    knop2.setChecked(False)
    knop3.setChecked(False)
    group.setExclusive(True)
    knop5.setText('Ответить')
    box.show()

def start_test():
    q = all_list[konst.cur_question]
    if 'Ответить' == knop5.text():
        check_answer(q)
    else:
        next_question()
        show_question()

def check_answer(q: Question):
    print('Всё работает!')
    if answers[0].isChecked():
        text2.setText('Правильно!')
        text3.setText(q.right_answer)
        konst.all_right += 1
        show_result()
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        text2.setText('Неправильно!')
        text3.setText(q.right_answer)
        show_result()
    else:
        print('Тест')

def next_question():
    if konst.last_question == 0:
        konst.cur_question = randint(0, len(all_list) - 1) 
    while konst.cur_question == konst.last_question:
        konst.cur_question = randint(0, len(all_list) - 1)
    if konst.total_question >= len(all_list):
        print('Статистика')
        print('-Кол-во вопросов:', len(all_list))
        print('-Правильных ответов:', konst.all_right)
        print('-Рейтинг:', konst.all_right/len(all_list)*100)
        konst.all_right = 0
        konst.total_question = 0
    q = all_list[konst.cur_question]
    ask(q)
    konst.last_question = konst.cur_question
    konst.total_question += 1

knop5.clicked.connect(start_test)

box1.hide()
konst.show()
konst.cur_question = -1
konst.last_question = 0
konst.total_question = 0
konst.all_right = 0
next_question()
prilozh.exec_()