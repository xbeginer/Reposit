from tkinter import*

tru_ansver =("лихо", "нагоняи получать", "собака лает", "яйца", "Билли Айлиш", "синего", "12", "Карл", "художники", "слепень",
             "святого Петра", "Капитан", "Иван Павлов", "Лукино Висконти", "не покладая рук", "Снежинка", "полномочия",
             "фронтмен", "«Каникулы Бонифация»", "Полина Гагарина", "Шико", "«Философский пароход»", "за историка")
def new():
    global a,b,c,d,root,text_1
    root = Tk()
    root.geometry("800x600")
    root.resizable(height=False, width=False)
    root.configure(bg='violet')
    text_1 = Label(root, text='Что, если принимать во внимание расхожую фразу, измеряют в фунтах?', font=("Arial", 16), fg="blue", bg="black")
    text_1.place(x=0,y=0, width=800, height=50)
    one = Button(root, text="лыко", font=("Arial", 16), fg="blue", bg="black", command=compare)
    one.place(x=100, y=200, width=150, height=150)
    two = Button(root, text="мыло", font=("Arial", 16), fg="blue", bg="black", command=compare_2)
    two.place(x=100, y=400, width=150, height=150)
    tre = Button(root,text="лихо", font=("Arial", 16), fg="blue", bg="black", command=compare_3)
    tre.place(x=400, y=200, width=150, height=150)
    four = Button(root, text="шило", font=("Arial", 16), fg="blue", bg="black", command=compare_4)
    four.place(x=400, y=400, width=150, height=150)
    a = one['text']
    b = two['text']
    c = tre['text']
    d = four['text']

def compare():
    global comparison_1, score
    comparison_1 = tru_ansver[0]
    if a == comparison_1:
        score = 10000
    else:
        arm = Label(root,text='Увы, ты проиграл!', font=("Arial", 30), fg="blue", bg="black")
        arm.place(x=0, y=0, width=800, height=600)
        home = Button(root,text=" Вернутся на главную!", font=("Arial", 16), fg="blue", bg="black", command=home_home)
        home.place(x=0, y=500, width=100, height=100)


def compare_2():
    if b == comparison_1:
        score = 10000
    else:
        arm_2 = Label(root,text='Увы, ты проиграл!', font=("Arial", 30), fg="blue", bg="black")
        arm_2.place(x=0, y=0, width=800, height=600)
        home = Button(root,text=" Вернутся на главную!", font=("Arial", 16), fg="blue", bg="black", command=home_home)
        home.place(x=0, y=500, width=100, height=100)


def compare_3():
    if c:
        global a_2, b_2, c_2, d_2
        score = 10000
        text_2 = Label(root, text="Чему не учат в школе в известной песне?",font=("Arial", 16), fg="blue", bg="black")
        text_2.place(x=0,y=0, width=800, height=50)
        one_2 = Button(root, text="вычитать и умножать", font=("Arial", 16), fg="blue", bg="black", command=compare_5)
        one_2.place(x=100, y=200, width=180, height=180)
        two_2 = Button(root, text="буквы разные писать", font=("Arial", 16), fg="blue", bg="black", command=compare_6)
        two_2.place(x=100, y=400, width=180, height=180)
        tre_2 = Button(root,text="нагоняи получать", font=("Arial", 16), fg="blue", bg="black", command=compare_7)
        tre_2.place(x=400, y=200, width=180, height=180)
        four_2 = Button(root, text="малышей не обижать", font=("Arial", 16), fg="blue", bg="black", command=compare_8)
        four_2.place(x=400, y=400, width=180, height=180)
        a_2 = one_2['text']
        b_2 = two_2['text']
        c_2 = tre_2['text']
        d_2 = four_2['text']

def compare_4():
    if d == comparison_1:
        score = 10000
    else:
        arm_4 = Label(root,text='Увы, ты проиграл!', font=("Arial", 30), fg="blue", bg="black")
        arm_4.place(x=0, y=0, width=800, height=600)
        home = Button(root,text=" Вернутся на главную!", font=("Arial", 16), fg="blue", bg="black", command=home_home)
        home.place(x=0, y=500, width=100, height=100)


