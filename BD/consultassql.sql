-- Trazer os Empréstimos realizados entre as datas 15/06/2024 
-- até 30/07/2024. Para cada empréstimo, desejo saber o nome do 
-- usuário, o email, título do livro, nome do autor, data de 
-- empréstimo e data de devolução.
select u.nome, u.email, l.titulo, a.nome, 
emp.data_emprestimo, data_devolucao
from emprestimo emp
left join usuario u on
emp.ID_usuario = u.ID
left join livro l on
emp.ID_livro = l.ID
left join autor a on
l.ID_autor = a.ID
WHERE data_emprestimo BETWEEN '2024-06-15' and '2024-07-30'
and u.nome LIKE '%sil%';



-- Quantos usuários cadastrados?
select COUNT(*) as quantidade_usuario from usuario;

-- Quantos empréstimos foram realizados?
select COUNT(*) as quantidade_emprestimo 
from emprestimo 
where data_emprestimo BETWEEN '2024-06-01' and '2024-06-30';

-- Quantos empréstimos cada usuário fez?
select u.nome, COUNT(emp.ID) as quantidade_emprestimo
from emprestimo emp
left join usuario u on
emp.ID_usuario = u.ID
group by u.ID;


-- Quantos empréstimos por autor foi realizado no mês de julho?