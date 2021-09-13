use L1
go


-- Constraints
alter table CITY
add constraint uqCityName unique (NAME)
go

alter table PRODUCT
add constraint chkProductPrice check (PRICE > 0)
go

alter table PRODUCT_OFFERS
add constraint chkProductDiscount check (DISCOUNT between 0 and 100)
go

alter table SHOP
add constraint chkShopHoursValue check 
(OPEN_HOUR between 0 and 23 and CLOSE_HOUR between 0 and 23)
go

alter table SHOP
add constraint chkShopHoursLogic check (OPEN_HOUR < CLOSE_HOUR)
go


-- Validators
create or alter function fctCheckStringContainsOnlyLetters (@str nvarchar(255))
returns int
as
begin
	declare @ret int = 1
	declare @i int = 1, @substr nvarchar(10)
	while @i <= (select len(@str)) and @ret = 1
	begin
		set @substr = substring(@str, @i, 1)
		if (@substr < 'A' or @substr > 'Z') and
			(@substr < 'a' or @substr > 'z')
		begin
			set @ret = 0
		end
		set @i = @i + 1
	end
	return @ret
end
go

create or alter function fctValidateName (@name nvarchar(255))
returns int
as
begin
	if len(@name) = 0
	begin
		return 0
	end
	declare @c varchar(1) = substring(@name, 1, 1)
	if unicode(@c) like unicode(lower(@c))
	begin
		return 0
	end
	return dbo.fctCheckStringContainsOnlyLetters(@name)
end
go


-- PRODUCT CRUD
create or alter proc uspInsertProduct @NAME nvarchar(255),
									  @PRODUCER nvarchar(255),
									  @PRICE int
as
begin
	if dbo.fctValidateName(@NAME) = 0
	begin
		throw 50001, 'Name not valid!', 1
	end
	if dbo.fctValidateName(@PRODUCER) = 0
	begin
		throw 50001, 'Producer not valid!', 1
	end

	insert into PRODUCT (NAME, PRODUCER, PRICE)
	values (@NAME, @PRODUCER, @PRICE)
end
go

create or alter proc uspDeleteProduct @ID_PRODUCT int
as
begin
	if not exists (select ID from PRODUCT where ID = @ID_PRODUCT)
	begin
		throw 50001, 'Product does not exists!', 1
	end

	delete from PRODUCT where ID = @ID_PRODUCT
end
go

create or alter proc uspUpdateProduct @ID_PRODUCT int,
									  @NAME nvarchar(255),
									  @PRODUCER nvarchar(255),
									  @PRICE int
as
begin
	if not exists (select ID from PRODUCT where ID = @ID_PRODUCT)
	begin
		throw 50001, 'Product does not exists!', 1
	end
	if dbo.fctValidateName(@NAME) = 0
	begin
		throw 50001, 'Name not valid!', 1
	end
	if dbo.fctValidateName(@PRODUCER) = 0
	begin
		throw 50001, 'Producer not valid!', 1
	end
	
	update PRODUCT
	set NAME = @NAME, PRODUCER = @PRODUCER, PRICE = @PRICE
	where ID = @ID_PRODUCT
end
go


-- PRODUCT_OFFERS CRUD
create or alter proc uspInsertProductOffer @DISCOUNT int,
									       @ID_PRODUCT int
as
begin
	if not exists (select ID from PRODUCT where ID = @ID_PRODUCT)
	begin
		throw 50001, 'Product does not exists!', 1
	end

	insert into PRODUCT_OFFERS (DISCOUNT, ID_PRODUCT)
	values (@DISCOUNT, @ID_PRODUCT)
end
go

create or alter proc uspDeleteProductOffer @ID_PRODUCT_OFFER int
as
begin
	if not exists (select ID from PRODUCT_OFFERS where ID = @ID_PRODUCT_OFFER)
	begin
		throw 50001, 'Offer does not exists!', 1
	end

	delete from PRODUCT_OFFERS where ID = @ID_PRODUCT_OFFER
end
go

create or alter proc uspUpdateProductOffer @ID_PRODUCT_OFFER int,
									       @DISCOUNT int
as
begin	
	if not exists (select ID from PRODUCT_OFFERS where ID = @ID_PRODUCT_OFFER)
	begin
		throw 50001, 'Offer does not exists!', 1
	end

	update PRODUCT_OFFERS
	set DISCOUNT = @DISCOUNT
	where ID = @ID_PRODUCT_OFFER
end
go


-- SHOP_OFFER CRUD
create or alter proc uspInsertShopOffer @ID_SHOP int,
									    @ID_OFFER int
as
begin
	if not exists (select ID from SHOP where ID = @ID_SHOP)
	begin
		throw 50001, 'Shop does not exists!', 1
	end
	if not exists (select ID from PRODUCT_OFFERS where ID = @ID_OFFER)
	begin
		throw 50001, 'Offer does not exists!', 1
	end

	insert into SHOP_OFFER (ID_SHOP, ID_OFFER)
	values (@ID_SHOP, @ID_OFFER)
