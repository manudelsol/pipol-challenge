import graphene
import pandas
from datetime import datetime


class ProductData(graphene.ObjectType):
    id_tie_fecha_valor = graphene.Date()
    id_cli_cliente = graphene.String()
    id_ga_vista = graphene.String()
    id_ga_tipo_dispositivo = graphene.String()
    id_ga_fuente_medio = graphene.String()
    desc_ga_sku_producto = graphene.String()
    desc_ga_categoria_producto = graphene.String()
    fc_agregado_carrito_cant = graphene.Int()
    fc_ingreso_producto_monto = graphene.Float()
    fc_retirado_carrito_cant = graphene.Int()
    fc_detalle_producto_cant = graphene.Int()
    fc_producto_cant = graphene.Int()
    desc_ga_nombre_producto = graphene.String()
    fc_visualizaciones_pag_cant = graphene.Int()
    flag_pipol = graphene.String()
    SASASA = graphene.String()
    id_ga_producto = graphene.String()
    desc_ga_nombre_producto_1 = graphene.String()
    desc_ga_sku_producto_1 = graphene.String()
    desc_ga_marca_producto = graphene.String()
    desc_ga_cod_producto = graphene.String()
    desc_categoria_producto = graphene.String()
    desc_categoria_prod_principal = graphene.String()


class Query(graphene.ObjectType):
    product_data = graphene.List(ProductData)

    def resolve_product_data(self, info):
        # relative path?
        csv_file_path = './../../../datasample.csv'

        df = pandas.read_csv(csv_file_path)

        data = df.to_dict(orient='records')

        # yyyymmdd date format to date
        for row in data:
            if 'id_tie_fecha_valor' in row:
                date_str = str(row['id_tie_fecha_valor'])
                row['id_tie_fecha_valor'] = datetime.strptime(date_str, "%Y%m%d").date()

        # Return a list of ProductData objects
        return [ProductData(**row) for row in data]

schema = graphene.Schema(query=Query)
