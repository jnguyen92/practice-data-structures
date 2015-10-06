__author__ = 'Nhuy'


from queue.queue import *

# Testing queue with hot potato
player_list = ["Sophia", "Emma", "Jackson", "Olivia", "Caden",
     "Aiden", "Liam", "Lucas", "Ava", "Noah",
     "Mason", "Mia", "Ethan", "Isabella", "Zoe",
     "Lily", "Emily", "Jacob", "Logan", "Madelyn"]

# hot potato with fixed n
# Parameters: a player list (array) and a fixed n (int)
# Returns: prints out who is eliminated and returns the winner
def hot_potato(player_list, n):
    # initialize the game
    q = Queue()
    for l in player_list:
        q.enqueue(l)
    counter = n

    # go around the circle, remove if counter is 0
    while q.size() != 1:
        hot_pot = q.dequeue()
        counter -= 1
        if counter == 0:
            print "%s has been eliminated" % hot_pot
            counter = n
        else:
            q.enqueue( hot_pot )

    # reveal the winner
    winner = q.dequeue()
    print "The last one standing is %s" % winner
    return winner

# run on data
hot_potato(player_list, 2)


import random
random.seed(1)

# hot potato with random n
# Parameters: player list (array)
# Returns: prints out who is eliminated and returns the winner
def hot_potato(player_list):
    # initialize the game
    q = Queue()
    for l in player_list:
        q.enqueue(l)
    counter = random.randint(1,100)

    # go around the circle, remove if counter is 0
    while q.size() != 1:
        hot_pot = q.dequeue()
        counter -= 1
        if counter == 0:
            print "%s has been eliminated" % hot_pot
            counter = random.randint(1,100)
        else:
            q.enqueue( hot_pot )

    # reveal the winner
    winner = q.dequeue()
    print "The last one standing is %s" % winner
    return winner

# run on data
hot_potato(player_list)