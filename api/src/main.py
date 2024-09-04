from flask import Flask
from graphql_folder.schema import product_schema
from flask_graphql import GraphQLView
app = Flask(__name__)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=product_schema,
        graphiql=True  # Enable GraphiQL interface
    )
)

@app.route("/")
def test():
    return "<h1>1st commit running?<h1>"

if __name__ == "__main__":
    app.run()