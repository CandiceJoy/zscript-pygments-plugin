from setuptools import setup

entry_points = '''
[pygments.lexers]
ZScriptLexer=zscript:ZScriptLexer

[pygments.styles]
ZScriptStyle=zscript:ZScriptStyle
'''

setup(
    name='ZScriptPlugin',
    version='1.2',
    packages=['zscript'],
    install_requires=['pygments>=2.0.2'],
    entry_points=entry_points,
    zip_safe=True
)