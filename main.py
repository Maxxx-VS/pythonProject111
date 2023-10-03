# #ДЗ №1.1 ########################################################################################
# a = int(input("Введиет число №1: "))
# b = int(input("Введиет число №2: "))
# c = int(input("Введиет число №3: "))
# print (a + b + c)
# print (a * b * c)
# #ДЗ №1.2 ########################################################################################
# a1 = int(input("Введие уровень з/п: "))
# b1 = int(input("Сумма платежа по кредиту: "))
# c1 = int(input("Комунальная оплата: "))
# print (a1 - b1 - c1)
# #ДЗ №1.3 ########################################################################################
# l1 = int(input("Введиет длину диагонали №1: "))
# l2 = int(input("Введиет длину диагонали №2: "))
# s = 0.5 * l1 * l2
# print (s)
# #ДЗ №1.4 ########################################################################################
# print ("To be", "or not", "to be", sep = "\n")

# #ДЗ №2.1 ########################################################################################
# day = 1
# l = 10
# p = int(input("Введите увеличение дистанции: "))
# if p > 0 and p < 51:
#     while l < 200:
#         l = l + p
#         day = day + 1
#     print(day)
#     print(l)
# else:
#     print ("Введите другое значение увеличения дистанции")

# #ДЗ №3.1 ########################################################################################
# num_1 = int(input("Enter num 1: "))
# num_2 = int(input("Enter num 2: "))
# num_3 = int(input("Enter num 3: "))
# print (num_1 * 100 + num_2 * 10 + num_3)
# #ДЗ №3.2 ########################################################################################
# num = int(input("Введите 4х значное число: "))
# num_1 = num // 1000
# num_2 = num // 100 % 10
# num_3 = num % 100 // 10
# num_4 = num % 10
# print (num_1 * num_2 * num_3 * num_4)
# #ДЗ №3.3 ########################################################################################
# l = int(input("Введите длину в метрах: "))
# print("Длина в см = ", l * 100)
# print("Длина в дм = ", l * 10)
# print("Длина в мм = ", l * 1000)
# print("Длина в милях = ", l / 1609.344)
# #ДЗ №3.4 ########################################################################################
# b = int(input("Введите длину основания: "))
# h = int(input("Введите длину высоты: "))
# print("S = ", 0.5 * b * h)
# #ДЗ №3.5 ########################################################################################
# number = int(input("Введите 4х значное число: "))
# a = number // 1000
# b = number // 100 % 10
# c = number % 100 // 10
# d = number % 10
# print (d, c, b, a, sep='')

# #ДЗ №4.1 ########################################################################################
# num_1 = int(input("Enter num 1: "))
# num_2 = int(input("Enter num 2: "))
# sum1 = 0
# sum2 = 0
# sum3 = 0
# s1 = 0
# s2 = 0
# s3 = 0
## for i in range (num_1, num_2):
#     if i % 2 == 0:
#         sum1 += i
#         s1 += 1
# print ("Сумма четных чисел: ")
# print (sum1)
# print ("Сред.арифм четных чисел: ")
# print (sum1 / s1)
# for i in range (num_1, num_2):
#     if i % 2 != 0:
#         sum2 += i
#         s2 += 1
# print ("Сумма нечетные чисел: ")
# print (sum2)
# print ("Сред.арифм нечетных чисел: ")
# print (sum2 / s2)
# for i in range (num_1, num_2):
#     if i % 9 == 0:
#         sum3 += i
#         s3 += 1
# print ("Сумма кратных 9 чисел: ")
# print (sum3)
# print ("Сред.арифм кратных 9 чисел: ")
# print (sum3 / s3)
# #ДЗ №4.2########################################################################################
# a = int(input("Длину: "))
# b = str(input("Символ: "))
# for i in range (0, a):
#     print(b)
# #ДЗ №4.3########################################################################################
# n = 0
# n_sum = 0
# n_max = 0
# n_min = 0
# while n != 7:
#     n = int(input("Enter also number : "))
#     n_sum = n_sum + n
#     if n > n_max:
#         n_max = n
#     elif n < n_min:
#         n_min = n
#     print ("Сумма введенных чисел равна", n_sum)
#     print ("Максимальное число равно ", n_max)
#     print("Минимальное число равно ", n_min)
# print ("!!!Good bye!!!")

