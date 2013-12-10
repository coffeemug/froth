
import sys

stack = []

def add():
    stack.append(stack.pop() + stack.pop())
def sub():
    i = stack.pop()
    j = stack.pop()
    stack.append(j - i)
def mul():
    stack.append(stack.pop() * stack.pop())
def div():
    i = stack.pop()
    j = stack.pop()
    stack.append(j / i)
def _apply():
    symbols[stack.pop()]()
def branch():
    i = stack.pop()
    j = stack.pop()
    k = stack.pop()
    if k != 0:
        stack.append(j)
    else:
        stack.append(i)
def pop():
    stack.pop()
def dup():
    i = stack.pop()
    stack.append(i)
    stack.append(i)

symbols = { 'add': add, 'sub': sub, 'mul': mul, 'div': div, 'apply': _apply, 'if': branch, 'pop': pop, 'dup': dup }

def _eval(word):
    # perhaps it's an int
    try:
        stack.append(int(word))
        return
    except ValueError:
        pass
    # nope. must be a symbol
    if word.startswith("'"):
        stack.append(word[1:])
    else:
        symbols[word]()

def repl():
    # evaluate whitespace separated words read from stdin
    while True:
        print '> ',
        line = sys.stdin.readline()
        if line == '':
            break
        words = line.split()
        for word in words:
            _eval(word)
        print stack

def main():
    repl()

if __name__ == "__main__":
    main()
