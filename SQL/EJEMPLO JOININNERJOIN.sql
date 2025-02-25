--Seleccionar el apellido, oficio, salario,
--numero de departamento y su nombre de todos
--los empleados cuyo salario sea mayor de 300000
select e.apellido
, e.oficio
, e.salario
, d.dept_no as NUMERO
, Dnombre as DEPARTAMENTO
from EMP e
inner join dept d on
e.dept_no = d.dept_no
where e.salario > 300000

select s.Nombre as NOMBRESALA
,h.Nombre as NOMBREHOSPITAL
from sala s
inner join hospital h on
s.hospital_cod = h.hospital_cod








