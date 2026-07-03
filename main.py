from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from middleware import RequestContextMiddleware
from ratelimiter import RateLimitMiddleware

app = FastAPI(
    title="Middleware Assignment API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://app-xyzh24.example.com",
        "https://exam.example.com"   # Replace with the actual exam page origin
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(RequestContextMiddleware)
app.add_middleware(RateLimitMiddleware)


@app.get("/")
def home():
    return {"message": "Middleware Assignment"}


@app.get("/ping")
def ping(request: Request):
    return {
        "email": "23f3001252@ds.study.iitm.ac.in",
        "request_id": request.state.request_id
    }


def main():
    print("Hello from middleware-api!")


if __name__ == "__main__":
    main()
