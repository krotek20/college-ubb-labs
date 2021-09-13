-- SHOP si PRODUCT_OFFERS

-- 1.
-- get product by name
create or alter function uf_getProductId(@name nvarchar(255))
returns int as
begin
	declare @rez int = -1
	if @name in (select NAME from PRODUCT)
	begin
		set @rez = (select ID from PRODUCT where NAME like @name)
	end
	return @rez
end
go

-- get city by name
create or alter function uf_getCityId(@name nvarchar(255))
returns int as
begin
	declare @rez int = -1
	if @name in (select NAME from CITY)
	begin
		set @rez = (select ID from CITY where NAME like @name)
	end
	return @rez
end
go

-- insert
create or alter proc FirstInsert @discount int,
								 @product_name nvarchar(255),
								 @location nvarchar(255),
								 @open_hour int,
								 @close_hour int,
								 @city_name nvarchar(255)
as
begin
	begin tran
	begin try

		declare @id_product int, @id_city int

		-- validate discount
		if (@discount not between 0 and 100)
		begin
			raiserror('Discount invalid', 14, 1)
		end

		-- get product id
		set @id_product = dbo.uf_getProductId(@product_name)
		if (@id_product = -1 or @id_product is null)
		begin
			raiserror('Product name invalid', 14, 1)
		end

		-- insert offer
		insert into PRODUCT_OFFERS(DISCOUNT, ID_PRODUCT)
		values(@discount, @id_product)

		declare @id_offer int = (select @@IDENTITY)

		-- validate location (street address)
		if (@location is null or len(@location) < 5)
		begin
			raiserror('Location invalid', 14, 1)
		end

		-- open hour validation
		if (@open_hour not between 0 and 23)
		begin
			raiserror('Open hour invalid', 14, 1)
		end

		-- close hour validation
		if (@close_hour not between 0 and 23)
		begin
			raiserror('Close hour invalid',14, 1)
		end

		-- get city id
		set @id_city = dbo.uf_getCityId(@city_name)
		if (@id_city = -1 or @id_city is null)
		begin
			raiserror('City name invalid', 14, 1)
		end

		-- insert shop
		insert into SHOP(LOCATION, OPEN_HOUR, CLOSE_HOUR, ID_CITY)
		values(@location, @open_hour, @close_hour, @id_city)

		declare @id_shop int = (select @@IDENTITY)

		-- insert shop_offer
		insert into SHOP_OFFER(ID_SHOP, ID_OFFER)
		values(@id_shop, @id_offer)

		commit tran
		select 'Transaction commited!'

	end try

	begin catch
		
		rollback tran
		select 'Transaction failed!'
		select ERROR_MESSAGE()

	end catch

end
go

-- valid tran
exec FirstInsert 50, 'Cleanplottor', 'newLocation', 8, 22, 'Atlantic'

-- invalid tran
exec FirstInsert 101, 'Cleanplottor', 'newLocation', 8, 22, 'Atlantic'
exec FirstInsert 99, 'Cleanplotto', 'newLocation', 8, 22, 'Atlantic'
exec FirstInsert 99, 'Cleanplottor', 'a', 8, 22, 'Atlantic'
exec FirstInsert 99, 'Cleanplottor', 'newLocation', 20, 25, 'Atlantic'
exec FirstInsert 9, 'Cleanplottor', 'newLocation', 8, 22, 'Atlanti'


-- 2.
create or alter proc SecondInsert @discount int,
								  @product_name nvarchar(255),
								  @location nvarchar(255),
								  @open_hour int,
								  @close_hour int,
								  @city_name nvarchar(255)
as
begin
	declare @id_product int, @id_city int, @id_offer int, @id_shop int

	begin tran
	begin try

		-- validate discount
		if (@discount not between 0 and 100)
		begin
			raiserror('Discount invalid', 14, 1)
		end

		-- get product id
		set @id_product = dbo.uf_getProductId(@product_name)
		if (@id_product = -1 or @id_product is null)
		begin
			raiserror('Product name invalid', 14, 1)
		end

		-- insert offer
		insert into PRODUCT_OFFERS(DISCOUNT, ID_PRODUCT)
		values(@discount, @id_product)

		set @id_offer = (select @@IDENTITY)

		commit tran
		select 'OFFER transaction commited!'

	end try

	begin catch

		rollback tran
		select 'OFFER transaction failed!'
		select ERROR_MESSAGE()

	end catch

	begin tran
	begin try

		-- validate location (street address)
		if (@location is null or len(@location) < 5)
		begin
			raiserror('Location invalid', 14, 1)
		end

		-- open hour validation
		if (@open_hour not between 0 and 23)
		begin
			raiserror('Open hour invalid', 14, 1)
		end

		-- close hour validation
		if (@close_hour not between 0 and 23)
		begin
			raiserror('Close hour invalid',14, 1)
		end

		-- get city id
		set @id_city = dbo.uf_getCityId(@city_name)
		if (@id_city = -1 or @id_city is null)
		begin
			raiserror('City name invalid', 14, 1)
		end

		-- insert shop
		insert into SHOP(LOCATION, OPEN_HOUR, CLOSE_HOUR, ID_CITY)
		values(@location, @open_hour, @close_hour, @id_city)

		set @id_shop = (select @@IDENTITY)

		commit tran
		select 'SHOP transaction commited!'

	end try

	begin catch
		
		rollback tran
		select 'SHOP transaction failed!'
		select ERROR_MESSAGE()

	end catch

	begin tran
	begin try

		-- insert shop_offer
		insert into SHOP_OFFER(ID_SHOP, ID_OFFER)
		values(@id_shop, @id_offer)

		commit tran
		select 'Full transaction commited!'

	end try

	begin catch

		rollback tran
		select 'Full transaction failed!'
		select ERROR_MESSAGE()

	end catch
end
go

-- valid tran
exec SecondInsert 2, 'Cleanplottor', 'Cevalocatin', 8, 22, 'Atlantic'

-- invalid tran
exec SecondInsert 101, 'Cleanplottor', 'newLocation', 8, 22, 'Atlantic'
exec SecondInsert 75, 'Cleanplottor', 'newLocation', 8, 22, 'Atlanti'

select * from PRODUCT_OFFERS
select * from SHOP_OFFER
select * from SHOP