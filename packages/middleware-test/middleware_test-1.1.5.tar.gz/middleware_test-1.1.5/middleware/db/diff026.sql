INSERT INTO `field_read_configuration` (`field_read_configuration_id`, `system_id`, `from_path`, `to_field_name`, `active`, `create_dttm`)
VALUES
  ('62', '1', '$.employeeID', 'person_number', TRUE, '2017-05-05 12:00:00');

INSERT INTO `field_write_configuration` (`field_write_configuration_id`, `system_id`, `from_field_name`, `to_path`, `active`, `create_dttm`)
VALUES
  ('58', '1', 'person_number', '$.employeeID', TRUE, '2017-05-05 12:00:00');

INSERT INTO `write_required_field` (`write_required_field_id`, `system_id`, `field_name`, `create_dttm`)
VALUES
  ('5', '3', 'person_number', '2017-05-05 12:00:00');