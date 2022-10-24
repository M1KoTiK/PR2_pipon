"""Simple Monitors changes programm
"""
import pathlib
from pathlib import Path
import argparse
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileCreatedEvent
import time
import sys
vowel_letters = {'а', 'ы', 'у', 'э', 'о', 'я', 'и', 'ю', 'е', 'ё', 'a', 'e', 'i', 'o', 'u'}
# Функция для выводв гласных и согласных, согласно требованиям)))
def check_and_print(string):
    for char in string:
        bk :char = char.lower()
        if bk in vowel_letters:
            print(bk)
        else:
            print(bk.upper())   
    print("", end = "\n")
    pass

class FileChecker(FileSystemEventHandler):
    def on_created(self, event):
        if isinstance(event, FileCreatedEvent):  
           check_and_print(Path(event.src_path).stem)      
    pass    

def main():
    # использование библиотеки pathlib для создания стандартного пути к редактируемому файлу
    path_to_file :str = pathlib.Path(pathlib.Path.cwd())
    # использование библиотеки agrparse для обработки аргументов начальной настройки программы (задание пути)
    set_up = argparse.ArgumentParser()
    # Аргументы строки (один аргумент, имеюющий стандартное относительное значение пути для редактируемого файла)
    set_up.add_argument('path', type=str, nargs='?', help=' path to file', default = str(path_to_file))
    arguments = set_up.parse_args()
    print("-------------------------------------------------------------------")
    print("Местоположение для проверки файлов - " + arguments.path)
    print("-------------------------------------------------------------------")
    """ Если нужно открыть папку в которуюю ведётся 
        запись, то можно использовать следующую команду:
        subprocess.Popen(r'explorer /select,' + arguments.path)
        :3
    """     
    path = arguments.path 
    ev_handler = FileChecker()
    observer = Observer()
    observer.schedule(ev_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
            pass
    except:
        observer.stop()
            

if __name__ == "__main__":
    main()