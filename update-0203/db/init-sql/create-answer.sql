
CREATE TABLE answers (
    id VARCHAR(36) PRIMARY KEY DEFAULT (gen_random_uuid())::text,
    question1 VARCHAR(100) NOT NULL,
    question2 VARCHAR(100) NOT NULL,
    question3 VARCHAR(100) NOT NULL,
    question4 VARCHAR(100) NOT NULL,
    question5 VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE match_results (
    id VARCHAR(36) PRIMARY KEY DEFAULT (gen_random_uuid())::text,
    employee_name VARCHAR(50) NOT NULL,
    superior_name VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);