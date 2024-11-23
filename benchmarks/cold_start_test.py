import time
import requests

def test_cold_start(url, function_name):
    print(f"Simulating cold start for {function_name}...")
    time.sleep(600)
    start_time = time.time()
    response = requests.get(url, params={"n": 15})
    end_time = time.time()
    
    print(f"{function_name} Cold Start Response Time: {end_time - start_time} seconds")
    print(f"Response: {response.status_code} -> {response.text}")
    return response

def benchmark_cold_start():
    aws_url = "<AWS_LAMBDA_URL>"  # Replace with AWS Lambda URL
    azure_url = "<AZURE_FUNCTION_URL>"  # Replace with Azure Function URL
    gcp_url = "<GCP_FUNCTION_URL>"  # Replace with GCP Cloud Function URL
    
    print("Benchmarking AWS Lambda Cold Start...")
    test_cold_start(aws_url, "AWS Lambda")

    print("Benchmarking Azure Function Cold Start...")
    test_cold_start(azure_url, "Azure Function")

    print("Benchmarking GCP Cloud Function Cold Start...")
    test_cold_start(gcp_url, "GCP Cloud Function")

if __name__ == "__main__":
    benchmark_cold_start()
