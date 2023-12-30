-- lists all the cities of California that can be found in the database hbtn_0d_usa
USE hbtn_0d_usa;
SELECT *
FROM cites
WHERE cities.state_id=
	( SELECT id
	  FROM states
	  WHERE name='Carlifornia'
	)
ORDER BY cities.id ASC
