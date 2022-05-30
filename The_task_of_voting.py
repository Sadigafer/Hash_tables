# The task of voting

voted = {}
def check(name):
    if voted.get(name):
        print ('Гони его')
    else:
        voted[name] = True
        print ('Позволь проголосовать')

# Checking

check("Сергей")