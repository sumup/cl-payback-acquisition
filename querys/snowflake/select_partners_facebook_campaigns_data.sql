select yearofweekiso(date) || '-'||weekiso(date) as date,
sum(amount_spent__facebook_Ads) as amount_spent
from "SHARED_FUNNEL_SUMUP__LM3JD3KWKTSKJUJGEZZ"."FUNNEL__LM3JD3KWKTSKJUJGEZZ"."PARTNERS_FACEBOOK_CAMPAIGNS_CHILE"
group by 1