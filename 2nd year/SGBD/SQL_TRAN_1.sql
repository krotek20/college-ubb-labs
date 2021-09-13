-- dirty reads
begin tran
update CITY set NAME = 'AtlanticModified' where NAME = 'Atlantic'
print 'City updated'
waitfor delay '00:00:10'
rollback tran
print 'Rollback!'
select * from CITY


-- unrepeatable reads
begin tran
select * from CITY
waitfor delay '00:00:10'
select * from CITY
commit tran


-- phantom reads
begin tran
set transaction isolation level repeatable read
select * from CITY
waitfor delay '00:00:10'
select * from CITY
commit tran


-- deadlock (unsolved)
begin tran
set transaction isolation level serializable
update PRODUCT set NAME = 'CabtoporModified1' where NAME = 'Cabtopor'
print 'Product updated in modified1'
waitfor delay '00:00:10'
update CITY set NAME = 'AtlanticModified1' where NAME = 'Atlantic'
print 'City updated in modified1'
commit tran


-- deadlock (solved)
declare @working int = 0
while (@working = 0)
begin
	begin try
		begin tran
		set transaction isolation level serializable
		update PRODUCT set NAME = 'CabtoporModified1' where NAME = 'Cabtopor'
		print 'Product updated in modified1'
		waitfor delay '00:00:10'
		update CITY set NAME = 'AtlanticModified1' where NAME = 'Atlantic'
		print 'City updated in modified1'
		commit tran
		set @working = 1
	end try
	begin catch
		print ERROR_MESSAGE()
		rollback tran
		declare @waitingTime varchar(12) = '00:00:0' + cast(rand() * 9 + 1 as varchar(10))
		print 'Waiting for ' + @waitingTime + ' seconds'
		waitfor delay @waitingTime
	end catch
end


-- procedura stocata deadlock1
create or alter proc uspGenerateDeadlock1 @currentCityName nvarchar(255),
										  @updatedCityName nvarchar(255),
										  @currentProductName nvarchar(255),
										  @updatedProductName nvarchar(255)
as
begin
	begin tran
	set transaction isolation level serializable
	update PRODUCT set NAME = @updatedProductName where NAME = @currentProductName
	waitfor delay '00:00:05'
	update CITY set NAME = @updatedCityName where NAME = @currentCityName
	commit tran
end
go