use L1
go

-- 1. afiseaza managerii locali din Turda ordonati crescator dupa rol
select LOCAL_MANAGER.NAME as Name, LOCAL_MANAGER.ROLE as Role, CITY.NAME as City
from LOCAL_MANAGER
	join CITY on LOCAL_MANAGER.ID_CITY = CITY.ID
where CITY.NAME = 'Turda'
order by Role asc

-- 2. afiseaza angajatii din Cluj-Napoca cu salarii mai mari de 2000
select EMPLOYEE.NAME as Name, EMPLOYEE.SALARY as Salary, CITY.NAME as City
from EMPLOYEE
	join SHOP on EMPLOYEE.ID_SHOP = SHOP.ID
	join CITY on SHOP.ID_CITY = CITY.ID
where CITY.NAME = 'Cluj-Napoca' and EMPLOYEE.SALARY > 2000

-- 3. afiseaza cei mai noi 5 posesori de card de fidelitate
select distinct top(5) CLIENT.NAME as Client, FIDELITY_CARD.ACTIVATED_DATE as Activated_Date, CITY.NAME as City
from FIDELITY_CARD
	join CLIENT on FIDELITY_CARD.ID = CLIENT.ID_CARD
	join SHOP on SHOP.ID = FIDELITY_CARD.ID_SHOP
	join CITY on CITY.ID = SHOP.ID_CITY
order by Activated_Date desc

-- 4. afiseaza cel mai mare discount al produselor din fiecare oras, ordonat descrescator
select CITY.NAME as City, max(PRODUCT_OFFERS.DISCOUNT) as Discount
from PRODUCT_OFFERS
	join SHOP_OFFER on PRODUCT_OFFERS.ID = SHOP_OFFER.ID_OFFER
	join SHOP on SHOP.ID = SHOP_OFFER.ID_SHOP
	right join CITY on CITY.ID = SHOP.ID_CITY
group by CITY.NAME
having max(PRODUCT_OFFERS.DISCOUNT) is not null
order by Discount desc

-- 5. afiseaza toti clientii cu cumparaturi de peste 50 de lei din anul curent
--	  clientii vor fi ordonati descarescator dupa data chitantei
select CLIENT.NAME as Client, RECEIPT.TOTAL_PRICE as TotalPrice, RECEIPT.DATE as Date
from RECEIPT
	join CLIENT ON RECEIPT.ID_CLIENT = CLIENT.ID
where year(RECEIPT.DATE) = year(getdate()) and RECEIPT.TOTAL_PRICE > 50
order by Date desc

-- 6. afiseaza randurile celei mai noi chitante
select CLIENT.NAME as Client, RECEIPT.DATE as Date, PRODUCT.NAME as Product,
	   RECEIPT_ROWS.UNITS as Units, RECEIPT_ROWS.PRICE_UNIT as Price_Unit,
	   PRODUCT_OFFERS.DISCOUNT as Discount
from RECEIPT_ROWS
	join RECEIPT on RECEIPT.ID = RECEIPT_ROWS.ID_RECEIPT
	join CLIENT on CLIENT.ID = RECEIPT.ID_CLIENT
	join PRODUCT on PRODUCT.ID = RECEIPT_ROWS.ID_PRODUCT
	join PRODUCT_OFFERS on PRODUCT.ID = PRODUCT_OFFERS.ID_PRODUCT
where RECEIPT.DATE = (select max(RECEIPT.DATE) 
					  from RECEIPT)
order by Date desc

-- 7. afiseaza cele mai vandute 5 produse din ultima luna
select distinct top(5) PRODUCT.NAME as Product, count(*) as Units_Purchased
from PRODUCT
	join RECEIPT_ROWS on PRODUCT.ID = RECEIPT_ROWS.ID_PRODUCT
	join RECEIPT on RECEIPT.ID = RECEIPT_ROWS.ID_RECEIPT
where year(RECEIPT.DATE) = year(getdate()) and month(RECEIPT.DATE) = month(getdate())
group by PRODUCT.NAME
having count(*) >= 1
order by Units_Purchased desc

-- 8. afiseaza produsele cu pretul final (dupa discount), ordonate descrescator dupa discount
select PRODUCT.NAME as Product, PRODUCT.PRICE as Price, PRODUCT_OFFERS.DISCOUNT as Discount,
	   (PRODUCT.PRICE + 0.0) - ((PRODUCT_OFFERS.DISCOUNT + 0.0) * (PRODUCT.PRICE + 0.0) / 100.0) as Final_Price
from PRODUCT
	left join PRODUCT_OFFERS on PRODUCT.ID = PRODUCT_OFFERS.ID_PRODUCT
order by Discount desc

-- 9. afiseaza magazinele care nu au oferte, ordonate crescator dupa oras
select CITY.NAME as City, SHOP.LOCATION as Adress, count(SHOP_OFFER.ID_SHOP) as Offers
from SHOP_OFFER
	join PRODUCT_OFFERS on PRODUCT_OFFERS.ID = SHOP_OFFER.ID_OFFER
	right join SHOP on SHOP.ID = SHOP_OFFER.ID_SHOP
	join CITY on CITY.ID = SHOP.ID_CITY
group by CITY.NAME, SHOP.LOCATION
having count(SHOP_OFFER.ID_SHOP) = 0
order by City asc

-- 10. afiseaza detinatorii de card de fidelitate care nu au facut cumparaturi in ultima luna
select distinct CLIENT.NAME as Client, CLIENT.CONTACT as Contact, CITY.NAME as City
from RECEIPT
	right join CLIENT on CLIENT.ID = RECEIPT.ID_CLIENT
	join FIDELITY_CARD on FIDELITY_CARD.ID = CLIENT.ID_CARD
	join SHOP on SHOP.ID = FIDELITY_CARD.ID_SHOP
	join CITY on CITY.ID = SHOP.ID_CITY
where exists (select *
			  from CLIENT 
			  where CLIENT.ID = RECEIPT.ID_CLIENT)
	  and year(RECEIPT.DATE) = year(getdate())
	  and month(RECEIPT.DATE) = month(getdate())