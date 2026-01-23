# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

In this assignment, you will learn how to build a modern, high-performance web API using Python and the FastAPI framework. You will understand the basics of RESTful architecture, how to define routes, and how to return JSON data.

## 📝 Tasks

### 🛠️ Task 1: Hello FastAPI

#### Description
Create a basic FastAPI application that runs on a local server. You will need to define a root endpoint (`/`) that returns a welcome message in JSON format.

#### Requirements
Completed program should:

- Import the necessary FastAPI module.
- Create an instance of the `FastAPI` class.
- Define a route for `GET` requests to the root URL (`/`).
- Return a JSON object with a message, e.g., `{"message": "Welcome to my API"}`.

### 🛠️ Task 2: dynamic Routes and items

#### Description
Expand your API to handle specific items. Create a route that can accept an item ID from the URL path and return specific data about that item.

#### Requirements
Completed program should:

- Define a new route, such as `/items/{item_id}`.
- Accept `item_id` as a path parameter.
- Return a JSON object containing the `item_id` and an item name (you can assume a static name or use a dictionary to look it up).
- (Optional) Use type hints to ensure `item_id` is an integer.

### 🛠️ Task 3: Query Parameters

#### Description
Add functionality to accept optional query parameters to filter or customize the response.

#### Requirements
Completed program should:

- detailed in Task 2, modify or create a new route that accepts a query parameter (e.g., `q` or `limit`).
- Ensure the parameter is optional.
- Return the query parameter value in the JSON response if it is provided.
