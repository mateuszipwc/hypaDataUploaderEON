# app.py
import streamlit as st

from helpers import (
    DEFAULT_BASE_URL,
    AUTH_PATH,
    ensure_token,
)

from pages_new.lookup_tables import render_lookup_tables_page


def main():
    st.set_page_config(page_title="EON - Hypatos Uploader", page_icon="🧾", layout="centered")
    st.title("🧾 EON - Hypatos Uploader")

    # ---- Global API config (shared for the lookup page) ----
    with st.sidebar:
        st.header("Connection")
        base_url = st.text_input("Base URL", value=DEFAULT_BASE_URL)
        auth_path = st.text_input("Auth token path", value=AUTH_PATH)
        client_id = st.text_input("Client ID")
        client_secret = st.text_input("Client Secret", type="password")

        # Persist config in session
        st.session_state["base_url"] = base_url
        st.session_state["auth_path"] = auth_path
        st.session_state["client_id"] = client_id
        st.session_state["client_secret"] = client_secret

        # Optional token helper
        if st.button("🔑 Get/Refresh Token"):
            ok, msg = ensure_token(base_url, client_id, client_secret, auth_path)
            if ok:
                st.success(msg)
            else:
                st.error(msg)

    # ---- Only Lookup Tables page ----
    render_lookup_tables_page()


if __name__ == "__main__":
    main()