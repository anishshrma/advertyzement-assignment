#Project Title
FastAPI Bank Branches API

##Project Description
A FastAPI application to provide bank branches data via GraphQL and REST API endpoints.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [GraphQL Example](#graphql-example)
- [Running Tests](#running-tests)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/fastapi-bank-branches-api.git
    cd fastapi-bank-branches-api
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```sh
    # Adjust the script path according to your project structure
    python init_db.py
    ```
## Usage

To start the server, run:
```sh
uvicorn main:app --reload
## API Endpoints

### REST API

- `GET /banks/`: Get the list of all banks.
- `GET /branches/{branch_id}/`: Get details of a specific branch.

### GraphQL

- `POST /gql`: GraphQL endpoint to query bank branches data.
## GraphQL Example

Example query to get branches data:

```graphql
query {
    branches {
        branch
        bank {
            name
        }
        ifsc
    }
}

### 8. Running Tests

Instructions on how to run tests, if applicable.

```markdown
## Running Tests

To run tests, use:

```sh
pytest

### 9. Deployment

Instructions on how to deploy the project.

```markdown
## Deployment

For deploying to Heroku, follow these steps:

1. Create a `Procfile` with the following content:
    ```sh
    web: uvicorn main:app --host 0.0.0.0 --port ${PORT:-5000}
    ```

2. Add the following to `requirements.txt`:
    ```sh
    uvicorn[standard]
    gunicorn
    ```

3. Deploy to Heroku:
    ```sh
    heroku create your-app-name
    git push heroku main
    ```

