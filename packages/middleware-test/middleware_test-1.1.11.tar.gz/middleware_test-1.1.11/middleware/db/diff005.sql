DELIMITER $$


DROP PROCEDURE IF EXISTS `get_field_read_configuration`;
CREATE PROCEDURE `get_field_read_configuration`()
  BEGIN
    SELECT *
    FROM `field_read_configuration`;
  END$$

DROP PROCEDURE IF EXISTS `get_field_write_configuration`$$
CREATE PROCEDURE `get_field_write_configuration`()
  BEGIN
    SELECT *
    FROM `field_write_configuration`;
  END$$

DROP PROCEDURE IF EXISTS `get_write_forbidden_field`$$
CREATE PROCEDURE `get_write_forbidden_field`()
  BEGIN
    SELECT *
    FROM `write_forbidden_field`;
  END$$


DROP PROCEDURE IF EXISTS `get_write_required_field`$$
CREATE PROCEDURE `get_write_required_field`()
  BEGIN
    SELECT *
    FROM `write_required_field`;
  END$$

DROP PROCEDURE IF EXISTS `get_write_empty_field_by_user`$$
CREATE PROCEDURE `get_write_empty_field_by_user`()
  BEGIN
    SELECT *
    FROM `write_empty_field_by_user`;
  END$$

DROP PROCEDURE IF EXISTS `get_logs_by_user_email`$$
CREATE PROCEDURE `get_logs_by_user_email`(IN email VARCHAR(255))
  BEGIN
    SELECT *
    FROM `log`
    WHERE `active_directory_user_id` IN ( SELECT `active_directory_user_id`
                                          FROM `active_directory_user`
                                          WHERE `email` LIKE CONCAT('%', email, '%') );
  END$$

DROP PROCEDURE IF EXISTS `get_ad_user_by_email`$$
CREATE PROCEDURE `get_ad_user_by_email`(IN email VARCHAR(255))
  BEGIN
    SELECT *
    FROM `active_directory_user`
    WHERE `email` LIKE CONCAT('%', email, '%');
  END$$

DROP PROCEDURE IF EXISTS `get_user_log_by_first_name`$$
CREATE PROCEDURE `get_user_log_by_first_name`(IN first_name VARCHAR(255))
  BEGIN
    SELECT *
    FROM `log`
    WHERE `active_directory_user_id` IN (
      SELECT *
      FROM `active_directory_user`
      WHERE `first_name` LIKE CONCAT('%', first_name, '%') );
  END$$

DROP PROCEDURE IF EXISTS `get_user_log_by_first_name_last_name`$$
CREATE PROCEDURE `get_user_log_by_first_name_last_name`(IN first_name VARCHAR(255), IN last_name VARCHAR(255))
  BEGIN
    SELECT *
    FROM `log`
    WHERE `active_directory_user_id` IN (
      SELECT *
      FROM `active_directory_user`
      WHERE `first_name` LIKE CONCAT('%', first_name, '%') AND `last_name` LIKE CONCAT('%', last_name, '%')
    );
  END$$

DROP PROCEDURE IF EXISTS `get_user_by_email_updated_dttm`$$
CREATE PROCEDURE `get_user_by_email_updated_dttm`(IN email VARCHAR(255), IN updated_at DATETIME)
  BEGIN
    SELECT *
    FROM `active_directory_user`
    WHERE `email` LIKE CONCAT('%', email, '%') AND `update_dttm` = updated_at;
  END$$

DROP PROCEDURE IF EXISTS `get_log_by_user_id_system_component_created`$$
CREATE PROCEDURE `get_log_by_user_id_system_component_created`(IN active_directory_user_id CHAR(36),
                                                               IN system_id                CHAR(36),
                                                               IN component_name           VARCHAR(36),
                                                               IN created_at               DATETIME)
  BEGIN
    SELECT *
    FROM `log`
    WHERE `active_directory_user_id` = active_directory_user_id AND `system_id` = system_id AND
          `component_name` = component_name AND `create_dttm` = created_at;
  END$$

DROP PROCEDURE IF EXISTS `get_log_by_user_id_created`$$
CREATE PROCEDURE `get_log_by_user_id_created`(IN active_directory_user_id CHAR(36), IN created_at DATETIME)
  BEGIN
    SELECT *
    FROM `log`
    WHERE `active_directory_user_id` = active_directory_user_id AND `create_dttm` = created_at;
  END$$

DROP PROCEDURE IF EXISTS `get_log_by_user_id_system_created`$$
CREATE PROCEDURE `get_log_by_user_id_system_created`(IN active_directory_user_id CHAR(36), IN system_id CHAR(36),
                                                     IN created_at               DATETIME)
  BEGIN
    SELECT *
    FROM `log`
    WHERE
      `active_directory_user_id` = active_directory_user_id AND `system_id` = system_id AND `create_dttm` = created_at;
  END$$


DROP PROCEDURE IF EXISTS `get_log_by_user_id_operation_created`$$
CREATE PROCEDURE `get_log_by_user_id_operation_created`(IN active_directory_user_id CHAR(36), IN operation VARCHAR(127),
                                                        IN created_at               DATETIME)
  BEGIN
    SELECT *
    FROM `log`
    WHERE
      `active_directory_user_id` = active_directory_user_id AND `operation` = operation AND `create_dttm` = created_at;
  END$$

DROP PROCEDURE IF EXISTS `get_actual_user_data`$$
CREATE PROCEDURE `get_actual_user_data`(IN active_directory_user_id CHAR(36))
  BEGIN
    SELECT *
    FROM `actual_user_data`
    WHERE `active_directory_user_id` = active_directory_user_id;
  END$$

