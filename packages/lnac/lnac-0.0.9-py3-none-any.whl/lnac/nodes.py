''' Node implementaitons used for parsing '''

import os
import platform

class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.uscore = '_' if platform.system() is 'Windows' else ''

    def __str__(self):
        return '{}{}{}'.format(self.name, '\n', str(self.value))

class Expression(Node):
    def __init__(self, name, value):
        Node.__init__(self, 'EXPRESSION', value)

class Constant(Expression):
    def __init__(self, number):
        self.number = number
        Expression.__init__(self, 'CONSTANT', self.number)

    def __str__(self):
        return 'movl\t${}, %eax'.format(str(self.number))

class UnaryOp(Expression):
    def __init__(self, tok, expression):
        self.tok = tok
        self.expression = expression
        Expression.__init__(self, 'UNARY', self.tok)

    def __str__(self):
        operations = {
            '-' : '{}{}neg\t\t%eax'.format(str(self.expression), '\n'),
            '!' : '{0}{1}cmpl\t$0, %eax{1}movl\t$0, %eax{1}sete\t%al'.format(str(self.expression), '\n')
        }
        return operations.get(self.tok, 'INVALID UNARY OPERATION')

class BinaryOp(Expression):
    def __init__(self, exprLeft, tok, exprRight):
        self.tok = tok
        self.left = exprLeft
        self.right = exprRight
        Expression.__init__(self, 'BINARY', self.tok)

    def __str__(self):
        operations = {
            '+' : '',
            '*' : '',
            '/' : '',
        }
        return operations.get(self.tok, 'INVALID BINARY OPERATION')

class Return(Node):
    def __init__(self, constant):
        self.constant = constant
        Node.__init__(self, 'RETURN', self.constant)

    def __str__(self):
        return '{}{}ret'.format(str(self.constant), '\n')

class Function(Node):
    def __init__(self, name, returns):
        self.returns = returns
        Node.__init__(self, name, self.returns)

    def __str__(self):
        return '{}{}:{}{}'.format(self.uscore, self.name, '\n', str(self.returns))

class Program(Node):
    def __init__(self, name, function):
        self.function = function
        Node.__init__(self, name, self.function)

    def __str__(self):
        return '.globl {}{}{}{}'.format(self.uscore, self.function.name, '\n', str(self.function))
