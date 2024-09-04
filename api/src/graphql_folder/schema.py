import os

import graphene
from datetime import datetime
from pathlib import Path

from . import csv_reader

csv_file_path = os.path.join(Path(__file__).resolve().parent.parent.parent.parent, 'datasample2.csv')

csv_data = csv_reader.read_csv_from_file(csv_file_path)


class ProductData(graphene.ObjectType):
    id_tie_fecha_valor = graphene.Date()
    id_cli_cliente = graphene.String()
    id_ga_vista = graphene.String()
    id_ga_tipo_dispositivo = graphene.String()
    id_ga_fuente_medio = graphene.String()
    desc_ga_sku_producto = graphene.String()
    desc_ga_categoria_producto = graphene.String()
    fc_agregado_carrito_cant = graphene.String()
    fc_ingreso_producto_monto = graphene.String()
    fc_retirado_carrito_cant = graphene.String()
    fc_detalle_producto_cant = graphene.String()
    fc_producto_cant = graphene.String()
    desc_ga_nombre_producto = graphene.String()
    fc_visualizaciones_pag_cant = graphene.String()
    flag_pipol = graphene.String()
    SASASA = graphene.String()
    id_ga_producto = graphene.String()
    desc_ga_nombre_producto_1 = graphene.String()
    desc_ga_sku_producto_1 = graphene.String()
    desc_ga_marca_producto = graphene.String()
    desc_ga_cod_producto = graphene.String()
    desc_categoria_producto = graphene.String()
    desc_categoria_prod_principal = graphene.String()

    def resolve_id_tie_fecha_valor(parent, info):
        date_str = parent.id_tie_fecha_valor
        return datetime.strptime(date_str, '%Y%m%d').date()




class Query(graphene.ObjectType):
    product_data = graphene.List(ProductData)

    def resolve_product_data(self, info):
        return [ProductData(**row) for row in csv_data]


product_schema = graphene.Schema(query=Query)
