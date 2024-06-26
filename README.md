# Simple-Probability-App

This repo contains a web-service that, given two non-negative integers $n$ and $m$, responds with the probability to obtain the sum $m$ when rolling $n$ six faced dice(s). 

---

For a given $n$ roll(s), the total number of outcomes is proportional to $6^n$ and then the problem reduces to obtaining the number of ways that sum $m$ can be attained by $n$ dice rolls. For this purpose, a dynamic programming approach that builds up solutions to sub-problems (sums achievable with fewer dice) to solve the larger problem (sums achievable with n dice) is used inspired by the following [approach](https://www.geeksforgeeks.org/count-ways-to-obtain-given-sum-by-repeated-throws-of-a-dice/). 

- `sum_probability.py` computes the desired probability using this approach which can be tested against some simple known cases of the problem using `test_probability.py`. To speed up the response to requests, `sum_probability.py` is decorated with caching functionality. 
- API is implemented in `prob_app.py` using `FastAPI` library which is a simple application with one endpoint that responds using `sum_probability.py` for a given Query parameters $n$ and $m$. The service takes 5 seconds to respond each request and shutsdown gracefully when receiving a SIGTERM. For the ease of simulating the receipt of the sigterm, the service returns PID of the process upon initiation. Then the SIGTERM signal can be sent by either keyboard interruption `Ctrl + C` in the terminal the app initiated or in a seperate terminal via `kill -SIGTERM <PID>`.

For an example local run the following commands in the terminal:  

1. Create an environment (within the directory of the repository)

   - `python -m venv venv`
   - `source venv/bin/activate`  # MacOS or UNIX  

2. Install dependencies

   - `pip install -r requirements.txt`

3. To Initiate the service:

   - run `python prob_app.py`

4. Test the service (in a seperate terminal):

   - run `test_server.py`
  
5. To simulate SIGTERM for graceful shutdown:

   - Note the PID in the app startup and send the signal in a seperate terminal using the command `kill -SIGTERM <PID>`