end
go

create or alter proc uspDeleteShopOffer @ID_SHOP int,
										@ID_OFFER int
as
begin
	if not exists (select ID_SHOP from SHOP_OFFER where ID_SHOP = @ID_SHOP and ID_OFFER = @ID_OFFER)
	begin
		throw 50001, 'Shop or offer does not exists!', 1
	end

	delete from SHOP_OFFER where ID_SHOP = @ID_SHOP and ID_OFFER = @ID_OFFER
end
go


-- SHOP CRUD
create or alter proc uspInsertShop @LOCATION nvarchar(255),
								   @OPEN_HOUR int,
								   @CLOSE_HOUR int,
								   @ID_CITY int
as
begin
	if not exists (select ID from CITY where ID = @ID_CITY)
	begin
		throw 50001, 'City does not exists!', 1
	end
	if len(@LOCATION) = 0
	begin
		throw 50001, 'Location not valid!', 1
	end

	insert into SHOP (LOCATION, OPEN_HOUR, CLOSE_HOUR, ID_CITY)
	values (@LOCATION, @OPEN_HOUR, @CLOSE_HOUR, @ID_CITY)
end
go

create or alter proc uspDeleteShop @ID_SHOP int
as
begin
	if not exists (select ID from SHOP where ID = @ID_SHOP)
	begin
		throw 50001, 'Shop does not exists!', 1
	end

	delete from SHOP where ID = @ID_SHOP
end
go

create or alter proc uspUpdateShop @ID_SHOP int,
								   @LOCATION nvarchar(255),
								   @OPEN_HOUR int,
								   @CLOSE_HOUR int
as
begin
	if not exists (select ID from SHOP where ID = @ID_SHOP)
	begin
		throw 50001, 'Shop does not exists!', 1
	end
	
	update SHOP
	set LOCATION = @LOCATION, OPEN_HOUR = @OPEN_HOUR, CLOSE_HOUR = @CLOSE_HOUR
	where ID = @ID_SHOP
end
go


-- CITY CRUD
create or alter proc uspInsertCity @NAME nvarchar(255)
as
begin
	if dbo.fctValidateName(@NAME) = 0
	begin
		throw 50001, 'Name not valid!', 1
	end

	insert into CITY(NAME) values(@NAME)
end
go

create or alter proc uspDeleteCity @ID_CITY int
as
begin
	if not exists (select ID from CITY where ID = @ID_CITY)
	begin
		throw 50001, 'City does not exists!', 1
	end

	delete from CITY where ID = @ID_CITY
end
go

create or alter proc uspUpdateCity @ID_CITY int,
								   @NAME nvarchar(255)
as
begin
	if not exists (select ID from CITY where ID = @ID_CITY)
	begin
		throw 50001, 'City does not exists!', 1
	end
	if dbo.fctValidateName(@NAME) = 0
	begin
		throw 50001, 'Name not valid!', 1
	end

	update CITY set NAME = @NAME where ID = @ID_CITY
end
go


-- Clean tables
delete from SHOP_OFFER
delete from RECEIPT_ROWS
delete from RECEIPT
delete from CLIENT
delete from FIDELITY_CARD
delete from EMPLOYEE
delete from SHOP
delete from PRODUCT_OFFERS
delete from LOCAL_MANAGER
delete from PRODUCT
delete from GENERAL_MANAGER
delete from CITY


-- Tests Product CRUD
exec uspInsertProduct 'Produs', 'Producator', 20
exec uspInsertProduct 'produs', 'producator', 20
exec uspInsertProduct 'Produs1', 'Producator1', 20
exec uspInsertProduct 'Produs', 'Producator', 0
exec uspInsertProduct '', '', 20

exec uspUpdateProduct 31014, 'Produsnou', 'Producatornou', 30
exec uspUpdateProduct 31014, 'produsnou', 'producatornou', 30
exec uspUpdateProduct 31014, 'Produsnou1', 'Producatornou1', 30
exec uspUpdateProduct 31014, 'Produsnou', 'Producatornou', 0
exec uspUpdateProduct 310141, 'Produsnou', 'Producatornou', 30
exec uspUpdateProduct 31014, '', '', 30

exec uspDeleteProduct 31014
exec uspDeleteProduct 310141

select * from PRODUCT


-- Tests Product_Offer CRUD
exec uspInsertProductOffer 20, 31014
exec uspInsertProductOffer -1, 31014
exec uspInsertProductOffer 101, 31014
exec uspInsertProductOffer 20, 310141

exec uspUpdateProductOffer 30051, 30
exec uspUpdateProductOffer 30051, -1
exec uspUpdateProductOffer 30051, 101
exec uspUpdateProductOffer 300511, 30

