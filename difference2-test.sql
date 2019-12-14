CREATE TABLE friends (
    id INT PRIMARY KEY,
    name TEXT,
    weight FLOAT);

INSERT INTO friends VALUES (1, "Jacela", 32, 165.5);
INSERT INTO friends VALUES (2, "Foxly", 30, 152.4);
INSERT INTO friends VALUES (3, "Pumpkin", NULL, NULL);

SELECT * FROM friends;


CREATE TABLE family (
    id INT PRIMARY KEY,
    name TEXT UNIQUE,
    age INT,
    weight FLOAT);

INSERT INTO family VALUES (1, "Jacela", 32, 165.5);
INSERT INTO family VALUES (2, "Foxly", 30, 152.4);
INSERT INTO family VALUES (3, "Pumpkin", NULL, NULL);

SELECT * FROM family;

UPDATE friends
SET name = "Pumpkin"
WHERE id = 1;

CREATE TABLE messages (
     id int,
     processed char(1) not null,
     receiver int not null,
     message varchar(255),
     primary key (id)
);
