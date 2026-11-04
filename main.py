import os  # F401: unused import


def main():
    unused_value = 123  # F841: unused local variable
    try:
        print("Testing broken lint")
    except:  # E722: bare except
        pass


if __name__ == "__main__":
    main()
