import sys  #import function

randomList = ['a', 0, 2] #class list
for entry in randomList:    #Loop in randomList member
    try:
        print("The entry is ",entry)
        r = 1/int(entry)
        break               #end loop if success
    except:
        print("Oops!", sys.exc_info()[0], "occured.") #show error msg + use function import
        print("Next entry")
        print()
print("The reciprocal of", entry, "is", r)      #show success msg and result
