import streamlit as st
import pandas as pd
from view import View
import time

class ManterclienteUi:
    def Main():
        st.header("cadastro de cliente")
        tab1, tab2, tab3, tab4 = st.tabs (["listar", "inserir", "atualizar", "excluir"])
        with tab1: ManterclienteUi.listar()
        with tab2: ManterclienteUi.inserir()
        with tab3: ManterclienteUi.atualizar()
        with tab4: ManterclienteUi.excluir()

    def listar():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("sem clientes")
        else:
            dic = []
            for obj in clientes: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
     nome = st.text_input("Informe o nome")
     email = st.text_input("Informe o e-mail")
     fone = st.text_input("Informe o fone")
     #senha = st.text_input("Informe a senha")
     if st.button("Inserir"):
      View.cliente_inserir(nome, email, fone) #, senha)
      st.success("Cliente inserido com sucesso")
      time.sleep(2)
      st.rerun()

    def atualizar():
     clientes = View.cliente_listar()
     if len(clientes) == 0:
      st.write("Nenhum cliente cadastrado")
     else:
      op = st.selectbox("Atualização de Clientes", clientes)
      nome = st.text_input("Informe o novo nome", op.get_nome())
      email = st.text_input("Informe o novo e-mail", op.get_email())
      fone = st.text_input("Informe o novo fone", op.get_fone())
      senha = st.text_input("Informe a nova senha")
      if st.button("Atualizar"):
        id = op.get_id()
        View.cliente_atualizar(id, nome, email, fone) #, senha)
        st.success("Cliente atualizado com sucesso")
        time.sleep(2)
        st.rerun()

    def excluir():
      clientes = View.cliente_listar()
      if len(clientes) == 0:
        st.write("lista vazia nao da pra excluir")
      else:
        op = st.selectbox("exclusao de cliente", clientes)
        if st.button("excluir"):
          id = op.get_id()
          View.cliente_excluir(id)
          st.success("cliente excluido")
          time.sleep(2)
          st.rerun()
    