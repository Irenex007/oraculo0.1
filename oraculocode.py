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
              "Todo apunta a un éxito rotundo.",
              "No cuentes con ello.",
              "Es un camino que mejor no recorrer ahora.",
              "Las energías no son propicias para esto.",
              "Absolutamente no.",
              "El futuro aún no está escrito; depende de ti.",
              "La niebla es espesa, vuelve a preguntar más tarde.",
              "Medítalo un poco más antes de actuar.",
              "La respuesta ya la tienes en tu interior.",
              "Los espíritus guardan silencio sobre este asunto.",
              "Ni sí, ni no, sino todo lo contrario.",
              "Los presagios indican lo contrario.",
              "El destino te tiene preparado algo distinto.",
              "Da el primer paso hoy mismo.",
              "Busca el consejo de alguien más sabio.",
              "Espera a que pase la tormenta antes de decidir.",
              "Atrévete, el riesgo valdrá la pena.",
              "Cambia tu perspectiva y verás la solución.",
              "Libérate de tus miedos primero.",
              "¿En serio me preguntas eso a mí?",
              "Incluso el oráculo necesita un café antes de responderte eso.",
              "Sí, pero prepárate para las consecuencias.",
              "Mi bola de cristal se acaba de quedar sin batería.",
              "Si te hace feliz creer que sí, adelante.",
              "Mejor tira una moneda, yo hoy no quiero responsabilidades."
]
st.markdown("---")
if st.button("Que el azar decida", use_container_width=True):
    st.success(f"**Tu respuesta es:**\n\n{random.choice(respuestas)}")
