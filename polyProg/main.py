from antlr4 import *
from PolyLexer import PolyLexer
from PolyParser import PolyParser

def beautify_lisp_string(in_string):
    indent_size = 3
    add_indent = ' '*indent_size
    out_string = in_string[0]  
    indent = ''
    for i in range(1, len(in_string)):
        if in_string[i] == '(' and in_string[i+1] != ' ':
            indent += add_indent
            out_string += "\n" + indent + '('
        elif in_string[i] == ')':
            out_string += ')'
            if len(indent) > 0:
                indent = indent.replace(add_indent, '', 1)
        else:
            out_string += in_string[i]
    return out_string
    
file_name = r"C:\Users\User\Desktop\polyProg_lab_5\polyProg\main.pol"
input_stream = FileStream(file_name)
lexer = PolyLexer(input_stream)
print('input_stream:')
print(input_stream)
print()
token_stream = CommonTokenStream(lexer)
token_stream.fill()
print('tokens:')
for tk in token_stream.tokens:
    print(tk)
print()

parser = PolyParser(token_stream)
tree = parser.program()
print('tree:')
lisp_tree_str = tree.toStringTree(recog=parser)
#print(beautify_lisp_string(lisp_tree_str))