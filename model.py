import csv
import random

shots = ['숏 서브', '롱 서브', '하이클리어', '언더클리어', '헤어핀', '드라이브', '스매시', '드롭', '커트 수비', '클리어 수비']

def get_position(shot, prev_pos=None):
    # 간이 규칙: 기본(Back), 헤어핀/커트수비 후 Front
    if shot in ['헤어핀', '커트 수비']:
        return 'Front'
    return 'Back'

def createData():
    with open('badminton_samples.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['Set','StrokeNo','Team','Player','Shot','Position'])
        for set_num in range(1,101):
            used = {'A':[], 'B':[], 'C':[], 'D':[]}
            seq = [
                ('A-B','A'), ('C-D','C'), ('A-B','A'), ('C-D','D'), 
                ('A-B','B'), ('C-D','C'), ('A-B','B'), ('C-D','D'),
                ('A-B','A'), ('C-D','C')
            ]
            for i, (team, player) in enumerate(seq):
                if i == 0:
                    shot = random.choice(['숏 서브', '롱 서브'])
                else:
                    choices = [s for s in shots if s not in used[player]]
                    shot = random.choice(choices)
                position = get_position(shot)
                used[player].append(shot)
                writer.writerow([set_num, i+1, team, player, shot, position])

