INSERT INTO `system` (`system_id`, `name`, `description`, `create_dttm`)
VALUES
  ('4', 'OfficeVibe', '', '2017-05-05 12:00:00');

INSERT INTO `field_read_configuration` (`field_read_configuration_id`, `system_id`, `from_path`, `to_field_name`, `active`, `create_dttm`)
VALUES
  ('56', '4', '$.data.email', 'email', TRUE, '2017-05-05 12:00:00'),
  ('57', '4', '$.data.fistName', 'first_name', TRUE, '2017-05-05 12:00:00'),
  ('58', '4', '$.data.lastName', 'last_name', TRUE, '2017-05-05 12:00:00'),
  ('59', '4', '$.data.jobTitle', 'job_title', TRUE, '2017-05-05 12:00:00'),
  ('60', '4', '$.updated_at', 'updated_at', TRUE, '2017-05-05 12:00:00'),
  ('61', '4', '$.manager', 'manager', TRUE, '2017-05-05 12:00:00');

INSERT INTO `field_write_configuration` (`field_write_configuration_id`, `system_id`, `from_field_name`, `to_path`, `active`, `create_dttm`)
VALUES
  ('52', '4', 'email', '$.email', TRUE, '2017-05-05 12:00:00'),
  ('53', '4', 'first_name', '$.fistName', TRUE, '2017-05-05 12:00:00'),
  ('54', '4', 'last_name', '$.lastName', TRUE, '2017-05-05 12:00:00'),
  ('55', '4', 'job_title', '$.jobTitle', TRUE, '2017-05-05 12:00:00'),
  ('56', '4', 'photo', '$.imageUrl', TRUE, '2017-05-05 12:00:00'),
  ('57', '4', 'manager', '$.manager', TRUE, '2017-05-05 12:00:00');
