# How much change do you have? 
Figure it out with the coin machine! practice.n0l3ptr.com 8889

### Part 1: Write a program that can solve one round of the change machine
The change machine gives a dollar amount and asks for the correct number of various bills 
needed to reach the right amount of money. It was a simple process to write a program that
grabs this number an computes the correct number of each bill, then submits those numbers to
the server. The code is put in a loop because it took a few hundred
correct runs before the server would give up the flag.

	import telnetlib

	HOST = "practice.n0l3ptr.com"
	PORT = 8889
	t = telnetlib.Telnet(HOST, PORT)
	t.open(HOST, PORT)

	n = int(input("How many loops? "))
	for i in range(0,n):
	  print t.read_until("$")
	  dollars = t.read_until(".")
	  cents = t.read_until("\n")

	  dollars = dollars[:-1]  # gets rid of ending .
	  dollars = int(dollars)  # convert string to int
	  cents = int(cents)

	  amounts = [10000, 5000, 1000, 500, 100, 50, 20, 10, 5, 1, 50, 25, 10, 5, 1]

	  for i in range(0, 15):
		  t.read_until(": ")
			if i < 10:  # For Dollar Amounts
			  bills = dollars / amounts[i]
			  dollars = dollars % amounts[i]
			else:  			# For Cent Amounts
			  bills = cents / amounts[i]
			  cents = cents % amounts[i]
		  bills = str(bills)      # write() only accepts strings
			t.write(bills + "\n")   # newline needed to finish user input

	 print t.read_until("correct!")


### Part 2: Get the flag!
Getting the flag took over 500 consecutive runs of the program! Definitely not something you'd
want to do by hand!

	flag{5t4cks_0n_5t4cks}
