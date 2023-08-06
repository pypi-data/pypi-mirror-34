DROP TABLE IF EXISTS `system_access_info`;
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
CREATE PROCEDURE `get_logs_by_user_email`(IN user_email VARCHAR(255))
  BEGIN
    SELECT *
    FROM `log`
    WHERE `active_directory_user_id` IN ( SELECT `active_directory_user_id`
                                          FROM `active_directory_user`
                                          WHERE `email` LIKE CONCAT('%', user_email, '%') );
  END$$

DROP PROCEDURE IF EXISTS `get_ad_user_by_email`$$
CREATE PROCEDURE `get_ad_user_by_email`(IN user_email VARCHAR(255))
  BEGIN
    SELECT *
    FROM `active_directory_user`
    WHERE `email` LIKE CONCAT('%', user_email, '%');
  END$$

DROP PROCEDURE IF EXISTS `get_user_log_by_first_name`$$
CREATE PROCEDURE `get_user_log_by_first_name`(IN user_first_name VARCHAR(255))
  BEGIN
    SELECT *
    FROM `log`
    WHERE `active_directory_user_id` IN (
      SELECT *
      FROM `active_directory_user`
      WHERE `first_name` LIKE CONCAT('%', user_first_name, '%') );
  END$$

DROP PROCEDURE IF EXISTS `get_user_log_by_first_name_last_name`$$
CREATE PROCEDURE `get_user_log_by_first_name_last_name`(IN user_first_name VARCHAR(255), IN user_last_name VARCHAR(255))
  BEGIN
    SELECT *
    FROM `log`
    WHERE `active_directory_user_id` IN (
      SELECT *
      FROM `active_directory_user`
      WHERE `first_name` LIKE CONCAT('%', user_first_name, '%') AND `last_name` LIKE CONCAT('%', user_last_name, '%')
    );
  END$$

DROP PROCEDURE IF EXISTS `get_user_by_email_updated_dttm`$$
CREATE PROCEDURE `get_user_by_email_updated_dttm`(IN user_email VARCHAR(255), IN updated_at DATETIME)
  BEGIN
    SELECT *
    FROM `active_directory_user`
    WHERE `email` LIKE CONCAT('%', user_email, '%') AND `update_dttm` = updated_at;
  END$$

DROP PROCEDURE IF EXISTS `get_log_by_user_id_system_component_created`$$
CREATE PROCEDURE `get_log_by_user_id_system_component_created`(IN user_id    CHAR(36),
                                                               IN system     CHAR(36),
                                                               IN component  VARCHAR(36),
                                                               IN created_at DATETIME)
  BEGIN
    SELECT *
    FROM `log`
    WHERE `active_directory_user_id` = user_id AND `system_id` = system AND
          `component_name` = component AND `create_dttm` = created_at;
  END$$

DROP PROCEDURE IF EXISTS `get_log_by_user_id_created`$$
CREATE PROCEDURE `get_log_by_user_id_created`(IN user_id CHAR(36), IN created_at DATETIME)
  BEGIN
    SELECT *
    FROM `log`
    WHERE `active_directory_user_id` = user_id AND `create_dttm` = created_at;
  END$$

DROP PROCEDURE IF EXISTS `get_log_by_user_id_system_created`$$
CREATE PROCEDURE `get_log_by_user_id_system_created`(IN user_id    CHAR(36), IN system CHAR(36),
                                                     IN created_at DATETIME)
  BEGIN
    SELECT *
    FROM `log`
    WHERE
      `active_directory_user_id` = user_id AND `system_id` = system AND `create_dttm` = created_at;
  END$$


DROP PROCEDURE IF EXISTS `get_log_by_user_id_operation_created`$$
CREATE PROCEDURE `get_log_by_user_id_operation_created`(IN user_id    CHAR(36), IN operation_name VARCHAR(127),
                                                        IN created_at DATETIME)
  BEGIN
    SELECT *
    FROM `log`
    WHERE
      `active_directory_user_id` = user_id AND `operation` = operation_name AND `create_dttm` = created_at;
  END$$

DROP PROCEDURE IF EXISTS `get_actual_user_data`$$
CREATE PROCEDURE `get_actual_user_data`(IN user_id CHAR(36))
  BEGIN
    SELECT *
    FROM `actual_user_data`
    WHERE `active_directory_user_id` = user_id;
  END$$

DROP PROCEDURE IF EXISTS `get_field_read_configuration_by_system`$$
CREATE PROCEDURE `get_field_read_configuration_by_system`(IN system    CHAR(36),
                                                          IN is_active BOOLEAN)
  BEGIN
    SELECT *
    FROM `field_read_configuration`
    WHERE `system_id` = system and `active` = is_active;
  END$$

DROP PROCEDURE IF EXISTS `get_field_write_configuration_by_system`$$
CREATE PROCEDURE `get_field_write_configuration_by_system`(IN system CHAR(36), IN is_active BOOLEAN)
  BEGIN
    SELECT *
    FROM `field_write_configuration`
    WHERE `system_id` = system and `active` = is_active;
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
CREATE PROCEDURE `get_top_log_by_user_id_system_component_create`(IN user_id    CHAR(36),
                                                                     system     CHAR(36),
                                                                     component  VARCHAR(36),
                                                                  IN created_at DATETIME)
  BEGIN
    SELECT *
    FROM `log`
    WHERE `active_directory_user_id` = user_id AND `system_id` = system AND
          `component_name` = component AND `create_dttm` = created_at
    LIMIT 5;
  END$$

