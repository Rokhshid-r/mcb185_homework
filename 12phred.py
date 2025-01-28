
import math
def char_to_prob(char:str):
    error_rate_num = ord(char) - 33
    error_rate = 10**(-1*error_rate_num/10)
    return error_rate
def prob_to_char(error_rate:float):
    num = -1 * math.log(error_rate, 10)
    ascii = 10 * math.ceil(num) + 33
    character = chr(int(ascii))
    return character
print(char_to_prob('A'))
print(char_to_prob('%'))
print(char_to_prob('!'))
print(prob_to_char(.001))