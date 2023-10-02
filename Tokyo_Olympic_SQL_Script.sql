SELECT TOP (100) [Name]
,[NOC]
,[Discipline]
 FROM [TokyoOlympicDB].[dbo].[athletes]

/*****counting no. of players by country****/
SELECT  [NOC], COUNT(Name) as Total_Athletes
FROM [TokyoOlympicDB].[dbo].[athletes]
GROUP BY NOC
order by Total_Athletes DESC

/*****counting no. of players by games****/
SELECT  [Discipline], COUNT(Name) as Total_Athletes
FROM [TokyoOlympicDB].[dbo].[athletes]
GROUP BY [Discipline]
order by Total_Athletes DESC

/*****counting no. of players by country and game ****/
SELECT  [Discipline], [NOC], COUNT(Name) as Total_Athletes
FROM [TokyoOlympicDB].[dbo].[athletes]
GROUP BY [Discipline], [NOC]


/*****counting no. of coaches by country****/
SELECT  [NOC], COUNT(Name) as Total_Coaches
FROM [TokyoOlympicDB].[dbo].[coaches]
GROUP BY NOC
order by Total_Coaches DESC

/*****counting no. of coaches by games****/
SELECT  [Discipline], COUNT(Name) as Total_Coaches
FROM [TokyoOlympicDB].[dbo].[coaches]
GROUP BY [Discipline]
order by Total_Coaches DESC

/*****Rank_by_Gold_Medals****/
SELECT *,
DENSE_RANK () over (order by Gold desc) as Rank_by_Gold_Medals
FROM [TokyoOlympicDB].[dbo].[medals]



