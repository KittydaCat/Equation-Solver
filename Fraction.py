# create a class that can store a fraction and do operations to it

class Fraction:

    def __init__(self, numerator, denominator):

        self.numer = numerator
        self.denom = denominator
        self.__name__ = "Fraction"

    def __repr__(self):
        # returns the fraction in simplified form "1 1/2"

        if self.numer >= 0:
            return str(self.numer//self.denom) + ' ' + str(self.numer % self.denom)+'/'+str(self.denom)

        if self.numer < 0:
            return '-' + str(abs(self.numer)//self.denom) + ' ' + str(abs(self.numer) % self.denom)+'/'+str(self.denom)

    def __invert__(self):

        self.numer, self.denom = self.denom, self.numer

        return self

    def __add__(self, other):
        # adds two fractions together

        # check if the input is also a fraction class
        if type(other) is not Fraction:

            # raise an error
            raise TypeError("Only Fractions allowed. You added" + str(type(other)))

        # returns a fraction class that is the two fractions added together
        return Fraction(self.numer * other.denom + other.numer * self.denom, self.denom * other.denom).simplify()

    def __sub__(self, other):
        # subtracts two fractions

        # check if the input is also a fraction class
        if type(other) is not Fraction:
            # raise an error
            raise TypeError("Only Fractions allowed. You subtracted" + str(type(other)))

        # returns a fraction class that is the two fractions subtracted
        return Fraction(self.numer * other.denom - other.numer * self.denom, self.denom * other.denom).simplify()

    def __mul__(self, other):
        # multiply two fractions together

        # check if the input is also a fraction class
        if type(other) is not Fraction:
            # raise an error
            raise TypeError("Only Fractions allowed. You multiplied" + str(type(other)))

        # returns a fraction class that is the two fractions together
        return Fraction(self.numer * other.numer, self.denom * other.denom).simplify()

    def __truediv__(self, other):
        # multiply two fractions together

        # check if the input is also a fraction class
        if type(other) is not Fraction:
            # raise an error
            raise TypeError("Only Fractions allowed. You divided" + str(type(other)))

        # returns a fraction class that is the two fractions together
        return Fraction(self.denom * other.numer, self.numer * other.denom).simplify()

    def __pow__(self, other, modulo=None):

        return Fraction(self.numer ^ (other.numer//other.denom), self.denom ^ (other.numer//other.denom))

    def transform(self, multiplyer):
        # changes the numerator and denominator by a value multiplyer
        self.numer = int(self.numer * multiplyer)
        self.denom = int(self.denom * multiplyer)
        return

    def simplify(self):

        # simplify the fraction as much as possible

        # check if the numerator or denominator is larger

        # if the numerator is larger use the denominator as the max
        if abs(self.numer) > abs(self.denom):

            primes = [True for _ in range(abs(self.denom)+1)]

        # if the denominator is larger or they are the same size
        else:

            primes = [True for _ in range(abs(self.numer)+1)]

        # sieve the primes

        # loop thru the primes
        p = 1
        while p*p <= len(primes):

            # check if the number is a prime
            if primes[p]:

                # loop thru the multiples of the prime
                for non_prime in range(p*2, len(primes), p):

                    # change the multiples of the prime to be not true
                    primes[non_prime-1] = False

            p += 1

        # change 1 and 0 to be not prime
        primes[0] = False
        primes[1] = False

        # change primes from a list of T and F to a list of primes

        listprimes = []
        for p in range(len(primes)):
            if primes[p]:
                listprimes.append(p)

        primes = listprimes

        # simplify the fraction using the primes list
        # loop until all the primes are gone
        while len(primes):

            # check if the biggest prime goes into the numer and denom
            if not self.numer % primes[-1] and not self.denom % primes[-1]:

                # simplify the fraction
                self.transform(1/primes[-1])

            # if the numer and denom arn't divisible by the prime
            else:
                # delete the last prime
                primes.pop(-1)

        return self


def tofraction(numer):
    
    numer = float(numer)

    denom = 1
    
    while not int(numer) == numer:

        numer *= 10
        denom *= 10

    return Fraction(int(numer), int(denom)).simplify()


# runs a test case
if __name__ == '__main__':

    a = Fraction(64, 128)
    print(a.simplify())