#ДЗ №5.1########################################################################################
# from random import randint
# a = []
# s1, s2, s3, s4, s5 = 0, 0, 0, 0, 0
# s_min = 0
# s_max = 0
# n = 0
# m = 0
# for i in range (10):
#     a.append(randint(-10, 10))
#     if a[i] < 0:# отбирет отрицательные
#         if a[i] % 2 == 0:#отбирает отрицательные чётные
#             s2 = (a[i] * -1) + s2
#         elif a[i] % 2 != 0:#отбирает отрицательные нечётные
#             s3 = (a[i] * -1) + s3
#         s1 = (a[i] * -1 )+ s1
#     elif a[i] > 0:# отбирет положительные
#         if a[i] % 2 == 0:# отбирет положительные чётные
#             s2 = a[i] + s2
#         elif a[i] % 2 != 0:# отбирет положительные нечётные
#             s3 = a[i] + s3
# s4 = a[3] * a[6] * a[9]
# for j in a:
#     if j > s_min:
#         s_min = j
#     elif j < s_max:
#         s_max = j
# for n in range (a[0], a[-1]):
#     if n >= 0:
#         n = a[i]
#         continue
# for m in range (a[-1], a[0]):
#     if m >= 0:
#         m = a[i]
#         continue
#
# print("Диапазон!: ", a)
# print("Сумма отрицательных!!!: ", s1)
# print("Сумма четных!!!: ", s2)
# print("Сумма нечетных!!!: ", s3)
# print("Произведение с идексами кратными 3!!!: ", s4)
# print("Произведение между мин и макс!!!: ", s_min * s_max)
# print("Сумма элементов между перв и последним полож: ", )
#ДЗ №5.2########################################################################################
# from random import randint
# a = []
# b = int(input("Enter len: "))
# chet = []
# nechet = []
# otr = []
# pol = []
# for i in range (b):
#     a.append(randint(-10, 10))
# print (a)
# for j in a:
#     if j % 2 == 0:#отбирает четные
#         if j < 0:
#             otr.append(j)
#         elif j > 0:
#             pol.append(j)
#         chet.append(j)
#     elif j % 2 != 0:#отбирает нечетные
#         if j < 0:
#             otr.append(j)
#         elif j > 0:
#             pol.append(j)
#         nechet.append(j)
# print ("Список четных: ", chet)
# print ("Список нечентых: ", nechet)
# print ("Список отрицательных: ", otr)
# print ("Список положительных: ", pol)

#ДЗ №7.1########################################################################################
# import random
# a, b, c, password = [], [], [], []
# file = open("Text_with_#.txt", "r")
# for i in file:
#     if len(i) >= 4 and len(i) <= 8:
#         a.append(i.capitalize().strip())
# print("Список слов нужной длины: ", a)
# l = 0
# while True :
#     b = random.choice(a)
#     c = random.choice(a)
#     password = b + c
#     l = len(password)
#     if 8 <= l <=10:
#         print("Длина пароля: ", l)
#         print("Первое рандомное слово: ", b)
#         print("Второе рандомное слово: ", c)
#         print("ПАРОЛЬ: ", password, sep="", end="")
#         break
# file.close()

#ДЗ №7.2########################################################################################
# def longest_words(file)
#     file = open("article.txt", "r", encoding="UTF-8")
#     lines = file.readlines()
#     lines1, lines2 = [], []
#     words = 0
#     for i in lines:
#         a = i.split()
#         for j in a:
#             lines1.append(j)
#     for ii in lines1:
#         a = len(ii)
#         if a > words:
#             words = len(ii)
#             lines2.clear()
#             lines2.append(ii)
#     print (f'Самое длинное слово имеет {words} смволов')
#     print (f'Самое длинное слово это {lines2}')

