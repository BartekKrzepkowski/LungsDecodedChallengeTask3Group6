import streamlit as st
from model_training_service import Code


pred = Code()


@st.cache
def process_prompt(completion_kwargs, topic):
    return pred.model_prediction(completion_kwargs=completion_kwargs, topic=topic)

def intro(api_key):
    # Setting up the Title
    st.title("Ekstraktor informacji medycznych z tekstu wspomagany przez GPT-3")

    st.write("")

    st.image("extr.jpeg", use_column_width=True, caption='.')

    st.write("---")

    st.write(f"""
    ### Disclaimer
    Dana aplikacja jest jedynie prototypem systemu wspomagającego pracę lekarza. 
    Nie powinna być, na tym etapie, używana jako właściwe narzędzie prawidłowej ekstracji informacji z opisu badania.
    """)

    st.write('''
    Możesz przeczytać na temat tego modelu pod podanym linkiem:
    
    GPT-3:
    https://en.wikipedia.org/wiki/GPT-3

    ''')



def func1(api_key):
    st.subheader("1. Wyekstrahuj informacje z tekstu")

    opis_badania = st.text_input('Wprowadz opis badania: ',
                              value='',
                              help='')
    # engine = st.radio('Engine',
    #     ('text-davinci-002', 'text-curie-001', 'text-babbage-001', 'text-ada-001'))
    # temp = st.slider('Temperature:', min_value=0., max_value=1., step=0.05)
    # max_len = st.slider('Max tokens:', min_value=0, max_value=4096 if 'davinci' in engine else 2048,
    #                     step=8, value=1000)
    engine = 'text-davinci-002'
    temp = 0.
    max_len = 1000
    if st.button('Wyekstrahuj informacje'):
        completion_kwargs = {
            "opis_badania2": (opis_badania,),
            "engine": engine,
            "temperature": temp,
            "max_tokens": max_len,
            "api_key": api_key
        }
        st.write('**Wyekstrahowane informacje:**')
        st.write(f"""---""")
        st.subheader('Opis badania:')
        st.write(opis_badania)
        with st.spinner(text='In progress'):
            report_text = process_prompt(completion_kwargs, "opis_badania2")
            report_text = report_text.replace('\n', '  \n')
            import json
            json_string = json.loads(report_text)
            json_dump = json.dumps(json_string)
            print(json_string)
            st.json(json_string, expanded=True)
            st.success('Done')
        st.download_button(
            label="Ściągnij wyekstrahowane dane w formacie JSON:",
            data=json_dump,
            file_name=f'wyekstrahowane_informacje.json',
            mime="application/json"
        )

