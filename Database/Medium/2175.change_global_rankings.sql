select 
  tp.team_id, 
  tp.name, 
  rank() over (order by tp.points desc, tp.name) - rank() over (order by (tp.points + pc.points_change) desc, tp.name)  rank_diff
from teampoints tp
join pointschange pc on tp.team_id = pc.team_id