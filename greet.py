def greet(name):
    """Call stack"""
    print("Hello, " + name + "!")
    greet2(name)
    print("Getting ready to say bye...")
    bye()
    
def greet2(name):
    print("How are you, " + name + "?")
    
def bye():
    print("Ok bye!")

# Example usage:
my_name = "Jun"
greet(my_name)