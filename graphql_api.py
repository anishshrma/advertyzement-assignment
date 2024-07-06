from ariadne import QueryType, make_executable_schema, graphql_sync
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy.orm import Session
from model import Bank, Branch
from database import get_db

type_defs = """
    type Bank {
        id: Int
        name: String
    }

    type Branch {
        ifsc: String
        branch: String
        bank: Bank
    }

    type Query {
        branches: [Branch]
    }
"""

query = QueryType()

@query.field("branches")
def resolve_branches(_, info):
    db: Session = next(get_db())
    branches = db.query(Branch).all()
    return branches

schema = make_executable_schema(type_defs, query)

PLAYGROUND_HTML = """
<!DOCTYPE html>
<html>

<head>
    <meta charset=utf-8/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GraphQL Playground</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/graphql-playground-react/build/static/css/index.css"/>
    <link rel="shortcut icon" href="https://cdn.jsdelivr.net/npm/graphql-playground-react/build/favicon.png"/>
    <script src="https://cdn.jsdelivr.net/npm/graphql-playground-react/build/static/js/middleware.js"></script>
</head>

<body>
    <div id="root"/>
    <script>window.addEventListener('load', function (event) { GraphQLPlayground.init(document.getElementById('root'), { endpoint: '/graphql' }) })</script>
</body>

</html>
"""

app = FastAPI()

@app.get("/graphql")
async def graphql_playground():
    return HTMLResponse(content=PLAYGROUND_HTML, status_code=200)

@app.post("/graphql")
async def graphql_server(request: Request):
    data = await request.json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return JSONResponse(content=result, status_code=status_code)
