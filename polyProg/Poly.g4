grammar Poly;

program: 'main' '{' variableDeclaration* statement* '}' ;

variableDeclaration: type ID ';' ;

statement: assignment ';'               # assignmentStatement
         | ifStatement                  # ifSt
         | whileStatement               # whileSt
         | forStatement                 # forStat
         | doWhileStatement             # doWhileSt
         | printStatement ';'           # printSt
         | readlineStatement ';'        # readlineSt
         | NEWLINE                       # emptyStatement
         ;

assignment: ID '=' expression ;

ifStatement: 'if' '(' boolExpression ')' '{' statement* '}' ('else' '{' statement* '}')?;

whileStatement: 'while' '(' boolExpression ')' '{' statement* '}';

forStatement: 'for' '(' assignment ';' boolExpression ';' assignment ')' '{' statement* '}';

doWhileStatement: 'do' '{' statement* '}' 'while' '(' boolExpression ')' ;

printStatement: 'print' '(' printArgument (',' printArgument)* ')' ;

printArgument: expression ;

readlineStatement: 'readline' '(' ID (',' ID)* ')' ;

type: 'int' | 'double' | 'bool' ;

expression: additiveExpression ;

additiveExpression: multiplicativeExpression ( ('+' | '-') multiplicativeExpression)* ;

multiplicativeExpression: powerExpression ( ('*' | '/') powerExpression)* ;

powerExpression: unaryExpression ( '^' unaryExpression )* ;

unaryExpression: '-'? primaryExpression ;

primaryExpression: ID | INT | FLOAT | 'true' | 'false' | '(' expression ')' ;

boolExpression: additiveExpression ( ('==' | '!=' | '<' | '<=' | '>' | '>=') additiveExpression)+;

COMMENT: '//' ~[\r\n]* -> skip;

ID      : ALPHABET (ALPHABET | DIGIT)* ;
FLOAT   : DIGIT* '.' DIGIT+ ;
INT     : DIGIT+ ;

fragment ALPHABET: [a-zA-Z] ;
fragment DIGIT: [0-9] ;

NEWLINE: '\r'? '\n' -> skip;

WS: [ \t]+ -> skip ;