#ДЗ №8.1########################################################################################
# class Employee:
#     def __init__ (self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def calc_salary(self):
#         return self.salary
#
#     def display_info(self):
#         print(f'Имя: {self.name}')
#         print(f'Зарплата: {self.calc_salary()}')
#
# class Manager(Employee):
#     def __init__ (self, name, salary, bonus):
#         super().__init__(name, salary)
#         self.bonus = bonus
#
#     def calc_salary(self):
#         return super().calc_salary() + self.bonus
#
# class Developer(Employee):
#     def __init__ (self, name, salary, tech):
#         super().__init__(name, salary)
#         self.tech = tech
#
#     def display_info(self):
#         super().display_info()
#         print(f'Язык: {self.tech}')
#
#
# man1 = Manager('Ivan', 50000, 7000)
# man1.display_info()
#
# dev1 = Developer('Max', 75000, 'Python')
# dev1.display_info()

#ДЗ №9.1########################################################################################
# import tkinter as tk
# import random
#
# class Hw:
#     def __init__(self):
#         self.window = tk.Tk()
#         self.window.title("Рандомная математика")
#         self.window.geometry("500x400")
#         self.window.resizable(width=False, height=False)
#         self.window.config(bg="lime")
#         self.o = tk.StringVar()
#         self.answer = 0
#         self.entry = tk.Entry(self.window, textvariable=self.o).place(x=200, y=210)
#         self.flag = True
#
#     def level_1(self):
#         global flag
#         self.flag = True
#
#     def level_2(self):
#         global flag
#         self.flag = False
#
#     def isert_num(self):
#         if self.flag == True:
#             self.num_1 = random.randint (1, 10)
#             self.num_2 = random.randint(1, 10)
#             self.operator = random.choice(['+', '-', '*', '/'])
#             self.lbl1 = tk.Label(self.window, bg='lime', text=f'РЕШИ ПРИМЕР: {self.num_1}  {self.operator}  {self.num_2}').place(x=200, y=130)
#         else:
#             self.num_1 = random.randint (1, 100)
#             self.num_2 = random.randint(1, 100)
#             self.operator = random.choice(['+', '-', '*', '/'])
#             self.lbl1 = tk.Label(self.window, bg='lime', text=f'РЕШИ ПРИМЕР: {self.num_1}  {self.operator}  {self.num_2}').place(x=200, y=130)
#
#         if self.operator == '+':
#             self.result = self.num_1 + self.num_2
#         elif self.operator == '-':
#             self.result = self.num_1 - self.num_2
#         elif self.operator == '*':
#             self.result = self.num_1 * self.num_2
#         elif self.operator == '/':
#             self.result = self.num_1 / self.num_2
#         return self.result
#
#     def valid_num(self):
#         self.answer = str(self.o.get())
#         if self.answer == str(self.result):
#             self.lbl4 = tk.Label(self.window, bg='green', text='!!!YES!!!').place(x=250, y=250)
#             # entry.delete(0, END)
#         else:
#             self.lbl4 = tk.Label(self.window, bg='red', text='!!!NO!!!').place(x=250, y=250)
#             # entry.delete(0, END)
#
#     def run(self):
#         self.btn1 = tk.Button(self.window, text='START', width=5, height=2, bg='blue', activebackground='red',
#                               command=self.isert_num).place(x=75, y=120)
#         self.btn2 = tk.Button(self.window, text='VALID', width=5, height=2, bg='red', activebackground='blue',
#                              command=self.valid_num).place(x=75, y=200)
#         self.btn3 = tk.Button(self.window, text='LIGHT', width=25, height=2, bg='pink', activebackground='yellow',
#                              command=self.level_1).place(x=55, y=25)
#         self.btn4 = tk.Button(self.window, text='HARD', width=25, height=2, bg='pink', activebackground='yellow',
#                               command=self.level_2).place(x=270, y=25)
#         self.window.mainloop()
#
# start = Hw()
# start.run()

