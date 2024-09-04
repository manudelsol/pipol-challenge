from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

from data_service.schema import product_schema
from flask_graphql import GraphQLView
app = Flask(__name__)

# swagger setup # Path to your Swagger JSON file
SWAGGER_URL = '/api/docs'
API_URL = '/swagger/swagger_spec.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Graphql API for Pipol Challenge"
    },
)

app.register_blueprint(swaggerui_blueprint)

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