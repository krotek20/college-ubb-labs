use L1
go

create or alter proc uspInsert_GENERAL_MANAGER @rows int
as
begin
	declare @rowID int = 1
	set identity_insert GENERAL_MANAGER on
	while(@rowID <= @rows) begin
		insert into GENERAL_MANAGER(ID, NAME, ROLE, CONTACT)
		values(@rowID, 'Ion', 'Executive', '+44 4037 90 3024')
		set @rowID = @rowID + 1
	end
	set identity_insert GENERAL_MANAGER off
end
go

create or alter proc uspInsert_SHOP @rows int
as
begin
	declare @rowID int = 1
	set identity_insert SHOP on
	while(@rowID <= @rows) begin
		insert into SHOP(ID, LOCATION, OPEN_HOUR, CLOSE_HOUR, ID_CITY)
		values(@rowID, 'Str. Castorului, nr. 11', 7, 22, 1)
		set @rowID = @rowID + 1
	end
	set identity_insert SHOP off
end
go

create or alter proc uspInsert_PRODUCT @rows int
as
begin
	declare @rowID int = 1
	set identity_insert PRODUCT on
	while(@rowID <= @rows) begin
		insert into PRODUCT(ID, NAME, PRODUCER, PRICE)
		values(@rowID, 'Speaklifiedor', 'Australian High-Technologies Inc.', floor(rand()*(1000-10+1))+10)
		set @rowID = @rowID + 1
	end
	set identity_insert PRODUCT off
end
go

create or alter proc uspInsert_PRODUCT_OFFERS @rows int
as
begin
	declare @rowID int = 1
	set identity_insert PRODUCT_OFFERS on
	while(@rowID <= @rows) begin
		insert into PRODUCT_OFFERS(ID, DISCOUNT, ID_PRODUCT)
		values(@rowID, floor(rand()*100), @rowID)
		set @rowID = @rowID + 1
	end
	set identity_insert PRODUCT_OFFERS off
end
go

create or alter proc uspInsert_SHOP_OFFER @rows int
as
begin
	declare @rowID int = 1
	while(@rowID <= @rows) begin
		insert into SHOP_OFFER
		values(@rowID, @rowID)
		set @rowID = @rowID + 1
	end
end
go

create or alter proc uspInsert_FIDELITY_CARD @rows int
as
begin
	declare @rowID int = 1
	while(@rowID <= @rows) begin
		insert into FIDELITY_CARD
		values(@rowID, @rowID, '1997-06-14')
		set @rowID = @rowID + 1
	end
end
go

create or alter proc uspInsert_CLIENT @rows int
as
begin
	declare @rowID int = 1
	set identity_insert CLIENT on
	while(@rowID <= @rows) begin
		insert into CLIENT(ID, NAME, AGE, CONTACT, ID_CARD)
		values(@rowID, 'Abraham Acevedo', 25, '+55 30 5790-7694', @rowID)
		set @rowID = @rowID + 1
	end
	set identity_insert CLIENT off
end
go

create or alter proc uspInserts @table_name varchar(50), @rows int
as
begin
	if @table_name = 'GENERAL_MANAGER' exec uspInsert_GENERAL_MANAGER @rows
	if @table_name = 'PRODUCT_OFFERS' exec uspInsert_PRODUCT_OFFERS @rows
	if @table_name = 'FIDELITY_CARD' exec uspInsert_FIDELITY_CARD @rows
	if @table_name = 'SHOP_OFFER' exec uspInsert_SHOP_OFFER @rows
	if @table_name = 'PRODUCT' exec uspInsert_PRODUCT @rows
	if @table_name = 'CLIENT' exec uspInsert_CLIENT @rows
	if @table_name = 'SHOP' exec uspInsert_SHOP @rows
end
go

create or alter proc uspRunTests
as
begin
	set nocount on
	declare @id_test int, @test_name varchar(30)
	declare @sql_query nvarchar(4000)
	declare @table_name nvarchar(50), @view_name nvarchar(50)
	declare @noOfRows int, @id_table int, @id_view int
	declare @id_test_runs int
	declare @start_time datetime
	
	delete from TestRunTables
	delete from TestRunViews
	delete from TestRuns

	declare cursor_tests cursor for select * from Tests
	open cursor_tests

	fetch next from cursor_tests into @id_test, @test_name
	while @@FETCH_STATUS = 0
	begin
		insert into TestRuns
		values(@test_name, current_timestamp, null)
		set @id_test_runs = @@IDENTITY

		-- Table delete testing
		declare cursor_deletes cursor
		for select Name from TestTables TT 
			join Tables T on TT.TableID = T.TableID
		where TT.TestID = @id_test
		order by Position desc
		open cursor_deletes

		fetch next from cursor_deletes into @table_name
		while @@FETCH_STATUS = 0
		begin
			set @sql_query = 'delete from ' + quotename(@table_name) 
			if(@table_name = 'SHOP') begin
				delete from CLIENT
				delete from FIDELITY_CARD
			end
			exec sp_executesql @sql_query
			fetch next from cursor_deletes into @table_name
		end
		close cursor_deletes
		deallocate cursor_deletes

		-- Table insert testing
		declare cursor_inserts cursor
		for select T.TableID, NoOfRows, Name from TestTables TT 
			join Tables T on TT.TableID = T.TableID
		where TT.TestID = @id_test
		order by Position
		open cursor_inserts

		fetch next from cursor_inserts into @id_table, @noOfRows, @table_name
		while @@FETCH_STATUS = 0
		begin
			set @start_time = current_timestamp
			exec uspInserts @table_name, @noOfRows
			insert into TestRunTables
			values(@id_test_runs, @id_table, @start_time, current_timestamp)
			fetch next from cursor_inserts into @id_table, @noOfRows, @table_name
		end
		close cursor_inserts
		deallocate cursor_inserts

		-- Table views testing
		declare cursor_views cursor
		for select V.ViewID, Name from TestViews TV
			join Views V on TV.ViewID = V.ViewID
		where TV.TestID = @id_test

		open cursor_views
		fetch next from cursor_views into @id_view, @view_name
		while @@FETCH_STATUS = 0
		begin
			set @start_time = current_timestamp
			set @sql_query = 'select * from ' + quotename(@view_name)
			exec sp_executesql @sql_query
			insert into TestRunViews
			values(@id_test_runs, @id_view, @start_time, current_timestamp)
			fetch next from cursor_views into @id_view, @view_name
		end
		close cursor_views
		deallocate cursor_views

		-- Update end time for current test run
		update TestRuns set EndAt = current_timestamp where TestRunID = @id_test_runs
		fetch next from cursor_tests into @id_test, @test_name
	end
	close cursor_tests
	deallocate cursor_tests

	set nocount off
end
go

exec uspRunTests

select * from TestRunTables
select * from TestRunViews
select * from TestRuns