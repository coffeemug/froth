
import sys

stack = []

def add():
    stack.append(stack.pop() + stack.pop())

symbols = { 'add': add }

def _eval(word):
    # perhaps it's an int
    try:
        stack.append(int(word))
        return
    except ValueError:
        pass
    # nope. must be a function
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
