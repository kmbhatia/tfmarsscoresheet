DROP TABLE IF EXISTS posts;CREATE TABLE posts (
    id INTEGER PRIMARY KEY,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    gameid INTEGER,
    tr INTEGER,
    award INTEGER,
    milestone INTEGER,
    gameboard INTEGER,
    cards INTEGER,
    player TEXT NOT NULL
    );