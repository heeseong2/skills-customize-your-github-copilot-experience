# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using the FastAPI framework. Students will create endpoints, work with request and response data, and practice handling JSON in a web application.

## 📝 Tasks

### 🛠️ Create a Basic API

#### Description
Build a small FastAPI application that exposes at least one endpoint returning JSON data for a list of items or a sample message.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Define a route that responds to a GET request
- Return JSON data in a clear, readable format
- Run the server locally with Uvicorn or FastAPI's built-in tools
- Confirm the endpoint works by opening the browser or using a client such as curl

### 🛠️ Add CRUD Functionality

#### Description
Expand the API to support creating, reading, updating, and deleting items using request data and route parameters.

#### Requirements
Completed program should:

- Define endpoints for creating, listing, updating, and deleting items
- Use request bodies to send item data in JSON format
- Validate input data with FastAPI and Pydantic models
- Return appropriate status codes such as `200` and `201`
- Handle a request for a missing item gracefully
- Keep the code organized with simple, readable functions
