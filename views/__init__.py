import streamlit as st
import pandas as pd

def mostrar_tabla(df: pd.DataFrame) -> None:
    st.dataframe(df, use_container_width=True, hide_index=True)
