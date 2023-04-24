grammar heist;

program
  : line* EOF
  ;

line
 : CR* statement CR*
 ;



statement
  : 'print' express=expr                                                                         # STMT_PRINT
  | 'if' express=expr 'then' ifblock 'end if'                                                    # STMT_IF
  | 'if' express=expr 'then' ifblock 'else' elseblock 'end if'                                   # STMT_IF_ELSE
  | 'do while' express=expr CR* line+ CR* 'loop'                                                 # STMT_DO_WHILE
  | 'for' varname=VAR '=' start=expr 'to' end=expr 'step'? stepcount=expr? CR* line+ CR* 'next'  # STMT_FOR
  | 'function' rec='tail-recurse'? varname=VAR? '(' args=arglist? ')' CR* line+ CR* 'end function'    # STMT_FUNC
  | 'return' express=expr                                                                        # STMT_RET
  | 'call'? varname=VAR '(' plist=paramlist? ')'                                                 # STMT_CALL
  | 'call'? ('('|'[') express=expr (')' | ']') '(' plist=paramlist? ')'                          # STMT_CALL_EXPR
  | 'exit'                                                                                       # STMT_EXIT
  | 'input' varname=VAR                                                                          # STMT_INPUT
  | varname=VAR op=('=' | ':=') varval=expr_statement                                            # STMT_ASSIGN
  | varname=VAR '(' num=expr ')'  op=('=' | ':=') varval=expr                                    # STMT_ARRAY_ASSIGN
  | varname=VAR 'as' ('array'|'Array') '(' num=expr ')'                                          # STMT_ARRAY
  | varname=VAR '(' num=expr ')'									                                               # STMT_ARRAY_VALUE
  | ('ubound'|'upperbound') '(' varname=VAR ')'                                                  # STMT_ARRAY_UPPERBOUND
  | ('isarray') '(' express=expr ')'                                                             # STMT_ISARRAY
  | ('isfunction') '(' express=expr ')'                                                          # STMT_ISFUNCTION
  | ('isnumber') '(' express=expr ')'                                                            # STMT_ISNUMBER
  | ('isinteger') '(' express=expr ')'                                                           # STMT_ISINTEGER
  | ('isdouble') '(' express=expr ')'                                                            # STMT_ISDOUBLE
  | ('isstring') '(' express=expr ')'                                                            # STMT_ISSTRING
  | ('isboolean') '(' express=expr ')'                                                           # STMT_ISBOOLEAN
  | ('isnull') '(' express=expr ')'                                                              # STMT_ISNULL
  | ('isempty') '(' express=expr ')'                                                             # STMT_ISEMPTY
  ;

function
  : 'nothing'
  ;

expr_statement
  : expr
  | statement
  ;

ifblock
  : (line)+
  ;

elseblock
  : (line)+
  ;

expr : const                                   # CONST
  | '-' num=expr                               # UMINUS
  | uop '(' num=expr ')'                       # UOPGRP
  | lexpr=expr '^' rexpr=expr                  # POW
  | lexpr=expr mulop rexpr=expr                # MULOP
  | lexpr=expr addop rexpr=expr                # ADDOP
  | '(' midexpr=expr ')'                       # PAREN
  | lexpr=expr (';' | '&' | '|' | '..' ) rexpr=expr          # CONCAT
  | urelop midexpr=expr                           # URELOP
  | lexpr=expr relop rexpr=expr                # RELOP
  | BOOLEAN                                    # BOOL
  | INT                                        # INT
  | DOUBLE                                     # DOUBLE
  | VAR                                        # VAR
  | STRING                                     # STRING
  | statement                                  # STATEMENT
  | null                                       # NULL
  ;



null : 'null' | 'nothing' | 'empty' | 'void' | 'nil' ;

const: 'pi' | 'e';

uop: 'sin' | 'cos' | 'tan' | 'abs' | 'sqrt' | 'ln' | 'log' | 'log10' | 'log2' | 'str' | 'factorial' | 'int' | 'float' |'tab' ;

addop : '+' | '-';

mulop : '*' | '/' | '%' | 'mod';

paramlist: param (',' param)*;

param: expr;

arglist : arg (',' arg)*;

relop
  : ('<' ('>' | '=' )?)
  | ('>' ('<' | '=' )?)
  | 'equals'
  | '=='
  | '<>'
  | 'and'
  | 'or'
  | 'xor'
  ;

urelop
  : 'not'
  ;

arg
  : VAR
  | STRING
  ;

INT : ('0' .. '9') + (('0' .. '9') +)?;

DOUBLE : ('0' .. '9') + ('.' ('0' .. '9') +)?;

BOOLEAN : 'true' | 'false';

STRING
  : '"' ~ ["\r\n]* '"'
  ;

VAR
  : [a-zA-Z0-9_?]+
  ;

CR
  : [\r\n]+
  ;

COMMENT
  : ('\''| 'rem ' | '#') ~ [\r\n]* CR -> channel(HIDDEN)
  ;

WS
  : [ \t] -> channel(HIDDEN)
  ;
