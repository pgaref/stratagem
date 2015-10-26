__author__ = 'MACSAMI'

import random
import time
from models.item import *
from models.user import *
from faker import Factory

def data(number_of_users):
    #get a list of users with a name randomly generated
    fake = Factory.create()
    users = []
    items = [Item('Table'),Item('Chair'),Item('Desk')]

    for i in range(number_of_users):
        users.append(User(fake.name()))

    print('%s have been created.\n' %number_of_users)

    for i in range(number_of_users):
        s = 'User %s is %s'
        print s %(i, users[i].name)
        print('---')
    return users, items

def round(users, item):
    for user in users:
        i = random_bid()
        user.make_bid(i, item)
        print '%s is bidding %s for %s.\n' %(user.name, i, item.name)
    print('---')
    return item.get_winning_bid()

def random_bid():
    return random.randint(0,9)

if __name__ == '__main__':

    number_of_users = input('How many users do you want for the auction? ')

    users, items = data(number_of_users)

    n = 1

    for item in items:
        #do one round for each item and get max bid
        r = round(users, item)
        print 'The winning bid for %s is %s by %s.\n' %(item.name, r.value, r.user.name)
        time.sleep(2)

    print 'End of auction'





