use L1
go

declare @id_test int, @test_name varchar(30)
declare @sql_query varchar(100)
declare @noOfRows int, @name varchar(50), @id_table int, @id_view int
declare @start datetime
declare @id_test_runs int
-- select @id_test = TestID, @test_name = Name from Tests

declare cursor_tests cursor
	for select * from Tests
open cursor_tests

fetch next from cursor_tests into @id_test, @test_name
while @@FETCH_STATUS = 0
begin
	declare cursor_tables cursor
	for select NoOfRows, Name from TestTables TT 
		join Tables T on TT.TableID = T.TableID
	where TT.TestID = @id_test
	order by Position
	open cursor_tables

	fetch next from cursor_tables into @name
	while @@FETCH_STATUS = 0
	begin
		set @sql_query = 'delete from ' + @name 
		exec sp_execute @sql_query
		fetch next from cursor_tables into @name
	end

	--fetch prior from cursor_tables into @name
	--while @@FETCH_STATUS = 0
	--begin
		--exec uspInserts @name, @noOfRows
		--fetch next from cursor_tables into @name
	--end
	close cursor_tables
	deallocate cursor_tables

	insert into TestRuns
	values(@test_name, GETDATE(), null)
	set @id_test_runs = @@IDENTITY

	declare cursor_tables cursor
	for select T.TableID, Name from TestTables TT 
		join Tables T on TT.TableID = T.TableID
	where TT.TestID = @id_test
	order by Position desc
	open cursor_tables

	fetch next from cursor_tables into @id_table, @noOfRows, @name
	while @@FETCH_STATUS = 0
	begin
		set @start = GETDATE()
		exec uspInserts @name, @noOfRows
		insert into TestRunTables
		values(@id_test_runs, @id_table, @start, GETDATE())

		fetch next from cursor_tables into @noOfRows, @name
	end
	close cursor_tables
	deallocate cursor_tables

	declare cursor_views cursor
	for select Name from TestViews TV
		join Views V on TV.ViewID = V.ViewID
	where TV.TestID = @id_test

	open cursor_views
	fetch next from cursor_views into @name
	while @@FETCH_STATUS = 0
	begin
		set @sql_query = 'select * from ' + @name
		exec sp_execute @sql_query

		fetch next from cursor_views into @name
	end
	close cursor_views
	deallocate cursor_views

	fetch next from cursor_tests into @id_test, @test_name
end

close cursor_tests
deallocate cursor_tests
go

create proc uspInsertGeneralManager(@rows int)
as
begin
	while(@id < @rows) begin
		declare @name 
		insert into GENERAL_MANAGER
		values(@name, 'Executive', @contact)
	end
end
go

create or alter proc uspInserts(@tableName varchar(50), @rows int)
as
begin
	if @tableName = 'GENERAL_MANAGER'
		exec uspInsertGeneralManager @rows
end
go