-- Solution #1

select
    a.user_id, case when b.confirmed_count/a.total_count is null then 0 else round(1.0*b.confirmed_count/a.total_count, 2) end as confirmation_rate
from (
    select
        s.user_id, count(c.action) total_count
    from signups s
    left join confirmations c
    on s.user_id = c.user_id
    group by  s.user_id
) a
left join
(
    select
        s.user_id, c.action, count(*) confirmed_count
    from signups s
    left join confirmations c
    on s.user_id = c.user_id
    group by  s.user_id, c.action
    having c.action = 'confirmed'
) b
on a.user_id = b.user_id


-- Solution #2 - MYSQL
select 
    s.user_id, round(avg(if(c.action="confirmed",1,0)),2) confirmation_rate
from Signups s 
left join Confirmations c 
on s.user_id= c.user_id group by user_id;
