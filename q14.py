# Initialize variables
num = 2
primes = []

# Loop through numbers from 2 to 100 (inclusive)
while num <= 100:
    # Initialize flag for prime check
    is_prime = True
    
    # Check if num is divisible by any number from 2 to num - 1
    for divisor in range(2, num):
        if num % divisor == 0:
            # Set flag to False if num is not prime
            is_prime = False
            break
    
    # If num is prime, add it to the list of primes
    if is_prime:
        primes.append(num)
    
    # Move on to the next number
    num += 1

# Print the list of prime numbers
print(primes)

