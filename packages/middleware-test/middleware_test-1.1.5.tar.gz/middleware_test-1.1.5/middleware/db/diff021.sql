INSERT INTO `field_read_configuration` (`field_read_configuration_id`, `system_id`, `from_path`, `to_field_name`, `active`, `create_dttm`)
VALUES
  ('52', '1', '$.thumbnailPhoto', 'photo', TRUE, '2017-05-05 12:00:00'),
  ('53', '3', '$.photo', 'photo', TRUE, '2017-05-05 12:00:00');


INSERT INTO `field_write_configuration` (`field_write_configuration_id`, `system_id`, `from_field_name`, `to_path`, `active`, `create_dttm`)
VALUES
  ('48', '1', 'photo', '$.thumbnailPhoto', TRUE, '2017-05-05 12:00:00');