from typing import Any

from sqlmodel import Session, select
from sqlalchemy import text

session: Session

insert_select_sql = text("""

---check supplier rate has a row for each criteria & set base rate if not on override -- 

INSERT INTO supplier_rate (owner_id,authority_id, supplier_id, circs_group_id, veh_group_id, rate)
SELECT 
    1 as owner_id,
    authority.id as authority_id,
    supplier.id as supplier_id,
    circs_group.id as circs_group_id,
    veh_group.id as veh_group_id,
    supplier.base_rate as rate
FROM 
    authority
    CROSS JOIN supplier
    CROSS JOIN circs_group
    CROSS JOIN veh_group
ON CONFLICT ON CONSTRAINT supplier_rate_constraint DO UPDATE
    SET rate = CASE WHEN EXCLUDED.rate_override = 'No' THEN EXCLUDED.rate ELSE supplier_rate.rate END;


---check supplier stats has a row for each criteria -- 

INSERT INTO supplier_stat (authority_id,supplier_id,circs_group_id,veh_group_id)
SELECT authority.id as authority_id, 
       supplier.id as supplier_id,
       circs_group.id as circs_group_id,
       veh_group.id as veh_group_id
FROM authority, supplier, circs_group, veh_group
ON CONFLICT ON CONSTRAINT supplier_stat_constraint
DO NOTHING;

--- Update supplier_stat rows with rate & rank ----

INSERT INTO supplier_stat (authority_id,supplier_id,circs_group_id,veh_group_id,rate_rank,rate)
SELECT authority_id, 
       supplier_id,
       circs_group_id,
       veh_group_id,
       RANK() OVER (
                    PARTITION BY authority_id,circs_group_id, veh_group_id
                    ORDER BY rate DESC) raterank,
       rate
       FROM
       supplier_rate
ON CONFLICT ON CONSTRAINT supplier_stat_constraint
DO UPDATE SET 
rate_rank = EXCLUDED.rate_rank,
rate = EXCLUDED.rate;

--- Update supplier_stat rows with Days To Hire & rank ----

INSERT INTO supplier_stat (
    authority_id,
    supplier_id,
    circs_group_id,
    veh_group_id,
    daystohire_rank,
    daystohire
)
SELECT
    Avetable.authorityid,
    Avetable.supplierid,
    Avetable.circs_groupid,
    Avetable.veh_groupid,
    RANK() OVER (ORDER BY Avetable.avg_daystohire DESC) AS daystohire_rank,
    Avetable.avg_daystohire
FROM (
    SELECT 
        basetable.authorityid,
        basetable.supplierid,
        basetable.circs_groupid,
        basetable.veh_groupid,
        ROUND(AVG(referral.daystohire), 2) AS avg_daystohire
    FROM (
        SELECT 
            authority.id AS authorityid, 
            supplier.id AS supplierid,
            circs_group.id AS circs_groupid,
            veh_group.id AS veh_groupid
        FROM 
            authority
        CROSS JOIN 
            supplier
        CROSS JOIN 
            circs_group
        CROSS JOIN 
            veh_group
    ) AS basetable
    LEFT JOIN referral
    ON referral.authority_id = basetable.authorityid
    AND referral.supplier_id = basetable.supplierid
    AND referral.circs_group_id = basetable.circs_groupid
    AND referral.veh_group_id = basetable.veh_groupid
    GROUP BY 
        basetable.authorityid,
        basetable.supplierid,
        basetable.circs_groupid,
        basetable.veh_groupid
) AS Avetable
ON CONFLICT ON CONSTRAINT supplier_stat_constraint
DO UPDATE SET 
    daystohire_rank = EXCLUDED.daystohire_rank,
    daystohire = EXCLUDED.daystohire;

update supplier_stat 
SET Total_Rank = daystohire_rank + rate_rank;""")


    
        # Execute the raw SQL
session.execute(insert_select_sql)
session.commit()

