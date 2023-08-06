CREATE TABLE IF NOT EXISTS `write_empty_field_by_user` (
  `write_empty_field_by_user_id` CHAR(36),
  `system_id`                    CHAR(36)     NOT NULL,
  `field_name`                   VARCHAR(127) NOT NULL,
  `user_email`                   VARCHAR(255),
  `default_value`                 VARCHAR(500),
  `create_dttm`                  DATETIME     NOT NULL,
  `update_dttm`                  DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `delete_dttm`                  DATETIME              DEFAULT NULL,
  PRIMARY KEY (`write_empty_field_by_user_id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;


INSERT INTO `write_empty_field_by_user` (`write_empty_field_by_user_id`, `system_id`, `field_name`, `user_email`, `default_value`, `create_dttm`)
VALUES
  ('1', '1', 'job_title', 'PDavidson@octopusinvestments.com', '', '2017-05-05 12:00:00'),
  ('2', '1', 'job_title', 'RCourt@octopusinvestments.com', '', '2017-05-05 12:00:00'),
  ('3', '1', 'job_title', 'GPaul-Florence@octopusinvestments.com', '', '2017-05-05 12:00:00'),
  ('4', '1', 'job_title', 'EKeelan@octopusinvestments.com', '', '2017-05-05 12:00:00'),
  ('5', '1', 'job_title', 'IPotter@octopusinvestments.com', '', '2017-05-05 12:00:00'),
  ('6', '1', 'job_title', 'CStreet@octopusinvestments.com', '', '2017-05-05 12:00:00');

