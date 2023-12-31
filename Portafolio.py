import streamlit as st 
from PIL import Image

############HEAD
st.markdown('<img src="https://media.licdn.com/dms/image/D4E16AQGRrB159RBbnA/profile-displaybackgroundimage-shrink_350_1400/0/1690208358854?e=1696464000&v=beta&t=27he1p8MoK_7FX1cYWGW1Ln1qzcP88QQDOWUgvFqxvU" alt="drawing" width="700"/>', unsafe_allow_html=True)
st.markdown("## Iván Miguel Cepeda")
st.markdown('### Data Analyst')

###########Body
st.markdown('Analista de datos, actualmente me desempeño como analista de rendimiento de fútbol para un equipo local, En mi vida he experimentado en múltiples campos del saber, desde las leyes, pasando por ventas, creación de contenido digital y ahora Analista, y en todas esas actividades siempre recurría a buscar datos que me ayudaran a mejorar, por lo que terminó convirtiéndose la ciencia de datos en mi verdadera pasión. Adicionalmente, he practicado artes marciales durante 31 años, y eso me ha dejado con un gran sentido de disciplina, responsabilidad, honor y lealtad.  Todos los días me levanto con un objetivo principal en mente, "Ser la mejor versión de mi"')

###Proyectos
st.markdown('## Proyectos')


##Sistema de notificación sísmica
st.markdown('## Sistema de Notificación Sísmica')
st.markdown('En este proyecto se creo una aplicación que permite analizar una base de datos, sobre sismos de tres paises. A su vez se conecta con una aplicación desarrollada en AWS, que extrae en tiempo real cuando un sismo sucede y los clasifica a través de un modelo de machine learning, y envía una notificación a un grupo de telegram')
st.markdown('Para acceder al repositorio para ampliar mas sobre este proyecto. Ingresa en el [link](https://github.com/Ivan-Cepeda/Sismos)')
st.markdown('Para acceder a la app princiapl en tiempo real, ingresar en el [link](https://sismos-notificacion.streamlit.app/)')

##MOOCS
st.markdown('## Analisis MOOCs')
st.markdown("En este proyecto, se me otorgarón 4 datasets, con datos de 3 empresas de cursos masivos y abiertos en línea, conocidos por sus siglas en inglés MOOC.")
st.markdown("Para acceder al repositorio para ampliar mas sobre este proyecto. Ingressa en el [link](https://github.com/Ivan-Cepeda/Analisis-MOOCs-PI2)")
st.markdown("![](https://github.com/Ivan-Cepeda/Analisis-MOOCs-PI2/blob/main/src/udem.jpeg)")

##SISTEMA DE RECOMENDACIÓN DE PELÍCULAS
st.markdown('## Sistema de Recomendación de películas')
st.markdown("En este proyecto, la intención era entregar un MVP, producto mínimo víable de un sistema de recomendación de películas, usando Machine Learning, en este caso se trabajaron 2 datasets, y de alí se realizaron una serie de transformaciones esenciales para entrenar un modelo de machine learning, y poder acceder a los datos solicitados")
st.markdown("Para mayor información sobre este proyecto entre a este [link](https://github.com/Ivan-Cepeda/Sistema-Recomendacion-PI)")

st.markdown("Aquí puedes acceder a mi CV")

with open("Docs/Iván Cepeda, Data Analyst-BI.pdf", "rb") as file:
    btn = st.download_button(
        label="Ivan Cepeda CV",
        data=file,
        file_name="Iván Cepeda, Data Analyst-BI.pdf",
        mime="application/pdf"
    )
