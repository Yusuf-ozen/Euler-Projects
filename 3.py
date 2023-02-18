## The prime factors of 13195 are 5, 7, 13 and 29.

## What is the largest prime factor of the number 600851475143 ?



prime_numbers_list = []

def prime_number(number):
    for i in range(2, number):
        state = False

        for j in range(2, i):

            if(i % j) == 0:
                state = True
        if state == False:
            

            if (number % i) == 0:
                #print(i)
                prime_numbers_list.append(i)

prime_number(600851475143)

print(max(prime_numbers_list))


