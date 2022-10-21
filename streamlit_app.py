import streamlit as st

from streamlit_compose import intro, func1
PAGES = {
    'Dashboard': intro,
    'Wyekstrahuj informacje z opisu badania': func1,
}


def main_app():
    # Creating an object of prediction service
    api_key = st.sidebar.text_input("OpenAI API Key:", type="password", value='XXX')

    with st.sidebar:
        selection = st.radio("", list(PAGES.keys()))

    if api_key:
        PAGES[selection](api_key)
    else:
        st.error("🔑 API Key Not Found!")
        st.info("💡 Copy paste your OpenAI API key that you can find in User -> API Keys section once you log in to the OpenAI API Playground")


if __name__ == '__main__':
    main_app()

