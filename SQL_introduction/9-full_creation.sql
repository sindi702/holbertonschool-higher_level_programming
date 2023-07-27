-- full creation
CREATE TABLE IF NOT EXISTS SECOND_TABLE (
    ID INT,
    NAME VARCHAR(256),
    SCORE INT
);

INSERT INTO SECOND_TABLE (
    ID,
    NAME,
    SCORE
) VALUES(
    1,
    "John",
    10
),
(
    2,
    "Alex",
    3
),
(
    3,
    "Bob",
    14
),
(
    4,
    "George",
    8
);