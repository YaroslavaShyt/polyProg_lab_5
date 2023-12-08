# Generated from C:/Users/User/Desktop/polyProg_lab_5/Expr.g by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#letter.
    def enterLetter(self, ctx:ExprParser.LetterContext):
        pass

    # Exit a parse tree produced by ExprParser#letter.
    def exitLetter(self, ctx:ExprParser.LetterContext):
        pass


    # Enter a parse tree produced by ExprParser#digit.
    def enterDigit(self, ctx:ExprParser.DigitContext):
        pass

    # Exit a parse tree produced by ExprParser#digit.
    def exitDigit(self, ctx:ExprParser.DigitContext):
        pass


    # Enter a parse tree produced by ExprParser#sign.
    def enterSign(self, ctx:ExprParser.SignContext):
        pass

    # Exit a parse tree produced by ExprParser#sign.
    def exitSign(self, ctx:ExprParser.SignContext):
        pass


    # Enter a parse tree produced by ExprParser#assignOp.
    def enterAssignOp(self, ctx:ExprParser.AssignOpContext):
        pass

    # Exit a parse tree produced by ExprParser#assignOp.
    def exitAssignOp(self, ctx:ExprParser.AssignOpContext):
        pass


    # Enter a parse tree produced by ExprParser#powerOp.
    def enterPowerOp(self, ctx:ExprParser.PowerOpContext):
        pass

    # Exit a parse tree produced by ExprParser#powerOp.
    def exitPowerOp(self, ctx:ExprParser.PowerOpContext):
        pass


    # Enter a parse tree produced by ExprParser#relOp.
    def enterRelOp(self, ctx:ExprParser.RelOpContext):
        pass

    # Exit a parse tree produced by ExprParser#relOp.
    def exitRelOp(self, ctx:ExprParser.RelOpContext):
        pass


    # Enter a parse tree produced by ExprParser#specialSign.
    def enterSpecialSign(self, ctx:ExprParser.SpecialSignContext):
        pass

    # Exit a parse tree produced by ExprParser#specialSign.
    def exitSpecialSign(self, ctx:ExprParser.SpecialSignContext):
        pass


    # Enter a parse tree produced by ExprParser#whiteSpace.
    def enterWhiteSpace(self, ctx:ExprParser.WhiteSpaceContext):
        pass

    # Exit a parse tree produced by ExprParser#whiteSpace.
    def exitWhiteSpace(self, ctx:ExprParser.WhiteSpaceContext):
        pass


    # Enter a parse tree produced by ExprParser#endOfLine.
    def enterEndOfLine(self, ctx:ExprParser.EndOfLineContext):
        pass

    # Exit a parse tree produced by ExprParser#endOfLine.
    def exitEndOfLine(self, ctx:ExprParser.EndOfLineContext):
        pass


    # Enter a parse tree produced by ExprParser#mathOp.
    def enterMathOp(self, ctx:ExprParser.MathOpContext):
        pass

    # Exit a parse tree produced by ExprParser#mathOp.
    def exitMathOp(self, ctx:ExprParser.MathOpContext):
        pass


    # Enter a parse tree produced by ExprParser#addOp.
    def enterAddOp(self, ctx:ExprParser.AddOpContext):
        pass

    # Exit a parse tree produced by ExprParser#addOp.
    def exitAddOp(self, ctx:ExprParser.AddOpContext):
        pass


    # Enter a parse tree produced by ExprParser#multOp.
    def enterMultOp(self, ctx:ExprParser.MultOpContext):
        pass

    # Exit a parse tree produced by ExprParser#multOp.
    def exitMultOp(self, ctx:ExprParser.MultOpContext):
        pass


    # Enter a parse tree produced by ExprParser#bracOp.
    def enterBracOp(self, ctx:ExprParser.BracOpContext):
        pass

    # Exit a parse tree produced by ExprParser#bracOp.
    def exitBracOp(self, ctx:ExprParser.BracOpContext):
        pass


    # Enter a parse tree produced by ExprParser#punctOp.
    def enterPunctOp(self, ctx:ExprParser.PunctOpContext):
        pass

    # Exit a parse tree produced by ExprParser#punctOp.
    def exitPunctOp(self, ctx:ExprParser.PunctOpContext):
        pass


    # Enter a parse tree produced by ExprParser#unsignInt.
    def enterUnsignInt(self, ctx:ExprParser.UnsignIntContext):
        pass

    # Exit a parse tree produced by ExprParser#unsignInt.
    def exitUnsignInt(self, ctx:ExprParser.UnsignIntContext):
        pass


    # Enter a parse tree produced by ExprParser#unsignDouble.
    def enterUnsignDouble(self, ctx:ExprParser.UnsignDoubleContext):
        pass

    # Exit a parse tree produced by ExprParser#unsignDouble.
    def exitUnsignDouble(self, ctx:ExprParser.UnsignDoubleContext):
        pass


    # Enter a parse tree produced by ExprParser#bool.
    def enterBool(self, ctx:ExprParser.BoolContext):
        pass

    # Exit a parse tree produced by ExprParser#bool.
    def exitBool(self, ctx:ExprParser.BoolContext):
        pass


    # Enter a parse tree produced by ExprParser#type.
    def enterType(self, ctx:ExprParser.TypeContext):
        pass

    # Exit a parse tree produced by ExprParser#type.
    def exitType(self, ctx:ExprParser.TypeContext):
        pass


    # Enter a parse tree produced by ExprParser#keywords.
    def enterKeywords(self, ctx:ExprParser.KeywordsContext):
        pass

    # Exit a parse tree produced by ExprParser#keywords.
    def exitKeywords(self, ctx:ExprParser.KeywordsContext):
        pass


    # Enter a parse tree produced by ExprParser#ident.
    def enterIdent(self, ctx:ExprParser.IdentContext):
        pass

    # Exit a parse tree produced by ExprParser#ident.
    def exitIdent(self, ctx:ExprParser.IdentContext):
        pass


    # Enter a parse tree produced by ExprParser#start.
    def enterStart(self, ctx:ExprParser.StartContext):
        pass

    # Exit a parse tree produced by ExprParser#start.
    def exitStart(self, ctx:ExprParser.StartContext):
        pass


    # Enter a parse tree produced by ExprParser#declarList.
    def enterDeclarList(self, ctx:ExprParser.DeclarListContext):
        pass

    # Exit a parse tree produced by ExprParser#declarList.
    def exitDeclarList(self, ctx:ExprParser.DeclarListContext):
        pass


    # Enter a parse tree produced by ExprParser#declaration.
    def enterDeclaration(self, ctx:ExprParser.DeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#declaration.
    def exitDeclaration(self, ctx:ExprParser.DeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#identList.
    def enterIdentList(self, ctx:ExprParser.IdentListContext):
        pass

    # Exit a parse tree produced by ExprParser#identList.
    def exitIdentList(self, ctx:ExprParser.IdentListContext):
        pass


    # Enter a parse tree produced by ExprParser#doSection.
    def enterDoSection(self, ctx:ExprParser.DoSectionContext):
        pass

    # Exit a parse tree produced by ExprParser#doSection.
    def exitDoSection(self, ctx:ExprParser.DoSectionContext):
        pass


    # Enter a parse tree produced by ExprParser#statementList.
    def enterStatementList(self, ctx:ExprParser.StatementListContext):
        pass

    # Exit a parse tree produced by ExprParser#statementList.
    def exitStatementList(self, ctx:ExprParser.StatementListContext):
        pass


    # Enter a parse tree produced by ExprParser#statement.
    def enterStatement(self, ctx:ExprParser.StatementContext):
        pass

    # Exit a parse tree produced by ExprParser#statement.
    def exitStatement(self, ctx:ExprParser.StatementContext):
        pass


    # Enter a parse tree produced by ExprParser#expression.
    def enterExpression(self, ctx:ExprParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#expression.
    def exitExpression(self, ctx:ExprParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#assign.
    def enterAssign(self, ctx:ExprParser.AssignContext):
        pass

    # Exit a parse tree produced by ExprParser#assign.
    def exitAssign(self, ctx:ExprParser.AssignContext):
        pass


    # Enter a parse tree produced by ExprParser#inp.
    def enterInp(self, ctx:ExprParser.InpContext):
        pass

    # Exit a parse tree produced by ExprParser#inp.
    def exitInp(self, ctx:ExprParser.InpContext):
        pass


    # Enter a parse tree produced by ExprParser#out.
    def enterOut(self, ctx:ExprParser.OutContext):
        pass

    # Exit a parse tree produced by ExprParser#out.
    def exitOut(self, ctx:ExprParser.OutContext):
        pass


    # Enter a parse tree produced by ExprParser#forStatement.
    def enterForStatement(self, ctx:ExprParser.ForStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#forStatement.
    def exitForStatement(self, ctx:ExprParser.ForStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:ExprParser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:ExprParser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#indExpr.
    def enterIndExpr(self, ctx:ExprParser.IndExprContext):
        pass

    # Exit a parse tree produced by ExprParser#indExpr.
    def exitIndExpr(self, ctx:ExprParser.IndExprContext):
        pass


    # Enter a parse tree produced by ExprParser#comment.
    def enterComment(self, ctx:ExprParser.CommentContext):
        pass

    # Exit a parse tree produced by ExprParser#comment.
    def exitComment(self, ctx:ExprParser.CommentContext):
        pass


    # Enter a parse tree produced by ExprParser#boolExpression.
    def enterBoolExpression(self, ctx:ExprParser.BoolExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#boolExpression.
    def exitBoolExpression(self, ctx:ExprParser.BoolExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#mathExpression.
    def enterMathExpression(self, ctx:ExprParser.MathExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#mathExpression.
    def exitMathExpression(self, ctx:ExprParser.MathExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#term.
    def enterTerm(self, ctx:ExprParser.TermContext):
        pass

    # Exit a parse tree produced by ExprParser#term.
    def exitTerm(self, ctx:ExprParser.TermContext):
        pass


    # Enter a parse tree produced by ExprParser#chunk.
    def enterChunk(self, ctx:ExprParser.ChunkContext):
        pass

    # Exit a parse tree produced by ExprParser#chunk.
    def exitChunk(self, ctx:ExprParser.ChunkContext):
        pass


    # Enter a parse tree produced by ExprParser#factor.
    def enterFactor(self, ctx:ExprParser.FactorContext):
        pass

    # Exit a parse tree produced by ExprParser#factor.
    def exitFactor(self, ctx:ExprParser.FactorContext):
        pass


    # Enter a parse tree produced by ExprParser#const.
    def enterConst(self, ctx:ExprParser.ConstContext):
        pass

    # Exit a parse tree produced by ExprParser#const.
    def exitConst(self, ctx:ExprParser.ConstContext):
        pass


    # Enter a parse tree produced by ExprParser#integer.
    def enterInteger(self, ctx:ExprParser.IntegerContext):
        pass

    # Exit a parse tree produced by ExprParser#integer.
    def exitInteger(self, ctx:ExprParser.IntegerContext):
        pass


    # Enter a parse tree produced by ExprParser#double.
    def enterDouble(self, ctx:ExprParser.DoubleContext):
        pass

    # Exit a parse tree produced by ExprParser#double.
    def exitDouble(self, ctx:ExprParser.DoubleContext):
        pass


    # Enter a parse tree produced by ExprParser#doBlock.
    def enterDoBlock(self, ctx:ExprParser.DoBlockContext):
        pass

    # Exit a parse tree produced by ExprParser#doBlock.
    def exitDoBlock(self, ctx:ExprParser.DoBlockContext):
        pass


    # Enter a parse tree produced by ExprParser#mathExpression1.
    def enterMathExpression1(self, ctx:ExprParser.MathExpression1Context):
        pass

    # Exit a parse tree produced by ExprParser#mathExpression1.
    def exitMathExpression1(self, ctx:ExprParser.MathExpression1Context):
        pass


    # Enter a parse tree produced by ExprParser#mathExpression2.
    def enterMathExpression2(self, ctx:ExprParser.MathExpression2Context):
        pass

    # Exit a parse tree produced by ExprParser#mathExpression2.
    def exitMathExpression2(self, ctx:ExprParser.MathExpression2Context):
        pass


    # Enter a parse tree produced by ExprParser#ifStatement.
    def enterIfStatement(self, ctx:ExprParser.IfStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#ifStatement.
    def exitIfStatement(self, ctx:ExprParser.IfStatementContext):
        pass



del ExprParser