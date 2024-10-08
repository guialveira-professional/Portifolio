import streamlit as st
from streamlit_image_select import image_select
from navigation.Statistics import statistics
from navigation.ML import Machine_learning
from navigation.Computer_vision import computer_vision
from navigation.aboutme import aboutme
from navigation.talk_to_me import talktome

st.set_page_config(page_title= "Guilherme Alves de Oliveira",
                   initial_sidebar_state="expanded",
                   layout='wide',
                   page_icon='imagens/pessoal.jpg')

def roll_page():
    # Definição barra de navegação
    #TALKTOME = "imagens/talktome_ico.jpg"
    ESTATISTICA = "imagens/Statistics_ico.jpg"
    ML = "imagens/ML_ico.jpg"
    VISION = "imagens/Computer_vision_ico.jpg"
    DL = "imagens/DL_ico.jpg"
    chosen_tab = image_select("", [ESTATISTICA, ML, VISION, DL],
                            captions= ["STATISTICS", "MACHINE LEARNING", "COMPUTER VISION", "DEEP LEARNING" ],
                            use_container_width=False)
    st.divider()
    #if chosen_tab == TALKTOME:
     #   talktome()
    if chosen_tab == ESTATISTICA:
        statistics()
    if chosen_tab == ML:
        Machine_learning()
    if chosen_tab == VISION:
        computer_vision()


with st.sidebar:
    st.image("imagens/pessoal.jpg")
    st.title("Guilherme")
    st.markdown("""<div style="text-align: justify;">Welcome to my portfolio! It's a pleasure to have you here</div>
                <div style="text-align: justify;">I'm a data professional with a passion in machine learning and deep learning for classification, regression and computer vision. </div>
                <div style="text-align: justify;">To know more about me click the button below </div>
                """,
                unsafe_allow_html=True)
    st.markdown("")
    about_button = st.button("About Me")
    st.markdown(
        """<h2 style='text-align: justify; color: white;'>E-mail</h2>
        <div style="text-align: justify;">guialveira@outlook.com</div>
        <h2 style='text-align: justify; color: white;'>Phone number</h2>
        <div style="text-align: justify;">+55 11 964308031</div>
        <h2 style='text-align: justify; color: white;'>Links</h2>
        <a href="https://github.com/guialveira-professional" target="_blank">GitHub</a>
        """,
        unsafe_allow_html=True)
    
    st.markdown("""<a href="https://www.linkedin.com/in/guilherme-alves-de-oliveira-914149258/" target="_blank">LinkedIn</a>""",
                unsafe_allow_html=True)
    
if about_button:
    aboutme()
else:
    roll_page()