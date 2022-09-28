

import pathlib
import os
import shutil
import string
import random
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import signal
def Pid():
    #get the pid
    pid = os.getpid()
    # report the pid
    os.kill(pid,signal.SIGTERM)
def Inicio():
    def RaizIden():
        drive = pathlib.Path.home().drive
        # Identificando a raiz do sistema
        if drive == 'C:':
            global c
            global d
            global e
            global f
            c = 'C:/'
            d = r'C:\!TrapFolder'
            e = r'C:\lTrapFolder'
            f = r'C:\zTrapFolder'
        elif drive == 'E:':
            c = 'E:/'
            d = r'C:\!TrapFolder'
            e = r'C:\lTrapFolder'
            f = r'C:\zTrapFolder'
        elif drive == 'D:':
            c = 'D:/'
            d = r'C:\!TrapFolder'
            e = r'C:\lTrapFolder'
            f = r'C:\zTrapFolder'
        elif drive == 'F:':
            c = 'F:/'
            d = r'C:\!TrapFolder'
            e = r'C:\lTrapFolder'
            f = r'C:\zTrapFolder'
    RaizIden()

    directory1 = "!TrapFolder" 
    directory2 = 'lTrapFolder'
    directory3 = 'zTrapFolder'

    parent_dir = c
    def CriandoPastas():
        # Criando as Pastas de armadilha no local determinado
        path1 = os.path.join(parent_dir, directory1)
        path2 = os.path.join(parent_dir, directory2)
        path3 = os.path.join(parent_dir, directory3)

        os.mkdir(path1)
        os.mkdir(path2)
        os.mkdir(path3)

    CriandoPastas()
    def Arquivos():
        number_of_strings = 5
        length_of_string = 5
        l = 0
        # Criando os arquivos .txt dentro das Pastas de armadilha
        for x in range(number_of_strings):
            while l < 5000:
                save_path1 = d
                name_of_file1 = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
                completeName1 = os.path.join(save_path1, name_of_file1+".txt")       
                file1 = open(completeName1, "w")
                toFile1 = "Lorem ipsum dolor sit amet"
                file1.write(toFile1)
                file1.close()
                l += 1
        m = 0        
        for y in range(number_of_strings):
            while m < 5000:
                save_path2 = e
                name_of_file2 = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
                completeName2 = os.path.join(save_path2, name_of_file2+".txt")
                file2 = open(completeName2, "w")
                toFile2 = "Lorem ipsum dolor sit amet"
                file2.write(toFile2)
                file2.close()
                m += 1
        n = 0 
        for z in range(number_of_strings):
            while n < 5000:
                save_path3 = f
                name_of_file3 = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
                completeName3 = os.path.join(save_path3, name_of_file3+".txt")
                file3 = open(completeName3, "w")
                toFile3 = "Lorem ipsum dolor sit amet"
                file3.write(toFile3)
                file3.close()
                n += 1
            
    Arquivos()
    print("Completo")


    start = time.time()
    lista = []
    def Obervador2():
    # Execução principal do Observador
        class MyEventHandler1(FileSystemEventHandler):
            def on_modified(self, event):
                print(event.src_path, 'Modificado')
                lista.append(event.src_path)
                if len(lista) > 2:
                    stop = time.time()
                    b = start - stop
                    if b < 10:
                        # Se 1000 arquivos forem modificados em menos de 10 segundos o programa detecta que é um ransomware.
                        print('Possivel Ransomware Detectado!!!!')
                        '''pid2 = os.getpid()
                        os.kill(pid2,signal.SIGTERM)'''
                        observer.stop()



        # Verificando modificações nas pastas !TrapFolder, lTrapFolder e zTrapFolder
        observer = Observer()
        observer.schedule(MyEventHandler1(), d, recursive=True)
        observer.schedule(MyEventHandler1(), e, recursive=True)
        observer.schedule(MyEventHandler1(), f, recursive=True)
        observer.start()

        try:
            while observer.is_alive():
                observer.join(1)
        except KeyboardInterrupt:
            shutil.rmtree("C:\!TrapFolder")
            shutil.rmtree("C:\lTrapFolder")
            shutil.rmtree("C:\zTrapFolder")
            print("Trap Folders Deletados!!")
            observer.stop()
    Obervador2()