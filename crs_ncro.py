import datetime
import numpy as np
import pandas as pd
import pytz
from sqlalchemy import true
from modules.sql import dwh
from os import path
from modules.snowflake_connector import sn_dwh

query_name= 'crs'
crs = dwh().dwh_to_pandas(
    filename=path.join('querys', 'server_querys', f'select_{query_name}.sql')
    )

query_name= 'ncro'
ncro = dwh().dwh_to_pandas(
    filename=path.join('querys', 'server_querys', f'select_{query_name}.sql')
    )


query_name = 'om_campaigns_data'
online_campaigns = sn_dwh(role='ACQUISITION_ANALYST_CL').cursor_to_pandas(
    filename=path.join('querys', 'snowflake', f'select_{query_name}.sql')
)

online_campaigns.columns = online_campaigns.columns.str.lower()
ratio = online_campaigns.groupby(['week','om_channel']).sum()['purchases_chile'].reset_index()

ratio = ratio.merge(online_campaigns.groupby(['week']).sum()['purchases_chile'].reset_index(),on='week',how='left',suffixes=['_channel','_total'])
ratio['channel_ratio'] = ratio['purchases_chile_channel']/ratio['purchases_chile_total']


crs  = crs.merge(ncro,how='left',left_on=['week_date','channel','cr_type'],right_on=['week_date','channel','cr_type'])
crs = crs.merge()

crs['ratio']