exec uspDeleteProductOffer 30051
exec uspDeleteProductOffer 300511

select * from PRODUCT_OFFERS


-- Tests City CRUD
exec uspInsertCity 'Oras'
exec uspInsertCity 'oras'
exec uspInsertCity 'Oras1'
exec uspInsertCity ''

exec uspUpdateCity 51, 'Orasnou'
exec uspUpdateCity 51, 'orasnou'
exec uspUpdateCity 51, 'Orasnou1'
exec uspUpdateCity 51, ''

exec uspDeleteCity 51
exec uspDeleteCity 511

select * from CITY


-- Tests Shop CRUD
exec uspInsertShop 'str. Cevastrada nr. 51', 9, 22, 51
exec uspInsertShop 'str. Cevastrada nr. 51', -1, -1, 51
exec uspInsertShop 'str. Cevastrada nr. 51', 24, 24, 51
exec uspInsertShop 'str. Cevastrada nr. 51', 15, 10, 51
exec uspInsertShop 'str. Cevastrada nr. 51', 9, 22, 511
exec uspInsertShop '', 9, 22, 51

exec uspUpdateShop 31008, 'str. Cevastradanoua nr. 52', 10, 23
exec uspUpdateShop 310081, 'str. Cevastradanoua nr. 52', 10, 23
exec uspUpdateShop 31008, 'str. Cevastradanoua nr. 52', -1, -1
exec uspUpdateShop 31008, 'str. Cevastradanoua nr. 52', 24, 24
exec uspUpdateShop 31008, 'str. Cevastradanoua nr. 52', 15, 10
exec uspUpdateShop 31008, '', 10, 23

exec uspDeleteShop 31008
exec uspDeleteShop 310081

select * from SHOP


-- Tests Shop_Offer CRUD
exec uspInsertShopOffer 31008, 30051
exec uspInsertShopOffer 310081, 30051
exec uspInsertShopOffer 31008, 300511

exec uspDeleteShopOffer 31008, 30051
exec uspInsertShopOffer 310081, 30051
exec uspInsertShopOffer 31008, 300511

select * from SHOP_OFFER


-- VIEWS
create or alter view ViewProductsOffers as
select PRODUCT.NAME as PRODUCT,
	   PRODUCT.PRODUCER as PRODUCER,
	   PRODUCT.PRICE as PRICE,
       convert(decimal(10,2), (PRODUCT.PRICE + 0.0) - ((PRODUCT_OFFERS.DISCOUNT + 0.0) * (PRODUCT.PRICE + 0.0) / 100.0)) as PRICE_AFTER_DISCOUNT
from PRODUCT
       join PRODUCT_OFFERS on PRODUCT_OFFERS.ID_PRODUCT = PRODUCT.ID
group by PRODUCT.NAME, PRODUCT.PRODUCER, PRODUCT.PRICE, PRODUCT_OFFERS.DISCOUNT
go

create or alter view ViewProductsOffersByShop as
select PRODUCT.NAME as PRODUCT,
       PRODUCT.PRODUCER as PRODUCER,
	   PRODUCT.PRICE as PRICE,
	   PRODUCT_OFFERS.DISCOUNT as DISCOUNT,
	   CITY.NAME as CITY,
	   SHOP.LOCATION as LOCATION,
	   SHOP.OPEN_HOUR as OPEN_HOUR,
	   SHOP.CLOSE_HOUR as CLOSE_HOUR
from SHOP_OFFER
	  join SHOP on SHOP.ID = SHOP_OFFER.ID_SHOP
	  join PRODUCT_OFFERS on PRODUCT_OFFERS.ID = SHOP_OFFER.ID_OFFER
	  join PRODUCT on PRODUCT.ID = PRODUCT_OFFERS.ID_PRODUCT
	  join CITY on CITY.ID = SHOP.ID_CITY
go

select * from ViewProductsOffers
select * from ViewProductsOffersByShop


-- INDEXES
create nonclustered index IX_PRODUCT on PRODUCT (ID, NAME, PRODUCER, PRICE)
create nonclustered index IX_PRODUCT_OFFERS on PRODUCT_OFFERS (ID, ID_PRODUCT, DISCOUNT)
create nonclustered index IX_SHOP_OFFER on SHOP_OFFER (ID_SHOP, ID_OFFER)
create nonclustered index IX_SHOP on SHOP (ID, ID_CITY, LOCATION, OPEN_HOUR, CLOSE_HOUR)
create nonclustered index IX_CITY on CITY (ID, NAME)

drop index IX_PRODUCT on PRODUCT
drop index IX_PRODUCT_OFFERS on PRODUCT_OFFERS
drop index IX_SHOP_OFFER on SHOP_OFFER
drop index IX_SHOP on SHOP
drop index IX_CITY on CITY