CREATE DATABASE feedback2;
\connect feedback2
CREATE TABLE feedback (
    id SERIAL,
    satisfaction varChar(100),
    timeEntered timestamp,
    comment text,
    surveyID int,
    PRIMARY KEY (id)
);
