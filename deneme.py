import streamlit as st
from PIL import Image

im = Image.open(r"C:\Users\eceer\PycharmProjects\pyth\map.jpg")
st.set_page_config(
    page_title="Truckin' App",
    page_icon=im

)
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Data Professor</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://youtube.com/dataprofessor" target="_blank">YouTube</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank">Twitter</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

st.title("Truckin App")
st.text("If you already have a Gantt Chart, upload it here")
st.sidebar.success("Select the Gantt Chart below")

st.file_uploader(
  'Browse files'
)

st.text("If you want to create your own Gantt Chart, Click Here:")
st.button(label="Help me make a Gantt Chart", key=None, help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False)