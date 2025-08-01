import csv
import random

shots = ['숏 서브', '롱 서브', '하이클리어', '언더클리어', '헤어핀', '드라이브', '스매시', '드롭', '커트 수비', '클리어 수비']
SERVES = ['숏 서브', '롱 서브']

def get_position(shot, prev_pos=None):
    # 간이 규칙: 기본(Back), 헤어핀/커트수비 후 Front
    if shot in ['헤어핀', '커트 수비']:
        return 'Front'
    return 'Back'

def createData():
    with open('badminton_samples.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['Set','StrokeNo','Team','Player','Shot','Position'])
        for set_num in range(1, 101):
            while True:
                # 시퀀스: 총 10번, 팀: A-B/C-D 번갈아, 선수: 2명씩 돌림
                seq = [
                    ('A-B','A'), ('C-D','C'),
                    ('A-B','B'), ('C-D','D'),
                    ('A-B','A'), ('C-D','C'),
                    ('A-B','B'), ('C-D','D'),
                    ('A-B','A'), ('C-D','C')
                ]
                used = {'A': [], 'B': [], 'C': [], 'D': []}
                shots_this_set = []
                ok = True
                for i, (team, player) in enumerate(seq):
                    # 첫 두 타(1,A / 2,C)는 서브
                    if i < 2:
                        shot = random.choice(SERVES)
                    else:
                        # 해당 선수가 아직 고르지 않은 기술 후보 (전부 소진되면 서브도 포함됨)
                        candidates = [s for s in shots if s not in used[player]]
                        # (단, 2번 조건 만족 위해, 마지막 스트로크 차례 등엔 강제 조정 필요)
                        # 서브 제외 중복제외 2가지 미만/이고, 남은 스텝 하나라면 "서브 제외"만 남기기
                        if i >= 8: # 9,10번째 스트로크에서는 조건 강제
                            nonserve_done = set(s for s in used[player] if s not in SERVES)
                            left_cnt = 10 - i
                            # "서브 제외 2가지가 안 됐고 남은 샷이 1/2개면" => 서브 제외만 강제
                            if len(nonserve_done) < 2:
                                candidates = [s for s in candidates if s not in SERVES]
                                if not candidates:
                                    candidates = [s for s in shots if s not in used[player] and s not in SERVES]
                        # 후보가 없으면 다시 전체(서브 포함) 중 아직 안쓴걸로
                        if not candidates:
                            candidates = [s for s in shots if s not in used[player]]
                        shot = random.choice(candidates)
                    used[player].append(shot)
                    shots_this_set.append( (set_num, i+1, team, player, shot, get_position(shot)) )
                # 2. 각 선수별 (서브 제외) 기술 종류가 2가지 이상인지 최종 체크
                ok = True
                for p in ['A','B','C','D']:
                    non_serve = set([s for s in used[p] if s not in SERVES])
                    if len(non_serve) < 2:
                        ok = False
                        break
                # 만약 위 if에서 ok==False면 루프 다시(새로 생성)
                if ok:
                    for record in shots_this_set:
                        writer.writerow(record)
                    break

if __name__ == '__main__':
    createData()
