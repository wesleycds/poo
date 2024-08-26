from manterclienteUI import ManterclienteUi
from view import View
import streamlit as st

class indexUI:
    def menu_adm():
        op = st.sidebar.selectbox("menu", ["manter cliente", ""])
        if op == "manter cliente": ManterclienteUi.Main()



    def sidebar():
        indexUI.menu_adm()

    def main():
        indexUI.sidebar()

indexUI.main()
