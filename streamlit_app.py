import streamlit as st

st.title("🎈 ike cahya's project")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.title("ike cahya's project")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")
import streamlit as st

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
import streamlit as st
st.write
sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"You selected: {sentiment_mapping[selected]}")
