drop table if exists users;

create table users (
    nome varchar(50) not null,
    email varchar(50) primary key,
    senha int not null
);