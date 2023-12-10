# Generated from C:/Users/User/Desktop/polyProg_lab_5/polyProg/Poly.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PolyParser import PolyParser
else:
    from PolyParser import PolyParser

# This class defines a complete listener for a parse tree produced by PolyParser.
class PolyListener(ParseTreeListener):

    # Enter a parse tree produced by PolyParser#program.
    def enterProgram(self, ctx:PolyParser.ProgramContext):
        pass

    # Exit a parse tree produced by PolyParser#program.
    def exitProgram(self, ctx:PolyParser.ProgramContext):
        pass


    # Enter a parse tree produced by PolyParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:PolyParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by PolyParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:PolyParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by PolyParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:PolyParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by PolyParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:PolyParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by PolyParser#ifSt.
    def enterIfSt(self, ctx:PolyParser.IfStContext):
        pass

    # Exit a parse tree produced by PolyParser#ifSt.
    def exitIfSt(self, ctx:PolyParser.IfStContext):
        pass


    # Enter a parse tree produced by PolyParser#whileSt.
    def enterWhileSt(self, ctx:PolyParser.WhileStContext):
        pass

    # Exit a parse tree produced by PolyParser#whileSt.
    def exitWhileSt(self, ctx:PolyParser.WhileStContext):
        pass


    # Enter a parse tree produced by PolyParser#forStat.
    def enterForStat(self, ctx:PolyParser.ForStatContext):
        pass

    # Exit a parse tree produced by PolyParser#forStat.
    def exitForStat(self, ctx:PolyParser.ForStatContext):
        pass


    # Enter a parse tree produced by PolyParser#doWhileSt.
    def enterDoWhileSt(self, ctx:PolyParser.DoWhileStContext):
        pass

    # Exit a parse tree produced by PolyParser#doWhileSt.
    def exitDoWhileSt(self, ctx:PolyParser.DoWhileStContext):
        pass


    # Enter a parse tree produced by PolyParser#printSt.
    def enterPrintSt(self, ctx:PolyParser.PrintStContext):
        pass

    # Exit a parse tree produced by PolyParser#printSt.
    def exitPrintSt(self, ctx:PolyParser.PrintStContext):
        pass


    # Enter a parse tree produced by PolyParser#readlineSt.
    def enterReadlineSt(self, ctx:PolyParser.ReadlineStContext):
        pass

    # Exit a parse tree produced by PolyParser#readlineSt.
    def exitReadlineSt(self, ctx:PolyParser.ReadlineStContext):
        pass


    # Enter a parse tree produced by PolyParser#emptyStatement.
    def enterEmptyStatement(self, ctx:PolyParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by PolyParser#emptyStatement.
    def exitEmptyStatement(self, ctx:PolyParser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by PolyParser#assignment.
    def enterAssignment(self, ctx:PolyParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PolyParser#assignment.
    def exitAssignment(self, ctx:PolyParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PolyParser#ifStatement.
    def enterIfStatement(self, ctx:PolyParser.IfStatementContext):
        pass

    # Exit a parse tree produced by PolyParser#ifStatement.
    def exitIfStatement(self, ctx:PolyParser.IfStatementContext):
        pass


    # Enter a parse tree produced by PolyParser#whileStatement.
    def enterWhileStatement(self, ctx:PolyParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by PolyParser#whileStatement.
    def exitWhileStatement(self, ctx:PolyParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by PolyParser#forStatement.
    def enterForStatement(self, ctx:PolyParser.ForStatementContext):
        pass

    # Exit a parse tree produced by PolyParser#forStatement.
    def exitForStatement(self, ctx:PolyParser.ForStatementContext):
        pass


    # Enter a parse tree produced by PolyParser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:PolyParser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by PolyParser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:PolyParser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by PolyParser#printStatement.
    def enterPrintStatement(self, ctx:PolyParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by PolyParser#printStatement.
    def exitPrintStatement(self, ctx:PolyParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by PolyParser#printArgument.
    def enterPrintArgument(self, ctx:PolyParser.PrintArgumentContext):
        pass

    # Exit a parse tree produced by PolyParser#printArgument.
    def exitPrintArgument(self, ctx:PolyParser.PrintArgumentContext):
        pass


    # Enter a parse tree produced by PolyParser#readlineStatement.
    def enterReadlineStatement(self, ctx:PolyParser.ReadlineStatementContext):
        pass

    # Exit a parse tree produced by PolyParser#readlineStatement.
    def exitReadlineStatement(self, ctx:PolyParser.ReadlineStatementContext):
        pass


    # Enter a parse tree produced by PolyParser#type.
    def enterType(self, ctx:PolyParser.TypeContext):
        pass

    # Exit a parse tree produced by PolyParser#type.
    def exitType(self, ctx:PolyParser.TypeContext):
        pass


    # Enter a parse tree produced by PolyParser#expression.
    def enterExpression(self, ctx:PolyParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PolyParser#expression.
    def exitExpression(self, ctx:PolyParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PolyParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:PolyParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by PolyParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:PolyParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by PolyParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:PolyParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by PolyParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:PolyParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by PolyParser#powerExpression.
    def enterPowerExpression(self, ctx:PolyParser.PowerExpressionContext):
        pass

    # Exit a parse tree produced by PolyParser#powerExpression.
    def exitPowerExpression(self, ctx:PolyParser.PowerExpressionContext):
        pass


    # Enter a parse tree produced by PolyParser#unaryExpression.
    def enterUnaryExpression(self, ctx:PolyParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by PolyParser#unaryExpression.
    def exitUnaryExpression(self, ctx:PolyParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by PolyParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:PolyParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by PolyParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:PolyParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by PolyParser#boolVal.
    def enterBoolVal(self, ctx:PolyParser.BoolValContext):
        pass

    # Exit a parse tree produced by PolyParser#boolVal.
    def exitBoolVal(self, ctx:PolyParser.BoolValContext):
        pass


    # Enter a parse tree produced by PolyParser#boolExpression.
    def enterBoolExpression(self, ctx:PolyParser.BoolExpressionContext):
        pass

    # Exit a parse tree produced by PolyParser#boolExpression.
    def exitBoolExpression(self, ctx:PolyParser.BoolExpressionContext):
        pass



del PolyParser