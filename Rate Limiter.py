# Token Bucket Rate Limiter Implementation
import time

class RateLimiter:
    def __init__(self, capacity: int, refill_rate: float):
        """
        :param capacity: Maximum number of tokens the bucket can hold.
        :param refill_rate: How many tokens are added per second.
        """
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_check = time.time()

    def allow_request(self) -> bool:
        now = time.time()
        
        # Calculate how many tokens were generated since the last request
        elapsed = now - self.last_check
        new_tokens = elapsed * self.refill_rate
        
        # Update bucket (without exceeding capacity)
        self.tokens = min(self.capacity, self.tokens + new_tokens)
        self.last_check = now

        # Check if we have at least one token
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        
        return False

# # Example Usage:
# # 5 tokens max, refills at 1 token per second
# limiter = RateLimiter(capacity=5, refill_rate=1)

# for i in range(7):
#     print(f"Request {i+1}: {'Allowed' if limiter.allow_request() else 'Rejected'}")
#     time.sleep(0.2) # Rapid fire requests


# Fixed Window Rate Limiter Implementation

import time
from collections import defaultdict

class FixedWindowLimiter:
    def __init__(self, limit: int, window_seconds: int):
        self.limit = limit
        self.window_seconds = window_seconds
        # Stores { window_timestamp: count }
        self.requests = defaultdict(int)

    def allow_request(self, identifier: str) -> bool:
        # Determine the current window (e.g., the current minute)
        current_window = int(time.time() // self.window_seconds)
        
        # Unique key for this user in this specific window
        key = f"{identifier}:{current_window}"
        
        if self.requests[key] < self.limit:
            self.requests[key] += 1
            return True
        
        return False

# # Example: Limit to 3 requests per 10-second window
# limiter = FixedWindowLimiter(limit=3, window_seconds=10)
# user_ip = "192.168.1.1"

# for i in range(5):
#     allowed = limiter.allow_request(user_ip)
#     print(f"Request {i+1}: {'Allowed' if allowed else 'Rejected'}")