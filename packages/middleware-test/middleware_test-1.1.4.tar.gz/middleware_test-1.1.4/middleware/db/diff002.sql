CREATE TABLE IF NOT EXISTS `write_forbidden_field` (
  `write_forbidden_field_id` CHAR(36),
  `system_id`                CHAR(36)     NOT NULL,
  `field_name`               VARCHAR(127) NOT NULL,
  `create_dttm`              DATETIME     NOT NULL,
  `update_dttm`              DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `delete_dttm`              DATETIME              DEFAULT NULL,
  PRIMARY KEY (`write_forbidden_field_id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;


INSERT INTO `write_forbidden_field` (`write_forbidden_field_id`, `system_id`, `field_name`, `create_dttm`)
VALUES
  ('1', '3', 'last_name', '2017-05-05 12:00:00'),
  ('2', '3', 'first_name', '2017-05-05 12:00:00'),
  ('3', '3', 'middle_name', '2017-05-05 12:00:00'),
  ('4', '3', 'gender', '2017-05-05 12:00:00'),
  ('5', '3', 'birth_date', '2017-05-05 12:00:00'),
  ('6', '3', 'nationality', '2017-05-05 12:00:00'),
  ('7', '3', 'start_date', '2017-05-05 12:00:00'),
  ('8', '3', 'end_date', '2017-05-05 12:00:00'),
  ('9', '1', 'updated_at', '2017-05-05 12:00:00'),
  ('10', '1', 'display_name', '2017-05-05 12:00:00'),
  ('11', '3', 'salutation', '2017-05-05 12:00:00'),
  ('12', '3', 'manager', '2017-05-05 12:00:00'),
  ('13', '3', 'team', '2017-05-05 12:00:00'),
  ('14', '3', 'job_title', '2017-05-05 12:00:00');

