from distutils.core import setup, Extension 
module_spam = Extension('spam', sources = ['spammodule.c']) 
setup( 
    name='TermProject',
    version='1.0', 
    py_modules=['TermProject'], 
    packages=[''], 
    package_data = {}, 
    ext_modules=[module_spam]
)