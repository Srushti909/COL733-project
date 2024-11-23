import time
import requests
from concurrent.futures import ThreadPoolExecutor

def test_cold_start(url, function_name):
    print(f"Simulating cold start for {function_name}...")
    time.sleep(600) 
    start_time = time.time()
    response = requests.get(url, params={"n": 15})
    end_time = time.time()
    
    print(f"{function_name} Cold Start Response Time: {end_time - start_time} seconds")
    print(f"Response: {response.status_code} -> {response.text}")
    return response

def test_concurrency(url, num_requests, function_name):
    def make_request():
        return requests.get(url, params={"n": 15})

    with ThreadPoolExecutor(max_workers=num_requests) as executor:
        responses = list(executor.map(make_request, range(num_requests)))
    
    print(f"Benchmarking {function_name} with {num_requests} concurrent requests:")
    for idx, response in enumerate(responses):
        print(f"Request {idx+1}: {response.status_code} -> {response.text}")

def test_memory_usage(url, payload_size, function_name):
    data = {"data": "A" * payload_size}
    print(f"Benchmarking {function_name} with payload size: {payload_size} bytes")
    response = requests.post(url, json=data)

    print(f"Response: {response.status_code} -> {response.text}")
    return response

def benchmark_all():
    aws_url = "<AWS_LAMBDA_URL>"  # Replace with AWS Lambda URL
    azure_url = "<AZURE_FUNCTION_URL>"  # Replace with Azure Function URL
    gcp_url = "<GCP_FUNCTION_URL>"  # Replace with GCP Cloud Function URL
    
    num_requests = 100  # Adjust the number of concurrent requests
    payload_size = 1048576  # 1MB payload, adjust as needed
    
    # Cold Start Benchmark
    print("Benchmarking AWS Lambda Cold Start...")
    test_cold_start(aws_url, "AWS Lambda")
    print("Benchmarking Azure Function Cold Start...")
    test_cold_start(azure_url, "Azure Function")
    print("Benchmarking GCP Cloud Function Cold Start...")
    test_cold_start(gcp_url, "GCP Cloud Function")
    
    # Concurrency Benchmark
    print("Benchmarking AWS Lambda Concurrency...")
    test_concurrency(aws_url, num_requests, "AWS Lambda")
    print("Benchmarking Azure Function Concurrency...")
    test_concurrency(azure_url, num_requests, "Azure Function")
    print("Benchmarking GCP Cloud Function Concurrency...")
    test_concurrency(gcp_url, num_requests, "GCP Cloud Function")
    
    # Memory Usage Benchmark
    print("Benchmarking AWS Lambda Memory Usage...")
    test_memory_usage(aws_url, payload_size, "AWS Lambda")
    print("Benchmarking Azure Function Memory Usage...")
    test_memory_usage(azure_url, payload_size, "Azure Function")
    print("Benchmarking GCP Cloud Function Memory Usage...")
    test_memory_usage(gcp_url, payload_size, "GCP Cloud Function")

if __name__ == "__main__":
    benchmark_all()
