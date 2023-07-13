'''
>>> JAAR
>>> 07/12/2023
>>> Practicing Fundamentals Program 5
>>> Version 1
'''

'''
>>> Results in a program that prints all numbers from 1 to 100, but for multiples of three, print "Fizz" instead, and for multiples of five, print "Buzz." For numbers that are multiples of both three and five, print "FizzBuzz."
'''

def main() :
    print('Fizz Buzz program!! Activate:')
    for n in range(1, 101) :
        punctuation = ', ' if n < 100 else '.'
        if n % 3 != 0 and n % 5 != 0 :
            print(n, end = punctuation)
        elif n % 5 != 0 and n % 3 == 0 :
            print('Fizz', end = punctuation)
        elif n % 3 != 0 and n % 5 == 0 :
            print('Buzz', end = punctuation)
        else :
            print('FizzBuzz', end = punctuation)

if __name__ == '__main__' :
    main()