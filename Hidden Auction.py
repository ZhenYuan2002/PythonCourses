
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         _________
                       .-------------.
                      _______________
'''
#print(logo)
#print('Welcome to the secret auction programme!')
#name = input('What is your name: ')
#bid = float(input('Whats your bid?: $'))
#bidders_left = input('Is there other bidders left? Yes or no')
#if bidders_left == 'Yes':
#    #Restart the loop
#elif bidders_left == 'No':
#    #Prints the highest bidder

print(logo)
print('Welcome to the secret auction programme!')
name = input('What is your name? ')
bid = float(input('Whats you bid?: $'))
bidders_left = input('Are the other bidders left? Yes or No?')

bidder_list = [
    {'Name' : name,
     'Bid' : bid,
     },
]



for bidder in bidder_list:
    if bidders_left == 'Yes':
        def new_bidder (newname, newbid):
            newbidder = {}
            newname = input('What is your name? ')
            newbid = float(input('Whats your bid?'))
            newbidder['Name'] = newname
            newbidder['Bid'] = newbid
            bidder_list.append(newbidder)
        new_bidder(name,bid)
        bidders_left = input('Are there any other bidders left? Yes or No?')
    elif bidders_left == 'No':
        myMax = float(max(d['Bid'] for d in bidder_list))
#Stuck here, able to get max value, unable to get key of max value in a list of dictionaries

#Course Answer(Done on replit, clear() funtion does not work the same in Pycharm)
        from replit import clear
        from art import logo

        print(logo)

        bids = {}
        bidding_finished = False


        def find_highest_bidder(bidding_record):
            highest_bid = 0
            winner = ""
            # bidding_record = {"Angela": 123, "James": 321}
            for bidder in bidding_record:
                bid_amount = bidding_record[bidder]
                if bid_amount > highest_bid:
                    highest_bid = bid_amount
                    winner = bidder
            print(f"The winner is {winner} with a bid of ${highest_bid}")


        while not bidding_finished:
            name = input("What is your name?: ")
            price = int(input("What is your bid?: $"))
            bids[name] = price
            should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
            if should_continue == "no":
                bidding_finished = True
                find_highest_bidder(bids)
            elif should_continue == "yes":
                clear()





