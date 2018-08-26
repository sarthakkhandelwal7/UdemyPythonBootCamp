#Have the user enter a number and find all Prime Factors (if there are any) and display them.

class Factors:
    def __init__(self):
        self.count = 0
        self.prime_factors_list = []
    def returns_factors(self,num):
        """
            This function finds factor of the given number and pass that factor to 'returns_prime_factors()' function
            Variables: 
            'num' stores user input 
            'i' is used in for loop
            'prime' stores the prime numbers returned form 'returns_prime_factors()' function  
        """
        for i in range(1,num):
            if(num%i==0):
                prime=self.returns_prime_factors(i)
                if (prime!= None):
                    self.prime_factors_list.append(prime)
                
    def returns_prime_factors(self,factor):
        """
            Returns the prime factor by counting the number of factors of current factor of the number 
            Variables:
            'count' count number of divisors of factor 
        """
        if(factor%2!=0):
            for y in range(2,factor):
                if factor%y==0:
                    self.count+=1
                    break
            if self.count==0:
                return factor
                
        elif(factor==2):
            return factor
another = True
factors=Factors()
while another:
    number=int(input("Please enter a number:"))
    factors.returns_factors(number)
    print(f'Prime factors are {factors.prime_factors_list}')
    another=input("Do you wanna check another number press y or n:")
    if another[0].lower()=='y':
        another = True
    else:
        another = False
        