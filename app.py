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
        .scroll-container {{
            width: 100%;
            overflow-x: auto;
            overflow-y: auto;
            padding: 10px;
            box-sizing: border-box;
        }}
        .fixed-content {{
            width: 1000px;  /* 콘텐츠 고정 너비 (모바일보다 넓게) */
            max-width: 1000px;
        }}

        @media only screen and (max-width: 600px) {{
            .fixed-content {{
                width: 800px;  /* 모바일에서도 충분히 넓게 설정 */
            }}
        }}
        </style>

        <div class="scroll-container">
            <div class="fixed-content">
                {html}
            </div>
        </div>
        """

        htmlviewer.html(html_content, height=1000)

with col2:
    with st.expander('Tips..'):
        st.info('Tips..')




st.markdown('<hr>', unsafe_allow_html=True)
st.write('<font color="BLUE">(c)copyright. all rights reserved by CHEOLSEUNG KIM', unsafe_allow_html=True)