def compare_5():
    global comparison_2, score
    comparison_2 = tru_ansver[1]
    if a_2 == comparison_2:
        score =+ 10000
    else:
        arm_5 = Label(root, text='Увы, ты проиграл!', font=("Arial", 30), fg="blue", bg="black")
        arm_5.place(x=0, y=0, width=800, height=600)
        home = Button(root, text=" Вернутся на главную!", font=("Arial", 16), fg="blue", bg="black", command=home_home)
        home.place(x=0, y=500, width=100, height=100)


def compare_6():
    if b_2 == comparison_2:
        score =+10000
    else:
        arm_3 = Label(root,text='Увы, ты проиграл!', font=("Arial", 30), fg="blue", bg="black")
        arm_3.place(x=0, y=0, width=800, height=600)
        home = Button(root,text=" Вернутся на главную!", font=("Arial", 16), fg="blue", bg="black", command=home_home)
        home.place(x=0, y=500, width=100, height=100)


def compare_7():
    if c_2:
        global tre_3
        score =+ 10000
        text_3 = Label(root, text="Что, согласно поговорке, происходит, когда идет караван?", font=("Arial", 16), fg="blue", bg="black")
        text_3.place(x=0, y=0, width=800, height=50)
        one_3 = Button(root, text="кошка мурлычет", font=("Arial", 16), fg="blue", bg="black", command=compare_5)
        one_3.place(x=100, y=200, width=180, height=180)
        two_3 = Button(root, text="ветер воет", font=("Arial", 16), fg="blue", bg="black", command=compare_6)
        two_3.place(x=100, y=400, width=180, height=180)
        tre_3 = Button(root, text="собака лает", font=("Arial", 16), fg="blue", bg="black", command=compare_9)
        tre_3.place(x=400, y=200, width=180, height=180)
        four_3 = Button(root, text="море волнуется", font=("Arial", 16), fg="blue", bg="black", command=compare_8)
        four_3.place(x=400, y=400, width=180, height=180)


def compare_8():
    if d_2 == comparison_2:
        score = 10000
    else:
        arm_6 = Label(root,text='Увы, ты проиграл!', font=("Arial", 30), fg="blue", bg="black")
        arm_6.place(x=0, y=0, width=800, height=600)
        home = Button(root,text=" Вернутся на главную!", font=("Arial", 16), fg="blue", bg="black", command=home_home)
        home.place(x=0, y=500, width=100, height=100)

def compare_9():
    if tre_3:
        global tre_4
        text_4 = Label(root, text="Что обычно готовят способом пашот?", font=("Arial", 16), fg="blue", bg="black")
        text_4.place(x=0, y=0, width=800, height=50)
        one_4 = Button(root, text="сыр", font=("Arial", 16), fg="blue", bg="black", command=compare_10)
        one_4.place(x=100, y=200, width=180, height=180)
        two_4 = Button(root, text="багет", font=("Arial", 16), fg="blue", bg="black", command=compare_10)
        two_4.place(x=100, y=400, width=180, height=180)
        tre_4 = Button(root, text=f"{tru_ansver[3]}", font=("Arial", 16), fg="blue", bg="black", command=compare_10)
        tre_4.place(x=400, y=200, width=180, height=180)
        four_4 = Button(root, text="ветчину", font=("Arial", 16), fg="blue", bg="black", command=compare_10)
        four_4.place(x=400, y=400, width=180, height=180)
    else:
        arm_4 = Label(root, text='Увы, ты проиграл!', font=("Arial", 30), fg="blue", bg="black")
        arm_4.place(x=0, y=0, width=800, height=600)
        home = Button(root, text=" Вернутся на главную!", font=("Arial", 16), fg="blue", bg="black", command=home_home)
        home.place(x=0, y=500, width=100, height=100)

def home_home():
    root.withdraw()

