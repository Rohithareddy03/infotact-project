import pandas as pd
import streamlit as st
import snowflake.connector


def load_analytics_data():
    conn = snowflake.connector.connect(
        account=st.secrets["snowflake"]["GZGDCQH-UU35933"],
        user=st.secrets["snowflake"]["ROHITHAREDDY"],
        password=st.secrets["snowflake"]["Rabbitreddy@2005"],
        warehouse=st.secrets["snowflake"]["COMPUTE_WH"],
        database="ATMOSYNC",
        schema="RAW",
    )

    try:
        query = """
            SELECT *
            FROM ATMOSYNC.RAW.MICROCLIMATE_ANALYTICS
            ORDER BY DATE
        """
        return pd.read_sql(query, conn)
    finally:
        conn.close()