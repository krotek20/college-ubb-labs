use L1
go

create view ViewGeneralManagers as
select ID, NAME, ROLE, CONTACT
from GENERAL_MANAGER
go

create view ViewRegisteredClients as
select CLIENT.ID as CLIENT_ID, 
	   CLIENT.NAME as CLIENT,
	   CLIENT.AGE as AGE,
	   CLIENT.CONTACT as CONTACT,
	   FIDELITY_CARD.ID as FIDELITY_CARD_ID,
	   FIDELITY_CARD.ACTIVATED_DATE as ACTIVATED_DATE
from CLIENT
	   join FIDELITY_CARD on CLIENT.ID_CARD = FIDELITY_CARD.ID
go

create view ViewProductsOffers as
select PRODUCT.NAME as PRODUCT,
	   PRODUCT.PRODUCER as PRODUCER,
	   PRODUCT.PRICE as PRICE,
       convert(decimal(10,2), (PRODUCT.PRICE + 0.0) - ((PRODUCT_OFFERS.DISCOUNT + 0.0) * (PRODUCT.PRICE + 0.0) / 100.0)) as PRICE_AFTER_DISCOUNT
from PRODUCT PRODUCT
       join PRODUCT_OFFERS on PRODUCT_OFFERS.ID_PRODUCT = PRODUCT.ID
group by PRODUCT.NAME, PRODUCT.PRODUCER, PRODUCT.PRICE, PRODUCT_OFFERS.DISCOUNT
go

create view ViewProductsOffersByShop as
select PRODUCT.NAME as PRODUCT,
       PRODUCT.PRODUCER as PRODUCER,
	   PRODUCT.PRICE as PRICE,
	   PRODUCT_OFFERS.DISCOUNT as DISCOUNT,
	   SHOP.LOCATION as LOCATION,
	   SHOP.OPEN_HOUR as OPEN_HOUR,
	   SHOP.CLOSE_HOUR as CLOSE_HOUR
from SHOP_OFFER
	  join SHOP on SHOP.ID = SHOP_OFFER.ID_SHOP
	  join PRODUCT_OFFERS on PRODUCT_OFFERS.ID = SHOP_OFFER.ID_OFFER
	  join PRODUCT on PRODUCT.ID = PRODUCT_OFFERS.ID_PRODUCT
go