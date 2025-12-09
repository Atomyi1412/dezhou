-- Create settings table to store gift tiers and images per year
create table if not exists public.settings (
  year int not null,
  key text not null,
  value jsonb,
  primary key (year, key)
);

-- Add gifts JSON column to teams to store member gift selections
alter table public.teams add column if not exists gifts jsonb;

