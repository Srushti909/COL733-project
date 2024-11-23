import requests

def test_memory_usage(url, payload_size, function_name):
    data = {"data": "A" * payload_size}
    print(f"Benchmarking {function_name} with payload size: {payload_size} bytes")
    response = requests.post(url, json=data)

    print(f"Response: {response.status_code} -> {response.text}")
    return response

def benchmark_memory_usage():
    aws_url = "<AWS_LAMBDA_URL>" 
    azure_url = "<AZURE_FUNCTION_URL>" 
    gcp_url = "<GCP_FUNCTION_URL>" 
    
    payload_size = 1048576  # 1MB payload, adjust as needed
    
    print("Benchmarking AWS Lambda Memory Usage...")
    test_memory_usage(aws_url, payload_size, "AWS Lambda")

    print("Benchmarking Azure Function Memory Usage...")
    test_memory_usage(azure_url, payload_size, "Azure Function")

    print("Benchmarking GCP Cloud Function Memory Usage...")
    test_memory_usage(gcp_url, payload_size, "GCP Cloud Function")

if __name__ == "__main__":
    benchmark_memory_usage()
