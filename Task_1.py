# Создаем через API 2 курьера и 3 заказа. 
# Через Android Studio Первый курьер принимает 1 заказ,  второй курьер принимает 2 заказа. 
# Так как во вкладе "Мои" баг и принятый заказ дублируется,  соответсвенно у 1го курьера 2 заказа, у 2го 4 заказа

SELECT c.login,
       COUNT(o.id) AS delivery_count
FROM "Couriers" AS c
LEFT JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery" = true
GROUP BY c.login;