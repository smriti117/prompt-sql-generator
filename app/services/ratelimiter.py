import time
from collections import deque


class SlidingWindowRateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = deque()

    def allow(self) -> bool:
        current_time = time.time()

        # Remove old timestamps
        while self.requests and self.requests[0] < current_time - self.window_seconds:
            self.requests.popleft()

        if len(self.requests) >= self.max_requests:
            return False

        self.requests.append(current_time)
        return True
