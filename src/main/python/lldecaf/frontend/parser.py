'''
Created on Dec 2, 2015

@author: pinogal
'''

from ply import *

import scanner
import sys

tokens = scanner.tokens
global decaf_parser

def printNode(n, space):
    print "-"*space + str(n)

#------
# Rules
#_-----

def p_Program(p):
    'Program :    DeclList'
    printNode("Program", 0)

def p_DeclList(p):
    '''
    DeclList :    DeclList Decl
            |    Decl
    '''
    printNode("DeclList", 1)
    
def p_Decl(p):
    '''
    Decl :    VarDec
        |    FuncDec
    '''
#          |    ClassDec
#          |    InterDec
#     '''
    printNode("Decl", 2)
    
def p_VarDec(p):
    'VarDec :    Var SEMI'
    printNode("VarDec", 3)
    
def p_Var(p):
    'Var :    Type ID'
    printNode("Var", 4)

def p_Type(p):
    '''
    Type :    INT
         |    DOUBLE
         |    BOOL
         |    STRING
         |    ID
         |    Type LBRACKET RBRACKET
    '''
    printNode("Type", 5)

def p_FuncDec(p):
    '''
    FuncDec :    Type ID LPAREN Formals RPAREN StmtBlock
            |    VOID ID LPAREN Formals RPAREN StmtBlock
    '''
    printNode("FuncDec", 6)

def p_Formals(p):
    '''
    Formals :    Formals COMMA Var
            |    Var
            |    Empty
    '''
    pass

def p_StmtBlock(p):
    'StmtBlock :    LBRACE VarDecList StmtList RBRACE'
    pass

def p_VarDecList(p):
    '''
    VarDecList :    VarDecList VarDec
               |    Empty
    '''
    pass

def p_StmtList(p):
    '''
    StmtList :    Stmt StmtList
             |    Empty
    '''
    pass

def p_Stmt(p):
    '''
    Stmt :    ExprP SEMI
         |    IfStmt
         |    WhileStmt
         |    ForStmt
         |    BreakStmt
         |    ReturnStmt
         |    PrintStmt
         |    StmtBlock
         |    SwitchStmt
    '''
    pass

def p_IfStmt(p):
    '''
    IfStmt :    IF LPAREN Assignment RPAREN Stmt ElseStmt
    '''
    pass

def p_ElseStmt(p):
    '''
    ElseStmt :    ELSE Stmt
             |    Empty
    '''
    pass

def p_WhileStmt(p):
    '''
    WhileStmt :    WHILE LPAREN Assignment RPAREN Stmt
    '''
    pass

def p_ForStmt(p):
    '''
    ForStmt :    FOR LPAREN ExprP SEMI Assignment SEMI ExprP RPAREN Stmt
    '''
    pass

def p_ReturnStmt(p):
    '''
    ReturnStmt :    RETURN ExprP SEMI
    '''
    pass

def p_SwitchStmt(p):
    '''
    SwitchStmt :    SWITCH LPAREN Assignment RPAREN LBRACE CaseList Default RBRACE
    '''
    pass

def p_CaseList(p):
    '''
    CaseList :    CASE ICONST COLON StmtList CaseList
             |    CASE ICONST COLON StmtList
    '''
    pass

def p_Default(p):
    '''
    Default :    DEFAULT COLON StmtList
            |    Empty
    '''
    pass

def p_ExprP(p):
    '''
    ExprP :    Assignment
          |    Empty
    '''
    pass

def p_BreakStmt(p):
    '''
    BreakStmt :    BREAK SEMI
    '''
    pass

def p_PrintStmt(p):
    '''
    PrintStmt :    PRINT LPAREN Assignment ExprList RPAREN SEMI
    '''
    pass

def p_ExprList(p):
    '''
    ExprList :    COMMA Assignment ExprList
             |    Empty
    '''
    pass

# =
def p_Assignment(p):
    '''
    Assignment :    LValue EQUALS Assignment
               |    LogicalOr
    '''
    pass

def p_LogicalOr(p):
    '''
    LogicalOr :    LogicalOr LOR LogicalAnd
              |    LogicalAnd
    '''
    pass

def p_LogicalAnd(p):
    '''
    LogicalAnd :    LogicalAnd LAND Equality
               |    Equality
    '''
    pass

