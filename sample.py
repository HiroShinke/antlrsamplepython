

from antlr4 import *

from dist.src.main.antlr4.com.github.hiroshinke.antlrsample.ArithmeticVisitor \
    import ArithmeticVisitor
from dist.src.main.antlr4.com.github.hiroshinke.antlrsample.ArithmeticParser \
    import ArithmeticParser
from dist.src.main.antlr4.com.github.hiroshinke.antlrsample.ArithmeticLexer \
    import ArithmeticLexer


class EvalVisitor(ArithmeticVisitor):

    def __init__(self):
        self.bindings = {}

    def visitFile_(self,ctx):
        eqs = ctx.stat()
        for e in eqs:
            ret = self.visit(e)
        return ret

    def visitExprStat(self,ctx):
        return self.visit(ctx.expression())

    def visitAssignStat(self,ctx):
        id = ctx.expression(0).getText()
        value = self.visit(ctx.expression(1));
        self.bindings[id] = value
        return value

    def visitParExpr(self,ctx):
        return self.visit(ctx.expression())

    def visitUnaryExpr(self,ctx):
        minuses = ctx.MINUS()
        sign = 1 if len(minuses) % 2 == 0 else -1
        v = self.visit(ctx.atom())
        return sign * v
    
    def visitAddtitiveExpr(self,ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        if ctx.PLUS() :
            return left + right
        elif ctx.MINUS() :
            return left - right
        else:
            raise Exception("somethin wrong")
        
    def visitPowExpr(self,ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left ** right

    def visitMultpricativeExpr(self,ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        if ctx.TIMES() :
            return left * right
        elif ctx.DIV() :
            return left / right
        else:
            raise Exception("somethin wrong")

    def visitAtom(self,ctx):
        
        if ctx1 := ctx.scientific():
            return float(ctx1.getText())
        if ctx2 := ctx.variable():
            id = ctx2.getText()
            if id in self.bindings:
                return self.bindings[id]
            else:
                return 0
        else:
            return 0


def runParser(str):
    visitor = EvalVisitor()    
    data =  InputStream(str)
    lexer = ArithmeticLexer(data)
    stream = CommonTokenStream(lexer)
    parser = ArithmeticParser(stream)
    tree = parser.file_()
    output = visitor.visit(tree)
    return output
    
def main():

    visitor = EvalVisitor()
    while True:
        str = input(">>> ")
        print(f"str = {str} {type(str)}")
        str += "\n"
        data =  InputStream(str)
        
        lexer = ArithmeticLexer(data)
        stream = CommonTokenStream(lexer)

        parser = ArithmeticParser(stream)
        tree = parser.file_()
        output = visitor.visit(tree)
        print(output)

if __name__ == "__main__":
    main()
    