def compare_10():
    if tre_4:
        global tre_5
        text_5 = Label(root, text="Как зовут известную американскую певицу, автора хита «Bad Guy»?", font=("Arial", 16), fg="blue", bg="black")
        text_5.place(x=0, y=0, width=800, height=50)
        one_5 = Button(root, text="Бенни Айриш", font=("Arial", 16), fg="blue", bg="black", command=compare_11)
        one_5.place(x=100, y=200, width=180, height=180)
        two_5 = Button(root, text="Питти Бейлиш", font=("Arial", 16), fg="blue", bg="black", command=compare_11)
        two_5.place(x=100, y=400, width=180, height=180)
        tre_5 = Button(root, text=f"{tru_ansver[4]}", font=("Arial", 16), fg="blue", bg="black", command=compare_11)
        tre_5.place(x=400, y=200, width=180, height=180)
        four_5 = Button(root, text="Санни Бритиш", font=("Arial", 16), fg="blue", bg="black", command=compare_11)
        four_5.place(x=400, y=400, width=180, height=180)
    else:
        arm_5 = Label(root, text='Увы, ты проиграл!', font=("Arial", 30), fg="blue", bg="black")
        arm_5.place(x=0, y=0, width=800, height=600)
        home = Button(root, text=" Вернутся на главную!", font=("Arial", 16), fg="blue", bg="black", command=home_home)
        home.place(x=0, y=500, width=100, height=100)
def compare_11():
    if tre_5:
        global tre_6
        text_6 = Label(root, text="Оттенком какого цвета является «ниагара»?", font=("Arial", 16), fg="blue", bg="black")
        text_6.place(x=0, y=0, width=800, height=50)
        one_6 = Button(root, text="зеленого", font=("Arial", 16), fg="blue", bg="black", command=compare_12)
        one_6.place(x=100, y=200, width=180, height=180)
        two_6 = Button(root, text="красного", font=("Arial", 16), fg="blue", bg="black", command=compare_12)
        two_6.place(x=100, y=400, width=180, height=180)
        tre_6 = Button(root, text=f"{tru_ansver[5]}", font=("Arial", 16), fg="blue", bg="black", command=compare_12)
        tre_6.place(x=400, y=200, width=180, height=180)
        four_6 = Button(root, text="желтого", font=("Arial", 16), fg="blue", bg="black", command=compare_12)
        four_6.place(x=400, y=400, width=180, height=180)
    else:
        arm_6 = Label(root, text='Увы, ты проиграл!', font=("Arial", 30), fg="blue", bg="black")
        arm_6.place(x=0, y=0, width=800, height=600)
        home = Button(root, text=" Вернутся на главную!", font=("Arial", 16), fg="blue", bg="black", command=home_home)
        home.place(x=0, y=500, width=100, height=100)
def compare_12():
    if tre_6:
        global tre_7
        text_7 = Label(root, text="Сколько человек разделили премию «Золотой орел» в номинации «Лучшая мужская роль» в 2008 году?", font=("Arial", 10), fg="blue", bg="black")
        text_7.place(x=0, y=0, width=800, height=50)
        one_7 = Button(root, text="2", font=("Arial", 16), fg="blue", bg="black", command=compare_13)
        one_7.place(x=100, y=200, width=180, height=180)
        two_7 = Button(root, text="3", font=("Arial", 16), fg="blue", bg="black", command=compare_13)
        two_7.place(x=100, y=400, width=180, height=180)
        tre_7 = Button(root, text=f"{tru_ansver[6]}", font=("Arial", 16), fg="blue", bg="black", command=compare_13)
        tre_7.place(x=400, y=200, width=180, height=180)
        four_7 = Button(root, text="5", font=("Arial", 16), fg="blue", bg="black", command=compare_13)
        four_7.place(x=400, y=400, width=180, height=180)
    else:
        arm_7 = Label(root, text='Увы, ты проиграл!', font=("Arial", 30), fg="blue", bg="black")
        arm_7.place(x=0, y=0, width=800, height=600)
        home = Button(root, text=" Вернутся на главную!", font=("Arial", 16), fg="blue", bg="black", command=home_home)
        home.place(x=0, y=500, width=100, height=100)

