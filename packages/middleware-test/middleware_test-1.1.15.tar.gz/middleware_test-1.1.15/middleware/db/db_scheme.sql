SET @@global.time_zone = '+00:00';

CREATE DATABASE `middleware`;
USE `middleware`;

CREATE TABLE IF NOT EXISTS `sync` (
  `sync_id`     CHAR(36),
  `create_dttm` DATETIME DEFAULT NULL,
  `update_dttm` DATETIME  DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `delete_dttm` DATETIME DEFAULT NULL,
  PRIMARY KEY (`sync_id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;


CREATE TABLE IF NOT EXISTS `system` (
  `system_id`    CHAR(36),
  `name`         VARCHAR(64) NOT NULL UNIQUE,
  `description`  VARCHAR(255),
  `sync_enabled` BOOLEAN     NOT NULL DEFAULT TRUE,
  `create_dttm`  DATETIME    NOT NULL,
  `update_dttm`  DATETIME    NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `delete_dttm`  DATETIME             DEFAULT NULL,
  PRIMARY KEY (`system_id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;


CREATE TABLE IF NOT EXISTS `active_directory_user` (
  `active_directory_user_id` CHAR(36),
  `first_name`               VARCHAR(127),
  `last_name`                VARCHAR(127),
  `login`                    VARCHAR(127) NOT NULL,
  `email`                    VARCHAR(255),
  `metadata`                 LONGTEXT     NOT NULL,
  `create_dttm`              DATETIME     NOT NULL,
  `update_dttm`              DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `delete_dttm`              DATETIME              DEFAULT NULL,
  PRIMARY KEY (`active_directory_user_id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

CREATE TABLE IF NOT EXISTS `log` (
  `log_id`                   BIGINT         AUTO_INCREMENT,
  `sync_id`                  CHAR(36),
  `component_id`             INT(2)            DEFAULT NULL,
  `component_name`           VARCHAR(36)       DEFAULT NULL,
  `data_1`                   LONGTEXT          DEFAULT NULL,
  `data_2`                   LONGTEXT          DEFAULT NULL,
  `data_3`                   LONGTEXT          DEFAULT NULL,
  `data_4`                   LONGTEXT          DEFAULT NULL,
  `data_5`                   LONGTEXT          DEFAULT NULL,
  `success`                  BOOLEAN,
  `message`                  VARCHAR(1024),
  `operation`                VARCHAR(127),
  `system_id`                CHAR(36),
  `active_directory_user_id` CHAR(36),
  `execution_time`           INT(11),
  `create_dttm`              DATETIME NOT NULL,
  `update_dttm`              DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `delete_dttm`              DATETIME          DEFAULT NULL,
  PRIMARY KEY (`log_id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;


CREATE TABLE IF NOT EXISTS `field_read_configuration` (
  `field_read_configuration_id` CHAR(36),
  `system_id`                   CHAR(36)      NOT NULL,
  `from_path`                   VARCHAR(1024) NOT NULL,
  `to_field_name`               VARCHAR(127)  NOT NULL,
  `active`                      BOOLEAN       NOT NULL DEFAULT TRUE,
  `create_dttm`                 DATETIME      NOT NULL,
  `update_dttm`                 DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `delete_dttm`                 DATETIME               DEFAULT NULL,
  PRIMARY KEY (`field_read_configuration_id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;


CREATE TABLE IF NOT EXISTS `actual_user_data` (
  `actual_user_data_id`      CHAR(36),
  `active_directory_user_id` CHAR(36) NOT NULL UNIQUE,
  `data`                     LONGTEXT NOT NULL,
  `create_dttm`              DATETIME NOT NULL,
  `update_dttm`              DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `delete_dttm`              DATETIME          DEFAULT NULL,
  PRIMARY KEY (`actual_user_data_id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;


CREATE TABLE IF NOT EXISTS `field_write_configuration` (
  `field_write_configuration_id` CHAR(36),
  `system_id`                    CHAR(36)      NOT NULL,
  `from_field_name`              VARCHAR(127)  NOT NULL,
  `to_path`                      VARCHAR(1024) NOT NULL,
  `active`                       BOOLEAN       NOT NULL DEFAULT TRUE,
  `create_dttm`                  DATETIME      NOT NULL,
  `update_dttm`                  DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `delete_dttm`                  DATETIME               DEFAULT NULL,
  PRIMARY KEY (`field_write_configuration_id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

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

CREATE TABLE IF NOT EXISTS `slack_user_group` (
  `slack_user_group_id`       MEDIUMINT         AUTO_INCREMENT,
  `slack_group_name`          VARCHAR(255)      NOT NULL,
  `active_directory_user_id`  CHAR(36) NOT NULL UNIQUE,
  `create_dttm` DATETIME      DEFAULT NULL,
  `update_dttm` DATETIME      DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `delete_dttm` DATETIME      DEFAULT NULL,
  PRIMARY KEY (`slack_user_group_id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

CREATE TABLE IF NOT EXISTS `user_field_change` (
  `user_field_change_id`     CHAR(36),
  `system`                   VARCHAR(127) NOT NULL,
  `sync_id` CHAR(36) DEFAULT NULL
  `field_name`               VARCHAR(127) NOT NULL,
  `first_name`               VARCHAR(127) NOT NULL,
  `last_name`                VARCHAR(127) NOT NULL,
  `active_directory_user_id` CHAR(36)     NOT NULL,
  `user_email`               VARCHAR(127) NOT NULL,
  `old_value`                VARCHAR(255),
  `changed_to`               VARCHAR(255) NOT NULL,
  `create_dttm`              DATETIME     NOT NULL,
  `update_dttm`              DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP
  ON UPDATE CURRENT_TIMESTAMP,
  `delete_dttm`              DATETIME              DEFAULT NULL,
  PRIMARY KEY (`user_field_change_id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;