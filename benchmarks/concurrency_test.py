import requests
from concurrent.futures import ThreadPoolExecutor

def test_concurrency(url, num_requests, function_name):
    def make_request():
        return requests.get(url, params={"n": 15})

    with ThreadPoolExecutor(max_workers=num_requests) as executor:
        responses = list(executor.map(make_request, range(num_requests)))
    
    print(f"Benchmarking {function_name} with {num_requests} concurrent requests:")
    for idx, response in enumerate(responses):
        print(f"Request {idx+1}: {response.status_code} -> {response.text}")

def benchmark_concurrency():
    aws_url = "<AWS_LAMBDA_URL>"  # Replace with AWS Lambda URL
    azure_url = "<AZURE_FUNCTION_URL>"  # Replace with Azure Function URL
    gcp_url = "<GCP_FUNCTION_URL>"  # Replace with GCP Cloud Function URL
    
    num_requests = 100  # You can adjust the number of concurrent requests
    
    print("Benchmarking AWS Lambda Concurrency...")
    test_concurrency(aws_url, num_requests, "AWS Lambda")

    print("Benchmarking Azure Function Concurrency...")
    test_concurrency(azure_url, num_requests, "Azure Function")

    print("Benchmarking GCP Cloud Function Concurrency...")
    test_concurrency(gcp_url, num_requests, "GCP Cloud Function")

if __name__ == "__main__":
    benchmark_concurrency()
