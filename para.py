# match ()

signal = {"}": "{", "]": "[", ")": "("}
signal_l, signal_r = signal.values(), signal.keys()
# type drive design 
##s: string
##c: char
## val lr : s -> bool = <func>

# test drive development
## "" -> True
## "{" -> False
## "{[] ()}" -> True
## "{[(])}" -> False

def lr(s):
    stack = []
    for c in s:
        if c in signal_l:
            stack.append(c)
        elif c in signal_r:
            if  stack and stack[-1] == signal[c]:
                stack.pop()
            else:
                return False
    return not stack

if __name__ == "__main__":
    print(lr("{[] ()}"))
    print(lr("{[(])}"))

    print(lr(""))
            


