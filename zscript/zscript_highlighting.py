from pygments.lexer import RegexLexer
from pygments.token import *

class ZScriptLexer(RegexLexer):
    name = 'ZScript'
    filenames = ['*.zs',"*.zc","*.zsc", "*.z"]
    aliases = ['zscript','zs']
    mimetypes = ['text/zs',"text/zscript"]
    tokens = {
        'root': [
            (r'\s+', Whitespace),
            (r'//.*?$', Comment.Single),
            (r'/(\n)?[*](.|\n)*?[*](\n)?/', Comment.Multiline),
            (r'\b(class|default|private|static|native|return|if|else|for|while|do|deprecated|null|readonly|true|false|struct|extend|clearscope|vararg|ui|play|virtual|virtualscope|meta|Property|in|out|states|override|super|is|let|const|replaces|protected|self|abstract|enum|switch|case)\b',Keyword),
            (r'\b(Class|[Bb]ot|[Pp]layer[Ii]nfo|[Aa]ctor|[Oo]bject|[Vv]ector2|[Vv]ector3|[Nn]ame|[Ss]tring|[Cc]olor|[Ss]ound|void|[Dd]ouble|[Bb]ool|int|float|float64|uint8|uint16|uint|int8|int16|TextureID|SpriteID|[Aa]rray|voidptr|short|action|state|statelabel|PSprite|Weapon)\b',Keyword.Type),
            (r'(?i)\b(goto|loop|stop|break|continue|fail)\b',Keyword),
            (r'[\\\-+/*=<>?:!~%&|]', Operator),
            (r'[(){}]|\\[|\\]', Punctuation),
            #(r'', Name),
            (r'\".+?\"', String),
            (r'\'.+?\'', String),
            (r'(?i)\b([0-9][.]*[0-9]*)+?\b',Number),
            (r'(?i)\b(0x[A-Fa-f0-9_]+)\b',Number.Hex),
            (r'(?i)\b(0b[0-1_]+)[FL]?\b',Number.Bin),
            (r'(?i)[\.]*[a-z0-9_]+[ ]*(?=[(]+)',Name.Function),
            (r'(?i)(\b(true|false)\b|NULL)',Name.Builtin),
            (r'(?i)\sclass +[a-z0-9_]+ *((:) +[a-z0-9.]+)?',Name.Class),
            (r'(?i)[a-z0-9.]+:',Name.Tag),
            (r'(?i)goto [a-z0-9]+[\\+0-9]*',Name.Tag),
            (r'(?i)#include',Comment.Preproc),
            (r'(?i)version',Comment.Preproc)
        ],
        'strings': [
            (r'(?i)\\(x[0-9a-f]{2}|.)', String.Escape),
            (r'.', String),
        ],
        'nl': [
            (r'\n', String),
        ]
    }

"""
filetype: zscript
# Loosely based on the csharp.yaml definition
# (?i) on everything because ZScript isn't case sensitive

detect:
    filename: "(?i)\\.z(c|sc)$"

rules:

    # ZScript only has one preprocessor directive and a required engine version declaration
    - preproc: "(?i)#include"
    - preproc: "(?i)version"

    # State labels ("goto" word overridden by state logic rule below)
    - symbol.tag: "(?i)[a-z0-9.]+:"
    - symbol.tag: "(?i)goto [a-z0-9]+[\\+0-9]*"

    # Classes
    - identifier.class: "(?i)class +[a-z0-9_]+ *((:) +[a-z0-9.]+)?"

    # Functions (open paren overridden by symbol.brackets rule because perl regex apparently doesn't support postive lookahead)
    - identifier: "(?i)[\\.]*[a-z0-9_]+[ ]*[(]+"

    # Variable types
    - type: "(?i)\\b(actor|object|vector2|vector3|name|string|color|sound|void|double|bool|int|float|float64|uint8|uint16|uint|int8|int16|TextureID|SpriteID|Array|voidptr|short|action|state|statelabel)\\b"

    # Keywords
    - statement: "(?i)\\b(class|default|private|static|native|return|if|else|for|while|do|deprecated|null|readonly|true|false|struct|extend|clearscope|vararg|ui|play|virtual|virtualscope|meta|Property|in|out|states|override|super|is|let|const|replaces|protected|self|abstract|enum|switch|case)\\b"

    # State logic keywords
    - special: "(?i)\\b(goto|loop|stop|break|continue|fail)\\b"

    # Symbols
    - symbol.operator: "[\\-+/*=<>?:!~%&|]"
    - symbol.brackets: "[(){}]|\\[|\\]"

    # Constants
    - constant.bool: "(?i)(\\b(true|false)\\b|NULL)"
    - constant.number: "(?i)\\b([0-9][.]*[0-9]*)+?\\b"
    - constant.number: "(?i)\\b(0x[A-Fa-f0-9_]+)?\\b"
    - constant.number: "(?i)\\b(0b[0-1_]+)[FL]?\\b"
    #- constant.number: "(?i)\\b(([0-9][.]*[0-9]*)+|0x[A-Fa-f0-9_]+|0b[0-1_]+)[FL]?\\b"

    # Strings
    - constant.string:
        start: "\""
        end: "\""
        skip: "\\\\."
        rules:
            - constant.specialChar: "\\\\([btnfr]|'|\\\"|\\\\)"
            - constant.specialChar: "\\\\u[A-Fa-f0-9]{4}"

    - constant.string:
        start: "'"
        end: "'"
        skip: "\\\\."
        rules:
            - constant.specialChar: "\\\\([btnfr]|'|\\\"|\\\\)"
            - constant.specialChar: "\\\\u[A-Fa-f0-9]{4}"

    # Comments
    - comment:
        start: "//"
        end: "$"
        rules:
            - todo: "(TODO|XXX|FIXME):?"

    - comment:
        start: "/\\*"
        end: "\\*/"
        rules:
            - todo: "(TODO|XXX|FIXME):?"
"""