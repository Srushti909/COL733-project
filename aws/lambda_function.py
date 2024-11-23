import math

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def lambda_handler(event, context):
    n = int(event.get('queryStringParameters', {}).get('n', 10))
    fib_num = fibonacci(n)
    return {
            'statusCode': 200,
            'body': {
                'fibonacci': fib_num,
                'is_prime': is_prime(fib_num)
            }
        }
    
