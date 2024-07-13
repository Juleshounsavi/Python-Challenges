#A function that takes in a decimal number and returns its equivalent binary representation.

def Decimal_to_binary(x):
    if x >= 1024 or x < 0:
        raise ValueError("The decimal number must be between 0 and 1023 inclusive.")
    #Convert the decimal number to binary and remove the '0b' prefix
    binary_representation = bin(x)[2:]
    #Pad the binary representation with leading zeros to make it 10 digits long
    binary_representation = binary_representation.zfill(10)

    return binary_representation

print(Decimal_to_binary(2))
