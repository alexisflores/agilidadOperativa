import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Simulación de Datos ---
data_sensing = {
    "Indicador": ["Implementación de Monitoreo", "Tiempo de Respuesta", "Reportes Publicados", "Tecnologías Identificadas"],
    "Valor Actual": [85, 10, 4, 3],
    "Meta": [100, 12, 5, 3]
}

data_seizing = {
    "Indicador": ["Tasa de Conversión", "Abandono del Carrito", "NPS", "Tiempo de Carga"],
    "Valor Actual": [18, 15, 70, 2],
    "Meta": [20, 10, 85, 1]
}

data_configuring = {
    "Indicador": ["Integración de TI Bimodal", "Procesos Automatizados", "Satisfacción Laboral", "Costos Operativos Reducidos"],
    "Valor Actual": [60, 50, 75, 10],
    "Meta": [100, 70, 85, 15]
}

# Convertir los datos en DataFrames
df_sensing = pd.DataFrame(data_sensing)
df_seizing = pd.DataFrame(data_seizing)
df_configuring = pd.DataFrame(data_configuring)

# --- Visualización en Streamlit ---
st.title("Dashboard de Agilidad Operativa")

# Tablero de detección
st.header("Capacidad: Detección (Sensing)")
st.dataframe(df_sensing)
fig_sensing, ax_sensing = plt.subplots()
ax_sensing.bar(df_sensing["Indicador"], df_sensing["Valor Actual"], color='blue', label="Actual")
ax_sensing.bar(df_sensing["Indicador"], df_sensing["Meta"], color='orange', alpha=0.5, label="Meta")
ax_sensing.set_title("Progreso en Indicadores de Sensing")
ax_sensing.legend()
st.pyplot(fig_sensing)

# Tablero de captación
st.header("Capacidad: Captación (Seizing)")
st.dataframe(df_seizing)
fig_seizing, ax_seizing = plt.subplots()
ax_seizing.bar(df_seizing["Indicador"], df_seizing["Valor Actual"], color='green', label="Actual")
ax_seizing.bar(df_seizing["Indicador"], df_seizing["Meta"], color='orange', alpha=0.5, label="Meta")
ax_seizing.set_title("Progreso en Indicadores de Seizing")
ax_seizing.legend()
st.pyplot(fig_seizing)

# Tablero de configuración
st.header("Capacidad: Configuración (Configuring)")
st.dataframe(df_configuring)
fig_configuring, ax_configuring = plt.subplots()
ax_configuring.bar(df_configuring["Indicador"], df_configuring["Valor Actual"], color='red', label="Actual")
ax_configuring.bar(df_configuring["Indicador"], df_configuring["Meta"], color='orange', alpha=0.5, label="Meta")
ax_configuring.set_title("Progreso en Indicadores de Configuring")
ax_configuring.legend()
st.pyplot(fig_configuring)

# --- Cultura y Liderazgo Digital ---
st.header("Cultura y Liderazgo Digital")
st.write("**OKR Adicional:** Fomentar la innovación a través de la colaboración interdisciplinaria.")
st.write("- **Objetivo:** Incrementar la colaboración entre departamentos.")
st.write("- **KPI:** Número de proyectos colaborativos lanzados por trimestre.")
data_cultura = {
    "Periodo": ["Q1", "Q2", "Q3", "Q4"],
    "Proyectos Colaborativos": [5, 7, 10, 12]
}
df_cultura = pd.DataFrame(data_cultura)
fig_cultura, ax_cultura = plt.subplots()
ax_cultura.plot(df_cultura["Periodo"], df_cultura["Proyectos Colaborativos"], marker='o', label="Proyectos")
ax_cultura.set_title("Evolución de Proyectos Colaborativos")
ax_cultura.set_ylabel("Número de Proyectos")
ax_cultura.legend()
st.pyplot(fig_cultura)
