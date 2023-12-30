-- lists all the cities of California that can be found in the database hbtn_0d_usa
USE hbtn_0d_usa;
SELECT id, name
FROM cites
WHERE state_id=
	( SELECT id
	  FROM states
	  WHERE name='Carlifornia'
	)
ORDER BY cities.id ASC