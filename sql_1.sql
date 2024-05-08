SELECT c.login, COUNT(o.id) AS "deliveryCount"
FROM "Couriers" c
LEFT JOIN "Orders" o ON c.id = o."courierId"
WHERE o."inDelivery" = true
GROUP BY c.login;