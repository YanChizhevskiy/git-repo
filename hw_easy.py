import sys
import os
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def create_10_dirs():
    for x in range(10):
        dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(x))
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            print('Такая директория уже существует')


def delete_10_dirs():
    for x in range(10):
        dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(x))
        try:
            os.rmdir(dir_path)
        except FileExistsError:
            print('Директории удалены')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def show_folders():
    print(os.listdir()) #как показать только папки?

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_cwd():
    first_file = __file__
    copy_file = first_file + '.copy'
    shutil.copy(first_file, copy_file)

# Задача-1 normal:

def ent_fld(fld_name):
    full_path = os.path.join(os.path.dirname(fld_name), fld_name)
    if os.path.exists(full_path):
        os.chdir(full_path)
        print('Вы перешли в директорию {}'.format(fld_name))
    else:
        print('Директория не найдена')

def content_fld():
    print(os.listdir())

def del_fld(fld_name):
    del_path = os.path.join(os.path.dirname(fld_name), fld_name)
    if os.path.exists(del_path):
        os.rmdir(del_path)
        print('Вы удалили в директорию {}'.format(fld_name))
    else:
        print('Директория не найдена')

def crt_fld(fld_name):
    crt_path = os.path.join(os.path.dirname(fld_name), fld_name)
    if not os.path.exists(crt_path):
        os.makedirs(crt_path)
        print('Вы создали директорию {}'.format(fld_name))
    else:
        print('Директория с таким именем уже существует')

