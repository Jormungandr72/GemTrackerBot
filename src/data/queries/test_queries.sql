-- SQLite, test misc sql statements here
insert into quests (main_monster, user_id) values ('Arkveld', 663063684620353586);
insert into quests (main_monster, user_id) values ('Rathalos', 663063684620353586);
insert into quests (main_monster, user_id) values ('Zoh Shia', 663063684620353586);

select (ROWID, main_monster, user_id) from quests
where user_id = '663063684620353586';