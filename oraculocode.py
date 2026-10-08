import streamlit as st
import random
st.set_page_config(page_title="Oráculo", page_icon="🔮", layout="centered")
st.title("Oráculo🔮")
st.markdown("### Deja que el oráculo decida por tí:")
respuestas = ["Sin duda alguna.",
              "El universo conspira a tu favor.",
              "Es tu destino; avanza con confianza.",
              "Los astros están alineados a tu favor.",
              "Definitivamente, sí.",
              "Todo apunta a un éxito rotundo."
]
st.markdown("---")
col1 = st.columns(1)
with col1:
    if st.button("Tu respuesta es:", use_container_width=True):
        st.success(f"**¡Hot Seat!**\n\n{random.choice(respuestas)}")
