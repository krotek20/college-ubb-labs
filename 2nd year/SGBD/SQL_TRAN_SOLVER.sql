-- dirty reads
begin tran
set transaction isolation level read committed
select * from CITY
commit tran


-- unrepeatable reads
begin tran
set transaction isolation level repeatable read
select * from CITY
waitfor delay '00:00:10'
select * from CITY
commit tran


-- phantom reads
begin tran
set transaction isolation level serializable
select * from CITY
waitfor delay '00:00:10'
select * from CITY
commit tran