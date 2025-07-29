import streamlit as st
st.set_page_config(layout="wide", page_title='배드민턴 팀 스트로크 루틴')
import streamlit.components.v1 as htmlviewer

# Title Msg#1
st.title('배드민턴 팀 스트로크 루틴 만들기')

with open('./index.html', 'r', encoding='utf-8') as f:
    html = f.read()
    f.close()

# html = '''
# <html>
#     <head>
#         <title> this is my html </title>
#     </head>

#     <body>
#         <h1>Topic</h1>
#         <h2>SubTopic</h2>
#     </body>
# </html>
# '''
# Box#1(4), Box#2(1)
col1, col2 = st.columns((4, 1))

with col1:
    with st.expander('content #1...'):
        url = 'https://www.youtube.com/watch?v=R5AbqmdVo6w'
        st.info('배드민턴 복식 로테이션을 알아보자!')
        st.video(url)

    with st.expander('content #2...'):
        html_content = f"""
        <style>
        .responsive-wrapper {{
            width: 100%;
            max-width: 1000px; /* 데스크탑 기준 최대 크기 */
            margin: 0 auto;
            box-sizing: border-box;
        }}

        .responsive-content {{
            width: 100%;
            height: auto;
        }}

        @media only screen and (max-width: 600px) {{
            .responsive-wrapper {{
                max-width: 100%;  /* 모바일에서는 전체 화면 */
                padding: 0 5px;
            }}
        }}
        </style>

        <div class="responsive-wrapper">
            <div class="responsive-content">
                {html}
            </div>
        </div>
        """

        htmlviewer.html(html_content, height=600)

with col2:
    with st.expander('Tips..'):
        st.info('Tips..')




st.markdown('<hr>', unsafe_allow_html=True)
st.write('<font color="BLUE">(c)copyright. all rights reserved by CHEOLSEUNG KIM', unsafe_allow_html=True)