DROP PROCEDURE IF EXISTS `get_actual_user_data`$$
CREATE PROCEDURE `get_actual_user_data`(IN active_directory_user_id CHAR(36))
  BEGIN
    SELECT *
    FROM `actual_user_data`
    WHERE `active_directory_user_id` = active_directory_user_id;
  END$$


DROP PROCEDURE IF EXISTS `get_field_read_configuration_by_system`$$
CREATE PROCEDURE `get_field_read_configuration_by_system`(IN system_id CHAR(36))
  BEGIN
    SELECT *
    FROM `field_read_configuration`
    WHERE `system_id` = system_id;
  END$$

DROP PROCEDURE IF EXISTS `get_field_write_configuration_by_system`$$
CREATE PROCEDURE `get_field_write_configuration_by_system`(IN system_id CHAR(36))
  BEGIN
    SELECT *
    FROM `field_write_configuration`
    WHERE `system_id` = system_id;
  END$$

DROP PROCEDURE IF EXISTS `get_components_list`$$
CREATE PROCEDURE `get_components_list`()
  BEGIN
    SELECT DISTINCT `component_name`
    FROM `log`;
  END$$

DROP PROCEDURE IF EXISTS `get_operations_list`$$
CREATE PROCEDURE `get_operations_list`()
  BEGIN
    SELECT DISTINCT `operation`
    FROM `log`;
  END$$


DROP PROCEDURE IF EXISTS `get_top_log_by_user_id_system_component_create`$$
CREATE PROCEDURE `get_top_log_by_user_id_system_component_create`(IN active_directory_user_id CHAR(36),
                                                                     system_id                CHAR(36),
                                                                     component_name           VARCHAR(36),
                                                                  IN created_at               DATETIME)
  BEGIN
    SELECT *
    FROM `log`
    WHERE `active_directory_user_id` = active_directory_user_id AND `system_id` = system_id AND
          `component_name` = component_name AND `create_dttm` = created_at
    LIMIT 5;
  END$$

DROP PROCEDURE IF EXISTS `add_field_read_configuration`$$
CREATE PROCEDURE `add_field_read_configuration`(IN field_read_configuration_id CHAR(36), system_id CHAR(36),
                                                IN from_path                   VARCHAR(1024),
                                                IN to_field_name               VARCHAR(127), IN active BOOLEAN,
                                                IN create_dttm                 DATETIME)
  BEGIN
    INSERT INTO `field_read_configuration` (`field_read_configuration_id`, `system_id`, `from_path`, `to_field_name`, `active`, `create_dttm`)
    VALUES
      ( field_read_configuration_id, system_id, from_path, to_field_name, active, create_dttm );
  END$$


DROP PROCEDURE IF EXISTS `add_field_write_configuration`$$
CREATE PROCEDURE `add_field_write_configuration`(IN add_field_write_configuration_id CHAR(36), system_id CHAR(36),
                                                 IN from_field_name                  VARCHAR(127),
                                                 IN to_path                          VARCHAR(1024), IN active BOOLEAN,
                                                 IN create_dttm                      DATETIME)
  BEGIN
    INSERT INTO `field_write_configuration` (`field_write_configuration_id`, `system_id`, `from_field_name`, `to_path`, `active`, `create_dttm`)
    VALUES
      ( field_write_configuration_id, system_id, from_field_name, to_path, active, create_dttm );
  END$$

DROP PROCEDURE IF EXISTS `add_system`$$
CREATE PROCEDURE `add_system`(IN system_id   CHAR(36), IN name VARCHAR(64), IN `description` VARCHAR(255),
                              IN create_dttm DATETIME)
  BEGIN
    INSERT INTO `system` (`system_id`, `name`, `description`, `create_dttm`)
    VALUES
      ( system_id, name, description, create_dttm );
  END$$


DROP PROCEDURE IF EXISTS `add_write_forbidden_field`$$
CREATE PROCEDURE `add_write_forbidden_field`(IN write_forbidden_field_id CHAR(36), IN system_id CHAR(36),
                                                field_name               VARCHAR(127), IN create_dttm DATETIME)
  BEGIN
    INSERT INTO `write_forbidden_field` (`write_forbidden_field_id`, `system_id`, `field_name`, `create_dttm`)
    VALUES
      ( write_forbidden_field_id, system_id, field_name, create_dttm );
  END$$


DROP PROCEDURE IF EXISTS `add_write_required_field`$$
CREATE PROCEDURE `add_write_required_field`(IN write_required_field_id CHAR(36), IN system_id CHAR(36),
                                               field_name              VARCHAR(127), IN create_dttm DATETIME)
  BEGIN
    INSERT INTO `write_required_field` (`write_required_field_id`, `system_id`, `field_name`, `create_dttm`)
    VALUES
      ( write_required_field_id, system_id, field_name, create_dttm );
  END$$

DROP PROCEDURE IF EXISTS `add_write_empty_field_by_user`$$
CREATE PROCEDURE `add_write_empty_field_by_user`(IN write_empty_field_by_user_id CHAR(36), IN system_id CHAR(36),
                                                    field_name                   VARCHAR(127),
                                                 IN user_email                   VARCHAR(255),
                                                 IN default_value                VARCHAR(500), IN create_dttm DATETIME)
  BEGIN
    INSERT INTO `write_empty_field_by_user` (`write_empty_field_by_user_id`, `system_id`, `field_name`, `user_email`, `default_value`, `create_dttm`)
    VALUES
      ( write_empty_field_by_user_id, system_id, field_name, user_email, default_value, create_dttm );
  END$$

DELIMITER ; $$