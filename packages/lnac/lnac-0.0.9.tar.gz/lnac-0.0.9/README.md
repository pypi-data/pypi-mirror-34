# LnaC

### A toy functional language compiler written in Python.

---

LnaC is a toy functional language compiler written in Python 3 that supports limited program generation.

For some sample programs, see the [demos directory](demos).

## Quickstart

To install LnaC:
```
pip3 install lnac
```

To create, compile, and run an example program:
```c
$ nano return0.lna
$ less return0.lna

main : int
main =
    => 0

$ lnac return0.lna
$ ./return0 && $?
True
```

## Implementation

### Lexer
The LnaC lexer is primarily implemented in [`lexer.py`](lnac/lexer.py). Additionally, [`tokens.py`](lnac/tokens.py) contains definitions of the token classes used in the lexer and instances of recognized keyword and symbol tokens.

### Parser
The LnaC parser is implemented in [`parser/parser.py`](lnac/parser/) and creates an abstract syntax tree of nodes defined in [`tree/nodes.py`](lnac/tree/nodes.py).

### Assembly
LnaC writes out an intermediary assembly file that gcc then generates an executable from. This assembly file is written following the AT&T assembly syntax and is deleted following a successful compilation.

## References
- Writing a C Compiler - https://norasandler.com/2017/11/29/Write-a-Compiler.html
- ShivyC - https://github.com/ShivamSarodia/ShivyC