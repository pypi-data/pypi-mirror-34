CREATE TABLE IF NOT EXISTS `write_required_field` (
  `write_required_field_id` CHAR(36),
  `system_id`               CHAR(36)     NOT NULL,
  `field_name`              VARCHAR(127) NOT NULL,
  `create_dttm`             DATETIME     NOT NULL,
  `update_dttm`             DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `delete_dttm`             DATETIME              DEFAULT NULL,
  PRIMARY KEY (`write_required_field_id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;


INSERT INTO `write_required_field` (`write_required_field_id`, `system_id`, `field_name`, `create_dttm`)
VALUES
  ('1', '3', 'manager', '2017-05-05 12:00:00'),
  ('2', '3', 'team', '2017-05-05 12:00:00'),
  ('3', '3', 'job_title', '2017-05-05 12:00:00'),
  ('4', '1', 'work_phone_number', '2017-05-05 12:00:00');

