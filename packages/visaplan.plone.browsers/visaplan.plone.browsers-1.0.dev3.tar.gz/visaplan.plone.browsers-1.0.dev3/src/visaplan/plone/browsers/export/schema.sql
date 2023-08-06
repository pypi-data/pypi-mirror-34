-- getProfile(all)
-- CREATE OR REPLACE VIEW export_profiles_view AS ...

CREATE OR REPLACE VIEW export_css_view AS
SELECT profile_id,
       css_name
  FROM unitracc_export_css
 ORDER BY profile_id, load_position;
ALTER VIEW public.export_css_view OWNER TO "www-data";

-- bis hierher enthalten in Rev. 9926

BEGIN TRANSACTION;
ALTER TABLE unitracc_export_profile
  ADD COLUMN pdfreactor_api_calls text;
COMMENT ON COLUMN unitracc_export_profile.pdfreactor_api_calls IS 'API-Aufrufe für PDFreactor';


DROP VIEW IF EXISTS export_profiles_view;
CREATE VIEW export_profiles_view AS
 SELECT profile.id,
        profile.creator,
        profile.creation_date,
        profile.active,
        profile.type_id,
        profile.manual_css,
        profile.pdfreactor_api_calls,
        subportal.id AS sid,
        subportal.subportal,
        subportal.uid,
        titles.title,
        titles.lang_code,
        type.id AS etype_id,
        type.etype
   FROM unitracc_export_profile profile
   JOIN unitracc_export_profile_titles titles ON titles.profile_id = profile.id
   JOIN unitracc_subportal_unitracc_export_profile ON unitracc_subportal_unitracc_export_profile.profile = profile.id
   JOIN unitracc_subportal subportal ON unitracc_subportal_unitracc_export_profile.subportal = subportal.id
   JOIN unitracc_export_type type ON type.id = profile.type_id
  WHERE profile.id IS NOT NULL;

COMMIT;

BEGIN TRANSACTION;
-- betroffene Sichten löschen
DROP VIEW IF EXISTS export_profiles_view;

ALTER TABLE unitracc_export_profile
  ADD COLUMN main_template text;
COMMENT ON COLUMN unitracc_export_profile.main_template IS 'Wichtig für SCORM-Exporte, oder für komplexere HTML-/PDF-Layouts';

ALTER TABLE unitracc_export_profile
  ADD COLUMN browser_id character varying(50);
COMMENT ON COLUMN unitracc_export_profile.main_template IS 'Wichtig für SCORM-Exporte';

CREATE VIEW export_profiles_view AS
 SELECT profile.id,
        profile.creator,
        profile.creation_date,
        profile.active,
        profile.type_id,
        profile.manual_css,
        profile.main_template,
        profile.browser_id,
        profile.pdfreactor_api_calls,
        subportal.id AS sid,
        subportal.subportal,
        subportal.uid,
        titles.title,
        titles.lang_code,
        type.id AS etype_id,
        type.etype
   FROM unitracc_export_profile profile
   JOIN unitracc_export_profile_titles titles ON titles.profile_id = profile.id
   JOIN unitracc_subportal_unitracc_export_profile ON unitracc_subportal_unitracc_export_profile.profile = profile.id
   JOIN unitracc_subportal subportal ON unitracc_subportal_unitracc_export_profile.subportal = subportal.id
   JOIN unitracc_export_type type ON type.id = profile.type_id
  WHERE profile.id IS NOT NULL;

ALTER TABLE export_profiles_view
  OWNER TO "www-data";

COMMENT ON COLUMN export_profiles_view.uid IS 'Subportal-UID';

COMMIT;

INSERT INTO unitracc_export_type (etype) VALUES ('SCORM');
