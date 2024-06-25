from fastapi import FastAPI, Query, HTTPException
import time
import signal
import threading
import logging

from dsum_probability import probability

# Initialize the app
app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/probability")
async def get_probability(
    n: int = Query(..., description="Number of dice", ge=0),
    m: int = Query(..., description="Desired sum", ge=0)
):
    if m < n or m > 6 * n:
        raise HTTPException(status_code=400, detail="Invalid sum for given number of dice and faces")

    # processing time
    time.sleep(5)

    prob = probability(m, n)
    logger.info(f"Probability of getting the sum S={m} calculated for n={n}, 6 faced dice(s): {prob}")
    return {"probability": prob}

def handle_sigterm(*args):
    print("Received SIGTERM. Shutting down gracefully.")
    threading.Thread(target=app.shutdown).start()

signal.signal(signal.SIGTERM, handle_sigterm)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
