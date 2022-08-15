import sys

def get_minput(prompt):
    print(prompt)
    _in_ = sys.stdin.read().split("\n")
    return _in_

if __name__ == "__main__":
    get_minput("copy n paste")