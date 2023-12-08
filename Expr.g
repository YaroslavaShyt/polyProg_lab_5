grammar Expr;

letter : 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z' ;

digit : '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' ;

sign : '-' ;

assignOp : '=' ;

powerOp : '^' ;

relOp : '==' | '!=' | '>' | '<' | '>=' | '<=' ;

specialSign : '.' | ',' | ':' | ';' | '(' | ')' | assignOp | '+' | sign | '*' | '/' | powerOp | relOp | whiteSpace | endOfLine | '{' | '}' ;

whiteSpace : ' ' | '\t' ;

endOfLine : '\r'? '\n';

mathOp : addOp | multOp | powerOp ;

addOp : '+' | '-' ;

multOp : '*' | '/' ;

bracOp : '(' | ')' | '{' | '}' ;

punctOp : '.' | ',' | ':' | ';' ;

unsignInt : digit+ ;

unsignDouble : unsignInt '.' unsignInt ;

bool : 'true' | 'false' ;

type : 'int' | 'double' | 'bool' ;

keywords : type | 'for' | 'do' | 'while' | 'if' | 'else' | 'print' | 'readLine' ;

ident : letter (letter | digit)*;

start : 'main' '{' declarList doSection '}' ;

declarList : declaration+ ;

declaration : type identList ';' | comment ;

identList : ident (',' ident)* ;

doSection : '{' statementList '}' ;

statementList : statement (';' statement)* ;

statement : assign | inp | out | forStatement | doWhileStatement | ifStatement | comment ;

expression : mathExpression | boolExpression;

assign : ident '=' expression ';' ;

inp : 'readLine' '(' identList ')' ';' ;

out : 'print' '(' (ident | const | expression) ')' ';' ;

forStatement : 'for' '(' indExpr ')' '{' doBlock '}' ;

doWhileStatement : 'do' '{' doBlock '}' 'while' '(' boolExpression ')' ;

indExpr : type ident '=' mathExpression1 ';' boolExpression ';' ident '=' mathExpression2 ;

comment : '//' ~('\r' | '\n')*;

boolExpression : mathExpression relOp mathExpression | bool | bool relOp bool ;

mathExpression : (sign)? term (addOp term)* ;

term : chunk (multOp chunk)* ;

chunk : factor (powerOp factor)* ;

factor : ident | const | '(' mathExpression ')' ;

const : integer | double | bool ;

integer : sign? unsignInt ;

double : sign? unsignDouble ;

doBlock : statement | statementList;

mathExpression1 : mathExpression;

mathExpression2 : mathExpression;

ifStatement : 'if' '(' boolExpression ')' '{' doBlock '}' ( 'else' '{' doBlock '}' )?;
