
import configparser


__all__ = ['XSD_CONF']

conf = configparser.ConfigParser()
conf.read('../config.ini')
XSD_CONF = conf['xsd_files']
