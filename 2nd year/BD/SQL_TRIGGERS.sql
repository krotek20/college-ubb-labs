begin tran

select * from RanduriFact

-- select * from Facturi

select id_produs, 
	(select denumire from Produse P where id_produs = P.id) as produs, 
	cantitate, pret, valoare, cantitate * pret as val_rand 
	from RanduriFact

-- select *, cantitate * pret as val_rand from RanduriFact - functioneaza

select F.id, serie, numar, sum(RF.cantitate * RF.pret) as val_fact
	from Facturi F
	left join RanduriFact RF on RF.id_factura = F.id
	group by F.id, serie, numar

insert into RanduriFact values(7,1,2,1,2.0)

delete from RanduriFact where id = 7

update RanduriFact set cantitate = 2 where id = 7

select * from Facturi