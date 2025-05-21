import streamlit as st
import pandas as pd
from typing import List
from core.data_models import FileScanResult

def display_scan_results(results: List[FileScanResult]):
    """
    Formats and displays the scan results in a Streamlit table.
    """
    if results:
        data_for_df = [res.to_dict() for res in results]
        df = pd.DataFrame(data_for_df)
        st.subheader("Scan Results:")
        st.table(df)
    else:
        st.info("No results to display.")