def compare_13():
    global tre_8
    if tre_7:
        text_8 = Label(root, text="Какое имя было самым распространенным у шведских королей?", font=("Arial", 16), fg="blue", bg="black")
        text_8.place(x=0, y=0, width=800, height=50)
        one_8 = Button(root, text="Густав", font=("Arial", 16), fg="blue", bg="black", command=compare_14)
        one_8.place(x=100, y=200, width=180, height=180)
        two_8 = Button(root, text="Фредрик", font=("Arial", 16), fg="blue", bg="black", command=compare_14)
        two_8.place(x=100, y=400, width=180, height=180)
        tre_8 = Button(root, text=f"{tru_ansver[7]}", font=("Arial", 16), fg="blue", bg="black", command=compare_14)
        tre_8.place(x=400, y=200, width=180, height=180)
        four_8 = Button(root, text="Оскар", font=("Arial", 16), fg="blue", bg="black", command=compare_14)
        four_8.place(x=400, y=400, width=180, height=180)
    else:
        arm_8 = Label(root, text='Увы, ты проиграл!', font=("Arial", 30), fg="blue", bg="black")
        arm_8.place(x=0, y=0, width=800, height=600)
        home = Button(root, text=" Вернутся на главную!", font=("Arial", 16), fg="blue", bg="black", command=home_home)
        home.place(x=0, y=500, width=100, height=100)

def compare_14():
    global tre_9
    if tre_8:
        text_9 = Label(root, text="Кто в начале прошлого века жил в общежитии «Корабль-прачечная» на Монмартре?", font=("Arial", 14), fg="blue", bg="black")
        text_9.place(x=0, y=0, width=800, height=50)
        one_9 = Button(root, text="матросы", font=("Arial", 16), fg="blue", bg="black", command=compare_15)
        one_9.place(x=100, y=200, width=180, height=180)
        two_9 = Button(root, text="прачки", font=("Arial", 16), fg="blue", bg="black", command=compare_15)
        two_9.place(x=100, y=400, width=180, height=180)
        tre_9 = Button(root, text=f"{tru_ansver[8]}", font=("Arial", 16), fg="blue", bg="black", command=compare_15)
        tre_9.place(x=400, y=200, width=180, height=180)
        four_9 = Button(root, text="официанты", font=("Arial", 16), fg="blue", bg="black", command=compare_15)
        four_9.place(x=400, y=400, width=180, height=180)
    else:
        arm_9 = Label(root, text='Увы, ты проиграл!', font=("Arial", 30), fg="blue", bg="black")
        arm_9.place(x=0, y=0, width=800, height=600)
        home = Button(root, text=" Вернутся на главную!", font=("Arial", 16), fg="blue", bg="black", command=home_home)
        home.place(x=0, y=500, width=100, height=100)

def compare_15():
    global tre_10
    if tre_9:
        text_10 = Label(root, text="Один из видов какого насекомого признали самым быстрым в мире?", font=("Arial", 14), fg="blue", bg="black")
        text_10.place(x=0, y=0, width=800, height=50)
        one_10 = Button(root, text="комар", font=("Arial", 16), fg="blue", bg="black", command=compare_16)
        one_10.place(x=100, y=200, width=180, height=180)
        two_10 = Button(root, text="майский жук", font=("Arial", 16), fg="blue", bg="black", command=compare_16)
        two_10.place(x=100, y=400, width=180, height=180)
        tre_10 = Button(root, text=f"{tru_ansver[9]}", font=("Arial", 16), fg="blue", bg="black", command=compare_16)
        tre_10.place(x=400, y=200, width=180, height=180)
        four_10 = Button(root, text="шершень", font=("Arial", 16), fg="blue", bg="black", command=compare_16)
        four_10.place(x=400, y=400, width=180, height=180)
    else:
        arm_9 = Label(root, text='Увы, ты проиграл!', font=("Arial", 30), fg="blue", bg="black")
        arm_9.place(x=0, y=0, width=800, height=600)
        home = Button(root, text=" Вернутся на главную!", font=("Arial", 16), fg="blue", bg="black", command=home_home)
        home.place(x=0, y=500, width=100, height=100)

