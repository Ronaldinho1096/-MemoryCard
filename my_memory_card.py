#создай приложение для запоминания информации#создай приложение для запоминания информации
#Создай интерфейс формы вопроса с вариантами ответов. Для этого:
#1) Подключи нужные модули (QtCore и QtWidgets и их элементы).
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

#2) Создай объект-приложение, окно приложения. Задай заголовок и размеры.
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('MemoryCard')
main_win.resize(600, 400)
#3) Создай виджет-вопрос и виджет-кнопку «Ответить».
question = QLabel('Какой национальности не существует')
btn = QPushButton('Ответить')
#4) Создай набор переключателей с вариантами ответов. Расположи их по лэйаутам и объедини в группу.
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1) 

#5) Расположи вопрос, группу переключателей и кнопку по лэйаутам.
AnsGroupBox = QGroupBox('Результат теста')
is_right = QLabel('Правильно/Не правильно')
right_answer = QLabel('Правильный ответ')
ans_layout = QVBoxLayout()
ans_layout.addWidget(is_right)
ans_layout.addWidget(right_answer, alignment=Qt.AlignCenter)
AnsGroupBox.setLayout(ans_layout)
#6) При необходимости, добавь пробелы между виджетами и выровняй их по краю/центру.
layout = QVBoxLayout()
layout.addWidget(question, alignment=Qt.AlignCenter)
layout.addWidget(RadioGroupBox)
layout.addWidget(AnsGroupBox)
layout.addWidget(btn, alignment=Qt.AlignCenter)
main_win.setLayout(layout)

RG = QButtonGroup()
RG.addButton(rbtn_1)
RG.addButton(rbtn_2)
RG.addButton(rbtn_3)
RG.addButton(rbtn_4)

class Question():
    def __init__(self, quest, right_answer, w1, w2, w3):
        self.question = quest
        self.right_answer = right_answer
        self.wrong1 = w1
        self.wrong2 = w2
        self.wrong3 = w3




def ask(q):
    question.setText(q.question)
    rbtn_1.setText(q.right_answer) 
    rbtn_2.setText(q.wrong1)
    rbtn_3.setText(q.wrong2)
    rbtn_4.setText(q.wrong3)

question_list = list()

question_list.append( Question(
    '1 Государственный язык Бразилии',
    'Португальский', 
    'Испанский', 'Итальянский', 'Бразильский') )


question_list.append( Question(
    '2 День народного единства',
    '6 ноября', 
    '7 октября', '12 июня', '21 ноября') )

question_list.append( Question(
    '3 Какого цвета нету на флаге Колумбии?',
    'Зелёного', 
    'Синего', 'Жёлтого', 'Красного') )

question_list.append( Question(
    '4 Число пи?',
    '3,14', 
    '0,1', '10', '6,34') )

question_list.append( Question(
    '5 Когда родился Пушкин?',
    '1799', 
    '1837', '1788', '1811') )

ask(question_list[0])


AnsGroupBox.hide()
def check_answer():
    if rbtn_1.isChecked():
        is_right.setText('Правильно')
        right_answer.setText(rbtn_1.text())    
        main_win.score += 1
    else:
        is_right.setText('Неправильно')
        right_answer.setText(rbtn_1.text())
    print('Стистика')
    print('Всего вопросов', main_win.total)
    print('Правельных ответов', main_win.score)
    print('Рейтинг:', main_win.score/main_win.total * 100, '%')


from random import randint
main_win.cur_question = -1
main_win.total = 0
main_win.score = 0


def next_question():
    main_win.total += 1
    main_win.cur_question = randint(0, len(question_list)-1)
    #if  main_win.cur_question == len (question_list):
    #     main_win.cur_question = 0
    q = question_list[main_win.cur_question]
    ask(q)

next_question()
main_win.cur_question = -1

def show_result():
    if btn.text() == "Следующий вопрос":
        RadioGroupBox.show()
        AnsGroupBox.hide()
        btn.setText("Ответить")  
        RG.setExclusive(False)
        rbtn_1.setChecked(False)
        rbtn_2.setChecked(False)
        rbtn_3.setChecked(False)
        rbtn_4.setChecked(False)
        RG.setExclusive(True)
        next_question()
    else:
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn.setText("Следующий вопрос")
        check_answer()

btn.clicked.connect(show_result)





main_win.show()
app.exec_()