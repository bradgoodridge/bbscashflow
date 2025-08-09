from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# List of URLs allowed to access your backend
origins = [
    "http://localhost:3000",  # local frontend dev URL
    "https://bbscashflow-frontend.onrender.com",  # your deployed frontend URL
]

# Add CORS middleware so frontend can call backend without blocking
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # allow these origins
    allow_credentials=True,
    allow_methods=["*"],        # allow all HTTP methods (GET, POST, etc)
    allow_headers=["*"],        # allow all headers
)

@app.get("/")
def read_root():
    return {"message": "Hello from backend!"}

@app.get("/hello")
def hello():
    return {"message": "hello from backend"}
