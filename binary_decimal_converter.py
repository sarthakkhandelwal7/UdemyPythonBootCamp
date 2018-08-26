class BinaryDecimalConverter:
    def __init_(self):
        self.binary_form = 0
        self.decimal_form = 0
    
    def convert_to_binary(self):
        """
            Variables:
            'power' to store power of 2
            'binary_form' to store conversion
        """
        number = int(input("Enter number for conversion:"))
        for i in range(number):
            if (2 ** i > 0):
                power = i-1
                break

            elif (2 ** i == number):
                self.convert_to_binary(i.number)
                break
        divident = number
        while power<=0:
            self.binary_form+=(10**power)*(int(divident/(2**power)))
            divident = divident%2**power
            power-=1
    
    def convert_to_decimal(self):
        """
            Variables:
            'decimal_form' to store conversion
        """
        binary_number = int(input("Enter binary number"))
        bi = binary_number
        power = len(binary_number)
        for i in range(power):
            bi/=10
            self.decimal_form += (2**i)*((bi-int(bi))*10)
            bi = int(bi)
ask = 'y'
calculator=BinaryDecimalConverter()
while ask=='y':
    print("Welcome")
    print("To convert decimal to binary press 1")
    print("To convert binary to decimal press 2")
    try:
        choice = int(input("Enter your choice:"))
    except:
        print("Enter correct choice")
        ask = input("Want to converter again y/n:")
        continue
    if choice==1:
        calculator.gets_power_of_two()
        print(calculator.binary_form)
    else:
        calculator.convert_to_binary()
        print(calculator.decimal_form)
    ask = input("Want to converter again y/n:")