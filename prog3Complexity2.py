
"""
Name: Joachim Isaac.
Course: CS 2433-101, Fall 19, Dr. Stringfellow.

Purpose: This program assess my ability to translate an algorithm
into code and my ability to improve the complexity of the algorithm.


Important points:(Things I learned):
--> you cannot have both a default constructor
    and a parameterized constructor in a python class.
--> pass is a null operation -- when it is executed, nothing happens.
    It is useful as a placeholder when a statement is required syntactically,
    but no code needs to be executed.
"""


import time

class Find_Primes2:

    #Member variable limit
    limit = 0

    #Default constructor
    def __init__(self):
        self.limit = 50

    #sets the limit.
    def set_limit(self,limit):
        if limit < 2:
            limit = 50

        self.limit = limit

    #Returns the curent limit
    def get_limit(self):
        return self.limit

    #Calculates the prime numbers less than the limit.
    #Time complexity: O(n*log(log(n)))
    def sieveofEratosthenes2(self):
        # Create a boolean array "prime[0..n]" and initialize
        # all entries it as true. A value in prime[i] will
        # finally be false if i is Not a prime, else true.
        result = []
        prime = [True for i in range(self.limit + 1)]
        p = 2
        while (p * p <= self.limit):

            # If prime[p] is not changed, then it is a prime
            if (prime[p] == True):

                # Update all multiples of p
                for i in range(p * 2, self.limit + 1, p):
                    prime[i] = False
            p += 1
        prime[0] = False
        prime[1] = False
        # Print all prime numbers
        for p in range(self.limit + 1):
            if prime[p]:
                result.append(p)
        return result



#Function which prints the Prime numbers
#from and array into a string. They are
#spaced out nicely.
def print_contents(array):
    result = ""
    line = ""
    counter = 20
    for number in array:
        line += str(number) + "  "
        counter = counter - 1
        if counter == 0:
            line += "\n"
            result += line
            line = ""
            counter = 20

    return result


#Reads in input file name and returns a file object.
def open_output_file():
    outfile = input("Please enter output file name: \n")
    file = open(outfile,'w')
    return file





numbers_to_check = [500,5000,50000,100000]

seive2 = Find_Primes2()

results = ""

outfile = open_output_file()



outfile.write("Name: Joachim Isaac:\n")
outfile.write("Program 3: Sieve of Eratosthenes and Complexity\n")
outfile.write("Complexity analysis 2, Prog2:\n\n")

for position in range(len(numbers_to_check)):
    if numbers_to_check[position] != 500:
        # pass
        if position == 1:
            outfile.write("%8s %24s %39s \n"%("Primes less than", "Number of Primes", "Time taken"))
        seive2.set_limit(numbers_to_check[position])
        start = time.time()
        result = seive2.sieveofEratosthenes2()
        elapsed_time_fl = (time.time() - start)
        outfile.write("%9d %24s %50s \n"
              %(numbers_to_check[position], len(result), str(elapsed_time_fl)))
    elif numbers_to_check[position] == 500:
        pass
        # seive1.set_limit(numbers_to_check[position])
        # start = time.time()
        # result = seive1.sieveofEratosthenes2()
        # elapsed_time_fl = (time.time() - start)
        # outfile.write("Prime less than: %2d ,  Number of Primes: %2s ,  Time taken: %4s \n\n"
        #       %(numbers_to_check[position], len(result), str(elapsed_time_fl)))
        # outfile.write("All Primes of 500: \n\n"+ print_contents(result) +"\n")

    start = 0
    elapsed_time_fl = 0

outfile.close()

