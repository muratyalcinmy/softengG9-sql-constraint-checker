sample
sample
sample
CREATE TABLE Student
(
ID int(6) NOT NULL,
NAME                        varchar(10) NOT NULL,
ADDRESS varchar(    2   0   )
);sample
sample
sample
sample
CREATE TABLE Orders
(
                        O_ID int NOT NULL,
ORDER_NO int NOT NULL,
C_ID int,
PRIMARY KEY                 (O_ID),
FOREIGN KEY (C_ID) REFERENCES Customers(C_ID)
);sample
sample
sample
sample