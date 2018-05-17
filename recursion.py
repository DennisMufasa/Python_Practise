def HelloWorld(count):
    if count > 0:
        print("Hello World")
        HelloWorld(count - 1)


HelloWorld(5)

