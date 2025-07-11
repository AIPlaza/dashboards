# 📄 PRD – Frontend Streamlit Educativo, Financiero y Comercial para Plataforma P2P

## 🧠 Propósito General

Diseñar e implementar un frontend en **Streamlit** que sirva como una interfaz educativa, analítica y comercial para el backend FastAPI que expone datos P2P de Binance (y eventualmente Bybit). Esta interfaz debe ser:

- 📚 Una **herramienta pedagógica** para explicar el mercado P2P.
- 📈 Un **visor financiero interactivo** con lógica de análisis.
- 💼 Un **prototipo comercial** para presentaciones a stakeholders.
- 🧪 Un **workbook** donde el usuario experimenta, filtra, analiza y aprende.

---

## 🔧 Arquitectura y Ejecución

### Estructura de Lanzamiento

- Backend: `uvicorn p2p_api.main:app --reload`
- Frontend: `streamlit run app.py`
- Futuros despliegues: recomendación de `Docker Compose` para orquestar ambos procesos.

### Estructura Modular Recomendada

```
app/
├── app.py
├── components/
│   ├── header.py
│   ├── filters.py
│   ├── charts.py
│   ├── finance_tools.py
│   └── feedback_panel.py
├── utils/
│   └── api.py
├── docs/
│   └── README.md
└── requirements.txt
```

---

## 🧩 Módulos Funcionales

### 1. Dashboard General
- Branding + explicación del proyecto.
- Última actualización.
- Vista resumen de tasas P2P destacadas.

### 2. Filtros Inteligentes
- Selector de fiat, crypto y tipo de operación.
- Uso del endpoint `/api/v1/binance/pairs` para sugerencias dinámicas.

### 3. Visualización de Ofertas
- Tabla limpia y ordenada con:
  - Precio, volumen, métodos de pago, límites
  - Ordenable por cualquier columna
- Botones para exportar CSV o copiar

### 4. Gráficos Financieros
- 📊 Profundidad de mercado
- 📈 Curva de liquidez acumulada
- 📉 Volatilidad local por par
- 🟢 Spread absoluto y relativo
- Promedio ponderado y su evolución

### 5. Perspectivas Analíticas
- 👁️ Vista Mercado: volumen, precios extremos, top merchants
- 🎓 Vista Educativa: explicación visual paso a paso
- 💼 Vista Stakeholder: storytelling + KPIs clave
- 📊 Vista Comparativa: múltiples pares en paralelo

### 6. Panel de Notas y Feedback
- Campo editable + botón de exportar `.txt`
- Pensado como diario de usuario, testing o focus group

---

## 🧮 Fórmulas y Enriquecimiento de Datos

### Cálculos internos (en frontend):
- Spread = diferencia entre mejor oferta de compra y venta
- Spread % = `(sell - buy) / buy * 100`
- Promedio ponderado por volumen
- Curvas de liquidez: acumulado de volumen
- Desviación estándar entre ofertas
- Clasificación de comerciantes (merchant o usuario común)

### Datos enriquecidos:
- Normalización de métodos de pago
- Score reputacional si disponible
- Agrupación por rangos de montos mínimos

---

## 🎨 UI/UX – Diseño y Experiencia

- Tema: **Modo oscuro profesional**
- Paleta:
  - Fondo: `#0F1117`
  - Texto: `#F5F5F5`
  - Verde análisis: `#00FF41`
  - Naranja énfasis: `#FF9100`
- Tipografías: Inter, Roboto
- Componentes clave: `st.dataframe`, `st.plotly_chart`, `st.expander`, `st.sidebar`, `st.columns`, `st.markdown`

---

## 📘 Documentación Educativa

- Glosario en línea (expandible)
- Tooltip en cada métrica financiera
- Botón “¿Qué significa esto?” para spreads, límites, etc.
- Diagrama visual de arquitectura

---

## 🧠 Buyer Personas

| Usuario | Rol | Qué busca |
|---------|-----|-----------|
| 📚 Estudiante | Aprendiz visual | Entender economía real desde el P2P |
| 💹 Trader | Usuario activo | Ver tasas, spreads y oportunidades rápido |
| 🧑‍💻 Dev / Analista | Técnico | Reusar API, evaluar lógica |
| 💼 Inversionista | Stakeholder | Percibir valor, experiencia y visión de escalado |

