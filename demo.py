import streamlit as st

def intro():
    import streamlit as st

    st.write("# Exemplos de aplicações Streamlit! 🗒")
    st.sidebar.success("Selecione uma demonstração.")

    st.markdown(
        """
        Streamlit é um framework open-source criada especificamente para
        Projetos de Machine Learning e Data Science.

        **👈Selecione uma demonstração no menu suspenso à esquerda** para ver alguns exemplos
        do que Streamlit pode fazer!

        ### Onde aprender mais?

        - Confira [streamlit.io](https://streamlit.io)
        - Entre na [documentação](https://docs.streamlit.io)
        - Faça perguntas no [forum da comunidade](https://discuss.streamlit.io)

        ### Veja demonstrações mais complexas

        - Use uma rede neural [analisar um dataset de imagens de carros autônomos da Udacity](https://github.com/streamlit/demo-self-driving)
        - Explore um [dataset de viagens compartilhadas de Nova York](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )

def mapping_demo():
    import streamlit as st
    import pandas as pd
    import pydeck as pdk

    from urllib.error import URLError

    st.markdown(f"# {list(page_names_to_funcs.keys())[2]}")
    st.write(
        """
        Demonstração que mostra como usar
[`st.pydeck_chart`](https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart)
para exibir dados geoespaciais.
"""
    )

    @st.cache_data
    def from_data_file(filename):
        url = (
            "http://raw.githubusercontent.com/streamlit/"
            "example-data/master/hello/v1/%s" % filename
        )
        return pd.read_json(url)

    try:
        ALL_LAYERS = {
            "Aluguel de bicicletas": pdk.Layer(
                "HexagonLayer",
                data=from_data_file("bike_rental_stats.json"),
                get_position=["lon", "lat"],
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                extruded=True,
            ),
            "Bart Stop Exits": pdk.Layer(
                "ScatterplotLayer",
                data=from_data_file("bart_stop_stats.json"),
                get_position=["lon", "lat"],
                get_color=[200, 30, 0, 160],
                get_radius="[exits]",
                radius_scale=0.05,
            ),
            "Bart Stop Names": pdk.Layer(
                "TextLayer",
                data=from_data_file("bart_stop_stats.json"),
                get_position=["lon", "lat"],
                get_text="name",
                get_color=[0, 0, 0, 200],
                get_size=15,
                get_alignment_baseline="'bottom'",
            ),
            "Fluxo de saída": pdk.Layer(
                "ArcLayer",
                data=from_data_file("bart_path_stats.json"),
                get_source_position=["lon", "lat"],
                get_target_position=["lon2", "lat2"],
                get_source_color=[200, 30, 0, 160],
                get_target_color=[200, 30, 0, 160],
                auto_highlight=True,
                width_scale=0.0001,
                get_width="outbound",
                width_min_pixels=3,
                width_max_pixels=30,
            ),
        }
        st.sidebar.markdown("### Camadas do mapa")
        selected_layers = [
            layer
            for layer_name, layer in ALL_LAYERS.items()
            if st.sidebar.checkbox(layer_name, True)
        ]
        if selected_layers:
            st.pydeck_chart(
                pdk.Deck(
                    map_style="mapbox://styles/mapbox/light-v9",
                    initial_view_state={
                        "latitude": 37.76,
                        "longitude": -122.4,
                        "zoom": 11,
                        "pitch": 50,
                    },
                    layers=selected_layers,
                )
            )
        else:
            st.error("Please choose at least one layer above.")
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**

            Connection error: %s
        """
            % e.reason
        )

def plotting_demo():
    import streamlit as st
    import time
    import numpy as np

    st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')
    st.write(
        """
        Esta demonstração ilustra uma combinação de plotagem e animação com Streamlit. Está sendo gerado vários números aleatórios em um loop por cerca de 5 segundos.
"""
    )

    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text("%i%% Completo" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

    progress_bar.empty()

    # Os widgets do Streamlit executam automaticamente o script
    # de cima para baixo. Como este botão não está conectado a
    # nenhuma outra lógica, ele apenas causa uma repetição simples.

    st.button("Recarregar")


def data_frame_demo():
    import streamlit as st
    import pandas as pd
    import altair as alt

    from urllib.error import URLError

    st.markdown(f"# {list(page_names_to_funcs.keys())[3]}")
    st.write(
        """
        Esta demonstração mostra como usar `st.write` para visualizar DataFrames do Pandas.

(Dados de [UN Data Explorer](http://data.un.org/Explorer.aspx).)
"""
    )

    @st.cache_data
    def get_UN_data():
        AWS_BUCKET_URL = "http://streamlit-demo-data.s3-us-west-2.amazonaws.com"
        df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
        return df.set_index("Region")

    try:
        df = get_UN_data()
        countries = st.multiselect(
            "Países para analise", list(df.index), ["China", "United States of America"]
        )
        if not countries:
            st.error("Por favor, selecione pelo menos um país.")
        else:
            data = df.loc[countries]
            data /= 1000000.0
            st.write("### Produção Agrícola Bruta ($B)", data.sort_index())

            data = data.T.reset_index()
            data = pd.melt(data, id_vars=["index"]).rename(
                columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
            )
            chart = (
                alt.Chart(data)
                .mark_area(opacity=0.3)
                .encode(
                    x=alt.X("year:T", title="ano"),
                    y=alt.Y("Gross Agricultural Product ($B):Q", stack=None, title="Produção Agrícola Bruta ($B)"),
                    color="Region:N",
                )
            )
            st.altair_chart(chart, use_container_width=True)
    except URLError as e:
        st.error(
            """
            **Para visualizar os dados, precisa está conectado a internet.**

            Erro de conexão: %s
        """
            % e.reason
        )

page_names_to_funcs = {
    "—": intro,
    "Plotting Demo": plotting_demo,
    "Mapping Demo": mapping_demo,
    "DataFrame Demo": data_frame_demo
}

demo_name = st.sidebar.selectbox("Escolha um exemplo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()