def compare_16():
    global tre_11
    if tre_10:
        text_11 = Label(root, text="Флаг какого святого не является частью флага Великобритании?", font=("Arial", 14), fg="blue", bg="black")
        text_11.place(x=0, y=0, width=800, height=50)
        one_11 = Button(root, text="святого Андрея", font=("Arial", 16), fg="blue", bg="black", command=compare_17)
        one_11.place(x=100, y=200, width=180, height=180)
        two_11 = Button(root, text="святого Патрика", font=("Arial", 16), fg="blue", bg="black", command=compare_17)
        two_11.place(x=100, y=400, width=180, height=180)
        tre_11 = Button(root, text=f"{tru_ansver[10]}", font=("Arial", 16), fg="blue", bg="black", command=compare_17)
        tre_11.place(x=400, y=200, width=180, height=180)
        four_11 = Button(root, text="святого Георгия", font=("Arial", 16), fg="blue", bg="black", command=compare_17)
        four_11.place(x=400, y=400, width=180, height=180)
    else:
        arm_9 = Label(root, text='Увы, ты проиграл!', font=("Arial", 30), fg="blue", bg="black")
        arm_9.place(x=0, y=0, width=800, height=600)
        home = Button(root, text=" Вернутся на главную!", font=("Arial", 16), fg="blue", bg="black", command=home_home)
        home.place(x=0, y=500, width=100, height=100)

def compare_17():
    global tre_12
    if tre_11:
        text_12 = Label(root, text="Какого романа нет у Артура Хейли?", font=("Arial", 14), fg="blue", bg="black")
        text_12.place(x=0, y=0, width=800, height=50)
        one_12 = Button(root, text="«Аэропорт»", font=("Arial", 16), fg="blue", bg="black", command=compare_18)
        one_12.place(x=100, y=200, width=180, height=180)
        two_12 = Button(root, text="«Отель»", font=("Arial", 16), fg="blue", bg="black", command=compare_18)
        two_12.place(x=100, y=400, width=180, height=180)
        tre_12 = Button(root, text=f"{tru_ansver[11]}", font=("Arial", 16), fg="blue", bg="black", command=compare_18)
        tre_12.place(x=400, y=200, width=180, height=180)
        four_12 = Button(root, text="«Колеса»", font=("Arial", 16), fg="blue", bg="black", command=compare_18)
        four_12.place(x=400, y=400, width=180, height=180)
    else:
        arm_9 = Label(root, text='Увы, ты проиграл!', font=("Arial", 30), fg="blue", bg="black")
        arm_9.place(x=0, y=0, width=800, height=600)
        home = Button(root, text=" Вернутся на главную!", font=("Arial", 16), fg="blue", bg="black", command=home_home)
        home.place(x=0, y=500, width=100, height=100)

def compare_18():
    if tre_12:
        root.destroy()
        txt['text'] = "Поздравляю, ваш выйгрыш составил 1000000 рублей!!!"
        start['text'] = "Пройти еще раз!"


window = Tk()
window.geometry("700x600")
window.resizable(height=False, width=False)
window.image = PhotoImage(file='logo_2.png')
bg_logo = Label(window, image=window.image)
bg_logo.grid(row=0, column= 0)
txt = Label(text="Добро пожаловать в игру 'Кто хочет стать миллионером!'", font=("Arial", 16), fg="blue", bg="black")
txt.place(x=0, y=0, width=700, height=50)
start = Button(text='Начать игру!', font=("Arial", 16), fg="blue", bg="black", command=new)
start.place(x=250, y=300, width=200, height=100)

window.mainloop()