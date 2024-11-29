import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

# Función para generar gráficos comparativos
def mostrar_grafico_comparativo(df, capacidad):
    st.write(f"### Información de OKRs y KPIs ({capacidad}):")
    st.dataframe(df[["Indicador", "OKR", "KPI"]])

    st.write("### Progreso en Indicadores:")
    x = np.arange(len(df["Indicador"]))  # Posiciones para las barras
    width = 0.35  # Ancho de las barras

    fig, ax = plt.subplots()
    ax.bar(x - width/2, df["Valor Actual"], width, label='Actual', color='blue')
    ax.bar(x + width/2, df["Meta"], width, label='Meta', color='orange')

    # Etiquetas y título
    ax.set_xlabel("Indicadores")
    ax.set_ylabel("Valores")
    ax.set_title(f"Progreso en Indicadores de {capacidad}")
    ax.set_xticks(x)
    ax.set_xticklabels(df["Indicador"], rotation=45, ha="right")
    ax.legend()

    st.pyplot(fig)

# Tablero de detección
st.header("Capacidad: Detección (Sensing)")
mostrar_grafico_comparativo(df_sensing, "Sensing")

# Tablero de captación
st.header("Capacidad: Captación (Seizing)")
mostrar_grafico_comparativo(df_seizing, "Seizing")

# Tablero de configuración
st.header("Capacidad: Configuración (Configuring)")
mostrar_grafico_comparativo(df_configuring, "Configuring")

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
st.write("### Evolución de Proyectos Colaborativos:")
fig_cultura, ax_cultura = plt.subplots()
ax_cultura.plot(df_cultura["Periodo"], df_cultura["Proyectos Colaborativos"], marker='o', label="Proyectos")
ax_cultura.set_title("Evolución de Proyectos Colaborativos")
ax_cultura.set_ylabel("Número de Proyectos")
ax_cultura.legend()
st.pyplot(fig_cultura)
