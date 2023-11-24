def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_sexy_primes_for_number(num):
    if num < 0:
        print("Please enter a positive number.")
        return
    
    sexy_primes = []
    if is_prime(num) and is_prime(num + 6):
        sexy_primes.append((num, num + 6))
    
    if is_prime(num - 6) and num - 6 > 0:
        sexy_primes.append((num - 6, num))
    
    return sexy_primes

# Get input from the user
user_input = int(input("Enter a number: "))
result = find_sexy_primes_for_number(user_input)

if result:
    print(f"Sexy prime number pairs for {user_input}:")
    print(result)
else:
    print(f"No sexy prime number pairs found for {user_input}.")
