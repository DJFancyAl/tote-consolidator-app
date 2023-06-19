# Imports
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import pandas as pd


# Initialize Connection
def get_inventory():
    load_dotenv()
    connection_string = os.getenv("SQL_CONNECTION")
    engine = create_engine(connection_string)
    connection = engine.connect()

    # Query the databse
    query = text("""SELECT T_ITEM.name AS tote_id, T_PACKAGE.batch, T_PACKAGE.weight, T_MATERIAL.name AS gmc, T_MATERIAL_META_INFORMATION.color,
            T_MATERIAL_META_INFORMATION.size, T_LOCATION.name AS location
    FROM  T_PACKAGE FULL OUTER JOIN
            T_MATERIAL ON T_PACKAGE.material_id = T_MATERIAL.id FULL OUTER JOIN
            T_MATERIAL_META_INFORMATION ON T_MATERIAL.name = T_MATERIAL_META_INFORMATION.gmc_barcode FULL OUTER JOIN
            T_LOAD_T_PACKAGE ON T_PACKAGE.id = T_LOAD_T_PACKAGE.packages_id FULL OUTER JOIN
            T_LOAD ON T_LOAD_T_PACKAGE.t_load_item_id = T_LOAD.item_id FULL OUTER JOIN
            T_ITEM ON T_LOAD.item_id = T_ITEM.id FULL OUTER JOIN
            T_ITEMTYPE ON T_ITEM.type_id = T_ITEMTYPE.id FULL OUTER JOIN
            T_LOCATION ON T_ITEM.location = T_LOCATION.id
    WHERE (T_ITEM.name IS NOT NULL) AND (NOT (T_MATERIAL.name = 'Empty')) AND (T_ITEMTYPE.name = 'Plastic totes') AND (T_MATERIAL_META_INFORMATION.type = 0) AND (T_LOAD.state = 2)""")

    df = pd.read_sql_query(query, engine)    
    connection.close()

    return df