__author__ = 'arya'
def main():
    script_status = False
    test = False
    try:
        if not test:
            print("return False")
            #return False

        print("main")
    except Exception as e:
        print("Exception")
    finally:
        print("finally")

#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# if __name__ == "__main__":
#     main()

X = None
Y = 0
if not (X or Y):
        print("No")
