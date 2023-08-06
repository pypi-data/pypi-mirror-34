COMMENT ON COLUMN unitracc_statistic_course.course_uid
IS 'UID des Kursobjekts';

COMMENT ON COLUMN unitracc_statistic_course.user_uid
IS 'UID des Autorenprofils des Kursteilnehmers';

COMMENT ON COLUMN unitracc_statistic_course.course_page_count
IS 'Gesamtanzahl der Seiten des Kurses';

CREATE OR REPLACE VIEW last_page_view_date AS
SELECT rid,
       MAX(page_view_date) AS last_view_date,
       COUNT(rid)          AS pages_viewed,
       MAX(page_number)    AS max_page_nr
  FROM unitracc_page_statistic_course
 GROUP BY rid;


-- DROP VIEW course_statistics_overview;
CREATE OR REPLACE VIEW course_statistics_overview AS
SELECT usc.user_uid,
       usc.course_uid,
       usc.course_page_count,
       lpv.rid,
       lpv.last_view_date,
       lpv.pages_viewed,
       lpv.max_page_nr,
       ps2.page_uid    AS max_page_uid,
       CASE
	 WHEN lpv.pages_viewed >= usc.course_page_count
	      THEN '100'
         WHEN usc.course_page_count > 0
	      THEN to_char(100.0 * lpv.pages_viewed / usc.course_page_count, '990.99')
	 ELSE '0'
       END             AS percent,
       ps1.page_number AS last_viewed_page_nr,
       ps1.page_uid    AS last_viewed_page_uid,
       ps1.page_view_type
  FROM unitracc_statistic_course usc
  LEFT JOIN last_page_view_date lpv
       ON usc.id = lpv.rid
  LEFT JOIN unitracc_page_statistic_course ps1
       ON lpv.last_view_date = ps1.page_view_date
  LEFT JOIN unitracc_page_statistic_course ps2
       ON usc.id = ps2.rid AND ps2.page_number = lpv.max_page_nr;

COMMENT ON COLUMN course_statistics_overview.percent
IS 'Prozentsatz der besuchten Seiten; wg. Verwendung für Styleangabe leider stets mit Dezimal*punkt*';

ALTER TABLE public.unitracc_page_statistic_course
DROP CONSTRAINT unitracc_page_statistic_course_rid_fkey,
ADD CONSTRAINT unitracc_page_statistic_course_rid_fkey
  FOREIGN KEY (rid)
  REFERENCES unitracc_statistic_course(id)
  ON DELETE CASCADE;

