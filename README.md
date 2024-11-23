# COL733-project

# Serverless Showdown: Comparing Google, AWS, and Azure for Performance, Reliability, and Cost

## Overview
This project demonstrates how to deploy a Fibonacci number generator and prime checker across AWS Lambda, Azure Functions, and Google Cloud Functions.

### Features
- Compute the N-th Fibonacci number.
- Check if the Fibonacci number is a prime number.
- Fully serverless deployment.

---

## Deployment Instructions

### AWS Lambda
1. Install the AWS CLI.
2. Set up your IAM role and replace `<ROLE_ARN>` in `aws/deploy.sh`.
3. Run:
   ```bash
   cd aws
   bash deploy.sh
4. Use the generated API endpoint to test.

### Azure Functions

1. Install Azure Functions Core Tools using:
    ```bash
    pip install -r requirements.txt
2. ```bash
    cd azure
    func init
    func new --template "HTTP trigger" --name FibonacciFunction
    func azure functionapp publish <YOUR_FUNCTION_APP_NAME>

### Google Cloud Functions

1. Install the GCP SDK and Flask:
    ```bash
    pip install -r requirements.txt
2. Authenticate using gcloud auth login:
    ```bash
    gcloud auth login
3. Run:
    ```bash
    cd gcp
    bash deploy.sh
4. Use the generated API endpoint to test.

## Benchmarking Guide for AWS Lambda, Azure Functions, and GCP Cloud Functions

### Overview
The **benchmarks** directory contains benchmarking scripts to test the performance of AWS Lambda, Azure Functions, and GCP Cloud Functions in terms of:

- **Cold Start Time**
- **Concurrency Handling**
- **Memory Usage**

### Requirements

- Python 3.x
- `requests` library: Install it using the following:
  
  ```bash
  pip install requests
- Make sure to replace the placeholder URLs (<AWS_LAMBDA_URL>, <AZURE_FUNCTION_URL>,            <GCP_FUNCTION_URL>) with the actual function URLs for each cloud platform.
- Run:
    ```bash
    cd benchmarks
    python cold_start_test.py
    python concurrency_test.py
    python memory_usage_test.py
- **Optional**: Run all benchmark tests in sequence using the combined **benchmark.py** script:
    ```bash
    python benchmark.py

