select d.*, t.[Srednia dobowa wilgotnosc wzgledna % ]
      ,t.[Srednia dobowa predkosc wiatru  m s ]
      ,t.[Srednie dobowe zachmurzenie ogolne  oktanty ] 
	  into weather
	  from dbo.k_d_m d join dbo.k_d_t_m t on d.[Kod stacji]=t.[Kod stacji] and d.[Nazwa stacji]=t.[Nazwa stacji]
and d.[Rok]=t.[Rok] and d.[Miesiac]=t.[Miesiac] and d.[Dzien]=t.[Dzien]
where d.[Dzien] not like 'Dzien'

select * from weather
select * from k_d_m
select * from k_d_t_m
