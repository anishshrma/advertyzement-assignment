from fastapi import FastAPI
from rest_api import app as rest_app
from graphql_api import app as gql_app

app = FastAPI()

app.mount("/api", rest_app)
app.mount("/graphql", gql_app)
