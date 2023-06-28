CREATE TABLE language (
  language_id VARCHAR(2) PRIMARY KEY,
  language_name VARCHAR(100)
);

CREATE TABLE translation (
    id SERIAL PRIMARY KEY,
    source_text TEXT,
    source_language VARCHAR(2),
    target_language VARCHAR(2),
    translated_text TEXT
);

CREATE USER api_project WITH PASSWORD 'apiproject123';
GRANT ALL PRIVILEGES ON DATABASE english_swahili TO api_project;
