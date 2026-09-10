import streamlit as st


def feature_card(icon, title, description):

    st.markdown(
        f"""
        <div class="card">

        <h2>{icon}</h2>

        <h3>{title}</h3>

        <p>{description}</p>

        </div>
        """,
        unsafe_allow_html=True,
    )