#### ПРОЕКТ ##########################################################################
# import tkinter as tk
# import PIL.ImageTk as ImageTk
# import random
#
# class Hp:
#     def __init__(self, image):
#         self.window = tk.Tk()
#         # Добавление картинки на задний фон
#         self.image_path = "ONE.PNG"
#         self.image = ImageTk.PhotoImage(file=self.image_path)
#         self.label = tk.Label(self.window, image=self.image)
#         self.label.pack()
#
#         self.window.title(" (^._.^) OLD PET  (˃ᆺ˂) ")
#         self.window.geometry("1366x768")
#         self.window.resizable(width=False, height=False)
#         self.window.config(bg="grey")
#         self.lbl = tk.Label(self.window,
#                             bg='grey',
#                             text='ЗДЕСЬ  ТЫ  СМОЖЕШЬ  УЗНАТЬ\n СКОЛЬКО  ЧЕЛОВЕЧЕСКИХ  ЛЕТ  ТВОЕМУ  ДОМАШНЕМУ  ЖИВОТНОМУ',
#                             font='Arial 24').place(x=110, y=0)
#
#     def win_1(self):
#         global answer
#         self.root = tk.Toplevel(self.window)
#         self.root.title("YOUR CAT'S AGE")
#         self.root.geometry("500x500")
#         self.root.config(bg="cadet blue")
#         self.root.resizable(width=False, height=False)
#         self.lbl0 = tk.Label(self.root,
#                              bg='cadet blue',
#                              font='Arial 16',
#                              text='ВВЕДИ ВОЗРАСТ СВОЕГО ЖВОТНОГО').place(x=75, y=50)
#         self.btn0 = tk.Button(self.root, text='ПЕРЕСЧИТАТЬ ВОЗРАСТ',
#                              font='Arial 14',
#                              width=26,
#                              height=2,
#                              bg='red',
#                              activebackground='blue',
#                              command=self.valid_1).pack(expand=True)
#         self.o = tk.StringVar()
#         self.answer = 0
#         self.entry = tk.Entry(self.root,
#                             textvariable=self.o).place(x=200, y=100)
#         # Добавление картинки на задний фон
#         self.image_path1 = "CAT.PNG"
#         self.image1 = ImageTk.PhotoImage(file=self.image_path1)
#         self.label = tk.Label(self.root, image=self.image1)
#         self.label.place(x=175, y=350)
#
#     def valid_1(self):
#         self.enter = int(self.o.get())
#         if self.enter <= 0:
#             self.lbl = tk.Label(self.root,
#                         bg='cadet blue',
#                         font='Arial 26',
#                         text=f'ВАША КОШКА\n ЕЩЕ НЕ РОДИЛАСЬ').place(relx=0.5, rely=0.5, anchor="center")
#         elif self.enter > 18:
#             self.lbl = tk.Label(self.root,
#                         bg='cadet blue',
#                         font='Arial 26',
#                         text=f'СТОЛЬКО КОШКИ\n НЕ ЖИВУТ!').place(relx=0.5, rely=0.5, anchor="center")
#         else:
#             self.lbl = tk.Label(self.root,
#                         bg='cadet blue',
#                         font='Arial 26',
#                         text=f'ВОЗРАСТ\n ВАШЕЙ КОШКИ =\n {round(self.enter * 4.7, 1)} ЧЕЛОВЕЧЕСКИХ ЛЕТ').place(relx=0.5,
#                                                                                                              rely=0.5,
#                                                                                                              anchor="center")
#
#     def win_2(self):
#         global answer
#         self.root = tk.Toplevel(self.window)
#         self.root.title("YOUR DOG'S AGE")
#         self.root.geometry("500x500")
#         # self.bard = Image.open(file="D:\Pet.jpg")
#         # self.bardejov = ImageTk.PhotoImage(bard)
#         self.root.config(bg="cadet blue")
#         self.root.resizable(width=False, height=False)
#         self.lbl0 = tk.Label(self.root,
#                              bg='cadet blue',
#                              font='Arial 16',
#                              text='ВВЕДИ ВОЗРАСТ СВОЕГО ЖВОТНОГО').place(x=75, y=50)
#         self.btn0 = tk.Button(self.root, text='ПЕРЕСЧИТАТЬ ВОЗРАСТ',
#                               font='Arial 14',
#                               width=26,
#                               height=2,
#                               bg='red',
#                               activebackground='blue',
#                               command=self.valid_2).pack(expand=True)
#         self.o = tk.StringVar()
#         self.answer = 0
#         self.entry = tk.Entry(self.root,
#                               textvariable=self.o).place(x=200, y=100)
#
#         self.image_path1 = "DOG.PNG"
#         self.image1 = ImageTk.PhotoImage(file=self.image_path1)
#         self.label = tk.Label(self.root, image=self.image1)
#         self.label.place(x=175, y=350)
#
#     def valid_2(self):
#         self.enter = int(self.o.get())
#         if self.enter <= 0:
#             self.lbl = tk.Label(self.root,
#                         bg='cadet blue',
#                         font='Arial 26',
#                         text=f'ВАША СОБАКА\n ЕЩЕ НЕ РОДИЛАСЬ').place(relx=0.5, rely=0.5, anchor="center")
#         elif self.enter > 15:
#             self.lbl = tk.Label(self.root,
#                         bg='cadet blue',
#                         font='Arial 26',
#                         text=f'СТОЛЬКО СОБАКИ\n НЕ ЖИВУТ!').place(relx=0.5, rely=0.5, anchor="center")
#         else:
#             self.lbl = tk.Label(self.root,
#                         bg='cadet blue',
#                         font='Arial 26',
#                         text=f'ВОЗРАСТ\n ВАШЕЙ СОБАКИ =\n {round(self.enter * 6.3, 1)} ЧЕЛОВЕЧЕСКИХ ЛЕТ').place(relx=0.5,
#                                                                                                               rely=0.5,
#                                                                                                               anchor="center")
#
#     def win_3(self):
#         global answer
#         self.root = tk.Toplevel(self.window)
#         self.root.title("YOUR PARROT'S AGE")
#         self.root.geometry("500x500")
#         # self.bard = Image.open(file="D:\Pet.jpg")
#         # self.bardejov = ImageTk.PhotoImage(bard)
#         self.root.config(bg="cadet blue")
#         self.root.resizable(width=False, height=False)
#         self.lbl0 = tk.Label(self.root,
#                              bg='cadet blue',
#                              font='Arial 16',
#                              text='ВВЕДИ ВОЗРАСТ СВОЕГО ЖВОТНОГО').place(x=75, y=50)
#         self.btn0 = tk.Button(self.root, text='ПЕРЕСЧИТАТЬ ВОЗРАСТ',
#                               font='Arial 14',
#                               width=26,
#                               height=2,
#                               bg='red',
#                               activebackground='blue',
#                               command=self.valid_3).pack(expand=True)
#         self.o = tk.StringVar()
#         self.answer = 0
#         self.entry = tk.Entry(self.root,
#                               textvariable=self.o).place(x=200, y=100)
#
#         self.image_path1 = "PAR.PNG"
#         self.image1 = ImageTk.PhotoImage(file=self.image_path1)
#         self.label = tk.Label(self.root, image=self.image1)
#         self.label.place(x=175, y=350)
#
#     def valid_3(self):
#         self.enter = int(self.o.get())
#         if self.enter <= 0:
#             self.lbl = tk.Label(self.root,
#                         bg='cadet blue',
#                         font='Arial 26',
#                         text=f'ВАШ ПОПУГАЙ\n ЕЩЕ НЕ РОДИЛСЯ').place(relx=0.5, rely=0.5, anchor="center")
#         elif self.enter > 45:
#             self.lbl = tk.Label(self.root,
#                         bg='cadet blue',
#                         font='Arial 26',
#                         text=f'СТОЛЬКО ПОПУГАИ\n НЕ ЖИВУТ!').place(relx=0.5, rely=0.5, anchor="center")
#         else:
#             self.lbl = tk.Label(self.root,
#                         bg='cadet blue',
#                         font='Arial 26',
#                         text=f'ВОЗРАСТ\n ВАШЕГО ПОПУГАЯ =\n {round(self.enter * 1.6, 1)} ЧЕЛОВЕЧЕСКИХ ЛЕТ').place(relx=0.5,
#                                                                                                               rely=0.5,
#                                                                                                               anchor="center")
#
#     def win_4(self):
#         global answer
#         self.root = tk.Toplevel(self.window)
#         self.root.title("YOUR TORTOISE'S AGE")
#         self.root.geometry("500x500")
#         # self.bard = Image.open(file="D:\Pet.jpg")
#         # self.bardejov = ImageTk.PhotoImage(bard)
#         self.root.config(bg="cadet blue")
#         self.root.resizable(width=False, height=False)
#         self.lbl0 = tk.Label(self.root,
#                              bg='cadet blue',
#                              font='Arial 16',
#                              text='ВВЕДИ ВОЗРАСТ СВОЕГО ЖВОТНОГО').place(x=75, y=50)
#         self.btn0 = tk.Button(self.root, text='ПЕРЕСЧИТАТЬ ВОЗРАСТ',
#                               font='Arial 14',
#                               width=26,
#                               height=2,
#                               bg='red',
#                               activebackground='blue',
#                               command=self.valid_4).pack(expand=True)
#         self.o = tk.StringVar()
#         self.answer = 0
#         self.entry = tk.Entry(self.root,
#                               textvariable=self.o).place(x=200, y=100)
#
#         self.image_path1 = "TOR.PNG"
#         self.image1 = ImageTk.PhotoImage(file=self.image_path1)
#         self.label = tk.Label(self.root, image=self.image1)
#         self.label.place(x=175, y=350)
#
#     def valid_4(self):
#         self.enter = int(self.o.get())
#         if self.enter <= 0:
#             self.lbl = tk.Label(self.root,
#                         bg='cadet blue',
#                         font='Arial 26',
#                         text=f'ВАША ЧЕРЕПАХА\n ЕЩЕ НЕ РОДИЛСЯ').place(relx=0.5, rely=0.5, anchor="center")
#         elif self.enter > 80:
#             self.lbl = tk.Label(self.root,
#                         bg='cadet blue',
#                         font='Arial 26',
#                         text=f'СТОЛЬКО ЧЕРЕПАХИ\n НЕ ЖИВУТ!').place(relx=0.5, rely=0.5, anchor="center")
#         else:
#             self.lbl = tk.Label(self.root,
#                         bg='cadet blue',
#                         font='Arial 26',
#                         text=f'ВОЗРАСТ\n ВАШЕЙ ЧЕРЕПАХИ =\n {round(self.enter * 3.6, 1)} ЧЕЛОВЕЧЕСКИХ ЛЕТ').place(relx=0.5,
#                                                                                                               rely=0.5,
#                                                                                                               anchor="center")
#
#     def win_5(self):
#         global answer
#         self.root = tk.Toplevel(self.window)
#         self.root.title("YOUR HAMSTER'S AGE")
#         self.root.geometry("500x500")
#         # self.bard = Image.open(file="D:\Pet.jpg")
#         # self.bardejov = ImageTk.PhotoImage(bard)
#         self.root.config(bg="cadet blue")
#         self.root.resizable(width=False, height=False)
#         self.lbl0 = tk.Label(self.root,
#                              bg='cadet blue',
#                              font='Arial 16',
#                              text='ВВЕДИ ВОЗРАСТ СВОЕГО ЖВОТНОГО').place(x=75, y=50)
#         self.btn0 = tk.Button(self.root, text='ПЕРЕСЧИТАТЬ ВОЗРАСТ',
#                               font='Arial 14',
#                               width=26,
#                               height=2,
#                               bg='red',
#                               activebackground='blue',
#                               command=self.valid_5).pack(expand=True)
#         self.o = tk.StringVar()
#         self.answer = 0
#         self.entry = tk.Entry(self.root,
#                               textvariable=self.o).place(x=200, y=100)
#
#         self.image_path1 = "HAM.PNG"
#         self.image1 = ImageTk.PhotoImage(file=self.image_path1)
#         self.label = tk.Label(self.root, image=self.image1)
#         self.label.place(x=175, y=350)
#
#     def valid_5(self):
#         self.enter = int(self.o.get())
#         if self.enter <= 0:
#             self.lbl = tk.Label(self.root,
#                         bg='cadet blue',
#                         font='Arial 26',
#                         text=f'ВАШ ХОМЯК\n ЕЩЕ НЕ РОДИЛСЯ').place(relx=0.5, rely=0.5, anchor="center")
#         elif self.enter > 3:
#             self.lbl = tk.Label(self.root,
#                         bg='cadet blue',
#                         font='Arial 26',
#                         text=f'СТОЛЬКО ХОМЯКИ\n НЕ ЖИВУТ!').place(relx=0.5, rely=0.5, anchor="center")
#         else:
#             self.lbl = tk.Label(self.root,
#                         bg='cadet blue',
#                         font='Arial 26',
#                         text=f'ВОЗРАСТ\n ВАШЕГО ХОМЯКА =\n {round(self.enter * 29.2, 1)} ЧЕЛОВЕЧЕСКИХ ЛЕТ').place(relx=0.5,
#                                                                                                               rely=0.5,
#                                                                                                               anchor="center")
#     def win_6(self):
#         global answer
#         self.root = tk.Toplevel(self.window)
#         self.root.title("YOUR RACCOON'S AGE")
#         self.root.geometry("500x500")
#         # self.bard = Image.open(file="D:\Pet.jpg")
#         # self.bardejov = ImageTk.PhotoImage(bard)
#         self.root.config(bg="cadet blue")
#         self.root.resizable(width=False, height=False)
#         self.lbl0 = tk.Label(self.root,
#                              bg='cadet blue',
#                              font='Arial 16',
#                              text='ВВЕДИ ВОЗРАСТ СВОЕГО ЖВОТНОГО').place(x=75, y=50)
#         self.btn0 = tk.Button(self.root, text='ПЕРЕСЧИТАТЬ ВОЗРАСТ',
#                               font='Arial 14',
#                               width=26,
#                               height=2,
#                               bg='red',
#                               activebackground='blue',
#                               command=self.valid_6).pack(expand=True)
#         self.o = tk.StringVar()
#         self.answer = 0
#         self.entry = tk.Entry(self.root,
#                               textvariable=self.o).place(x=200, y=100)
#
#         self.image_path1 = "RAC.PNG"
#         self.image1 = ImageTk.PhotoImage(file=self.image_path1)
#         self.label = tk.Label(self.root, image=self.image1)
#         self.label.place(x=175, y=350)
#
#     def valid_6(self):
#         self.enter = int(self.o.get())
#         if self.enter <= 0:
#             self.lbl = tk.Label(self.root,
#                         bg='cadet blue',
#                         font='Arial 26',
#                         text=f'ВАШ ЕНОТ\n ЕЩЕ НЕ РОДИЛСЯ').place(relx=0.5, rely=0.5, anchor="center")
#         elif self.enter > 55:
#             self.lbl = tk.Label(self.root,
#                         bg='cadet blue',
#                         font='Arial 26',
#                         text=f'СТОЛЬКО ЕНОТЫ\n НЕ ЖИВУТ!').place(relx=0.5, rely=0.5, anchor="center")
#         else:
#             self.lbl = tk.Label(self.root,
#                         bg='cadet blue',
#                         font='Arial 26',
#                         text=f'ВОЗРАСТ\n ВАШЕГО ЕНОТА =\n {round(self.enter * 20.8, 1)} ЧЕЛОВЕЧЕСКИХ ЛЕТ').place(relx=0.5,
#                                                                                                               rely=0.5,
#                                                                                                               anchor="center")
#
#     def run(self):
#         self.btn1 = tk.Button(self.window, text='CAT', font='Arial 14', width=30, height=2, bg='pink', activebackground='yellow',
#                              command=self.win_1).place(x=50, y=175)
#         self.btn2 = tk.Button(self.window, text='DOG', font='Arial 14',  width=30, height=2, bg='pink', activebackground='yellow',
#                               command=self.win_2).place(x=500, y=175)
#         self.btn3 = tk.Button(self.window, text='PARROT', font='Arial 14', width=30, height=2, bg='pink', activebackground='yellow',
#                               command=self.win_3).place(x=975, y=175)
#         self.btn4 = tk.Button(self.window, text='TORTOISE', font='Arial 14',  width=30, height=2, bg='pink', activebackground='yellow',
#                               command=self.win_4).place(x=50, y=300)
#         self.btn5 = tk.Button(self.window, text='HAMSTER', font='Arial 14',  width=30, height=2, bg='pink', activebackground='yellow',
#                               command=self.win_5).place(x=500, y=300)
#         self.btn6 = tk.Button(self.window, text='RACCOON', font='Arial 14',  width=30, height=2, bg='pink', activebackground='yellow',
#                               command=self.win_6).place(x=975, y=300)
#         self.window.mainloop()
# start = Hp('CAT.png')
# start.run()














