import streamlit as st
import streamlit.components.v1 as htmlviewer
from model import createData

st.set_page_config(layout="wide", page_title='배드민턴 팀 스트로크 루틴')
st.title('배드민턴 팀 스트로크 루틴 만들기')

with open('./index.html', 'r', encoding='utf-8') as f:
    html = f.read()

col1, col2 = st.columns((4, 1))

with col1:
    with st.expander('content #1'):
        url = 'https://www.youtube.com/watch?v=R5AbqmdVo6w'
        st.info('배드민턴 복식 로테이션을 알아보자!')
        st.video(url)

with col1:
    with st.expander("content #2"):
        st.info("배드민턴 기술을 분류하고, 상황에 맞는 포지셔닝을 학습해보자!")
        st.markdown("### 🏸 배드민턴 기술 분류 드래그 앤 드롭 시뮬레이터")

        drag_drop_html = """
        <style>
          .container {
            display: flex;
            justify-content: space-around;
            margin-top: 20px;
            gap: 20px;
          }
          .drop-box {
            width: 45%;
            min-height: 220px;
            border: 2px dashed #888;
            border-radius: 10px;
            padding: 12px;
            background-color: #f5f5f5;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 8px;
          }
          .drop-box.drag-over {
            background-color: #eef5ff;
            border-color: #5b9bd5;
          }
          .drop-box h3 {
            text-align: center;
            color: #444;
            margin-top: 4px;
            margin-bottom: 8px;
          }
          .draggable-items {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 24px;
          }
          .item {
            padding: 10px 15px;
            background-color: #d9edf7;
            border-radius: 8px;
            border: 1px solid #bce8f1;
            cursor: grab;
            user-select: none;
            margin: 0;
            width: auto;
            box-sizing: border-box;
          }
        </style>

        <div class="container">
          <div class="drop-box" id="front" ondrop="drop(event)" ondragover="allowDrop(event)" ondragleave="leave(event)">
            <h3>전위 기술</h3>
          </div>
          <div class="drop-box" id="rear" ondrop="drop(event)" ondragover="allowDrop(event)" ondragleave="leave(event)">
            <h3>후위 기술</h3>
          </div>
        </div>

        <div class="draggable-items" id="start-zone">
          <div class="item" draggable="true" ondragstart="drag(event)" id="헤어핀">헤어핀</div>
          <div class="item" draggable="true" ondragstart="drag(event)" id="푸시">푸시</div>
          <div class="item" draggable="true" ondragstart="drag(event)" id="언더클리어">언더클리어</div>
          <div class="item" draggable="true" ondragstart="drag(event)" id="드라이브">드라이브</div>
          <div class="item" draggable="true" ondragstart="drag(event)" id="드롭">드롭</div>
          <div class="item" draggable="true" ondragstart="drag(event)" id="하이클리어">하이클리어</div>
          <div class="item" draggable="true" ondragstart="drag(event)" id="스매시">스매시</div>
        </div>

        <div style="margin-top: 20px; text-align: center;">
          <button onclick="checkAnswer()">정답 제출</button>
          <button onclick="resetItems()">재도전</button>
        </div>

        <script>
        const frontCorrect = ["헤어핀", "푸시", "언더클리어"];
        const rearCorrect = ["드라이브", "드롭", "하이클리어", "스매시"];
        let originalZone = document.getElementById("start-zone");

        function allowDrop(ev) {
          ev.preventDefault();
          ev.currentTarget.classList.add("drag-over");
        }

        function leave(ev) {
          ev.currentTarget.classList.remove("drag-over");
        }

        function drag(ev) {
          ev.dataTransfer.setData("text/plain", ev.target.id);
        }

        function drop(ev) {
          ev.preventDefault();
          ev.currentTarget.classList.remove("drag-over");
          const data = ev.dataTransfer.getData("text/plain");
          const dragged = document.getElementById(data);
          ev.currentTarget.appendChild(dragged);
        }

        function checkAnswer() {
          let frontBox = document.getElementById("front");
          let rearBox = document.getElementById("rear");

          let frontItems = Array.from(frontBox.querySelectorAll(".item")).map(el => el.id);
          let rearItems = Array.from(rearBox.querySelectorAll(".item")).map(el => el.id);

          frontItems.sort();
          rearItems.sort();
          let isCorrect = JSON.stringify(frontItems) === JSON.stringify(frontCorrect.sort()) &&
                          JSON.stringify(rearItems) === JSON.stringify(rearCorrect.sort());

          alert(isCorrect ? "정답입니다! 🎉" : "오답입니다. 다시 시도해보세요!");
        }

        function resetItems() {
          const allItems = document.querySelectorAll(".item");
          allItems.forEach(item => {
            originalZone.appendChild(item);
          });
        }
        </script>
        """
        htmlviewer.html(drag_drop_html, height=640)

        st.markdown("---")
        st.subheader("📌 사용한 기술에 따른 포지셔닝 선택")
        col_left, col_right = st.columns(2)

        with col_left:
            selected_skill = st.selectbox("🎯 내가 사용한 기술", [
                "헤어핀", "푸시", "언더클리어", "드라이브", "드롭", "하이클리어", "스매시"
            ])
        with col_right:
            selected_position = st.selectbox("🧍 우리 팀의 포지셔닝", [
                "앞-뒤 (공격형 포지션)", "양 옆 (수비형 포지션)"
            ])
        st.success(f"✅ **선택한 기술**: {selected_skill} → **우리 팀 포지션**: {selected_position}")

with col1:
    with st.expander('content #3'):
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
            width: 1000px;
            max-width: 1000px;
        }}
        @media only screen and (max-width: 600px) {{
            .fixed-content {{
                width: 800px;
            }}
        }}
        </style>
        <div class="scroll-container">
            <div class="fixed-content">
                {html}
            </div>
        </div>
        """
        htmlviewer.html(html_content, height=900)

with col2:
    with st.expander('Tips..'):
        st.info('Tips..')

st.markdown('<hr>', unsafe_allow_html=True)
st.write('<font color="BLUE">(c)copyright. all rights reserved by CHEOLSEUNG KIM', unsafe_allow_html=True)
