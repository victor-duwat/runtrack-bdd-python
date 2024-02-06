USE LaPlateforme;

SELECT CONCAT('la capacité des sales est de : ', SUM(capacite)) AS capacite_totale
FROM sales;