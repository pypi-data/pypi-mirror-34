SET @@global.time_zone = '+00:00';

CREATE TABLE IF NOT EXISTS `sync` (
  `sync_id`     CHAR(36),
  `create_dttm` DATETIME DEFAULT NULL,
  `update_dttm` DATETIME DEFAULT NULL,
  `delete_dttm` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
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


CREATE TABLE IF NOT EXISTS `system_access_info` (
  `system_access_info_id`    CHAR(36),
  `system_id`                CHAR(36) NOT NULL,
  `active_directory_user_id` CHAR(36) NOT NULL,
  `access_info`              LONGTEXT NOT NULL,
  `create_dttm`              DATETIME NOT NULL,
  `update_dttm`              DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `delete_dttm`              DATETIME          DEFAULT NULL,
  PRIMARY KEY (`system_access_info_id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;


CREATE UNIQUE INDEX unique_system_id_and_active_directory_user_id_index
  ON `system_access_info` (`system_id`, `active_directory_user_id`);


CREATE TABLE IF NOT EXISTS `log` (
  `log_id`                   MEDIUMINT         AUTO_INCREMENT,
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