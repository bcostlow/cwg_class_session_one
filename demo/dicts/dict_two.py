# dicts can take an iterable of pairs as a constructor
from collections import ChainMap

module_defaults = {'width': 1024, 'height': 768, 'debug': False, 'logging': 'off'}
pretend_environ = {'logging': 'on'}
pretend_cmd_line = {'debug': True}

settings = ChainMap(pretend_cmd_line, pretend_environ, module_defaults)

print(settings['width'])
print(settings['height'])
print(settings['debug'])
print(settings['logging'])

module_defaults['width'] = 800
print(settings['width'])
