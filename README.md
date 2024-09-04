# Challenge project

## Overview

This project is a Flask-based web application that utilizes GraphQL with Graphene and Swagger for API documentation. The app is containerized using Docker for easy deployment.

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your machine.

## Directory Structure

```
.
├── api/
│   ├── src/
│   │   ├── data_service/
│   │   │   ├── __init__.py
│   │   │   ├── csv_reader.py
│   │   │   └── schema.py
│   │   ├── static/
│   │   │   ├── swagger_spec.json
│   │   ├── __init__.py
│   │   └── main.py
│   └── requirements.txt
├── datasample.csv
└── Dockerfile
```

## Docker Setup

### 1. Build the Docker Image

To build the Docker image for the application, run the following command in the root of the project directory (where the `Dockerfile` is located):

```sh
docker build -t my-flask-app .
```

### 2. Run the Docker Container

Once the image is built, you can run the container by mapping an available port on your host to the Flask app's port inside the container:

```sh
docker run -p 5001:5000 my-flask-app
```

- **`-p 5001:5000`**: Maps port `5001` on your host machine to port `5000` inside the container, where the Flask app is running.

### 3. Access the Application

After running the container, the application will be accessible at:

```
http://localhost:5001
```

## Usage

### Swagger UI

Once you access `http://localhost:5001` in your browser, you will be directed to the Swagger UI. This interface provides documentation and allows you to test the API endpoints directly from the browser. The UI includes examples of queries and shows possible `200` (success) and `400` (error) responses.

### GraphiQL Interface

You can also interact with the GraphQL API using the GraphiQL interface by visiting:

```
http://localhost:5001/graphql
```

This interface allows you to write and test GraphQL queries interactively.

### Using cURL or Postman

If you prefer using `cURL` or Postman, you can POST requests to the GraphQL endpoint to retrieve data. Here’s an example using `cURL`:

```sh
curl -X POST \
  http://localhost:5001/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "query { productData(descGaSkuProducto: \"K\") { idTieFechaValor descGaSkuProducto } }"}'
```

This query fetches `idTieFechaValor` and `descGaSkuProducto` fields for products where `descGaSkuProducto` contains the letter "K".

## Queryable Fields
The following fields are available for querying in the productData query:
```
idTieFechaValor
idCliCliente
idGaVista
idGaTipoDispositivo
idGaFuenteMedio
descGaSkuProducto
descGaCategoriaProducto
fcAgregadoCarritoCant
fcIngresoProductoMonto
fcRetiradoCarritoCant
fcDetalleProductoCant
fcProductoCant
descGaNombreProducto
fcVisualizacionesPagCant
flagPipol
sasasa
idGaProducto
descGaNombreProducto1
descGaSkuProducto1
descGaMarcaProducto
descGaCodProducto
descCategoriaProducto
descCategoriaProdPrincipal
```
---