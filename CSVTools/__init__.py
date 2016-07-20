
import configparser

__all__ = ['conf', 'default']
conf = configparser.ConfigParser()
conf.read(filenames='conf.ini', encoding='utf-8')
default = conf['default']
