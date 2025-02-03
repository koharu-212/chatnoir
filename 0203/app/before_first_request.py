from models import db, MatchResult
import uuid

def initialize_data():

    # データがない場合は初期データを登録
    id1 = str(uuid.uuid4())
    name1 = "山田太郎"
    best_match1 = "あいり"

    id2 = str(uuid.uuid4())
    name2 = "田中花子"
    best_match2 = "こはる"

    id3 = str(uuid.uuid4())
    name3 = "鈴木一郎"
    best_match3 = "しゅん"

    initialize_data1 = MatchResult(id=id1, employee_name=name1, superior_name=best_match1)
    initialize_data2 = MatchResult(id=id2, employee_name=name2, superior_name=best_match2)  
    initialize_data3 = MatchResult(id=id3, employee_name=name3, superior_name=best_match3)  
    db.session.add(initialize_data1)
    db.session.add(initialize_data2)
    db.session.add(initialize_data3)
    db.session.commit()