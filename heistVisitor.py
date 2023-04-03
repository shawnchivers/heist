# Generated from heist.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .heistParser import heistParser
else:
    from heistParser import heistParser

# This class defines a complete generic visitor for a parse tree produced by heistParser.

class heistVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by heistParser#program.
    def visitProgram(self, ctx:heistParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#line.
    def visitLine(self, ctx:heistParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STMT_PRINT.
    def visitSTMT_PRINT(self, ctx:heistParser.STMT_PRINTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STMT_IF.
    def visitSTMT_IF(self, ctx:heistParser.STMT_IFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STMT_IF_ELSE.
    def visitSTMT_IF_ELSE(self, ctx:heistParser.STMT_IF_ELSEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STMT_DO_WHILE.
    def visitSTMT_DO_WHILE(self, ctx:heistParser.STMT_DO_WHILEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STMT_FOR.
    def visitSTMT_FOR(self, ctx:heistParser.STMT_FORContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STMT_FUNC.
    def visitSTMT_FUNC(self, ctx:heistParser.STMT_FUNCContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STMT_RET.
    def visitSTMT_RET(self, ctx:heistParser.STMT_RETContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STMT_CALL.
    def visitSTMT_CALL(self, ctx:heistParser.STMT_CALLContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STMT_CALL_EXPR.
    def visitSTMT_CALL_EXPR(self, ctx:heistParser.STMT_CALL_EXPRContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STMT_EXIT.
    def visitSTMT_EXIT(self, ctx:heistParser.STMT_EXITContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STMT_INPUT.
    def visitSTMT_INPUT(self, ctx:heistParser.STMT_INPUTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STMT_ASSIGN.
    def visitSTMT_ASSIGN(self, ctx:heistParser.STMT_ASSIGNContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STMT_ARRAY_ASSIGN.
    def visitSTMT_ARRAY_ASSIGN(self, ctx:heistParser.STMT_ARRAY_ASSIGNContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STMT_ARRAY.
    def visitSTMT_ARRAY(self, ctx:heistParser.STMT_ARRAYContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STMT_ARRAY_VALUE.
    def visitSTMT_ARRAY_VALUE(self, ctx:heistParser.STMT_ARRAY_VALUEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STMT_ARRAY_UPPERBOUND.
    def visitSTMT_ARRAY_UPPERBOUND(self, ctx:heistParser.STMT_ARRAY_UPPERBOUNDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STMT_ISARRAY.
    def visitSTMT_ISARRAY(self, ctx:heistParser.STMT_ISARRAYContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STMT_ISFUNCTION.
    def visitSTMT_ISFUNCTION(self, ctx:heistParser.STMT_ISFUNCTIONContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STMT_ISNUMBER.
    def visitSTMT_ISNUMBER(self, ctx:heistParser.STMT_ISNUMBERContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STMT_ISINTEGER.
    def visitSTMT_ISINTEGER(self, ctx:heistParser.STMT_ISINTEGERContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STMT_ISDOUBLE.
    def visitSTMT_ISDOUBLE(self, ctx:heistParser.STMT_ISDOUBLEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STMT_ISSTRING.
    def visitSTMT_ISSTRING(self, ctx:heistParser.STMT_ISSTRINGContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STMT_ISBOOLEAN.
    def visitSTMT_ISBOOLEAN(self, ctx:heistParser.STMT_ISBOOLEANContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STMT_ISNULL.
    def visitSTMT_ISNULL(self, ctx:heistParser.STMT_ISNULLContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STMT_ISEMPTY.
    def visitSTMT_ISEMPTY(self, ctx:heistParser.STMT_ISEMPTYContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#function.
    def visitFunction(self, ctx:heistParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#expr_statement.
    def visitExpr_statement(self, ctx:heistParser.Expr_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#ifblock.
    def visitIfblock(self, ctx:heistParser.IfblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#elseblock.
    def visitElseblock(self, ctx:heistParser.ElseblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STATEMENT.
    def visitSTATEMENT(self, ctx:heistParser.STATEMENTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#MULOP.
    def visitMULOP(self, ctx:heistParser.MULOPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#NULL.
    def visitNULL(self, ctx:heistParser.NULLContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#UOPGRP.
    def visitUOPGRP(self, ctx:heistParser.UOPGRPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#VAR.
    def visitVAR(self, ctx:heistParser.VARContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#CONCAT.
    def visitCONCAT(self, ctx:heistParser.CONCATContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#PAREN.
    def visitPAREN(self, ctx:heistParser.PARENContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#INT.
    def visitINT(self, ctx:heistParser.INTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#UMINUS.
    def visitUMINUS(self, ctx:heistParser.UMINUSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#ADDOP.
    def visitADDOP(self, ctx:heistParser.ADDOPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#BOOL.
    def visitBOOL(self, ctx:heistParser.BOOLContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#CONST.
    def visitCONST(self, ctx:heistParser.CONSTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STRING.
    def visitSTRING(self, ctx:heistParser.STRINGContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#POW.
    def visitPOW(self, ctx:heistParser.POWContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#DOUBLE.
    def visitDOUBLE(self, ctx:heistParser.DOUBLEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#RELOP.
    def visitRELOP(self, ctx:heistParser.RELOPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#null.
    def visitNull(self, ctx:heistParser.NullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#const.
    def visitConst(self, ctx:heistParser.ConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#uop.
    def visitUop(self, ctx:heistParser.UopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#addop.
    def visitAddop(self, ctx:heistParser.AddopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#mulop.
    def visitMulop(self, ctx:heistParser.MulopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#paramlist.
    def visitParamlist(self, ctx:heistParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#param.
    def visitParam(self, ctx:heistParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#arglist.
    def visitArglist(self, ctx:heistParser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#relop.
    def visitRelop(self, ctx:heistParser.RelopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#arg.
    def visitArg(self, ctx:heistParser.ArgContext):
        return self.visitChildren(ctx)



del heistParser