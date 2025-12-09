-- Create table for rank change logs
create table if not exists public.rank_change_logs (
  id bigint generated always as identity primary key,
  year text not null,
  created_at timestamptz not null default now(),
  operation_type text not null, -- single | bulk
  ref_type text,                -- hand | wish | team
  ref_identifier text,          -- serial or other id
  operator text,
  status text not null,         -- snapshot | computed
  summary text,
  details jsonb,
  pre_hand_ranks jsonb,
  pre_wish_ranks jsonb,
  pre_final_ranks jsonb,
  post_hand_ranks jsonb,
  post_wish_ranks jsonb,
  post_final_ranks jsonb,
  diff jsonb
);

create index if not exists idx_rank_change_logs_year_created on public.rank_change_logs(year, created_at desc);
create index if not exists idx_rank_change_logs_status on public.rank_change_logs(status);
