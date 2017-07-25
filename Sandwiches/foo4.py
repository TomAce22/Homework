while True:
    userSandwich = input("How many sandwiches can you eat? ")
    brotherSandwich = userSandwich +1
    print "My brother can eat ", (brotherSandwich), " sandwiches, therefore you lose!"
    if (userSandwich > 4):
        print "Although, you will get sick if you eat that many sandwiches!"
    if (userSandwich < 0):
        break
print "Even a baby can eat 0 sandwiches!"
        