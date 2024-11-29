import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Simulación de Datos ---
data_sensing = {
    "Indicador": ["Implementación de Monitoreo", "Tiempo de Respuesta", "Reportes Publicados", "Tecnologías Identificadas"],
    "Valor Actual": [85, 10, 4, 3],
    "Meta": [100, 12, 5, 3],
    "OKR": [
        "Desarrollar un sistema de monitoreo en tiempo real.",
        "Reducir el tiempo de respuesta a cambios detectados.",
        "Publicar reportes trimestrales sobre tendencias.",
        "Identificar tecnologías aplicables al negocio."
    ],
    "KPI": [
        "Porcentaje de implementación.",
        "Tiempo promedio de respuesta (horas).",
        "Número de reportes generados.",
        "Cantidad de tecnologías identificadas."
    ]
}

data_seizing = {
    "Indicador": ["Tasa de Conversión", "Abandono del Carrito", "NPS", "Tiempo de Carga"],
    "Valor Actual": [18, 15, 70, 2],
    "Meta": [20, 10, 85, 1],
    "OKR": [
        "Incrementar la tasa de conversión en canales digitales.",
        "Reducir el abandono del carrito en un 25%.",
        "Incrementar el puntaje NPS en un 15%.",
        "Reducir el tiempo de carga de plataformas."
    ],
    "KPI": [
        "Tasa de conversión (%).",
        "Porcentaje de abandono del carrito (%).",
        "Puntaje Net Promoter Score (NPS).",
        "Tiempo promedio de carga (segundos)."
    ]
}

data_configuring = {
    "Indicador": ["Integración de TI Bimodal", "Procesos Automatizados", "Satisfacción Laboral", "Costos Operativos Reducidos"],
    "Valor Actual": [60, 50, 75, 10],
    "Meta": [100, 70, 85, 15],
    "OKR": [
        "Completar la integración de TI bimodal en un año.",
        "Automatizar procesos prioritarios en 12 meses.",
        "Incrementar la satisfacción laboral en un 10%.",
        "Reducir costos operativos relacionados en un 15%."
    ],
    "KPI": [
        "Porcentaje de integración (%).",
        "Porcentaje de procesos automatizados (%).",
        "Nivel de satisfacción laboral (%).",
        "Porcentaje de reducción de costos operativos."
    ]
}

# Convertir los datos en DataFrames
df_sensing = pd.DataFrame(data_sensing)
df_seizing = pd.DataFrame(data_seizing)
df_configuring = pd.DataFrame(data_configuring)

# --- Visualización en Streamlit ---
st.title("Dashboard de Agilidad Operativa")

# Tablero de detección
st.header("Capacidad: Detección (Sensing)")
st.write("### Información de OKRs y KPIs:")
st.dataframe(df_sensing[["Indicador", "OKR", "KPI"]])

st.write("### Progreso en Indicadores:")
fig_sensing, ax_sensing = plt.subplots()
ax_sensing.bar(df_sensing["Indicador"], df_sensing["Valor Actual"], color='blue', label="Actual")
ax_sensing.bar(df_sensing["Indicador"], df_sensing["Meta"], color='orange', alpha=0.5, label="Meta")
ax_sensing.set_title("Progreso en
