# I like to call this game, ‘A Fork in the Road: Decisions”.  I wanted to be able to have the game ask the user their name and to use that name throughout the game and through
# all the decisions that you can make. I was able to have a couple decisions to choose from at the start of the game and a few options for each decision.














                                                                              # A Fork in the Road: Decisions

person = raw_input('Enter your name: ')
print 'Greetings', person,'!'

print 'You come to an onimous fork in the road. Do you travel left or right?'
road = raw_input('> ')

if road == "left":
    print 'Left was a good choice', person, ', after traveling down the road for awhile, you come across a fallen tree, blocking your path...'
    print 'what do you want to do?'
    print '#1 Spend the day clearing the road for you and others'
    print '#2 Clear just enough for your to fit through'
    print '#3 Travel back to the fork and head the other direction'

    tree = raw_input('> ')

    if tree == "1":
        print 'You spend the day chopping the sizable tree down, clearing the path for everybody to come'

    if tree == "2":
        print 'You clear just enough space to fit through, leaving the majority of the tree blocking the road'
        
    if tree == "3":
        print 'You decide to leave the tree for another traveler and head back to the fork to try your luck in the other direction'

if road == "right":
    print person, ', right might not be the best choice, you stare down the road, but something seems off...'
    print 'Your sense of adventure is pulling you to the right, but it is close to night. How would you like to proceed?'
    print '#1. Wait until the following morning'
    print '#2. Be couragous and start down the road right now'
    print '#3. Play it really safe and wait for another traveler to accompany you'
    couragous = raw_input('> ')

    if couragous == "1":
        print 'The morning sun brings along the sense of comfort, you continue on your journy with a new found motivation'
        
    if couragous == "2":
        print 'You feel like your courage made you make a hasty decision, you feel like somebody... or something... is watching you'
        
    if couragous == "3":
        print 'No other travelers show. Now it is to late into the night, so you wait until the morning anyways'


