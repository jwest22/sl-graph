import streamlit as st
import streamlit.components.v1 as components
from pyvis.network import Network
import network_graph

st.title('Data Symmetry')

if 'physics-key' not in st.session_state:
    st.session_state['physics-key'] = False
    
if 'hierarchy-key' not in st.session_state:
    st.session_state['hierarchy-key'] = False

if st.toggle('Enable Physics', value=st.session_state['physics-key']):
    st.session_state['physics-key']=True
else:
    st.session_state['physics-key']=False

if st.toggle('Enable Hierarchy Layout', value=st.session_state['hierarchy-key']):
    st.session_state['hierarchy-key']=True
else:
    st.session_state['hierarchy-key']=False
    
network_graph.network_func(
                           st.session_state['physics-key'],
                           st.session_state['hierarchy-key']
                           )

HtmlFile = open("front.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, height = 1200,width=1000)