DROP PROCEDURE IF EXISTS `add_field_read_configuration`$$
CREATE PROCEDURE `add_field_read_configuration`(IN id         CHAR(36), system CHAR(36),
                                                IN from_p     VARCHAR(1024),
                                                IN to_field   VARCHAR(127), IN is_active BOOLEAN,
                                                IN created_at DATETIME)
  BEGIN
    INSERT INTO `field_read_configuration` (`field_read_configuration_id`, `system_id`, `from_path`, `to_field_name`, `active`, `create_dttm`)
    VALUES
      ( id, system, from_p, to_field, is_active, created_at );
  END$$


DROP PROCEDURE IF EXISTS `add_field_write_configuration`$$
CREATE PROCEDURE `add_field_write_configuration`(IN id         CHAR(36), system CHAR(36),
                                                 IN from_field VARCHAR(127),
                                                 IN path       VARCHAR(1024), IN is_active BOOLEAN,
                                                 IN created_at DATETIME)
  BEGIN
    INSERT INTO `field_write_configuration` (`field_write_configuration_id`, `system_id`, `from_field_name`, `to_path`, `active`, `create_dttm`)
    VALUES
      ( id, system, from_field, path, is_active, created_at );
  END$$

DROP PROCEDURE IF EXISTS `add_system`$$
CREATE PROCEDURE `add_system`(IN id         CHAR(36), IN system_name VARCHAR(64), IN descrip VARCHAR(255),
                              IN created_at DATETIME)
  BEGIN
    INSERT INTO `system` (`system_id`, `name`, `description`, `create_dttm`)
    VALUES
      ( id, system_name, descrip, created_at );
  END$$


DROP PROCEDURE IF EXISTS `add_write_forbidden_field`$$
CREATE PROCEDURE `add_write_forbidden_field`(IN id    CHAR(36), IN system CHAR(36),
                                                field VARCHAR(127), IN created_at DATETIME)
  BEGIN
    INSERT INTO `write_forbidden_field` (`write_forbidden_field_id`, `system_id`, `field_name`, `create_dttm`)
    VALUES
      ( id, system, field, created_at );
  END$$


DROP PROCEDURE IF EXISTS `add_write_required_field`$$
CREATE PROCEDURE `add_write_required_field`(IN id    CHAR(36), IN system CHAR(36),
                                               field VARCHAR(127), IN created_at DATETIME)
  BEGIN
    INSERT INTO `write_required_field` (`write_required_field_id`, `system_id`, `field_name`, `create_dttm`)
    VALUES
      ( id, system, field, created_at );
  END$$

DROP PROCEDURE IF EXISTS `add_write_empty_field_by_user`$$
CREATE PROCEDURE `add_write_empty_field_by_user`(IN id        CHAR(36), IN system CHAR(36),
                                                    field     VARCHAR(127),
                                                 IN email     VARCHAR(255),
                                                 IN default_v VARCHAR(500), IN created_at DATETIME)
  BEGIN
    INSERT INTO `write_empty_field_by_user` (`write_empty_field_by_user_id`, `system_id`, `field_name`, `user_email`, `default_value`, `create_dttm`)
    VALUES
      ( id, system, field, email, default_v, created_at );
  END$$

DROP PROCEDURE IF EXISTS `get_system_by_system_id`$$
CREATE PROCEDURE `get_system_by_system_id`(IN system CHAR(36))
  BEGIN
    SELECT *
    FROM `system`
    where `system_id` = system;
  END$$

DROP PROCEDURE IF EXISTS `get_user_by_login`$$
CREATE PROCEDURE `get_user_by_login`(in user_login VARCHAR(127))
  BEGIN
    SELECT *
    FROM `active_directory_user`
    where `login` = user_login;
  END$$

DROP PROCEDURE IF EXISTS `get_user_by_first_name_last_name`$$
CREATE PROCEDURE `get_user_by_first_name_last_name`(in user_first_name VARCHAR(127),
                                                       user_last_name  VARCHAR(127))
  BEGIN
    SELECT *
    FROM `active_directory_user`
    where `first_name` = user_first_name and `last_name` = user_last_name;
  END$$

DROP PROCEDURE IF EXISTS `get_user_by_id`$$
CREATE PROCEDURE `get_user_by_id`(in user_id CHAR(36))
  BEGIN
    SELECT *
    FROM `active_directory_user`
    where `active_directory_user_id` = user_id;
  END$$

DROP PROCEDURE IF EXISTS `get_write_forbidden_field_by_system`$$
CREATE PROCEDURE `get_write_forbidden_field_by_system`(in system CHAR(36))
  BEGIN
    SELECT *
    FROM `write_forbidden_field`
    where `system_id` = system;
  END$$

DROP PROCEDURE IF EXISTS `get_write_required_field_by_system`$$
CREATE PROCEDURE `get_write_required_field_by_system`(in system CHAR(36))
  BEGIN
    SELECT *
    FROM `write_required_field`
    where `system_id` = system;
  END$$

DROP PROCEDURE IF EXISTS `get_write_empty_field_by_user_by_system`$$
CREATE PROCEDURE `get_write_empty_field_by_user_by_system`(in system CHAR(36),
                                                           in email  VARCHAR(255))
  BEGIN
    SELECT *
    FROM `write_empty_field_by_user`
    where `system_id` = system and `user_email` = email;
  END$$

DELIMITER ; $$