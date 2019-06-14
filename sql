
SELECT FirstName, State=(CASE StateCode
 WHEN 'MP' THEN 'Madhya_Pradesh'
 WHEN 'UP' THEN 'Uttar_Pradesh'
 WHEN 'DL' THEN 'Delhi'
 ELSE NULL
 END), PayRate
FROM dbo.Customer

    CASE ISNUMERIC(ABCD_DEF) > 1 THEN NULL

SELECT FirstName,State=(CASE
 WHEN StateCode = 'MP' THEN 'Madhya Pradesh'
 WHEN StateCode = 'UP' THEN 'Uttar Pradesh'
 WHEN StateCode = 'DL' THEN 'Delhi'
 ELSE NULL
 END), PayRate
FROM dbo.Customer