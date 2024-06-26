import requests
import time

SERVER_URL = "http://127.0.0.1:8000"

# Utility function to measure request time
def measure_request_time(endpoint, params):
    start_time = time.time()
    response = requests.get(endpoint, params=params)
    end_time = time.time()
    return response, end_time - start_time

# Test probability endpoint with n and m parameters
def test_probability(n, m):
    endpoint = f"{SERVER_URL}/probability"
    params = {"n": n, "m": m}
    
    response = requests.get(endpoint, params=params)
    _, duration = measure_request_time(endpoint, params)

    print(f"Probability request with params {params} took {duration:.1f} seconds.\n Response: {response.text}")
    

if __name__ == "__main__":
    # Perform tests
    test_probability(2, 2)
    test_probability(3, 5)
    test_probability('a', 53) # invalid entry
    test_probability(1, 7) # test zero probability case 
    test_probability(10, 53) # test a largish number 
    test_probability(30, 123) # test a largish number
    
    
    

    
