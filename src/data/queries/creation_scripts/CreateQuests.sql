-- SQLite, creates table quests
drop table if exists quests;
create table quests (
    main_monster varchar(20) not null,
    is_tempered bool,
    has_gem bool,
    artian_count int,
    decoration_count int,
    user_id varchar(30) not null -- Discord user id
);