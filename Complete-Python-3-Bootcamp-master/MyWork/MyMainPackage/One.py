#One.py

def func():
    print("I'm a func in One.py")

print("TOP LEVEL IN ONE.PY")


if __name__ == '__main__':
    print("One.py is being run directly")
else:
    print("One.py has been imported")