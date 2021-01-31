def processSpam(someFruit):
    pos = len(someFruit) - 1
    print(pos)
    someFruit.insert(pos,'and')
    #return 'apples, bananas, tofu, and cats'
    
    return someFruit


    
fruits =['apples', 'bananas', 'tofu', 'cats']


output = processSpam(fruits)
print(output)
print(fruits)
fruits =['apples', 'bananas', 'tofu', 'cats', 'dogs']


output = processSpam(fruits)
print(output)
print(fruits)
