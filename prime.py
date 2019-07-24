#!/usr/bin/env python3
# coding: utf-8class Solution(object):
    """"Find the first prime above a specific number, whose 
    separate digit sums are also prime.
    """    def is_prime(self, number):
        """Check whether the given number is a prime."""
        for num in range(2, int(number ** 0.5) + 1):
            if number % num == 0:
                return False
        return True    def find_primes(self, number):
        """Find the prime above the given number."""
        while True:
            sum_of_digits = sum(map(int, str(number)))
            if self.is_prime(number)and 
                self.is_prime(sum_of_digits):
                return number
            number += 1
def main():
    """The main routine."""
    number = int(input().strip())
    result = Solution()
    print("The first prime after %s is %d" % 
        (number, result.find_primes(number)))if __name__ == '__main__':
    main()
