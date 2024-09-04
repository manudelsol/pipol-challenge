from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

from data_service.schema import product_schema
from flask_graphql import GraphQLView
app = Flask(__name__)

# Swagger UI setup
SWAGGER_URL = '' # so the home screen is the swagger UI
API_URL = '/static/swagger_spec.json'  # URL for exposing Swagger spec

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Flask GraphQL API"
    }
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

if __name__ == "__main__":
    app.run()