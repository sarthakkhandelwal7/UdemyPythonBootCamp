import pdb
class BinaryDecimalConverter:
    def __init__(self):
        self.binary_form = 0
        self.decimal_form = 0
    
    def convert_to_binary(self):
        self.binary_form = 0
        """
            Variables:
            'power' to store power of 2
            'binary_form' to store conversion
        """
        number = int(input("Enter number for conversion:"))
        for x in range(0,number):
            if (2 ** x > number):
                power = x-1
                break

            elif (2 ** x == number):
                power = x
                break
        divident = number
        while power>=0:
            self.binary_form+=(10**power)*(int(divident/(2**power)))
            
            divident = divident%2**power
            power-=1
    
    def convert_to_decimal(self):
        self.decimal_form = 0
        """
            Variables:
            'decimal_form' to store conversion
            'rou' to solve the problem of decimal
        """
        binary_number = int(input("Enter binary number"))
        bi = binary_number
        power = len(str(binary_number))
        for i in range(0,power):
            bi/=10
            rou = round((bi-int(bi))*10)
            self.decimal_form += (2**i)*(rou)           
            bi = int(bi)
ask = 'y'
converter=BinaryDecimalConverter()
while ask=='y':
    print("Welcome")
    print("To convert decimal to binary press 1")
    print("To convert binary to decimal press 2")
    try:
        choice = int(input("Enter your choice:"))
    except:
        print("Enter correct choice")
        ask = input("Want to converter again y/n:")
    else:
         if choice==1:
            converter.convert_to_binary()
            print(converter.binary_form)
         elif(choice!=1 and choice!=2):
            print('Enter correct choice')
         else:
            converter.convert_to_decimal()
            print(converter.decimal_form)
    ask = input("Want to converter again y/n:")