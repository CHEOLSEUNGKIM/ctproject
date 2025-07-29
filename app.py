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
# col1, col2 = st.columns((4,1))
# with col1:
#     with st.expander('content #1...'):
#         url = 'https://www.youtube.com/watch?v=R5AbqmdVo6w'
#         st.info('배드민턴 복식 로테이션을 알아보자!')
#         st.video(url)
    
#     with st.expander('content #2...'):
#         #st.write(html, unsafe_allow_html=True)
#         htmlviewer.html(html, height=800)
        
# with col2:
#     with st.expander('Tips..'):
#         st.info('Tips..')

col1, col2 = st.columns((4,1))

with col1:
    with st.expander('content #1...'):
        url = 'https://www.youtube.com/watch?v=R5AbqmdVo6w'
        st.info('배드민턴 복식 로테이션을 알아보자!')
        st.video(url)
        
    with st.expander('content #2...'):
        # 수평/수직 중앙 정렬을 위해 div로 감싸고, CSS flexbox를 활용합니다.
        # width: 100%로 가득 채우면서 내부 콘텐츠는 최대 너비(예: 100%)를 넘지 않도록 조절합니다.
        # height는 min(80vh, 800px)로 화면 높이에 따라 크기가 달라지도록 설정했습니다.
        html_content = f"""
        <div style="
            display: flex;
            justify-content: center;
            align-items: center;
            height: min(80vh, 800px);
            width: 100%;
            ">
            <div style="width: 100%; max-width: 100%;">
                {html}
            </div>
        </div>
        """
        htmlviewer.html(html_content, height=None)

with col2:
    with st.expander('Tips..'):
        st.info('Tips..')

st.markdown('<hr>', unsafe_allow_html=True)
st.write('<font color="BLUE">(c)copyright. all rights reserved by CHEOLSEUNG KIM', unsafe_allow_html=True)