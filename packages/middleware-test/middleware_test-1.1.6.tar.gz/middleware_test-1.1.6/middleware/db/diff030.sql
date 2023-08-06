CREATE TABLE IF NOT EXISTS `user_field_change` (
  `user_field_change_id`     CHAR(36),
  `system`                   VARCHAR(127) NOT NULL,
  `field_name`               VARCHAR(127) NOT NULL,
  `first_name`               VARCHAR(127) NOT NULL,
  `last_name`                VARCHAR(127) NOT NULL,
  `active_directory_user_id` CHAR(36)     NOT NULL,
  `user_email`               VARCHAR(127) NOT NULL,
  `old_value`                VARCHAR(255) NOT NULL,
  `changed_to`               VARCHAR(255) NOT NULL,
  `create_dttm`              DATETIME     NOT NULL,
  `update_dttm`              DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP
  ON UPDATE CURRENT_TIMESTAMP,
  `delete_dttm`              DATETIME              DEFAULT NULL,
  PRIMARY KEY (`user_field_change_id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;
