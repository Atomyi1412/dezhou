create table if not exists public.teams (
  year integer not null,
  serial text not null,
  name text not null,
  members text[] not null default '{}',
  count integer not null default 0,
  time text not null,
  sort_key integer not null default 0,
  primary key (year, serial)
);

create index if not exists idx_teams_year on public.teams(year);

create table if not exists public.wishes (
  year integer not null,
  serial text not null,
  team_name text,
  wishes jsonb not null,
  total integer not null default 0,
  primary key (year, serial)
);

create index if not exists idx_wishes_year on public.wishes(year);

create table if not exists public.hands (
  year integer not null,
  serial text not null,
  team_name text,
  hand_type_name text,
  cards jsonb not null,
  hand_points integer not null default 0,
  hand_raw_score bigint not null default 0,
  primary key (year, serial)
);

create index if not exists idx_hands_year on public.hands(year);

create table if not exists public.final_rankings (
  year integer not null,
  serial text not null,
  team_name text,
  members text[],
  wish_total integer,
  wish_points integer,
  hand_type_name text,
  hand_cards jsonb,
  hand_points integer,
  hand_raw_score bigint,
  final_score integer,
  rank integer,
  primary key (year, serial)
);

create index if not exists idx_final_rankings_year on public.final_rankings(year);
