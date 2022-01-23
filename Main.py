from art import logo
import os


# define our clear function
def clear():
    # for windows the name is 'nt'
    if os.name == 'nt':
        _ = os.system('cls')

    # and for mac and linux, the os.name is 'posix'
    # else:
    #     _ = system('clear')


# Then, whenever you want to clear the screen, just use this clear function as:
# clear()
print(logo)
choice = False
bidders_dic = {}


def highest_bidder(dic):
    highest_bid = 0
    bidders_name = ""
    for key in dic:
        if dic[key] > highest_bid:
            highest_bid = dic[key]
            bidders_name = key
    print(bidders_name, "raises the highest bid of", highest_bid)


while not choice:
    bidders_name = input("Enter the Bidder's name: ")
    bidders_price = int(input("Enter Bidder's price: $"))
    bidders_dic[bidders_name] = bidders_price
    c = input("Enter more bidder's, type 'yes' or 'no': ")
    if c == 'no':
        choice = True
        highest_bidder(bidders_dic)
    elif c == 'yes':
        clear()
