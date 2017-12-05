create table events(
    id integer primary key,
    title nvarchar,
    place nvarchar,
    price nvarchar,
    description nvarchar,
    contacts nvarchar,
    date float,
    type nvarchar,
    thumbnail nvarchar
)


create table movies(
	id integer primary key,
	title nvarchar,
	thumbnail nvarchar,
	trailer nvarchar
)

create table cinemas(
	movie_id integer,
	date float,
	price nvarchar
)
