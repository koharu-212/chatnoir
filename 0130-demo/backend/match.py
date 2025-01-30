from collections import Counter
from models import db, Answer, MatchResult
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import UUID as UUIDType

# 上司のマッチング表
matching_criteria = {
    "MBTI": {
        "INTJ": "あいり", "ENTP": "しゅん", "INFJ": "みさき", "ESTP": "こはる",
        "ISTJ": "こはる", "ISFJ": "きずな", "ENTJ": "こはる", "ENFP": "きずな",
        "ISTP": "あいり", "ISFP": "しゅん", "ESTJ": "あいり", "ESFJ": "みさき",
        "INFP": "きずな", "ESFP": "しゅん", "INTP": "みさき", "ENFJ": "あいり"
    },
    "仕事の進め方": {
        "チーム全員で意見を出し合いながら進める": "あいり",
        "個人で集中して進める": "こはる",
        "明確な計画に基づいて進める": "みさき",
        "必要に応じて方法を調整する": "しゅん",
        "柔軟に対応しながら進める": "きずな"
    },
    "コミュニケーション方法": {
        "チャットやメールでのやり取りが中心": "あいり",
        "最低限の連絡で済ませたい": "こはる",
        "定期的なミーティングで進捗を確認する": "みさき",
        "直接あって話し相談する": "しゅん",
        "必要に応じて適切な方法を選ぶ": "きずな"
    },
    "理想の上司像": {
        "常にチーム全体を気にかけてくれる人": "あいり",
        "自由に任せてくれる人": "こはる",
        "明確な指示を出してくれる人": "みさき",
        "必要なときにだけサポートしてくれる人": "しゅん",
        "対話を重視しながら一緒に進めてくれる人": "きずな"
    },
    "モチベーションの源泉": {
        "チームで成功したとき": "あいり",
        "スキルの成長を感じたとき": "こはる",
        "目標を達成したとき": "みさき",
        "新しいチャレンジに成功したとき": "しゅん",
        "周囲から認められたとき": "きずな"
    }
}

# マッチング処理関数
def match_supervisors(employees):
    matches = []

    for emp in employees:
        match_counts = Counter()
        
        # 各質問に対して対応する上司をカウント
        match_counts[matching_criteria["MBTI"].get(emp.question1, "")] += 1.5
        match_counts[matching_criteria["仕事の進め方"].get(emp.question2, "")] += 1
        match_counts[matching_criteria["コミュニケーション方法"].get(emp.question3, "")] += 1
        match_counts[matching_criteria["理想の上司像"].get(emp.question4, "")] += 1
        match_counts[matching_criteria["モチベーションの源泉"].get(emp.question5, "")] += 1

        # 一番カウントが多い上司を選ぶ
        best_match = match_counts.most_common(1)[0][0]

        # データベースに保存
    new_match = MatchResult(id=emp.id, employee_name=emp.name, superior_name=best_match)
    db.session.add(new_match)
    db.session.commit()

    matches.append(new_match)
    
    return matches
