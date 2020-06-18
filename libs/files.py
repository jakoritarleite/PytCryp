from os import rename

class Manager(object):
    def __init__(self):
        self.rename = lambda _file, tp: rename(_file, _file + '.pcrp') if not tp else rename(_file, _file.replace('.pcrp', ''))

    @staticmethod
    def __read__(FILE: 'path/filename') -> 'raw data in file bytes':
        with open(FILE, 'rb') as _file:
            inFile = _file.read()
            _file.close()

        return inFile

    @staticmethod
    def __write__(FILE: 'path/filename', CONTENT: 'raw data file bytes'):
        with open(FILE, 'wb') as _file:
            _file.write(CONTENT)
            _file.close()
