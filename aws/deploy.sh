#!/bin/bash

# Replace with the ARN (Amazon Resource Name) of an IAM role

zip function.zip lambda_function.py
aws lambda create-function \
    --function-name FibonacciPrimeChecker \
    --runtime python3.9 \
    --role <ROLE_ARN> \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://function.zip
