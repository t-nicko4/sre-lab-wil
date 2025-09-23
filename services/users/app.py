


import time
from fastapi import Request
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

from fastapi import FastAPI, Response
from typing import List

app = FastAPI(title="users-service", version="0.1.0")

HTTP_REQUESTS_TOTAL = Counter(
    "users_http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "http_status"],
)

HTTP_REQUEST_DURATION_SECONDS = Histogram(
    "users_http_request_duration_seconds",
    "Request latency (seconds)",
    buckets=(0.05, 0.1, 0.2, 0.3, 0.5, 1, 2, 5),
    labelnames=("method", "endpoint"),
)

USERS = [{"id": 1, "name": "Ada"}, {"id": 2, "name": "Linus"}]

@app.get("/health")
async def health(request: Request):
    start = time.perf_counter()
    try:
        return {"status": "ok"}
    finally:
        duration = time.perf_counter() - start
        HTTP_REQUEST_DURATION_SECONDS.labels(request.method, "/health").observe(duration)
        HTTP_REQUESTS_TOTAL.labels(request.method, "/health", "200").inc()

@app.get("/users", response_model=List[dict])
async def list_users(request: Request):
    start = time.perf_counter()
    try:
        return USERS
    finally:
        duration = time.perf_counter() - start
        HTTP_REQUEST_DURATION_SECONDS.labels(request.method, "/users").observe(duration)
        HTTP_REQUESTS_TOTAL.labels(request.method, "/users", "200").inc()


# Expose Prometheus metrics endpoint
@app.get("/metrics")
async def metrics():
    data = generate_latest()
    return Response(content=data, media_type=CONTENT_TYPE_LATEST)