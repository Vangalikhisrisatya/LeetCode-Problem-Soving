# Write your MySQL query statement below
with cte1 as
(select author_id from Views
where author_id=viewer_id)
select distinct author_id as id from cte1
order by author_id