---

## 🚀 Roadmap Fases

| Fase | Entregable | Propósito |
|------|------------|-----------|
| MVP UI | app.py con filtros, tabla y branding | Mostrar proyecto funcionando |
| Vistas | Módulos de mercado, educación, stakeholder | Diferenciar por audiencia |
| Finanzas | Cálculos y visualizaciones interactivas | Aumentar valor percibido |
| Históricos | Integrar PostgreSQL + gráficos tiempo | Soporte a decisiones |
| Agentes | Añadir módulo MCP + lenguaje natural | Prototipo IA P2P |
| Comunidad | Notas, favoritos, login, feedback UX | Testing + escalabilidad comercial

---

## 📦 Entregables Esperados

- `app.py` y módulos por componente
- Documentación por sección
- PRD + Wireframes
- Manual de pitch y demo
- Lista de mejoras post-pitch

---

## ✅ Conclusión

Esta interfaz es mucho más que una pantalla: es un **ecosistema visual y educativo**, un **visor financiero profesional**, y un **prototipo comercial convincente**. Diseñada para explicar, analizar y presentar el potencial completo del backend P2P.

> **Mostrar el backend es enseñar; interactuar con este frontend es convencer.**

---

## 🗺️ Plan de Implementación (Gemini CLI)

### 1. Estructura del Proyecto

Se creará un nuevo directorio de nivel superior llamado `streamlit_app/` para alojar todos los archivos de la aplicación Streamlit, manteniéndolo separado del código existente de la API.

```
C:/Users/DELL/P2P-Dashboard/
├───... (archivos y carpetas existentes)
├───streamlit_app/
│   ├───app.py                 # Aplicación principal de Streamlit
│   ├───requirements.txt       # Dependencias para la aplicación Streamlit
│   ├───utils/
│   │   └───api.py             # Módulo para interactuar con el backend FastAPI
│   └───docs/
│       └───README.md          # Documentación para la aplicación Streamlit
```

### 2. Instalación y Configuración

Se proporcionarán instrucciones para instalar Streamlit y otros paquetes Python necesarios dentro de un nuevo entorno virtual para `streamlit_app`.

### 3. Ejecución del Backend y Frontend

Se detallarán los pasos para ejecutar tanto el backend FastAPI como el nuevo frontend Streamlit simultáneamente, asegurando que operen en puertos diferentes.

### 4. Desarrollo de la Aplicación Streamlit (Enfoque por Fases)

*   **Fase 1: MVP UI (Entrega Inicial)**
    *   **`streamlit_app/app.py`**:
        *   Implementación del diseño principal de Streamlit con el tema de modo oscuro y la paleta de colores especificados.
        *   Adición de la marca y una explicación general del proyecto.
        *   Integración de filtros inteligentes (fiat, cripto, tipo de operación) mediante llamadas al endpoint `/api/v1/binance/pairs` del backend.
        *   Visualización de una tabla limpia y ordenable de ofertas.
    *   **`streamlit_app/utils/api.py`**:
        *   Creación de funciones para realizar solicitudes HTTP al backend FastAPI (ej. para obtener pares, ofertas).
    *   **`streamlit_app/requirements.txt`**:
        *   Listado de `streamlit`, `requests` y cualquier otra librería necesaria.

*   **Fase 2: Vistas Analíticas y Financieras**
    *   Desarrollo de las "Vista de Mercado", "Vista Educativa" y "Vista para Stakeholders" como secciones o páginas distintas dentro de la aplicación Streamlit.
    *   Implementación de los gráficos financieros (profundidad de mercado, curva de liquidez, volatilidad, spread) utilizando `st.plotly_chart`.
    *   Incorporación de los cálculos internos especificados (spread, promedio ponderado, curvas de liquidez, desviación estándar) dentro de la lógica de la aplicación Streamlit.

*   **Fase 3: Documentación y Feedback**
    *   Adición de elementos educativos como un glosario, tooltips para métricas financieras y botones "¿Qué significa esto?".
    *   Implementación del panel de notas y feedback.

### 5. Documentación

Se creará un archivo `README.md` dentro del directorio `streamlit_app/`, detallando cómo configurar, ejecutar e interactuar con la aplicación Streamlit, junto con una descripción general de sus características.
