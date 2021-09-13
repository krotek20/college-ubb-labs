-- dirty reads
begin tran
set transaction isolation level read uncommitted
select * from CITY
commit tran


-- unrepeatable reads
begin tran
update CITY set NAME = 'AtlanticModified' where NAME = 'Atlantic'
print 'City modified!'
commit tran
--update CITY set NAME = 'Atlantic' where NAME = 'AtlanticModified'


-- phantom reads
begin tran
insert into CITY values('newCity')
print 'City inserted!'
commit tran
--delete from CITY where NAME = 'newCity'


-- deadlock (unsolved)
begin tran
set transaction isolation level serializable
update CITY set NAME = 'AtlanticModified2' where NAME = 'Atlantic'
print 'City updated in modified2'
waitfor delay '00:00:10'
update PRODUCT set NAME = 'CabtoporModified2' where NAME = 'Cabtopor'
print 'Product updated in modified2'
commit tran
--update CITY set NAME = 'Atlantic' where NAME = 'AtlanticModified1'
--update PRODUCT set NAME = 'Cabtopor' where NAME = 'CabtoporModified1'


-- deadlock (solved)
declare @working int = 0
while (@working = 0)
begin
	begin try
		begin tran
		set transaction isolation level serializable
		update CITY set NAME = 'AtlanticModified2' where NAME = 'Atlantic'
		print 'City updated in modified2'
		waitfor delay '00:00:10'
		update PRODUCT set NAME = 'CabtoporModified2' where NAME = 'Cabtopor'
		print 'Product updated in modified2'
		commit tran
		set @working = 1
	end try
	begin catch
		rollback tran
		declare @waitingTime varchar(12) = '00:00:0' + cast(rand() * 9 + 1 as varchar(2))
		print 'Waiting for ' + @waitingTime + ' seconds'
		waitfor delay @waitingTime
	end catch
end


-- procedura stocata deadlock2
create or alter proc uspGenerateDeadlock2 @currentCityName nvarchar(255),
										  @updatedCityName nvarchar(255),
										  @currentProductName nvarchar(255),
										  @updatedProductName nvarchar(255)
as
begin
	begin tran
	set transaction isolation level serializable
	update CITY set NAME = @updatedCityName where NAME = @currentCityName
	waitfor delay '00:00:05'
	update PRODUCT set NAME = @updatedProductName where NAME = @currentProductName
	commit tran
end
go

select * from CITY
select * from PRODUCT