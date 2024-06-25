import requests

BASE_URL = "http://127.0.0.1:8000"

# Test probability endpoint with n and m parameters
def test_probability(n, m):
    endpoint = f"{BASE_URL}/probability"
    params = {"n": n, "m": m}
    
    response = requests.get(endpoint, params=params)

    print(f"Request sent to {endpoint} with params {params}.\n Response: {response.text}")
    

if __name__ == "__main__":
    # Perform tests
    test_probability(2, 2)
    test_probability(3, 5)
    test_probability('a', 53) # invalid entry
    test_probability(1, 7) # test zero probability case 
    test_probability(10, 53) # test a largish number 
    
    
    

    
