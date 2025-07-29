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
        # padding과 overflow-x 추가로 좌측 잘림 해결 시도
        html_content = f"""
        <style>
        .responsive-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            max-width: 100%;
            height: 80vh;
            max-height: 800px;
            overflow-x: auto;    /* 좌우 스크롤 허용 */
            overflow-y: auto;    /* 필요시 세로 스크롤도 허용 */
            padding-left: 10px;  /* 좌측 여백 추가 */
            box-sizing: border-box; /* 패딩 포함 크기 계산 */
        }}
        .responsive-content {{
            width: 100%;
            max-width: 100%;
            max-height: 100%;
            box-sizing: border-box;
        }}
        </style>

        <div class="responsive-container">
            <div class="responsive-content">
                {html}
            </div>
        </div>
        """

        # height는 적당히 조절하거나 고정값 사용 가능
        htmlviewer.html(html_content, height=600)

with col2:
    with st.expander('Tips..'):
        st.info('Tips..')



st.markdown('<hr>', unsafe_allow_html=True)
st.write('<font color="BLUE">(c)copyright. all rights reserved by CHEOLSEUNG KIM', unsafe_allow_html=True)