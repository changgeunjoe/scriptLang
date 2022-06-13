from distutils.core import setup, Extension 
module_spam = Extension('spam', sources = ['spammodule.c']) 
setup( 
    name='TermProject',
    version='1.0', 
    py_modules=['TermProject'], 
    packages=['images', 'sub', 'telegram', 'spamFile'],
    package_data = {'images': ['*.gif'], 'sub': ['*.py'], 'telegram': ['*.py'], 'spamFile':['*.pyd']}, 
    ext_modules=[module_spam]
)