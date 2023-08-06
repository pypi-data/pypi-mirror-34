BEGIN TRANSACTION;  -- -*- coding: utf-8 -*- äöü

DROP VIEW IF EXISTS  course_statistic_page;
CREATE OR REPLACE VIEW course_statistics_page AS
SELECT usc.user_uid,
       usc.course_uid,
       page_uid,
       page_number,
       page_view_date,
       page_view_type,
       usc.id AS user_and_course_id
  FROM unitracc_statistic_course usc
  JOIN unitracc_page_statistic_course psc
       ON psc.rid = usc.id;

CREATE OR REPLACE VIEW course_statistics_overview AS
SELECT usc.user_uid,
       usc.course_uid,
       usc.course_page_count,
       lpv.rid,
       lpv.last_view_date,
       lpv.pages_viewed,
       lpv.max_page_nr,
       ps2.page_uid AS max_page_uid,
       CASE
	   WHEN lpv.pages_viewed >= usc.course_page_count THEN '100'::text
	   WHEN usc.course_page_count > 0 THEN to_char(100.0 * lpv.pages_viewed::numeric / usc.course_page_count::numeric, '990.99'::text)
	   ELSE '0'::text
       END AS percent,
       ps1.page_number AS last_viewed_page_nr,
       ps1.page_uid AS last_viewed_page_uid,
       ps1.page_view_type,
       usc.id AS user_and_course_id
   FROM unitracc_statistic_course usc
   LEFT JOIN last_page_view_date lpv ON usc.id = lpv.rid
   LEFT JOIN unitracc_page_statistic_course ps1 ON lpv.last_view_date = ps1.page_view_date
   LEFT JOIN unitracc_page_statistic_course ps2 ON usc.id = ps2.rid AND ps2.page_number = lpv.max_page_nr;

END;
