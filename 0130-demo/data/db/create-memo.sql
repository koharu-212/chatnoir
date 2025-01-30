-- テーブル作成
CREATE TABLE IF NOT EXISTS Answer (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    namae VARCHAR(100) NOT NULL,
    question1 VARCHAR(100) NOT NULL,
    question2 VARCHAR(100) NOT NULL,
    question3 VARCHAR(100) NOT NULL,
    question4 VARCHAR(100) NOT NULL,
    question5 VARCHAR(100) NOT NULL
);

-- ダミーデータ挿入
INSERT INTO Answer (id, namae, question1, question2,question3, question4, question5) VALUES
('3b4b60c6-3a90-48c9-b8ed-4df5d1231231', '山田太郎', 'INTJ', '個人で集中して進める', '最低限の連絡で済ませたい', '自由に任せてくれる人', 'スキルの成長を感じたとき'),
('3b4b60c6-3a90-48c9-b8ed-4df5d1231232', '山田花子', 'INTJ', '個人で集中して進める', '最低限の連絡で済ませたい', '自由に任せてくれる人', 'スキルの成長を感じたとき'),
('3b4b60c6-3a90-48c9-b8ed-4df5d1231233', '山田次郎', 'INTJ', '個人で集中して進める', '最低限の連絡で済ませたい', '自由に任せてくれる人', 'スキルの成長を感じたとき');