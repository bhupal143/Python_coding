def spam():
    global eggs
    eggs = 'Spam' #This is global
    print(eggs)
def bacon():
    eggs = 'bacon'  #This is a locals
    print(eggs)
def ham():
    print(eggs)

eggs = 43  # This is global
ham()
print(eggs)
spam()
print(eggs)
bacon()
print(eggs)
ham()
print(eggs)
