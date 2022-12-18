from pygments.style import Style
from pygments.token import Token, Comment, Keyword, Name, String, \
     Error, Generic, Number, Operator

class ZScriptStyle(Style):

    styles = {
        Token:                  '',
        Comment:                '#111',
        Keyword:                'bold #f80',
        Keyword.Type:           'bold #c00',
        Name:                   '#f00',
        Name.Class:             'bold #0f0',
        Name.Function:          '#ee0',
        String:                 '#080',
        Number:                 '#080'
    }