from flask import Flask, request, render_template, redirect, url_for
from match import match_supervisors
from models import db, Answer, MatchResult
from flask_migrate import Migrate  
import uuid
from before_first_request import initialize_data

# Flaskアプリケーションの作成
app = Flask(__name__)

# PostgreSQLへの接続設定（Dockerコンテナ内のdbサービスを使用）
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://your_db_user:your_db_password@db:5432/your_db_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # SQLAlchemyの変更追跡を無効化

# dbインスタンスをFlaskアプリケーションにバインド
db.init_app(app)
migrate = Migrate(app, db)

# データベースの初期化
@app.before_first_request
def init_db():
    db.create_all()  # 初回リクエスト時にテーブルを作成
    # データがない場合は初期データを登録
    if MatchResult.query.count() == 0:
        initialize_data()

# メイン画面を表示
@app.route("/")
def index():
    return render_template('mainmenu.html')

# 質問画面を表示
@app.route('/question', methods=['GET'])
def question():
    return render_template('question.html')

# 結果一覧画面を表示
@app.route('/results_history', methods=['GET'])
def results_history():
    results_history = MatchResult.query.order_by(MatchResult.created_at.desc()).all()
    return render_template('results_history.html', results_history=results_history)

# 結果画面を表示
@app.route('/results', methods=['GET'])
def results():
    matches = request.args.getlist('matches')
    return render_template('results.html',matches=matches)

# メイン画面を表示
@app.route('/mainmenu', methods=['GET'])
def mainmenu():
    return render_template('mainmenu.html')

# 回答を登録
@app.route('/submit_answers', methods=['POST'])
def submit_answers():
    name = request.form.get("name")
    q1 = request.form.get("q1")
    q2 = request.form.get("q2")
    q3 = request.form.get("q3")
    q4 = request.form.get("q4")
    q5 = request.form.get("q5")
    
    id = str(uuid.uuid4())
    # 新しい回答をデータベースに追加
    new_answer = Answer(id=id, name=name, question1=q1, question2=q2, question3=q3, question4=q4, question5=q5)
    db.session.add(new_answer)
    db.session.commit()

    employees = [new_answer]
    matches = match_supervisors(employees)
    
    return render_template('results.html', matches=matches)

# 全てのマッチ履歴を削除するルート
@app.route('/delete_matches', methods=['POST'])
def delete_matches():
    try:
        # MatchResultテーブルの全てのレコードを削除
        while True:
            result = MatchResult.query.order_by(MatchResult.id.desc()).first()
            if not result:  # 削除すべきレコードが無ければ終了
                break
            db.session.delete(result)
            db.session.commit()
        initialize_data() # 初期データを再登録
        return redirect(url_for('index'))  # 削除後にトップページにリダイレクト
    except Exception as e:
        db.session.rollback()
        return f"エラーが発生しました: {str(e)}", 500

# アプリケーションを起動
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)