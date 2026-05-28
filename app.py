               

import streamlit as st
st.set_page_config(layout="wide")

st.sidebar.image('logo.png',use_container_width=True)
st.sidebar.header("""Bill of Materials to Input‑Output Inventory Converter
*Version 1.1*""")
st.sidebar.markdown("Convert BOM files into structured outputs for LCI and costing.")

st.sidebar.markdown("----", unsafe_allow_html=True)

#navigation at the bottom
st.sidebar.markdown("Select a page to navigate to:")
page=st.sidebar.radio("",["Home","BOM Transformation", "Disclaimer"], index=0)

#page routing 
if page=="Home":
    st.title("Bill of Materials to Input‑Output Inventory Converter")
    st.subheader("*Version 1.1*")
    st.image('workflow_diagram.jpg',use_container_width=True)
    st.subheader("Welcome")
    st.write("""*This tool converts BOMs into structured outputs for analysis.*      
             *This tool is in Beta*""")

    st.write("""
             
             This Python-based tool streamlines the conversion of bill of material (BOM) data from legacy PDF lists into a consistent Input-Output Inventory format, significantly reducing manual effort and improving accuracy for supply chain analysis, Build America, Buy America (BABA), and other analysis. 
             The solution builds on previously developed inventory data collection templates, which have strong potential to transform data practices in the buildings equipment sectors. 
             By automating the transfer process, this code enables entities to efficiently populate the Excel-based inventory template with critical supply chain information, supporting comprehensive analysis. 
             This advancement not only accelerates data-driven decision-making but also reinforces PNNL’s leadership in addressing compliance essential products and systems. 
             Ultimately, the tool bridges the gap between outdated manual workflows and modern, structured data collection, empowering analysis with greater precision and speed.
             
             This script has been developed for use by industry partners to convert legacy data into usable inventory and costing tables. 
             This tool is broadly applicable to any partner with a PDF or Excel based BOM, it is currently optimized for partners within the mechanical & electrical (M&E) industries – specifically thermal systems (e.g., heating, ventilation, air conditioning). 
             Use by partners in other industries is possible but may result in unforeseen errors.
             
             To use the tool, users upload a PDF or Excel file containing their BOM. After upload, users make a series of selections that are processed internally by the script.
             Upon completion, the tool generates two output tables (inventory and costing) which can be directly uploaded into the inventory templates available on Datahub. """)
    st.write("""**For any questions of inquiries please reach out via**: LCI-template@pnnl.gov      
             **IR Number:PNNL-SA-222555**""")
elif page=="BOM Transformation":
    import modules.BOM_transformation as BOM_transformation
    BOM_transformation.show()
elif page=="Disclaimer":
    import modules.Disclaimer as Disclaimer
