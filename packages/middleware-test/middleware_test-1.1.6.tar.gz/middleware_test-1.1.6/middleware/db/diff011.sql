
DELIMITER $$

DROP PROCEDURE IF EXISTS `get_user_by_email_updated_dttm`$$
CREATE PROCEDURE `get_user_by_email_updated_dttm`(IN user_email VARCHAR(255), IN updated_at varchar(127))
  BEGIN
    SELECT *
    FROM `active_directory_user`
    WHERE `email` LIKE CONCAT('%', user_email, '%') AND `update_dttm` LIKE CONCAT('%', updated_at, '%');
  END$$

DROP PROCEDURE IF EXISTS `get_log_by_user_id_system_component_created`$$
CREATE PROCEDURE `get_log_by_user_id_system_component_created`(IN user_id    CHAR(36),
                                                               IN system     CHAR(36),
                                                               IN component  VARCHAR(36),
                                                               IN created_at varchar(127))
  BEGIN
    SELECT *
    FROM `log`
    WHERE `active_directory_user_id` = user_id AND `system_id` = system AND
          `component_name` LIKE CONCAT('%', component, '%') AND `create_dttm` LIKE CONCAT('%', created_at, '%');
  END$$

DROP PROCEDURE IF EXISTS `get_log_by_user_id_created`$$
CREATE PROCEDURE `get_log_by_user_id_created`(IN user_id CHAR(36), IN created_at varchar(127))
  BEGIN
    SELECT *
    FROM `log`
    WHERE `active_directory_user_id` = user_id AND `create_dttm` LIKE CONCAT('%', created_at, '%');
  END$$

DROP PROCEDURE IF EXISTS `get_log_by_user_id_system_created`$$
CREATE PROCEDURE `get_log_by_user_id_system_created`(IN user_id    CHAR(36), IN system CHAR(36),
                                                     IN created_at varchar(127))
  BEGIN
    SELECT *
    FROM `log`
    WHERE
      `active_directory_user_id` = user_id AND `system_id` = system AND `create_dttm` LIKE CONCAT('%', created_at, '%');
  END$$


DROP PROCEDURE IF EXISTS `get_log_by_user_id_operation_created`$$
CREATE PROCEDURE `get_log_by_user_id_operation_created`(IN user_id    CHAR(36), IN operation_name VARCHAR(127),
                                                        IN created_at varchar(127))
  BEGIN
    SELECT *
    FROM `log`
    WHERE
      `active_directory_user_id` = user_id AND `operation` LIKE CONCAT('%', operation_name, '%') AND `create_dttm` LIKE CONCAT('%', created_at, '%');
  END$$


DROP PROCEDURE IF EXISTS `get_top_log_by_user_id_system_component_create`$$
CREATE PROCEDURE `get_top_log_by_user_id_system_component_create`(IN user_id    CHAR(36),
                                                                     system     CHAR(36),
                                                                     component  VARCHAR(36),
                                                                  IN created_at varchar(127))
  BEGIN
    SELECT *
    FROM `log`
    WHERE `active_directory_user_id` = user_id AND `system_id` = system AND
          `component_name` LIKE CONCAT('%', component, '%') AND `create_dttm` LIKE CONCAT('%', created_at, '%')
    LIMIT 5;
  END$$

DELIMITER ; $$