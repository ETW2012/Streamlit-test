import streamlit as st

st.set_page_config(page_title="Font Size Demo")

# Example: Change font size using HTML + CSS
st.markdown(
    """
    <style>
    .big-font {
        font-size:30px !important;
        color:#A9A9A9;
    </style>
    """,
    unsafe_allow_html=True
)

if 'times_clicked' not in st.session_state:
    st.session_state['times_clicked'] = 0

plus_1 = st.button('Plus 1')

if (plus_1):
    st.session_state['times_clicked'] += 1

plus_2 = st.button('Plus 2')

if (plus_2):
    st.session_state['times_clicked'] += 2

plus_3 = st.button('Plus 3')

if (plus_3):
    st.session_state['times_clicked'] += 3

plus_4 = st.button('Plus 4')

if (plus_4):
    st.session_state['times_clicked'] += 4

reset = st.button('Reset')

if (reset):
    st.session_state['times_clicked'] = 0

st.markdown(st.button plus_1:hover {
    transition: scale(1.05);
}
     
    ,unsafe_allow_html=True
)

#st.write('Button clicked', st.session_state['times_clicked'], 'times.')
st.markdown('<p class="big-font">Button clicked ' + str(st.session_state['times_clicked']) + ' times.</p>', unsafe_allow_html=True)

