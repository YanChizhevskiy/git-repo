import os
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
if __name__ == '__main__':

    def specify_folder():
        global fld_name
        fld_name = input("Укажите название директории: ")

    def process_launch():
        print(" [1] - Перейти в папку")
        print(" [2] - Посмотреть содержимое текущей папки")
        print(" [3] - Удалить папку")
        print(" [4] - Создать папку")
        print(" [5] - Вернуться в директорию этого файла")
        global option
        option = int(input("укажите номер действия: "))

    while True:
        process_launch()

        if option == 1:
            specify_folder()
            from Lesson_5.hw_easy import ent_fld
            ent_fld(fld_name)

        elif option == 2:
            from Lesson_5.hw_easy import content_fld
            content_fld()

        elif option == 3:
            specify_folder()
            from Lesson_5.hw_easy import del_fld
            del_fld(fld_name)

        elif option == 4:
            specify_folder()
            from Lesson_5.hw_easy import crt_fld
            crt_fld(fld_name)

        elif option == 5:
            os.chdir(os.path.join(os.path.dirname(__file__)))
            print('Вы вернулись в директорию этого файла')
