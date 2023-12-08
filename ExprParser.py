# Generated from C:/Users/User/Desktop/polyProg_lab_5/Expr.g by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,74,370,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,124,
        8,6,1,7,1,7,1,8,3,8,129,8,8,1,8,1,8,1,9,1,9,1,9,3,9,136,8,9,1,10,
        1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,4,14,147,8,14,11,14,12,14,
        148,1,15,1,15,1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,3,18,167,8,18,1,19,1,19,1,19,5,19,172,8,19,10,
        19,12,19,175,9,19,1,20,1,20,1,20,1,20,1,20,1,20,1,21,4,21,184,8,
        21,11,21,12,21,185,1,22,1,22,1,22,1,22,1,22,3,22,193,8,22,1,23,1,
        23,1,23,5,23,198,8,23,10,23,12,23,201,9,23,1,24,1,24,1,24,1,24,1,
        25,1,25,1,25,5,25,210,8,25,10,25,12,25,213,9,25,1,26,1,26,1,26,1,
        26,1,26,1,26,1,26,3,26,222,8,26,1,27,1,27,3,27,226,8,27,1,28,1,28,
        1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,
        1,30,3,30,244,8,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,
        1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,
        1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,34,1,34,5,34,279,
        8,34,10,34,12,34,282,9,34,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,
        1,35,3,35,293,8,35,1,36,3,36,296,8,36,1,36,1,36,1,36,1,36,5,36,302,
        8,36,10,36,12,36,305,9,36,1,37,1,37,1,37,1,37,5,37,311,8,37,10,37,
        12,37,314,9,37,1,38,1,38,1,38,1,38,5,38,320,8,38,10,38,12,38,323,
        9,38,1,39,1,39,1,39,1,39,1,39,1,39,3,39,331,8,39,1,40,1,40,1,40,
        3,40,336,8,40,1,41,3,41,339,8,41,1,41,1,41,1,42,3,42,344,8,42,1,
        42,1,42,1,43,1,43,3,43,350,8,43,1,44,1,44,1,45,1,45,1,46,1,46,1,
        46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,3,46,368,8,46,1,
        46,0,0,47,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,
        84,86,88,90,92,0,11,1,0,1,26,1,0,27,36,1,0,40,45,1,0,57,58,2,0,37,
        37,52,52,1,0,53,54,2,0,50,51,55,56,1,0,46,49,1,0,61,62,1,0,63,65,
        1,0,59,60,379,0,94,1,0,0,0,2,96,1,0,0,0,4,98,1,0,0,0,6,100,1,0,0,
        0,8,102,1,0,0,0,10,104,1,0,0,0,12,123,1,0,0,0,14,125,1,0,0,0,16,
        128,1,0,0,0,18,135,1,0,0,0,20,137,1,0,0,0,22,139,1,0,0,0,24,141,
        1,0,0,0,26,143,1,0,0,0,28,146,1,0,0,0,30,150,1,0,0,0,32,154,1,0,
        0,0,34,156,1,0,0,0,36,166,1,0,0,0,38,168,1,0,0,0,40,176,1,0,0,0,
        42,183,1,0,0,0,44,192,1,0,0,0,46,194,1,0,0,0,48,202,1,0,0,0,50,206,
        1,0,0,0,52,221,1,0,0,0,54,225,1,0,0,0,56,227,1,0,0,0,58,232,1,0,
        0,0,60,238,1,0,0,0,62,248,1,0,0,0,64,256,1,0,0,0,66,265,1,0,0,0,
        68,276,1,0,0,0,70,292,1,0,0,0,72,295,1,0,0,0,74,306,1,0,0,0,76,315,
        1,0,0,0,78,330,1,0,0,0,80,335,1,0,0,0,82,338,1,0,0,0,84,343,1,0,
        0,0,86,349,1,0,0,0,88,351,1,0,0,0,90,353,1,0,0,0,92,355,1,0,0,0,
        94,95,7,0,0,0,95,1,1,0,0,0,96,97,7,1,0,0,97,3,1,0,0,0,98,99,5,37,
        0,0,99,5,1,0,0,0,100,101,5,38,0,0,101,7,1,0,0,0,102,103,5,39,0,0,
        103,9,1,0,0,0,104,105,7,2,0,0,105,11,1,0,0,0,106,124,5,46,0,0,107,
        124,5,47,0,0,108,124,5,48,0,0,109,124,5,49,0,0,110,124,5,50,0,0,
        111,124,5,51,0,0,112,124,3,6,3,0,113,124,5,52,0,0,114,124,3,4,2,
        0,115,124,5,53,0,0,116,124,5,54,0,0,117,124,3,8,4,0,118,124,3,10,
        5,0,119,124,3,14,7,0,120,124,3,16,8,0,121,124,5,55,0,0,122,124,5,
        56,0,0,123,106,1,0,0,0,123,107,1,0,0,0,123,108,1,0,0,0,123,109,1,
        0,0,0,123,110,1,0,0,0,123,111,1,0,0,0,123,112,1,0,0,0,123,113,1,
        0,0,0,123,114,1,0,0,0,123,115,1,0,0,0,123,116,1,0,0,0,123,117,1,
        0,0,0,123,118,1,0,0,0,123,119,1,0,0,0,123,120,1,0,0,0,123,121,1,
        0,0,0,123,122,1,0,0,0,124,13,1,0,0,0,125,126,7,3,0,0,126,15,1,0,
        0,0,127,129,5,59,0,0,128,127,1,0,0,0,128,129,1,0,0,0,129,130,1,0,
        0,0,130,131,5,60,0,0,131,17,1,0,0,0,132,136,3,20,10,0,133,136,3,
        22,11,0,134,136,3,8,4,0,135,132,1,0,0,0,135,133,1,0,0,0,135,134,
        1,0,0,0,136,19,1,0,0,0,137,138,7,4,0,0,138,21,1,0,0,0,139,140,7,
        5,0,0,140,23,1,0,0,0,141,142,7,6,0,0,142,25,1,0,0,0,143,144,7,7,
        0,0,144,27,1,0,0,0,145,147,3,2,1,0,146,145,1,0,0,0,147,148,1,0,0,
        0,148,146,1,0,0,0,148,149,1,0,0,0,149,29,1,0,0,0,150,151,3,28,14,
        0,151,152,5,46,0,0,152,153,3,28,14,0,153,31,1,0,0,0,154,155,7,8,
        0,0,155,33,1,0,0,0,156,157,7,9,0,0,157,35,1,0,0,0,158,167,3,34,17,
        0,159,167,5,66,0,0,160,167,5,67,0,0,161,167,5,68,0,0,162,167,5,69,
        0,0,163,167,5,70,0,0,164,167,5,71,0,0,165,167,5,72,0,0,166,158,1,
        0,0,0,166,159,1,0,0,0,166,160,1,0,0,0,166,161,1,0,0,0,166,162,1,
        0,0,0,166,163,1,0,0,0,166,164,1,0,0,0,166,165,1,0,0,0,167,37,1,0,
        0,0,168,173,3,0,0,0,169,172,3,0,0,0,170,172,3,2,1,0,171,169,1,0,
        0,0,171,170,1,0,0,0,172,175,1,0,0,0,173,171,1,0,0,0,173,174,1,0,
        0,0,174,39,1,0,0,0,175,173,1,0,0,0,176,177,5,73,0,0,177,178,5,55,
        0,0,178,179,3,42,21,0,179,180,3,48,24,0,180,181,5,56,0,0,181,41,
        1,0,0,0,182,184,3,44,22,0,183,182,1,0,0,0,184,185,1,0,0,0,185,183,
        1,0,0,0,185,186,1,0,0,0,186,43,1,0,0,0,187,188,3,34,17,0,188,189,
        3,46,23,0,189,190,5,49,0,0,190,193,1,0,0,0,191,193,3,68,34,0,192,
        187,1,0,0,0,192,191,1,0,0,0,193,45,1,0,0,0,194,199,3,38,19,0,195,
        196,5,47,0,0,196,198,3,38,19,0,197,195,1,0,0,0,198,201,1,0,0,0,199,
        197,1,0,0,0,199,200,1,0,0,0,200,47,1,0,0,0,201,199,1,0,0,0,202,203,
        5,55,0,0,203,204,3,50,25,0,204,205,5,56,0,0,205,49,1,0,0,0,206,211,
        3,52,26,0,207,208,5,49,0,0,208,210,3,52,26,0,209,207,1,0,0,0,210,
        213,1,0,0,0,211,209,1,0,0,0,211,212,1,0,0,0,212,51,1,0,0,0,213,211,
        1,0,0,0,214,222,3,56,28,0,215,222,3,58,29,0,216,222,3,60,30,0,217,
        222,3,62,31,0,218,222,3,64,32,0,219,222,3,92,46,0,220,222,3,68,34,
        0,221,214,1,0,0,0,221,215,1,0,0,0,221,216,1,0,0,0,221,217,1,0,0,
        0,221,218,1,0,0,0,221,219,1,0,0,0,221,220,1,0,0,0,222,53,1,0,0,0,
        223,226,3,72,36,0,224,226,3,70,35,0,225,223,1,0,0,0,225,224,1,0,
        0,0,226,55,1,0,0,0,227,228,3,38,19,0,228,229,5,38,0,0,229,230,3,
        54,27,0,230,231,5,49,0,0,231,57,1,0,0,0,232,233,5,72,0,0,233,234,
        5,50,0,0,234,235,3,46,23,0,235,236,5,51,0,0,236,237,5,49,0,0,237,
        59,1,0,0,0,238,239,5,71,0,0,239,243,5,50,0,0,240,244,3,38,19,0,241,
        244,3,80,40,0,242,244,3,54,27,0,243,240,1,0,0,0,243,241,1,0,0,0,
        243,242,1,0,0,0,244,245,1,0,0,0,245,246,5,51,0,0,246,247,5,49,0,
        0,247,61,1,0,0,0,248,249,5,66,0,0,249,250,5,50,0,0,250,251,3,66,
        33,0,251,252,5,51,0,0,252,253,5,55,0,0,253,254,3,86,43,0,254,255,
        5,56,0,0,255,63,1,0,0,0,256,257,5,67,0,0,257,258,5,55,0,0,258,259,
        3,86,43,0,259,260,5,56,0,0,260,261,5,68,0,0,261,262,5,50,0,0,262,
        263,3,70,35,0,263,264,5,51,0,0,264,65,1,0,0,0,265,266,3,34,17,0,
        266,267,3,38,19,0,267,268,5,38,0,0,268,269,3,88,44,0,269,270,5,49,
        0,0,270,271,3,70,35,0,271,272,5,49,0,0,272,273,3,38,19,0,273,274,
        5,38,0,0,274,275,3,90,45,0,275,67,1,0,0,0,276,280,5,74,0,0,277,279,
        8,10,0,0,278,277,1,0,0,0,279,282,1,0,0,0,280,278,1,0,0,0,280,281,
        1,0,0,0,281,69,1,0,0,0,282,280,1,0,0,0,283,284,3,72,36,0,284,285,
        3,10,5,0,285,286,3,72,36,0,286,293,1,0,0,0,287,293,3,32,16,0,288,
        289,3,32,16,0,289,290,3,10,5,0,290,291,3,32,16,0,291,293,1,0,0,0,
        292,283,1,0,0,0,292,287,1,0,0,0,292,288,1,0,0,0,293,71,1,0,0,0,294,
        296,3,4,2,0,295,294,1,0,0,0,295,296,1,0,0,0,296,297,1,0,0,0,297,
        303,3,74,37,0,298,299,3,20,10,0,299,300,3,74,37,0,300,302,1,0,0,
        0,301,298,1,0,0,0,302,305,1,0,0,0,303,301,1,0,0,0,303,304,1,0,0,
        0,304,73,1,0,0,0,305,303,1,0,0,0,306,312,3,76,38,0,307,308,3,22,
        11,0,308,309,3,76,38,0,309,311,1,0,0,0,310,307,1,0,0,0,311,314,1,
        0,0,0,312,310,1,0,0,0,312,313,1,0,0,0,313,75,1,0,0,0,314,312,1,0,
        0,0,315,321,3,78,39,0,316,317,3,8,4,0,317,318,3,78,39,0,318,320,
        1,0,0,0,319,316,1,0,0,0,320,323,1,0,0,0,321,319,1,0,0,0,321,322,
        1,0,0,0,322,77,1,0,0,0,323,321,1,0,0,0,324,331,3,38,19,0,325,331,
        3,80,40,0,326,327,5,50,0,0,327,328,3,72,36,0,328,329,5,51,0,0,329,
        331,1,0,0,0,330,324,1,0,0,0,330,325,1,0,0,0,330,326,1,0,0,0,331,
        79,1,0,0,0,332,336,3,82,41,0,333,336,3,84,42,0,334,336,3,32,16,0,
        335,332,1,0,0,0,335,333,1,0,0,0,335,334,1,0,0,0,336,81,1,0,0,0,337,
        339,3,4,2,0,338,337,1,0,0,0,338,339,1,0,0,0,339,340,1,0,0,0,340,
        341,3,28,14,0,341,83,1,0,0,0,342,344,3,4,2,0,343,342,1,0,0,0,343,
        344,1,0,0,0,344,345,1,0,0,0,345,346,3,30,15,0,346,85,1,0,0,0,347,
        350,3,52,26,0,348,350,3,50,25,0,349,347,1,0,0,0,349,348,1,0,0,0,
        350,87,1,0,0,0,351,352,3,72,36,0,352,89,1,0,0,0,353,354,3,72,36,
        0,354,91,1,0,0,0,355,356,5,69,0,0,356,357,5,50,0,0,357,358,3,70,
        35,0,358,359,5,51,0,0,359,360,5,55,0,0,360,361,3,86,43,0,361,367,
        5,56,0,0,362,363,5,70,0,0,363,364,5,55,0,0,364,365,3,86,43,0,365,
        366,5,56,0,0,366,368,1,0,0,0,367,362,1,0,0,0,367,368,1,0,0,0,368,
        93,1,0,0,0,26,123,128,135,148,166,171,173,185,192,199,211,221,225,
        243,280,292,295,303,312,321,330,335,338,343,349,367
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'a'", "'b'", "'c'", "'d'", "'e'", "'f'", 
                     "'g'", "'h'", "'i'", "'j'", "'k'", "'l'", "'m'", "'n'", 
                     "'o'", "'p'", "'q'", "'r'", "'s'", "'t'", "'u'", "'v'", 
                     "'w'", "'x'", "'y'", "'z'", "'0'", "'1'", "'2'", "'3'", 
                     "'4'", "'5'", "'6'", "'7'", "'8'", "'9'", "'-'", "'='", 
                     "'^'", "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", 
                     "'.'", "','", "':'", "';'", "'('", "')'", "'+'", "'*'", 
                     "'/'", "'{'", "'}'", "' '", "'\\t'", "'\\r'", "'\\n'", 
                     "'true'", "'false'", "'int'", "'double'", "'bool'", 
                     "'for'", "'do'", "'while'", "'if'", "'else'", "'print'", 
                     "'readLine'", "'main'", "'//'" ]

    symbolicNames = [  ]

    RULE_letter = 0
    RULE_digit = 1
    RULE_sign = 2
    RULE_assignOp = 3
    RULE_powerOp = 4
    RULE_relOp = 5
    RULE_specialSign = 6
    RULE_whiteSpace = 7
    RULE_endOfLine = 8
    RULE_mathOp = 9
    RULE_addOp = 10
    RULE_multOp = 11
    RULE_bracOp = 12
    RULE_punctOp = 13
    RULE_unsignInt = 14
    RULE_unsignDouble = 15
    RULE_bool = 16
    RULE_type = 17
    RULE_keywords = 18
    RULE_ident = 19
    RULE_start = 20
    RULE_declarList = 21
    RULE_declaration = 22
    RULE_identList = 23
    RULE_doSection = 24
    RULE_statementList = 25
    RULE_statement = 26
    RULE_expression = 27
    RULE_assign = 28
    RULE_inp = 29
    RULE_out = 30
    RULE_forStatement = 31
    RULE_doWhileStatement = 32
    RULE_indExpr = 33
    RULE_comment = 34
    RULE_boolExpression = 35
    RULE_mathExpression = 36
    RULE_term = 37
    RULE_chunk = 38
    RULE_factor = 39
    RULE_const = 40
    RULE_integer = 41
    RULE_double = 42
    RULE_doBlock = 43
    RULE_mathExpression1 = 44
    RULE_mathExpression2 = 45
    RULE_ifStatement = 46

    ruleNames =  [ "letter", "digit", "sign", "assignOp", "powerOp", "relOp", 
                   "specialSign", "whiteSpace", "endOfLine", "mathOp", "addOp", 
                   "multOp", "bracOp", "punctOp", "unsignInt", "unsignDouble", 
                   "bool", "type", "keywords", "ident", "start", "declarList", 
                   "declaration", "identList", "doSection", "statementList", 
                   "statement", "expression", "assign", "inp", "out", "forStatement", 
                   "doWhileStatement", "indExpr", "comment", "boolExpression", 
                   "mathExpression", "term", "chunk", "factor", "const", 
                   "integer", "double", "doBlock", "mathExpression1", "mathExpression2", 
                   "ifStatement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    T__51=52
    T__52=53
    T__53=54
    T__54=55
    T__55=56
    T__56=57
    T__57=58
    T__58=59
    T__59=60
    T__60=61
    T__61=62
    T__62=63
    T__63=64
    T__64=65
    T__65=66
    T__66=67
    T__67=68
    T__68=69
    T__69=70
    T__70=71
    T__71=72
    T__72=73
    T__73=74

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class LetterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_letter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetter" ):
                listener.enterLetter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetter" ):
                listener.exitLetter(self)




    def letter(self):

        localctx = ExprParser.LetterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_letter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 134217726) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DigitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_digit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDigit" ):
                listener.enterDigit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDigit" ):
                listener.exitDigit(self)




    def digit(self):

        localctx = ExprParser.DigitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_digit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 137304735744) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_sign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSign" ):
                listener.enterSign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSign" ):
                listener.exitSign(self)




    def sign(self):

        localctx = ExprParser.SignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(ExprParser.T__36)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_assignOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignOp" ):
                listener.enterAssignOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignOp" ):
                listener.exitAssignOp(self)




    def assignOp(self):

        localctx = ExprParser.AssignOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(ExprParser.T__37)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PowerOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_powerOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowerOp" ):
                listener.enterPowerOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowerOp" ):
                listener.exitPowerOp(self)




    def powerOp(self):

        localctx = ExprParser.PowerOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_powerOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(ExprParser.T__38)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_relOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelOp" ):
                listener.enterRelOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelOp" ):
                listener.exitRelOp(self)




    def relOp(self):

        localctx = ExprParser.RelOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_relOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 69269232549888) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpecialSignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignOp(self):
            return self.getTypedRuleContext(ExprParser.AssignOpContext,0)


        def sign(self):
            return self.getTypedRuleContext(ExprParser.SignContext,0)


        def powerOp(self):
            return self.getTypedRuleContext(ExprParser.PowerOpContext,0)


        def relOp(self):
            return self.getTypedRuleContext(ExprParser.RelOpContext,0)


        def whiteSpace(self):
            return self.getTypedRuleContext(ExprParser.WhiteSpaceContext,0)


        def endOfLine(self):
            return self.getTypedRuleContext(ExprParser.EndOfLineContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_specialSign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecialSign" ):
                listener.enterSpecialSign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecialSign" ):
                listener.exitSpecialSign(self)




    def specialSign(self):

        localctx = ExprParser.SpecialSignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_specialSign)
        try:
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.match(ExprParser.T__45)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.match(ExprParser.T__46)
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 3)
                self.state = 108
                self.match(ExprParser.T__47)
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 4)
                self.state = 109
                self.match(ExprParser.T__48)
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 5)
                self.state = 110
                self.match(ExprParser.T__49)
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 6)
                self.state = 111
                self.match(ExprParser.T__50)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 7)
                self.state = 112
                self.assignOp()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 8)
                self.state = 113
                self.match(ExprParser.T__51)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 9)
                self.state = 114
                self.sign()
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 10)
                self.state = 115
                self.match(ExprParser.T__52)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 11)
                self.state = 116
                self.match(ExprParser.T__53)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 12)
                self.state = 117
                self.powerOp()
                pass
            elif token in [40, 41, 42, 43, 44, 45]:
                self.enterOuterAlt(localctx, 13)
                self.state = 118
                self.relOp()
                pass
            elif token in [57, 58]:
                self.enterOuterAlt(localctx, 14)
                self.state = 119
                self.whiteSpace()
                pass
            elif token in [59, 60]:
                self.enterOuterAlt(localctx, 15)
                self.state = 120
                self.endOfLine()
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 16)
                self.state = 121
                self.match(ExprParser.T__54)
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 17)
                self.state = 122
                self.match(ExprParser.T__55)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhiteSpaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_whiteSpace

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhiteSpace" ):
                listener.enterWhiteSpace(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhiteSpace" ):
                listener.exitWhiteSpace(self)




    def whiteSpace(self):

        localctx = ExprParser.WhiteSpaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_whiteSpace)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            _la = self._input.LA(1)
            if not(_la==57 or _la==58):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndOfLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_endOfLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndOfLine" ):
                listener.enterEndOfLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndOfLine" ):
                listener.exitEndOfLine(self)




    def endOfLine(self):

        localctx = ExprParser.EndOfLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_endOfLine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==59:
                self.state = 127
                self.match(ExprParser.T__58)


            self.state = 130
            self.match(ExprParser.T__59)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MathOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addOp(self):
            return self.getTypedRuleContext(ExprParser.AddOpContext,0)


        def multOp(self):
            return self.getTypedRuleContext(ExprParser.MultOpContext,0)


        def powerOp(self):
            return self.getTypedRuleContext(ExprParser.PowerOpContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_mathOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMathOp" ):
                listener.enterMathOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMathOp" ):
                listener.exitMathOp(self)




    def mathOp(self):

        localctx = ExprParser.MathOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_mathOp)
        try:
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37, 52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.addOp()
                pass
            elif token in [53, 54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.multOp()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 3)
                self.state = 134
                self.powerOp()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_addOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddOp" ):
                listener.enterAddOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddOp" ):
                listener.exitAddOp(self)




    def addOp(self):

        localctx = ExprParser.AddOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_addOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            _la = self._input.LA(1)
            if not(_la==37 or _la==52):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_multOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultOp" ):
                listener.enterMultOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultOp" ):
                listener.exitMultOp(self)




    def multOp(self):

        localctx = ExprParser.MultOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_multOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            _la = self._input.LA(1)
            if not(_la==53 or _la==54):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BracOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_bracOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBracOp" ):
                listener.enterBracOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBracOp" ):
                listener.exitBracOp(self)




    def bracOp(self):

        localctx = ExprParser.BracOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_bracOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 111464090777419776) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PunctOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_punctOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPunctOp" ):
                listener.enterPunctOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPunctOp" ):
                listener.exitPunctOp(self)




    def punctOp(self):

        localctx = ExprParser.PunctOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_punctOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1055531162664960) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnsignIntContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def digit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.DigitContext)
            else:
                return self.getTypedRuleContext(ExprParser.DigitContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_unsignInt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnsignInt" ):
                listener.enterUnsignInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnsignInt" ):
                listener.exitUnsignInt(self)




    def unsignInt(self):

        localctx = ExprParser.UnsignIntContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_unsignInt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 145
                self.digit()
                self.state = 148 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 137304735744) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnsignDoubleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unsignInt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.UnsignIntContext)
            else:
                return self.getTypedRuleContext(ExprParser.UnsignIntContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_unsignDouble

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnsignDouble" ):
                listener.enterUnsignDouble(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnsignDouble" ):
                listener.exitUnsignDouble(self)




    def unsignDouble(self):

        localctx = ExprParser.UnsignDoubleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_unsignDouble)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.unsignInt()
            self.state = 151
            self.match(ExprParser.T__45)
            self.state = 152
            self.unsignInt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_bool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)




    def bool_(self):

        localctx = ExprParser.BoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_bool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            _la = self._input.LA(1)
            if not(_la==61 or _la==62):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = ExprParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            _la = self._input.LA(1)
            if not(((((_la - 63)) & ~0x3f) == 0 and ((1 << (_la - 63)) & 7) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeywordsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(ExprParser.TypeContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_keywords

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeywords" ):
                listener.enterKeywords(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeywords" ):
                listener.exitKeywords(self)




    def keywords(self):

        localctx = ExprParser.KeywordsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_keywords)
        try:
            self.state = 166
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [63, 64, 65]:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.type_()
                pass
            elif token in [66]:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.match(ExprParser.T__65)
                pass
            elif token in [67]:
                self.enterOuterAlt(localctx, 3)
                self.state = 160
                self.match(ExprParser.T__66)
                pass
            elif token in [68]:
                self.enterOuterAlt(localctx, 4)
                self.state = 161
                self.match(ExprParser.T__67)
                pass
            elif token in [69]:
                self.enterOuterAlt(localctx, 5)
                self.state = 162
                self.match(ExprParser.T__68)
                pass
            elif token in [70]:
                self.enterOuterAlt(localctx, 6)
                self.state = 163
                self.match(ExprParser.T__69)
                pass
            elif token in [71]:
                self.enterOuterAlt(localctx, 7)
                self.state = 164
                self.match(ExprParser.T__70)
                pass
            elif token in [72]:
                self.enterOuterAlt(localctx, 8)
                self.state = 165
                self.match(ExprParser.T__71)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def letter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.LetterContext)
            else:
                return self.getTypedRuleContext(ExprParser.LetterContext,i)


        def digit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.DigitContext)
            else:
                return self.getTypedRuleContext(ExprParser.DigitContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_ident

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdent" ):
                listener.enterIdent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdent" ):
                listener.exitIdent(self)




    def ident(self):

        localctx = ExprParser.IdentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_ident)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.letter()
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 137438953470) != 0):
                self.state = 171
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]:
                    self.state = 169
                    self.letter()
                    pass
                elif token in [27, 28, 29, 30, 31, 32, 33, 34, 35, 36]:
                    self.state = 170
                    self.digit()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarList(self):
            return self.getTypedRuleContext(ExprParser.DeclarListContext,0)


        def doSection(self):
            return self.getTypedRuleContext(ExprParser.DoSectionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = ExprParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(ExprParser.T__72)
            self.state = 177
            self.match(ExprParser.T__54)
            self.state = 178
            self.declarList()
            self.state = 179
            self.doSection()
            self.state = 180
            self.match(ExprParser.T__55)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(ExprParser.DeclarationContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_declarList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarList" ):
                listener.enterDeclarList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarList" ):
                listener.exitDeclarList(self)




    def declarList(self):

        localctx = ExprParser.DeclarListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_declarList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 182
                self.declaration()
                self.state = 185 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 63)) & ~0x3f) == 0 and ((1 << (_la - 63)) & 2055) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(ExprParser.TypeContext,0)


        def identList(self):
            return self.getTypedRuleContext(ExprParser.IdentListContext,0)


        def comment(self):
            return self.getTypedRuleContext(ExprParser.CommentContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = ExprParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_declaration)
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [63, 64, 65]:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.type_()
                self.state = 188
                self.identList()
                self.state = 189
                self.match(ExprParser.T__48)
                pass
            elif token in [74]:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.comment()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.IdentContext)
            else:
                return self.getTypedRuleContext(ExprParser.IdentContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_identList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentList" ):
                listener.enterIdentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentList" ):
                listener.exitIdentList(self)




    def identList(self):

        localctx = ExprParser.IdentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_identList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.ident()
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==47:
                self.state = 195
                self.match(ExprParser.T__46)
                self.state = 196
                self.ident()
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementList(self):
            return self.getTypedRuleContext(ExprParser.StatementListContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_doSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoSection" ):
                listener.enterDoSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoSection" ):
                listener.exitDoSection(self)




    def doSection(self):

        localctx = ExprParser.DoSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_doSection)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(ExprParser.T__54)
            self.state = 203
            self.statementList()
            self.state = 204
            self.match(ExprParser.T__55)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_statementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementList" ):
                listener.enterStatementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementList" ):
                listener.exitStatementList(self)




    def statementList(self):

        localctx = ExprParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_statementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.statement()
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==49:
                self.state = 207
                self.match(ExprParser.T__48)
                self.state = 208
                self.statement()
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(ExprParser.AssignContext,0)


        def inp(self):
            return self.getTypedRuleContext(ExprParser.InpContext,0)


        def out(self):
            return self.getTypedRuleContext(ExprParser.OutContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(ExprParser.ForStatementContext,0)


        def doWhileStatement(self):
            return self.getTypedRuleContext(ExprParser.DoWhileStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(ExprParser.IfStatementContext,0)


        def comment(self):
            return self.getTypedRuleContext(ExprParser.CommentContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = ExprParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_statement)
        try:
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.assign()
                pass
            elif token in [72]:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.inp()
                pass
            elif token in [71]:
                self.enterOuterAlt(localctx, 3)
                self.state = 216
                self.out()
                pass
            elif token in [66]:
                self.enterOuterAlt(localctx, 4)
                self.state = 217
                self.forStatement()
                pass
            elif token in [67]:
                self.enterOuterAlt(localctx, 5)
                self.state = 218
                self.doWhileStatement()
                pass
            elif token in [69]:
                self.enterOuterAlt(localctx, 6)
                self.state = 219
                self.ifStatement()
                pass
            elif token in [74]:
                self.enterOuterAlt(localctx, 7)
                self.state = 220
                self.comment()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mathExpression(self):
            return self.getTypedRuleContext(ExprParser.MathExpressionContext,0)


        def boolExpression(self):
            return self.getTypedRuleContext(ExprParser.BoolExpressionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = ExprParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expression)
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.mathExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.boolExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(ExprParser.IdentContext,0)


        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = ExprParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.ident()
            self.state = 228
            self.match(ExprParser.T__37)
            self.state = 229
            self.expression()
            self.state = 230
            self.match(ExprParser.T__48)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identList(self):
            return self.getTypedRuleContext(ExprParser.IdentListContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_inp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInp" ):
                listener.enterInp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInp" ):
                listener.exitInp(self)




    def inp(self):

        localctx = ExprParser.InpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_inp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(ExprParser.T__71)
            self.state = 233
            self.match(ExprParser.T__49)
            self.state = 234
            self.identList()
            self.state = 235
            self.match(ExprParser.T__50)
            self.state = 236
            self.match(ExprParser.T__48)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(ExprParser.IdentContext,0)


        def const(self):
            return self.getTypedRuleContext(ExprParser.ConstContext,0)


        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_out

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOut" ):
                listener.enterOut(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOut" ):
                listener.exitOut(self)




    def out(self):

        localctx = ExprParser.OutContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_out)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(ExprParser.T__70)
            self.state = 239
            self.match(ExprParser.T__49)
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 240
                self.ident()
                pass

            elif la_ == 2:
                self.state = 241
                self.const()
                pass

            elif la_ == 3:
                self.state = 242
                self.expression()
                pass


            self.state = 245
            self.match(ExprParser.T__50)
            self.state = 246
            self.match(ExprParser.T__48)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indExpr(self):
            return self.getTypedRuleContext(ExprParser.IndExprContext,0)


        def doBlock(self):
            return self.getTypedRuleContext(ExprParser.DoBlockContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)




    def forStatement(self):

        localctx = ExprParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(ExprParser.T__65)
            self.state = 249
            self.match(ExprParser.T__49)
            self.state = 250
            self.indExpr()
            self.state = 251
            self.match(ExprParser.T__50)
            self.state = 252
            self.match(ExprParser.T__54)
            self.state = 253
            self.doBlock()
            self.state = 254
            self.match(ExprParser.T__55)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoWhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def doBlock(self):
            return self.getTypedRuleContext(ExprParser.DoBlockContext,0)


        def boolExpression(self):
            return self.getTypedRuleContext(ExprParser.BoolExpressionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_doWhileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoWhileStatement" ):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoWhileStatement" ):
                listener.exitDoWhileStatement(self)




    def doWhileStatement(self):

        localctx = ExprParser.DoWhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_doWhileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(ExprParser.T__66)
            self.state = 257
            self.match(ExprParser.T__54)
            self.state = 258
            self.doBlock()
            self.state = 259
            self.match(ExprParser.T__55)
            self.state = 260
            self.match(ExprParser.T__67)
            self.state = 261
            self.match(ExprParser.T__49)
            self.state = 262
            self.boolExpression()
            self.state = 263
            self.match(ExprParser.T__50)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(ExprParser.TypeContext,0)


        def ident(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.IdentContext)
            else:
                return self.getTypedRuleContext(ExprParser.IdentContext,i)


        def mathExpression1(self):
            return self.getTypedRuleContext(ExprParser.MathExpression1Context,0)


        def boolExpression(self):
            return self.getTypedRuleContext(ExprParser.BoolExpressionContext,0)


        def mathExpression2(self):
            return self.getTypedRuleContext(ExprParser.MathExpression2Context,0)


        def getRuleIndex(self):
            return ExprParser.RULE_indExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndExpr" ):
                listener.enterIndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndExpr" ):
                listener.exitIndExpr(self)




    def indExpr(self):

        localctx = ExprParser.IndExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_indExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.type_()
            self.state = 266
            self.ident()
            self.state = 267
            self.match(ExprParser.T__37)
            self.state = 268
            self.mathExpression1()
            self.state = 269
            self.match(ExprParser.T__48)
            self.state = 270
            self.boolExpression()
            self.state = 271
            self.match(ExprParser.T__48)
            self.state = 272
            self.ident()
            self.state = 273
            self.match(ExprParser.T__37)
            self.state = 274
            self.mathExpression2()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = ExprParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(ExprParser.T__73)
            self.state = 280
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 277
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==59 or _la==60:
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 282
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mathExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.MathExpressionContext)
            else:
                return self.getTypedRuleContext(ExprParser.MathExpressionContext,i)


        def relOp(self):
            return self.getTypedRuleContext(ExprParser.RelOpContext,0)


        def bool_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.BoolContext)
            else:
                return self.getTypedRuleContext(ExprParser.BoolContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_boolExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolExpression" ):
                listener.enterBoolExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolExpression" ):
                listener.exitBoolExpression(self)




    def boolExpression(self):

        localctx = ExprParser.BoolExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_boolExpression)
        try:
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.mathExpression()
                self.state = 284
                self.relOp()
                self.state = 285
                self.mathExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.bool_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 288
                self.bool_()
                self.state = 289
                self.relOp()
                self.state = 290
                self.bool_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MathExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.TermContext)
            else:
                return self.getTypedRuleContext(ExprParser.TermContext,i)


        def sign(self):
            return self.getTypedRuleContext(ExprParser.SignContext,0)


        def addOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.AddOpContext)
            else:
                return self.getTypedRuleContext(ExprParser.AddOpContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_mathExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMathExpression" ):
                listener.enterMathExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMathExpression" ):
                listener.exitMathExpression(self)




    def mathExpression(self):

        localctx = ExprParser.MathExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_mathExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 294
                self.sign()


            self.state = 297
            self.term()
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37 or _la==52:
                self.state = 298
                self.addOp()
                self.state = 299
                self.term()
                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def chunk(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ChunkContext)
            else:
                return self.getTypedRuleContext(ExprParser.ChunkContext,i)


        def multOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.MultOpContext)
            else:
                return self.getTypedRuleContext(ExprParser.MultOpContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = ExprParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.chunk()
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==53 or _la==54:
                self.state = 307
                self.multOp()
                self.state = 308
                self.chunk()
                self.state = 314
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChunkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.FactorContext)
            else:
                return self.getTypedRuleContext(ExprParser.FactorContext,i)


        def powerOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.PowerOpContext)
            else:
                return self.getTypedRuleContext(ExprParser.PowerOpContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_chunk

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChunk" ):
                listener.enterChunk(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChunk" ):
                listener.exitChunk(self)




    def chunk(self):

        localctx = ExprParser.ChunkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_chunk)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.factor()
            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 316
                self.powerOp()
                self.state = 317
                self.factor()
                self.state = 323
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(ExprParser.IdentContext,0)


        def const(self):
            return self.getTypedRuleContext(ExprParser.ConstContext,0)


        def mathExpression(self):
            return self.getTypedRuleContext(ExprParser.MathExpressionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = ExprParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_factor)
        try:
            self.state = 330
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self.ident()
                pass
            elif token in [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 61, 62]:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.const()
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 3)
                self.state = 326
                self.match(ExprParser.T__49)
                self.state = 327
                self.mathExpression()
                self.state = 328
                self.match(ExprParser.T__50)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integer(self):
            return self.getTypedRuleContext(ExprParser.IntegerContext,0)


        def double(self):
            return self.getTypedRuleContext(ExprParser.DoubleContext,0)


        def bool_(self):
            return self.getTypedRuleContext(ExprParser.BoolContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_const

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConst" ):
                listener.enterConst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConst" ):
                listener.exitConst(self)




    def const(self):

        localctx = ExprParser.ConstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_const)
        try:
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.integer()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
                self.double()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 334
                self.bool_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unsignInt(self):
            return self.getTypedRuleContext(ExprParser.UnsignIntContext,0)


        def sign(self):
            return self.getTypedRuleContext(ExprParser.SignContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_integer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)




    def integer(self):

        localctx = ExprParser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 337
                self.sign()


            self.state = 340
            self.unsignInt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoubleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unsignDouble(self):
            return self.getTypedRuleContext(ExprParser.UnsignDoubleContext,0)


        def sign(self):
            return self.getTypedRuleContext(ExprParser.SignContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_double

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDouble" ):
                listener.enterDouble(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDouble" ):
                listener.exitDouble(self)




    def double(self):

        localctx = ExprParser.DoubleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_double)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 342
                self.sign()


            self.state = 345
            self.unsignDouble()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ExprParser.StatementContext,0)


        def statementList(self):
            return self.getTypedRuleContext(ExprParser.StatementListContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_doBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoBlock" ):
                listener.enterDoBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoBlock" ):
                listener.exitDoBlock(self)




    def doBlock(self):

        localctx = ExprParser.DoBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_doBlock)
        try:
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.statementList()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MathExpression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mathExpression(self):
            return self.getTypedRuleContext(ExprParser.MathExpressionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_mathExpression1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMathExpression1" ):
                listener.enterMathExpression1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMathExpression1" ):
                listener.exitMathExpression1(self)




    def mathExpression1(self):

        localctx = ExprParser.MathExpression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_mathExpression1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.mathExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MathExpression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mathExpression(self):
            return self.getTypedRuleContext(ExprParser.MathExpressionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_mathExpression2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMathExpression2" ):
                listener.enterMathExpression2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMathExpression2" ):
                listener.exitMathExpression2(self)




    def mathExpression2(self):

        localctx = ExprParser.MathExpression2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_mathExpression2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.mathExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolExpression(self):
            return self.getTypedRuleContext(ExprParser.BoolExpressionContext,0)


        def doBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.DoBlockContext)
            else:
                return self.getTypedRuleContext(ExprParser.DoBlockContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = ExprParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(ExprParser.T__68)
            self.state = 356
            self.match(ExprParser.T__49)
            self.state = 357
            self.boolExpression()
            self.state = 358
            self.match(ExprParser.T__50)
            self.state = 359
            self.match(ExprParser.T__54)
            self.state = 360
            self.doBlock()
            self.state = 361
            self.match(ExprParser.T__55)
            self.state = 367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==70:
                self.state = 362
                self.match(ExprParser.T__69)
                self.state = 363
                self.match(ExprParser.T__54)
                self.state = 364
                self.doBlock()
                self.state = 365
                self.match(ExprParser.T__55)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





