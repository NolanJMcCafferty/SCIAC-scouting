import mysql
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="marin3rs",
  database="sciac",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

sql = "INSERT INTO pages_pitcher (Team_id,Name,urlname,Year,Hand,APP,GS,W,L,SV,CG,IP,H,ER,BB,K,K_9,HR,ERA) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"


val = [
(3, 'Chris Fousek Jr.', 'chrisfousekjr', 'So.',	'R',	18,	4,	4,	1,	1,	0,	45.2,	41,		13,	6,	33,	6.50,	1,	2.56),
(3, 'Matt Crow',	'mattcrow', 'Fr.',	'R',	12,	2,	2,	0,0,	0,	23.1,	20,		14,	13,	27,	10.41,	0,	5.40),
(3, 'Justin Yang', 'justinyang', 'Fr.', 'R',	19,	0,	1,	3,	6,	0,	22.1,	22,		10,	8,	20,	8.06,	0,	4.03),
(3, 'Austin Williams',	'austinwilliams', 'So.',	'R', 	21,	0,	0,	0,0,	0,	18.2,	15,		7,	9,	6,	2.89,	2,	3.38),
(3, 'Michael Rishebarger', 	'michaelrishebarger', 'So.',	'R',	6,	2,3,	0,	0,	0,	17.0,	9,	6,	3,	4,	2.12,	1,	3.18),
(3, 'Cal Bridges', 'calbridges', 'Fr.',	'R',	10,	0,	1,	0,	0,	0,	13.1,	11,	5,	5,	8,	5.40,	1,	3.38),
(3, 'Nick Hammel',	'nickhammel', 'Fr.', 'R',	11,	0,	1,	0,	0,	0,	12.1,	14,	8,8,	12,	8.76,	0,	5.84),
(3, 'Mason Hitz',	'masonhitz', 'Fr.',	'R',	3,	0,	0,	1,	0,	0,	4.0,	7,	5,	4,	1,	2.25,	0,	11.25),
(3, 'Parker Sand',	'parkersand', 'Fr.', 'L',	3,	0,	0,	0,	0,	0,	3.0,	5,	7,	9,	1,	3.00,	0,	21.00),
(3, 'Jake Stewart',	'jakestewart', 'Fr.', 'R',	2,	0,	0,	0,	0,	0,	3.0,	3,	0,	3,	3,	9.00,	0,	0.00)
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")