def p_Equality(p):
    '''
    Equality :    Relational EQUALS Equality
             |    Relational NE Equality
             |    Relational
    '''
    pass

def p_Relational(p):
    '''
    Relational :    Expression LT Relational
               |    Expression LE Relational
               |    Expression GT Relational
               |    Expression GE Relational
               |    Expression
    '''
    pass

def p_Expression(p):
    '''
    Expression :    Expression PLUS Expression
               |    Expression MINUS Expression
               |    Terminal
    '''
    pass

def p_Terminal(p):
    '''
    Terminal :    Terminal TIMES Factor
             |    Terminal DIVIDE Factor
             |    Terminal MOD Factor
             |    Factor
    '''
    pass

def p_Factor(p):
    '''
    Factor :    MINUS Basic
           |    LNOT Basic
           |    Basic PLUSPLUS
           |    Basic MINUSMINUS
           |    Basic
    '''
    pass

def p_LValue(p):
    '''
    LValue :    Atomic PERIOD ID
           |    ArrayAccess
           |    ID
    '''
    pass

def p_Basic(p):
    '''
    Basic :    Atomic PERIOD ID
          |    ArrayAccess
          |    Atomic
    '''
    pass

def p_ArrayAccess(p):
    '''
    ArrayAccess :    ArrayAccess LBRACKET Expression RBRACKET
                |    Atomic LBRACKET Expression RBRACKET
    '''
    pass

def p_Atomic(p):
    '''
    Atomic :    Constant
           |    THIS
           |    ID
           |    LPAREN Expression RPAREN
           |    READINTEGER
           |    READLINE
           |    NEW LPAREN ID RPAREN
           |    NEWARRAY LPAREN Assignment COMMA Type RPAREN
           |    Call
    '''
    pass

def p_Call(p):
    '''
    Call :    ID LPAREN Actuals RPAREN
         |    Atomic PERIOD ID LPAREN Actuals RPAREN
    '''
    pass

def p_Actuals(p):
    '''
    Actuals :    Assignment ExprList
            |    Empty
    '''
    pass

def p_Constant(p):
    '''
    Constant :    ICONST
             |    FCONST
             |    BCONST
             |    SCONST
             |    NULL
    '''
    pass

# Empty
def p_Empty(p):
    '''Empty : '''

# def p_expression_plus(p):
#     'expression : expression PLUS term'
#     p[0] = p[1] + p[3]
# 
# def p_expression_minus(p):
#     'expression : expression MINUS term'
#     p[0] = p[1] - p[3]
# 
# def p_expression_term(p):
#     'expression : term'
#     p[0] = p[1]
# 
# def p_term_times(p):
#     'term : term TIMES factor'
#     p[0] = p[1] * p[3]
# 
# def p_term_div(p):
#     'term : term DIVIDE factor'
#     p[0] = p[1] / p[3]
# 
# def p_term_factor(p):
#     'term : factor'
#     p[0] = p[1]
# 
# def p_factor_num(p):
#     'factor : NUMBER'
#     p[0] = p[1]
# 
# def p_factor_expr(p):
#     'factor : LPAREN expression RPAREN'
#     p[0] = p[2]

# Error rule for syntax errors
# Catastrophic error handler
def p_error(p):
    # Read ahead looking for a terminating ";"
    if p:
        line = "%s = %r at line %d near %s" % (p.type, p.value, p.lineno, p.value)
        while True:
            tok = decaf_parser.token()             # Get the next token
            if not tok or tok.type == 'SEMI': 
                break
            else:
                line = line + tok.value
    
        if len(line) > 0:
            print("Syntax error at token " + line)
    else:
        print("Syntax error at EOF")

# Build the parser
decaf_parser = yacc.yacc()

def parse(data, debug_flag=False):
    decaf_parser.error = 0
    prog = decaf_parser.parse(data, debug=debug_flag)
    if decaf_parser.error: return None
    return prog

if __name__ == '__main__':
    if len(sys.argv) == 2:
        data = open(sys.argv[1]).read()
        prog = parse(data, False)

# while True:
#     try:
#         s = raw_input('decaf > ')
#     except EOFError:
#         break
#     if not s: continue
#     result = parser.parse(s)
#     print(result)