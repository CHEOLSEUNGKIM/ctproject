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
        .responsive-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            height: 80vh; /* 화면 높이 80%로 반응형 */
            max-height: 800px;
            padding-left: 10px;
            padding-right: 10px;
            box-sizing: border-box;
            overflow-x: auto;
            overflow-y: auto;
        }}
        .responsive-content {{
            width: 100%;
            max-width: 100%;
            height: 100%;
            box-sizing: border-box;
        }}

        /* 모바일 대응: 화면 폭 600px 이하일 때 크기 조정 */
        @media only screen and (max-width: 600px) {{
            .responsive-container {{
                height: 60vh;
                padding-left: 5px;
                padding-right: 5px;
            }}
            .responsive-content {{
                transform: scale(0.7);  /* 60% 더 축소 */
                transform-origin: top center;
            }}
        }}
        </style>

        <div class="responsive-container">
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