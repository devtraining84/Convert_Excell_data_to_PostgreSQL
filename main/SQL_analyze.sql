
-------------------------------------------------------
drop table if exists payd
CREATE TEMPORARY TABLE payd AS (
	select id from main_palukridersmodel where payment is True
);


drop table if exists tshirts 
CREATE TEMPORARY TABLE TSHIRTS AS (SELECT
	count(id) AS quantity,
	shirt 
FROM 	main_palukridersmodel
WHERE id IN (select id from main_palukridersmodel where payment is True)
GROUP BY 2

UNION ALL

SELECT
	count(id) as quantity,
	P_shirt
FROM 	main_palukridersmodel

GROUP BY 2

ORDER BY 2)
;
-----------------------------------------------------
select  
sum(quantity) as amount,
shirt
 
from tshirts
group by shirt
order by 1 desc;
