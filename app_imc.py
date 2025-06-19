import streamlit as st

# Título de la app
st.title("Calculadora de IMC (Índice de Masa Corporal)")

# Entradas del usuario
peso = st.number_input("Ingresa tu peso (kg):", min_value=0.0, format="%.2f")
altura = st.number_input("Ingresa tu altura (m):", min_value=0.0, format="%.2f")

# Calcular IMC
if st.button("Calcular IMC"):
    if altura > 0:
        imc = peso / (altura ** 2)
        st.success(f"Tu IMC es: {imc:.2f}")

        # Interpretación
        if imc < 18.5:
            st.warning("Bajo peso")
        elif 18.5 <= imc < 25:
            st.success("Peso normal")
        elif 25 <= imc < 30:
            st.warning("Sobrepeso")
        else:
            st.error("Obesidad")
    else:
        st.error("¡La altura debe ser mayor que cero!")