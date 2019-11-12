
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
---> execution time and time complexity does not always have a predictable
     outcome. Sometimes a time complexity that is better does not always
     run faster than a time complexity that is worst; for every case.
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
            self.limit = 50

        self.limit = limit

    #Returns the curent limit
    def get_limit(self):
        return self.limit




        # Calculates the prime numbers less than the limit.
        # Time complexity: O(n)
        """
        It Loads in numbers less than the limit 
        and then removes all multiples of i*prime[j] which are not primes. 
        This runs with a Time complexity of O(n).
        What is interesting is that although it has a time complexity 
        of O(n), it's run time is still more than the run time of the
        first algorithm; when checking the values of [500,5000,50000,100000].
        This is most likely is because for values of 'n' where 'n' is the
        limit (value inputted to check for primes, less than itself). For values 
        of 'n' that are not very large, we don't see a significant difference
        in run time between the two algorithms. Although the time complexity
        of O(n) is better than the time complexity of O(n*log(log(n))). 
        For these test cases this algorithm performs worst than the 
        first algorithm. This could also because it has to load two arrays
        isprime and SPF up to 'n'(MAXSIZE) times before loading another array
        'prime' with the actual answers. O(n) but the steps invloved makes it take longer
        than the algortihm that has a time complexity of O(n * log(log(n))).
        """
    def sieveofEratosthenes2(self):
        MAX_SIZE = self.limit

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
                # put i into prime[] list
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
        elapsed_time = (time.time() - start)
        outfile.write("%9d %24s %50s \n"
              %(numbers_to_check[position], len(result), str(elapsed_time)))
    elif numbers_to_check[position] == 500:
        pass
        # seive2.set_limit(numbers_to_check[position])
        # start = time.time()
        # result = seive2.sieveofEratosthenes2()
        # elapsed_time = (time.time() - start)
        # outfile.write("Prime less than: %2d ,  Number of Primes: %2s ,  Time taken: %4s \n\n"
        #       %(numbers_to_check[position], len(result), str(elapsed_time)))
        # outfile.write("All Primes of 500: \n\n"+ print_contents(result) +"\n")

    start = 0
    elapsed_time = 0

outfile.close()

