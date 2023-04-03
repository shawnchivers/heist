# Generated from heist.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .heistParser import heistParser
else:
    from heistParser import heistParser

# This class defines a complete listener for a parse tree produced by heistParser.
class heistListener(ParseTreeListener):

    # Enter a parse tree produced by heistParser#program.
    def enterProgram(self, ctx:heistParser.ProgramContext):
        pass

    # Exit a parse tree produced by heistParser#program.
    def exitProgram(self, ctx:heistParser.ProgramContext):
        pass


    # Enter a parse tree produced by heistParser#line.
    def enterLine(self, ctx:heistParser.LineContext):
        pass

    # Exit a parse tree produced by heistParser#line.
    def exitLine(self, ctx:heistParser.LineContext):
        pass


    # Enter a parse tree produced by heistParser#STMT_PRINT.
    def enterSTMT_PRINT(self, ctx:heistParser.STMT_PRINTContext):
        pass

    # Exit a parse tree produced by heistParser#STMT_PRINT.
    def exitSTMT_PRINT(self, ctx:heistParser.STMT_PRINTContext):
        pass


    # Enter a parse tree produced by heistParser#STMT_IF.
    def enterSTMT_IF(self, ctx:heistParser.STMT_IFContext):
        pass

    # Exit a parse tree produced by heistParser#STMT_IF.
    def exitSTMT_IF(self, ctx:heistParser.STMT_IFContext):
        pass


    # Enter a parse tree produced by heistParser#STMT_IF_ELSE.
    def enterSTMT_IF_ELSE(self, ctx:heistParser.STMT_IF_ELSEContext):
        pass

    # Exit a parse tree produced by heistParser#STMT_IF_ELSE.
    def exitSTMT_IF_ELSE(self, ctx:heistParser.STMT_IF_ELSEContext):
        pass


    # Enter a parse tree produced by heistParser#STMT_DO_WHILE.
    def enterSTMT_DO_WHILE(self, ctx:heistParser.STMT_DO_WHILEContext):
        pass

    # Exit a parse tree produced by heistParser#STMT_DO_WHILE.
    def exitSTMT_DO_WHILE(self, ctx:heistParser.STMT_DO_WHILEContext):
        pass


    # Enter a parse tree produced by heistParser#STMT_FOR.
    def enterSTMT_FOR(self, ctx:heistParser.STMT_FORContext):
        pass

    # Exit a parse tree produced by heistParser#STMT_FOR.
    def exitSTMT_FOR(self, ctx:heistParser.STMT_FORContext):
        pass


    # Enter a parse tree produced by heistParser#STMT_FUNC.
    def enterSTMT_FUNC(self, ctx:heistParser.STMT_FUNCContext):
        pass

    # Exit a parse tree produced by heistParser#STMT_FUNC.
    def exitSTMT_FUNC(self, ctx:heistParser.STMT_FUNCContext):
        pass


    # Enter a parse tree produced by heistParser#STMT_RET.
    def enterSTMT_RET(self, ctx:heistParser.STMT_RETContext):
        pass

    # Exit a parse tree produced by heistParser#STMT_RET.
    def exitSTMT_RET(self, ctx:heistParser.STMT_RETContext):
        pass


    # Enter a parse tree produced by heistParser#STMT_CALL.
    def enterSTMT_CALL(self, ctx:heistParser.STMT_CALLContext):
        pass

    # Exit a parse tree produced by heistParser#STMT_CALL.
    def exitSTMT_CALL(self, ctx:heistParser.STMT_CALLContext):
        pass


    # Enter a parse tree produced by heistParser#STMT_CALL_EXPR.
    def enterSTMT_CALL_EXPR(self, ctx:heistParser.STMT_CALL_EXPRContext):
        pass

    # Exit a parse tree produced by heistParser#STMT_CALL_EXPR.
    def exitSTMT_CALL_EXPR(self, ctx:heistParser.STMT_CALL_EXPRContext):
        pass


    # Enter a parse tree produced by heistParser#STMT_EXIT.
    def enterSTMT_EXIT(self, ctx:heistParser.STMT_EXITContext):
        pass

    # Exit a parse tree produced by heistParser#STMT_EXIT.
    def exitSTMT_EXIT(self, ctx:heistParser.STMT_EXITContext):
        pass


    # Enter a parse tree produced by heistParser#STMT_INPUT.
    def enterSTMT_INPUT(self, ctx:heistParser.STMT_INPUTContext):
        pass

    # Exit a parse tree produced by heistParser#STMT_INPUT.
    def exitSTMT_INPUT(self, ctx:heistParser.STMT_INPUTContext):
        pass


    # Enter a parse tree produced by heistParser#STMT_ASSIGN.
    def enterSTMT_ASSIGN(self, ctx:heistParser.STMT_ASSIGNContext):
        pass

    # Exit a parse tree produced by heistParser#STMT_ASSIGN.
    def exitSTMT_ASSIGN(self, ctx:heistParser.STMT_ASSIGNContext):
        pass


    # Enter a parse tree produced by heistParser#STMT_ARRAY_ASSIGN.
    def enterSTMT_ARRAY_ASSIGN(self, ctx:heistParser.STMT_ARRAY_ASSIGNContext):
        pass

    # Exit a parse tree produced by heistParser#STMT_ARRAY_ASSIGN.
    def exitSTMT_ARRAY_ASSIGN(self, ctx:heistParser.STMT_ARRAY_ASSIGNContext):
        pass


    # Enter a parse tree produced by heistParser#STMT_ARRAY.
    def enterSTMT_ARRAY(self, ctx:heistParser.STMT_ARRAYContext):
        pass

    # Exit a parse tree produced by heistParser#STMT_ARRAY.
    def exitSTMT_ARRAY(self, ctx:heistParser.STMT_ARRAYContext):
        pass


    # Enter a parse tree produced by heistParser#STMT_ARRAY_VALUE.
    def enterSTMT_ARRAY_VALUE(self, ctx:heistParser.STMT_ARRAY_VALUEContext):
        pass

    # Exit a parse tree produced by heistParser#STMT_ARRAY_VALUE.
    def exitSTMT_ARRAY_VALUE(self, ctx:heistParser.STMT_ARRAY_VALUEContext):
        pass


    # Enter a parse tree produced by heistParser#STMT_ARRAY_UPPERBOUND.
    def enterSTMT_ARRAY_UPPERBOUND(self, ctx:heistParser.STMT_ARRAY_UPPERBOUNDContext):
        pass

    # Exit a parse tree produced by heistParser#STMT_ARRAY_UPPERBOUND.
    def exitSTMT_ARRAY_UPPERBOUND(self, ctx:heistParser.STMT_ARRAY_UPPERBOUNDContext):
        pass


    # Enter a parse tree produced by heistParser#STMT_ISARRAY.
    def enterSTMT_ISARRAY(self, ctx:heistParser.STMT_ISARRAYContext):
        pass

    # Exit a parse tree produced by heistParser#STMT_ISARRAY.
    def exitSTMT_ISARRAY(self, ctx:heistParser.STMT_ISARRAYContext):
        pass


    # Enter a parse tree produced by heistParser#STMT_ISFUNCTION.
    def enterSTMT_ISFUNCTION(self, ctx:heistParser.STMT_ISFUNCTIONContext):
        pass

    # Exit a parse tree produced by heistParser#STMT_ISFUNCTION.
    def exitSTMT_ISFUNCTION(self, ctx:heistParser.STMT_ISFUNCTIONContext):
        pass


    # Enter a parse tree produced by heistParser#STMT_ISNUMBER.
    def enterSTMT_ISNUMBER(self, ctx:heistParser.STMT_ISNUMBERContext):
        pass

    # Exit a parse tree produced by heistParser#STMT_ISNUMBER.
    def exitSTMT_ISNUMBER(self, ctx:heistParser.STMT_ISNUMBERContext):
        pass


    # Enter a parse tree produced by heistParser#STMT_ISINTEGER.
    def enterSTMT_ISINTEGER(self, ctx:heistParser.STMT_ISINTEGERContext):
        pass

    # Exit a parse tree produced by heistParser#STMT_ISINTEGER.
    def exitSTMT_ISINTEGER(self, ctx:heistParser.STMT_ISINTEGERContext):
        pass


    # Enter a parse tree produced by heistParser#STMT_ISDOUBLE.
    def enterSTMT_ISDOUBLE(self, ctx:heistParser.STMT_ISDOUBLEContext):
        pass

    # Exit a parse tree produced by heistParser#STMT_ISDOUBLE.
    def exitSTMT_ISDOUBLE(self, ctx:heistParser.STMT_ISDOUBLEContext):
        pass


    # Enter a parse tree produced by heistParser#STMT_ISSTRING.
    def enterSTMT_ISSTRING(self, ctx:heistParser.STMT_ISSTRINGContext):
        pass

    # Exit a parse tree produced by heistParser#STMT_ISSTRING.
    def exitSTMT_ISSTRING(self, ctx:heistParser.STMT_ISSTRINGContext):
        pass


    # Enter a parse tree produced by heistParser#STMT_ISBOOLEAN.
    def enterSTMT_ISBOOLEAN(self, ctx:heistParser.STMT_ISBOOLEANContext):
        pass

    # Exit a parse tree produced by heistParser#STMT_ISBOOLEAN.
    def exitSTMT_ISBOOLEAN(self, ctx:heistParser.STMT_ISBOOLEANContext):
        pass


    # Enter a parse tree produced by heistParser#STMT_ISNULL.
    def enterSTMT_ISNULL(self, ctx:heistParser.STMT_ISNULLContext):
        pass

    # Exit a parse tree produced by heistParser#STMT_ISNULL.
    def exitSTMT_ISNULL(self, ctx:heistParser.STMT_ISNULLContext):
        pass


    # Enter a parse tree produced by heistParser#STMT_ISEMPTY.
    def enterSTMT_ISEMPTY(self, ctx:heistParser.STMT_ISEMPTYContext):
        pass

    # Exit a parse tree produced by heistParser#STMT_ISEMPTY.
    def exitSTMT_ISEMPTY(self, ctx:heistParser.STMT_ISEMPTYContext):
        pass


    # Enter a parse tree produced by heistParser#function.
    def enterFunction(self, ctx:heistParser.FunctionContext):
        pass

    # Exit a parse tree produced by heistParser#function.
    def exitFunction(self, ctx:heistParser.FunctionContext):
        pass


    # Enter a parse tree produced by heistParser#expr_statement.
    def enterExpr_statement(self, ctx:heistParser.Expr_statementContext):
        pass

    # Exit a parse tree produced by heistParser#expr_statement.
    def exitExpr_statement(self, ctx:heistParser.Expr_statementContext):
        pass


    # Enter a parse tree produced by heistParser#ifblock.
    def enterIfblock(self, ctx:heistParser.IfblockContext):
        pass

    # Exit a parse tree produced by heistParser#ifblock.
    def exitIfblock(self, ctx:heistParser.IfblockContext):
        pass


    # Enter a parse tree produced by heistParser#elseblock.
    def enterElseblock(self, ctx:heistParser.ElseblockContext):
        pass

    # Exit a parse tree produced by heistParser#elseblock.
    def exitElseblock(self, ctx:heistParser.ElseblockContext):
        pass


    # Enter a parse tree produced by heistParser#STATEMENT.
    def enterSTATEMENT(self, ctx:heistParser.STATEMENTContext):
        pass

    # Exit a parse tree produced by heistParser#STATEMENT.
    def exitSTATEMENT(self, ctx:heistParser.STATEMENTContext):
        pass


    # Enter a parse tree produced by heistParser#MULOP.
    def enterMULOP(self, ctx:heistParser.MULOPContext):
        pass

    # Exit a parse tree produced by heistParser#MULOP.
    def exitMULOP(self, ctx:heistParser.MULOPContext):
        pass


    # Enter a parse tree produced by heistParser#NULL.
    def enterNULL(self, ctx:heistParser.NULLContext):
        pass

    # Exit a parse tree produced by heistParser#NULL.
    def exitNULL(self, ctx:heistParser.NULLContext):
        pass


    # Enter a parse tree produced by heistParser#UOPGRP.
    def enterUOPGRP(self, ctx:heistParser.UOPGRPContext):
        pass

    # Exit a parse tree produced by heistParser#UOPGRP.
    def exitUOPGRP(self, ctx:heistParser.UOPGRPContext):
        pass


    # Enter a parse tree produced by heistParser#VAR.
    def enterVAR(self, ctx:heistParser.VARContext):
        pass

    # Exit a parse tree produced by heistParser#VAR.
    def exitVAR(self, ctx:heistParser.VARContext):
        pass


    # Enter a parse tree produced by heistParser#CONCAT.
    def enterCONCAT(self, ctx:heistParser.CONCATContext):
        pass

    # Exit a parse tree produced by heistParser#CONCAT.
    def exitCONCAT(self, ctx:heistParser.CONCATContext):
        pass


    # Enter a parse tree produced by heistParser#PAREN.
    def enterPAREN(self, ctx:heistParser.PARENContext):
        pass

    # Exit a parse tree produced by heistParser#PAREN.
    def exitPAREN(self, ctx:heistParser.PARENContext):
        pass


    # Enter a parse tree produced by heistParser#INT.
    def enterINT(self, ctx:heistParser.INTContext):
        pass

    # Exit a parse tree produced by heistParser#INT.
    def exitINT(self, ctx:heistParser.INTContext):
        pass


    # Enter a parse tree produced by heistParser#UMINUS.
    def enterUMINUS(self, ctx:heistParser.UMINUSContext):
        pass

    # Exit a parse tree produced by heistParser#UMINUS.
    def exitUMINUS(self, ctx:heistParser.UMINUSContext):
        pass


    # Enter a parse tree produced by heistParser#ADDOP.
    def enterADDOP(self, ctx:heistParser.ADDOPContext):
        pass

    # Exit a parse tree produced by heistParser#ADDOP.
    def exitADDOP(self, ctx:heistParser.ADDOPContext):
        pass


    # Enter a parse tree produced by heistParser#BOOL.
    def enterBOOL(self, ctx:heistParser.BOOLContext):
        pass

    # Exit a parse tree produced by heistParser#BOOL.
    def exitBOOL(self, ctx:heistParser.BOOLContext):
        pass


    # Enter a parse tree produced by heistParser#CONST.
    def enterCONST(self, ctx:heistParser.CONSTContext):
        pass

    # Exit a parse tree produced by heistParser#CONST.
    def exitCONST(self, ctx:heistParser.CONSTContext):
        pass


    # Enter a parse tree produced by heistParser#STRING.
    def enterSTRING(self, ctx:heistParser.STRINGContext):
        pass

    # Exit a parse tree produced by heistParser#STRING.
    def exitSTRING(self, ctx:heistParser.STRINGContext):
        pass


    # Enter a parse tree produced by heistParser#POW.
    def enterPOW(self, ctx:heistParser.POWContext):
        pass

    # Exit a parse tree produced by heistParser#POW.
    def exitPOW(self, ctx:heistParser.POWContext):
        pass


    # Enter a parse tree produced by heistParser#DOUBLE.
    def enterDOUBLE(self, ctx:heistParser.DOUBLEContext):
        pass

    # Exit a parse tree produced by heistParser#DOUBLE.
    def exitDOUBLE(self, ctx:heistParser.DOUBLEContext):
        pass


    # Enter a parse tree produced by heistParser#RELOP.
    def enterRELOP(self, ctx:heistParser.RELOPContext):
        pass

    # Exit a parse tree produced by heistParser#RELOP.
    def exitRELOP(self, ctx:heistParser.RELOPContext):
        pass


    # Enter a parse tree produced by heistParser#null.
    def enterNull(self, ctx:heistParser.NullContext):
        pass

    # Exit a parse tree produced by heistParser#null.
    def exitNull(self, ctx:heistParser.NullContext):
        pass


    # Enter a parse tree produced by heistParser#const.
    def enterConst(self, ctx:heistParser.ConstContext):
        pass

    # Exit a parse tree produced by heistParser#const.
    def exitConst(self, ctx:heistParser.ConstContext):
        pass


    # Enter a parse tree produced by heistParser#uop.
    def enterUop(self, ctx:heistParser.UopContext):
        pass

    # Exit a parse tree produced by heistParser#uop.
    def exitUop(self, ctx:heistParser.UopContext):
        pass


    # Enter a parse tree produced by heistParser#addop.
    def enterAddop(self, ctx:heistParser.AddopContext):
        pass

    # Exit a parse tree produced by heistParser#addop.
    def exitAddop(self, ctx:heistParser.AddopContext):
        pass


    # Enter a parse tree produced by heistParser#mulop.
    def enterMulop(self, ctx:heistParser.MulopContext):
        pass

    # Exit a parse tree produced by heistParser#mulop.
    def exitMulop(self, ctx:heistParser.MulopContext):
        pass


    # Enter a parse tree produced by heistParser#paramlist.
    def enterParamlist(self, ctx:heistParser.ParamlistContext):
        pass

    # Exit a parse tree produced by heistParser#paramlist.
    def exitParamlist(self, ctx:heistParser.ParamlistContext):
        pass


    # Enter a parse tree produced by heistParser#param.
    def enterParam(self, ctx:heistParser.ParamContext):
        pass

    # Exit a parse tree produced by heistParser#param.
    def exitParam(self, ctx:heistParser.ParamContext):
        pass


    # Enter a parse tree produced by heistParser#arglist.
    def enterArglist(self, ctx:heistParser.ArglistContext):
        pass

    # Exit a parse tree produced by heistParser#arglist.
    def exitArglist(self, ctx:heistParser.ArglistContext):
        pass


    # Enter a parse tree produced by heistParser#relop.
    def enterRelop(self, ctx:heistParser.RelopContext):
        pass

    # Exit a parse tree produced by heistParser#relop.
    def exitRelop(self, ctx:heistParser.RelopContext):
        pass


    # Enter a parse tree produced by heistParser#arg.
    def enterArg(self, ctx:heistParser.ArgContext):
        pass

    # Exit a parse tree produced by heistParser#arg.
    def exitArg(self, ctx:heistParser.ArgContext):
        pass


