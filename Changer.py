"""Simple file creator
"""
import argparse
import pathlib
import subprocess
def main():
    # использование библиотеки pathlib для создания стандартного пути к редактируемому файлу
    path_to_file :str = pathlib.Path(pathlib.Path.cwd())
    # использование библиотеки agrparse для обработки аргументов начальной настройки программы (задание пути)
    set_up = argparse.ArgumentParser()
    # Аргументы строки (один аргумент, имеюющий стандартное относительное значение пути для редактируемого файла)
    set_up.add_argument('path', type=str, nargs='?', help=' path to file', default = str(path_to_file))
    arguments = set_up.parse_args()
    print("-------------------------------------------------------------------")
    print("Местоположение для создания файлов - " + arguments.path)
    print("-------------------------------------------------------------------")
    """ Если нужно открыть папку в которуюю ведётся 
        запись, то можно использовать следующую команду:
        subprocess.Popen(r'explorer /select,' + arguments.path)
        :3
    """ 
    # Логика):
    
    while True:
        print("Введите название для файла (не менее 3 симв. и только буквы)")
        str_inp :str = input()
        if(len(str_inp) >= 3):
            pass
        else:
            continue
        if(str_inp.isalpha()):
            pass
        else:
            continue
        try:
            full_path : str = pathlib.Path(arguments.path,str_inp + ".txt")
            file = open(full_path, "a")
            file.close()
        except:
            print("Незарезирвированная ошибка")
        print("Создан файл " + str_inp + ".txt")
        break
        

if __name__ == "__main__":
    main()