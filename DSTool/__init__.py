import configparser

__all__ = ['conf']
conf = configparser.ConfigParser()
conf.read(filenames='RDF/conf.ini', encoding='utf-8')
