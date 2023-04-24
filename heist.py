from antlr4 import *
import antlr4 as antlr4
from heistLexer import heistLexer
from heistParser import heistParser
from heistVisitor import heistVisitor
import argparse
import math
import copy
import uuid
import os
import sys 

debug : bool = False


class myHeistVisitor(heistVisitor):

    def __init__(self) -> None:
        super().__init__()
        self._vars = {}
        self._returnVal = None
        self._funcCall = None

    def printError(self, msg):
        # print("Error:", msg)
        raise Exception( f"Exception: {msg}")

    def relCompare(self,lhs, rhs, reop):
      if(reop == "="):
         return lhs == rhs
      if(reop == ">"):
         return lhs > rhs
      if(reop == "<"):
         return lhs < rhs
      if(reop == ">="):
         return lhs >= rhs
      if(reop == "<="):
         return lhs <= rhs
      if(reop == "<>"):
         return lhs != rhs
      return False

    def visitLine(self, ctx:heistParser.LineContext):
                
        if debug:
            for line in ctx.getText().split():
                print ("> ", line )
            input()

        if self._returnVal is None:
            return self.visitChildren(ctx)
        else:
            if (hasattr(self._returnVal, 'varname')): #it is a function
                self._returnVal._env = self._vars.copy()
            
            return self._returnVal

    def visitSTMT_PRINT(self, ctx:heistParser.STMT_PRINTContext):
        val = self.visitChildren(ctx)

        if isinstance(val, str):
            print(val)
        elif isinstance(val, int):
            print(val)
        elif isinstance(val, float):
            print(val)
        elif isinstance(val, list):
            print(val)
        elif isinstance(val, bool):
            if val:
                print("#true")
            else:
                print("#false")
        elif isinstance(val,heistParser.STMT_FUNCContext):
            print(f"#function");
        elif isinstance(val,heistParser.FunctionContext):
            print(f"#function context");
        elif val is None:
            print("#null")
        else:
            self.printError("Cannot print non-string value.")
            return None

    def visitSTMT_IF(self, ctx:heistParser.STMT_IFContext):
        val = self.visit(ctx.express)

        if not isinstance(val, bool):
            self.printError("Expression is not a relational expression.")
            return None

        if val == True:
            self.visitChildren(ctx.ifblock())        

    def visitSTMT_IF_ELSE(self, ctx:heistParser.STMT_IF_ELSEContext):
        val = self.visit(ctx.express)

        if not isinstance(val, bool):
            self.printError("Expression is not a relational expression.")
            return None

        if val == True:
            self.visit(ctx.ifblock())
        else:
            self.visitChildren(ctx.elseblock())

    def visitSTMT_DO_WHILE(self, ctx:heistParser.STMT_DO_WHILEContext):
        val = self.visit(ctx.express)

        if not isinstance(val, bool):
            self.printError("Expression is not a relational expression.")
            return None

        while val and (self._returnVal is None):
            self.visitChildren(ctx)

            val = self.visit(ctx.express)

            if not isinstance(val, bool):
                self.printError("Expression is not a relational expression.")
                return None

    def visitSTMT_FOR(self, ctx:heistParser.STMT_FORContext):
        start = self.visit(ctx.start)
        end = self.visit(ctx.end)
        varname = ctx.varname.text

        # set step increment
        inc = 1 if ctx.stepcount == None else self.visit(ctx.stepcount)
        # flip relational operator if needed
        reop = ">=" if inc < 0 else "<="

        current = start

        while self.relCompare(current, end, reop) and (self._returnVal is None):
            self._vars[varname] = current
            self.visitChildren(ctx)
            current = current + inc

    def visitSTMT_FUNC(self, ctx:heistParser.STMT_FUNCContext):
        func = ctx
        func._env = copy.copy(self._vars)

        # assign uuid to anonymous function
        varname = uuid.uuid4() if func.varname is None else func.varname.text

        self._vars[varname] = func
        self._vars[varname]._env.update( copy.copy(self._vars) )
        self._vars[varname]._tcoFlag = self.callsSelf(func) and func.rec is not None
        return self._vars[varname]

    def callsSelf(self, func :heistParser.STMT_FUNCContext):
        func = copy.copy(func)

        if func.varname is None:
            return False

        funcName = func.varname.text

        stack = []
        stack.append(func.children)

        hasTailCall = False

        while stack:
            children = stack.pop()
            for child in children:
                if isinstance(child, heistParser.STMT_CALLContext):
                    if child.varname.text == funcName:
                        child.tailcall = True
                        hasTailCall = True
                if hasattr(child, 'children'):
                    stack.append(child.children)

        return hasTailCall

    def visitSTMT_RET(self, ctx:heistParser.STMT_RETContext):
        self._returnVal = self.visit(ctx.express)

    def visitSTMT_CALL_EXPR(self, ctx:heistParser.STMT_CALL_EXPRContext):
        func = self.visit(ctx.express)
        
        # get global environment
        vars = copy.copy(self._vars)
        # get function environment
        env = copy.copy(func._env)
        # override global with function environment
        vars.update(env)

        # append the calling vars to the environment
        if(hasattr(ctx.plist, 'param')): # has parameters?
            for i in range( len(ctx.plist.param()) ):
                argVal =  copy.copy( self.visit(ctx.plist.param(i).expr()) ) 
                varname = func.args.arg(i).getText()
                vars[varname] = argVal

        # create visitor
        callVisitor = myHeistVisitor()
        callVisitor._vars = vars
        callVisitor.visitChildren(func)

        return callVisitor._returnVal

    def visitSTMT_CALL(self, ctx:heistParser.STMT_CALLContext):
        funcName = ctx.varname.text

        if not funcName in self._vars:
            self.printError(f"Function '{funcName}' not found.")
            return None
        
        # array access
        if type(self._vars[funcName]) is list:
            pos = int(self.visit(ctx.paramlist().param(0)))
            return copy.copy(self._vars[funcName][pos])
        elif type(self._vars[funcName]) is int or type(self._vars[funcName]) is float or type(self._vars[funcName]) is bool:
            # self.printError(f"Cannot call non-function '{funcName}'.")
            return None
        else:
            # it is a function call
            func = self._vars[funcName]

            # get global environment
            vars = copy.copy(self._vars)
            # get function environment
            env = copy.copy(func._env)
            # override global with function environment
            vars.update(env)

            # tail call optimization
            if hasattr(ctx, 'tailcall') and func._tcoFlag:                
                if(hasattr(ctx.plist, 'param')): # has parameters?
                    for i in range( len(ctx.plist.param()) ):
                        argVal = copy.copy( self.visit(ctx.plist.param(i).expr()) ) 
                        varname = func.args.arg(i).getText()
                        vars[varname] = argVal
                        
                self._vars = vars
                return None

            # append the calling vars to the environment
            if(hasattr(ctx.plist, 'param')): # has parameters?
                for i in range( len(ctx.plist.param()) ):
                    argVal = copy.copy( self.visit(ctx.plist.param(i).expr()) ) 
                    varname = func.args.arg(i).getText()
                    vars[varname] = argVal

            if func._tcoFlag:
                callVisitor = myHeistVisitor()
                callVisitor._vars = vars

                while (callVisitor._returnVal is None):
                    callVisitor.visitChildren(func)

                return callVisitor._returnVal
            else:
                # create visitor
                callVisitor = myHeistVisitor()
                callVisitor._vars = vars
                callVisitor.visitChildren(self._vars[ctx.varname.text])

                return callVisitor._returnVal

    def isNumber(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def isInt(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False


    def visitSTMT_INPUT(self, ctx:heistParser.STMT_INPUTContext):
        varname = ctx.varname.text
        uinput = input()

        if uinput.lower() == 'true':
            self._vars[varname] = True
        elif uinput.lower() == 'false':
            self._vars[varname] = False
        elif self.isInt(uinput) and '.' not in uinput:
            self._vars[varname] = int(uinput)
        elif self.isNumber(uinput):
            self._vars[varname] = float(uinput)
        else:
            self._vars[varname] = str(uinput)

        return uinput

    def visitSTMT_ASSIGN(self, ctx:heistParser.STMT_ASSIGNContext):
        varname = ctx.varname.text
        varval = self.visitChildren(ctx)
        self._vars[varname] = copy.copy(varval)

    def visitSTMT_ARRAY_ASSIGN(self, ctx:heistParser.STMT_ARRAY_ASSIGNContext):
        pos = int(self.visit(ctx.num))
        varname = ctx.varname.text
        varval = self.visitChildren(ctx)
        self._vars[varname][pos] = copy.copy(varval)

    def visitSTMT_ARRAY(self, ctx:heistParser.STMT_ARRAYContext):
        varname = ctx.varname.text
        size = int(self.visit(ctx.num))
        self._vars[varname] = [0] * size

    def visitSTMT_ARRAY_VALUE(self, ctx:heistParser.STMT_ARRAY_VALUEContext):
        pos = int(self.visit(ctx.num))
        varname = ctx.varname.text
        return self._vars[varname][pos]

    def visitSTMT_ARRAY_UPPERBOUND(self, ctx:heistParser.STMT_ARRAY_UPPERBOUNDContext):
        varname = ctx.varname.text
        return len(self._vars[varname])-1

    # Visit a parse tree produced by heistParser#STMT_ISARRAY.
    def visitSTMT_ISARRAY(self, ctx:heistParser.STMT_ISARRAYContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#STMT_ISFUNCTION.
    def visitSTMT_ISFUNCTION(self, ctx:heistParser.STMT_ISFUNCTIONContext):
        val = self.visit(ctx.express)
        if not val in self._vars:
            return val is heistParser.STMT_FUNCContext
        else:
            return type(self._vars[val]) is heistParser.STMT_FUNCContext


    # Visit a parse tree produced by heistParser#STMT_ISNUMBER.
    def visitSTMT_ISNUMBER(self, ctx:heistParser.STMT_ISNUMBERContext):
        val = self.visit(ctx.express)
        return val is int or val is float
        
    # Visit a parse tree produced by heistParser#STMT_ISINTEGER.
    def visitSTMT_ISINTEGER(self, ctx:heistParser.STMT_ISINTEGERContext):
        return type(self.visit(ctx)) is int


    # Visit a parse tree produced by heistParser#STMT_ISDOUBLE.
    def visitSTMT_ISDOUBLE(self, ctx:heistParser.STMT_ISDOUBLEContext):
        return type(self.visit(ctx)) is float

    # Visit a parse tree produced by heistParser#STMT_ISSTRING.
    def visitSTMT_ISSTRING(self, ctx:heistParser.STMT_ISSTRINGContext):
        return type(self.visit(ctx.express)) is str


    # Visit a parse tree produced by heistParser#STMT_ISBOOLEAN.
    def visitSTMT_ISBOOLEAN(self, ctx:heistParser.STMT_ISBOOLEANContext):
        return type(self.visit(ctx.express)) is bool


    # Visit a parse tree produced by heistParser#STMT_ISNULL.
    def visitSTMT_ISNULL(self, ctx:heistParser.STMT_ISNULLContext):
        return type(self.visit(ctx.express)) is None

    def visitMULOP(self, ctx:heistParser.MULOPContext):
        op = ctx.mulop().getText()
        
        lhs = self.visit(ctx.lexpr)
        rhs = self.visit(ctx.rexpr)

        if isinstance(lhs, str) or isinstance(rhs, str):
            self.printError("Cannot perform arithmetic operation on string.")
            return None

        if op == "*":
            return lhs * rhs
        elif op == "/":
            return lhs / rhs
        elif op == "%" or "mod":
            return lhs % rhs

    # Visit a parse tree produced by heistParser#URELOP.
    def visitURELOP(self, ctx:heistParser.URELOPContext):
        op = ctx.urelop().getText()
        
        midnum = self.visit(ctx.midexpr)

        if op == "not":
            return not midnum

    def visitUOPGRP(self, ctx:heistParser.UOPGRPContext):
        op = ctx.uop().getText()
        num = self.visit(ctx.num)

        if isinstance(num, str):
            self.printError("Cannot perform unary operation on string.")
            return None

        if num is None:
            self.printError("Cannot perform unary operation on None.")
            return None

        if(op == "sin"):
            return math.sin(num)
        elif(op == "cos"):
            return math.cos(num)
        elif(op == "tan"):
            return math.tan(num)
        elif(op == "abs"):
            return abs(num)
        elif(op == "sqrt"):
            return math.sqrt(num)
        elif(op == "log2"):
            return math.log2(num)
        elif(op == "log" or op == "ln"):
            return math.log(num)
        elif(op == "log10"):
            return math.log10(num)
        elif(op == "str"):
            return str(num)
        elif(op == "factorial"):
            return math.factorial(num)
        elif(op == "int"):
            return int(num)
        elif(op == "tab"):
            return "\t" * int(num)
        elif(op == "float"):
            return float(num)
        return self.visit(ctx.num)

    def visitVAR(self, ctx:heistParser.VARContext):
        varname = ctx.VAR().getText()

        if varname in self._vars:
            return self._vars[varname]  
        else:   
            self.printError(f"Variable '{varname}' not found.")
            return None
    
    def visitCONCAT(self, ctx:heistParser.CONCATContext):
        lhs = self.visit(ctx.lexpr)
        rhs = self.visit(ctx.rexpr)

        if not isinstance(lhs, float) and not isinstance(lhs, int) and not isinstance(lhs, str) and lhs is not None:
            self.printError(f"Cannot concatenate non-string value '{lhs}'.")
            return None

        if not isinstance(rhs, float) and not isinstance(rhs, int) and not isinstance(rhs, str) and rhs is not None:
            self.printError(f"Cannot concatenate non-string value '{rhs}'.")
            return None

        return str(lhs) + str(rhs)

    def visitPAREN(self, ctx:heistParser.PARENContext):
        return self.visit(ctx.midexpr)

    def visitINT(self, ctx:heistParser.INTContext):
        return int(ctx.INT().getText())

    def visitUMINUS(self, ctx:heistParser.UMINUSContext):
        val = self.visit(ctx.num)

        if isinstance(val, str):    
            self.printError("Cannot perform unary operation on string.")
            return None

        return -1* val

    def visitADDOP(self, ctx:heistParser.ADDOPContext):
        op = ctx.addop().getText()

        lhs = self.visit(ctx.lexpr)
        rhs = self.visit(ctx.rexpr)

        if isinstance(lhs, str) or isinstance(rhs, str):
            self.printError("Cannot perform arithmetic operation on string.")
            return None

        if op == "+":
            return lhs + rhs
        elif op == "-":
            return lhs - rhs

    def visitBOOL(self, ctx:heistParser.BOOLContext):
        if ctx.BOOLEAN().getText() == "true":
            return True
        else:
            return False

    def visitCONST(self, ctx:heistParser.CONSTContext):
        sym = ctx.getText()

        if sym == 'pi':
            return math.pi
        elif sym == 'e':
            return math.e
        else:
            self.printError("Unknown constant: " + sym)
            return None 

    def visitSTRING(self, ctx:heistParser.STRINGContext):
        return str(ctx.getText()[1:-1])

    def visitPOW(self, ctx:heistParser.POWContext):
        
        lhs = self.visit(ctx.lexpr)
        rhs = self.visit(ctx.rexpr)

        if isinstance(lhs, str) or isinstance(rhs, str):
            self.printError("Cannot perform arithmetic operation on string.")
            return None

        return lhs ** rhs

    def visitDOUBLE(self, ctx:heistParser.DOUBLEContext):
        return float(ctx.DOUBLE().getText())

    
    # Visit a parse tree produced by heistParser#RELOP.
    def visitRELOP(self, ctx:heistParser.RELOPContext):
        op = ctx.relop().getText()

        lhs = self.visit(ctx.lexpr)
        rhs = self.visit(ctx.rexpr)

        if op == ">":
            return lhs > rhs
        elif op == "<":
            return lhs < rhs
        elif op == ">=":
            return lhs >= rhs
        elif op == "<=":
            return lhs <= rhs
        elif op == "and":
            return lhs and rhs
        elif op == "or":
            return lhs or rhs
        elif op == "xor":
            return lhs ^ rhs
        if op == "!=":
            return lhs != rhs
        elif op == "==":
            return lhs == rhs
        elif op =="equals": 
            return lhs == rhs
        elif op == "<>":
            return lhs != rhs
        elif op == "not":
            return not rhs
        else:
            self.printError("Unknown operator: " + op)
            return None 


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


    # Visit a parse tree produced by heistParser#arglist.
    def visitArglist(self, ctx:heistParser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#relop.
    def visitRelop(self, ctx:heistParser.RelopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by heistParser#arg.
    def visitArg(self, ctx:heistParser.ArgContext):
        return self.visitChildren(ctx)


# argument parsing
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("InputFile", help='inputfile')
arg_parser.add_argument("-debug","--Debug", default='off', choices=['on','off'], help="debug of course")
args = vars(arg_parser.parse_args())

# create a lexer and parser
debug = True if args["Debug"] == 'on' else False
input_stream = FileStream(args['InputFile'])
lexer = heistLexer(input_stream)
stream = CommonTokenStream(lexer)

parser = heistParser(stream)
tree = parser.program()

try:
    visitor = myHeistVisitor()
    visitor.visitProgram(tree)
except Exception as e:
    print(e)
