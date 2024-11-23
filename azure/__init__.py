import logging
from .function_app import fibonacci, is_prime
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    n = int(req.params.get('n', 10))
    fib_num = fibonacci(n)
    return func.HttpResponse(
        f"Fibonacci: {fib_num}, Is Prime: {is_prime(fib_num)}",
        status_code=200
    )
