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
import math


class Find_Primes1:

    #Member variable
    limit = 2

    #Default Constructor
    def __init__(self):
        self.limit = 50

    #Sets the limit.
    def set_limit(self,limit):
        if limit < 2:
            limit = 50

        self.limit = limit

    #Returns the current limit.
    def get_limit(self):
        return self.limit

    # #Calculates the prime numbers less than the limit.
    #     # def sieveofEratosthenes1(self):
    #     #     primes = []
    #     #     for i in range(2, self.limit + 1):
    #     #         primes.append(i)
    #     #
    #     #     i = 2
    #     #     # from 2 to sqrt(limit)
    #     #     while (i <= int(math.sqrt(self.limit))):
    #     #         # if i is in list
    #     #         # then we gotta delete its multiples
    #     #         if i in primes:
    #     #             # j will give multiples of i,
    #     #             # starting from 2*i
    #     #             for j in range(i * 2, self.limit + 1, i):
    #     #                 if j in primes:
    #     #                     # deleting the multiple if found in list
    #     #                     primes.remove(j)
    #     #         i = i + 1
    #     #     return primes


    # Calculates the prime numbers less than the limit.
    #  Time complexity O(n)
    def sieveofEratosthenes1(self):
        MAX_SIZE = 1000001

        # isPrime[] : isPrime[i] is true if
        #             number is prime
        # prime[] : stores all prime number
        #           less than N
        # SPF[] that store smallest prime
        # factor of number [for ex : smallest
        # prime factor of '8' and '16'
        # is '2' so we put SPF[8] = 2 ,
        # SPF[16] = 2 ]
        isprime = [True] * MAX_SIZE
        prime = []
        SPF = [None] * (MAX_SIZE)

        # 0 and 1 are not prime
        isprime[0] = isprime[1] = False

        # Fill rest of the entries
        for i in range(2, self.limit):

            # If isPrime[i] == True then i is
            # prime number
            if isprime[i] == True:
                # put i into prime[] vector
                prime.append(i)

                # A prime number is its own smallest
                # prime factor
                SPF[i] = i

                # Remove all multiples of i*prime[j]
            # which are not prime by making is
            # Prime[i * prime[j]] = false and put
            # smallest prime factor of i*Prime[j]
            # as prime[j] [ for exp :let i = 5 , j = 0 ,
            # prime[j] = 2 [ i*prime[j] = 10 ]
            # so smallest prime factor of '10' is '2'
            # that is prime[j] ] this loop run only one
            # time for number which are not prime
            j = 0
            while (j < len(prime) and i * prime[j] < self.limit and
                   prime[j] <= SPF[i]):
                isprime[i * prime[j]] = False

                # put smallest prime factor of i*prime[j]
                SPF[i * prime[j]] = prime[j]

                j += 1

        return prime


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


seive1 = Find_Primes1()

results = ""

outfile = open_output_file()


outfile.write("Name: Joachim Isaac:\n")
outfile.write("Program 3: Sieve of Eratosthenes and Complexity \n")
outfile.write("Complexity analysis 1, Prog1:\n\n")

for position in range(len(numbers_to_check)):
    if numbers_to_check[position] != 500:
        # pass
        if position == 1:
            outfile.write("%8s %24s %39s \n"
                  %("Primes less than", "Number of Primes", "Time taken"))
        seive1.set_limit(numbers_to_check[position])
        start = time.time()
        result = seive1.sieveofEratosthenes1()
        elapsed_time_fl = (time.time() - start)
        outfile.write("%9d %24s %50s \n"
              %(numbers_to_check[position], len(result), str(elapsed_time_fl)))
    elif numbers_to_check[position] == 500:
        pass
        # seive1.set_limit(numbers_to_check[position])
        # start = time.time()
        # result = seive1.sieveofEratosthenes1()
        # elapsed_time_fl = (time.time() - start)
        # outfile.write("Prime less than: %2d ,  Number of Primes: %2s ,  Time taken: %4s \n\n"
        #       %(numbers_to_check[position],len(result), str(elapsed_time_fl)))
        # outfile.write("All Primes of 500: \n\n"+ print_contents(result) +"\n")


    start = 0
    elapsed_time_fl = 0

#Closes the file
outfile.close()
