voted = {}

def check_voter(name):
    """Check voter using hash table"""
    if voted.get(name):
        print("Kick them out!")
    else:
        voted[name] = True
        print("Let them vote!")

check_voter("tom")
check_voter("mike")
check_voter("mike")