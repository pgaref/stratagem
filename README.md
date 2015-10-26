# Stratagem Engineering Programming Exercise 

## Subject
You have been tasked with building part of a simple online auction system which will allow users to bid on items for sale.

Provide a bid tracker interface and concrete implementation with the following functionality:

* Record a user's bid on an item
* Get the current winning bid for an item
* Get all the bids for an item
* Get all the items on which a user has bid

You are not required to implement a GUI (or CLI) or persistent storage. 
Please implement this in Python and include test coverage.

You may use any appropriate libraries to help, but do not include the library files in your submission.

## Remarks
How the auction works:

* One round per item.
* Bids are done randomly.

## Requirements

Only one external library was used : `fake-factory`

Run `pip install -r requirements.txt` to install it.

## Instructions

Run `python main.py` and follow the instructions to participate to the auction.

Run `python -m unittest discover` to see if all tests have passed.
