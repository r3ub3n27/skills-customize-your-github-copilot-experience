from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Task 1: Create a root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Task 2: Create a dynamic route for items
# TODO: Implement the item endpoint here

# Task 3: Add support for query parameters
# TODO: meaningful query params implementation
