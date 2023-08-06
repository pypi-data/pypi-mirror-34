BEGIN TRANSACTION;  -- -*- coding: utf-8 -*- äöü

CREATE INDEX fki__unitracc_page_statistic_course__rid__fkey
          ON unitracc_page_statistic_course (rid);
CREATE INDEX fki__unitracc_page_statistic_course__page_view_date__fkey
          ON unitracc_page_statistic_course (page_view_date);
CREATE INDEX fki__unitracc_page_statistic_course__page_number__fkey
          ON unitracc_page_statistic_course (page_number);

END;
