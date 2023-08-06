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
CREATE PROCEDURE `get_system_by_system_id`(IN system_col CHAR(36))
  BEGIN
    SELECT *
    FROM `system`
    where `system_id` = system_col;
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

DROP PROCEDURE IF EXISTS `delete_logs`$$
CREATE PROCEDURE `delete_logs`(in days int)
  BEGIN
    DELETE FROM `log`
    WHERE `create_dttm` < CURRENT_DATE - INTERVAL days DAY;
  END$$


DROP PROCEDURE IF EXISTS `add_system`$$
CREATE PROCEDURE `add_system`(IN id      CHAR(36), IN system_name VARCHAR(64), IN descrip VARCHAR(255),
                              IN enabled tinyint)
  BEGIN
    INSERT INTO `system` (`system_id`, `name`, `description`, `sync_enabled`)
    VALUES
      ( id, system_name, descrip, enabled );
  END$$

DROP PROCEDURE IF EXISTS `update_active_directory_user`$$
CREATE PROCEDURE `update_active_directory_user`(IN id      CHAR(36), IN f_name VARCHAR(127), IN l_name VARCHAR(127),
                                                in login_v VARCHAR(127), in user_email VARCHAR(255), in m_data longtext)
  BEGIN
    Update `active_directory_user`
    set
      `first_name`  = f_name, `last_name` = l_name, `login` = login_v, `email` = user_email, `metadata` = m_data,
      `delete_dttm` = NULL
    where `active_directory_user_id` = id;
  END$$

DROP PROCEDURE IF EXISTS `update_actual_user_data`$$
CREATE PROCEDURE `update_actual_user_data`(IN id       CHAR(36), ad_user_id CHAR(36),
                                           IN new_data longtext)
  BEGIN
    Update `actual_user_data`
    set `active_directory_user_id` = ad_user_id, `data` = new_data
    where `actual_user_data_id` = id;
  END$$


DROP PROCEDURE IF EXISTS `add_log`$$
CREATE PROCEDURE `add_log`(sync           CHAR(36), component int(2), component_n varchar(36), data1 longtext,
                           data2          longtext, data3 longtext, data4 longtext, data5 longtext,
                           is_success     tinyint(1), message_ varchar(1024),
                           operation_name varchar(127), system char(36), ad_user_id char(36), exec_time int(11))
  BEGIN
    INSERT INTO `log` (`sync_id`, `component_id`, `component_name`, `data_1`,
                       `data_2`, `data_3`, `data_4`, `data_5`, `success`, `message`, `operation`, `system_id`, `active_directory_user_id`,
                       `execution_time`, `create_dttm`)
    VALUES ( sync, component, component_n, data1,
                   data2, data3, data4, data5, is_success, message_,
                   operation_name, system, ad_user_id, exec_time, CURRENT_TIMESTAMP );
  END$$


DROP PROCEDURE IF EXISTS `get_all_users`$$
CREATE PROCEDURE `get_all_users`()
  BEGIN
    SELECT *
    FROM `active_directory_user`
    where `delete_dttm` is NULL;
  END$$

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
      `active_directory_user_id` = user_id AND `operation` LIKE CONCAT('%', operation_name, '%') AND
      `create_dttm` LIKE CONCAT('%', created_at, '%');
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


DROP PROCEDURE IF EXISTS `delete_active_directory_user`$$
CREATE PROCEDURE `delete_active_directory_user`(in id char(36))
  BEGIN
    Update `active_directory_user`
    set `delete_dttm` = CURRENT_TIMESTAMP
    where `active_directory_user_id` = id;
  END$$

DROP PROCEDURE IF EXISTS `add_active_directory_user`$$
CREATE PROCEDURE `add_active_directory_user`(IN id      CHAR(36), IN f_name VARCHAR(127), IN l_name VARCHAR(127),
                                             in login_v VARCHAR(127), in user_email VARCHAR(255), in m_data longtext)
  BEGIN
    INSERT INTO `active_directory_user` (`active_directory_user_id`, `first_name`, `last_name`, `login`, `email`, `metadata`, `create_dttm`)
    VALUES
      ( id, f_name, l_name, login_v, user_email, m_data, current_timestamp );
  END$$

DROP PROCEDURE IF EXISTS `add_actual_user_data`$$
CREATE PROCEDURE `add_actual_user_data`(IN id       CHAR(36), ad_user_id CHAR(36),
                                        IN new_data longtext)
  BEGIN
    INSERT INTO `actual_user_data` (`actual_user_data_id`, `active_directory_user_id`, `data`, `create_dttm`)
    VALUES
      ( id, ad_user_id, new_data, CURRENT_TIMESTAMP );
  END$$

DROP PROCEDURE IF EXISTS `add_sync`$$
CREATE PROCEDURE `add_sync`(IN sync CHAR(36))
  BEGIN
    INSERT INTO `sync` (`sync_id`, `create_dttm`)
    VALUES ( sync, current_timestamp );
  END$$

DROP PROCEDURE IF EXISTS `add_slack_user_group`$$
CREATE PROCEDURE `add_slack_user_group`(in group_name varchar(255), ad_user_id CHAR(36))
  BEGIN
    INSERT INTO `slack_user_group` (`slack_group_name`, `active_directory_user_id`, `create_dttm`)
    VALUES
      ( group_name, ad_user_id, CURRENT_TIMESTAMP );
  END$$

DROP PROCEDURE IF EXISTS `update_slack_user_group`$$
CREATE PROCEDURE `update_slack_user_group`(in group_name varchar(255), ad_user_id CHAR(36))
  BEGIN
    UPDATE `slack_user_group`
    SET `slack_group_name` = group_name
    WHERE `active_directory_user_id` = ad_user_id;

  END$$

DROP PROCEDURE IF EXISTS `get_slack_user_group_name`$$
CREATE PROCEDURE `get_slack_user_group_name`(ad_user_id CHAR(36))
  BEGIN
    SELECT `slack_group_name`
    FROM `slack_user_group`
    WHERE `active_directory_user_id` = ad_user_id;
  END$$

DROP PROCEDURE IF EXISTS `get_full_logs`$$
CREATE PROCEDURE `get_full_logs`(IN create_date VARCHAR(255))
  BEGIN
    SELECT *
    FROM log
    WHERE create_dttm LIKE CONCAT('%', create_date, '%');
  END$$

DROP PROCEDURE IF EXISTS `get_user_field_change_by_date`$$
CREATE PROCEDURE `get_user_field_change_by_date`(IN create_date VARCHAR(255))
  BEGIN
    SELECT *
    FROM user_field_change
    WHERE
      create_dttm LIKE CONCAT('%', create_date, '%')
    ORDER BY user_email;
  END$$

DROP PROCEDURE IF EXISTS `get_user_field_change_by_date_email`$$
CREATE PROCEDURE `get_user_field_change_by_date_email`(IN create_date VARCHAR(255), email VARCHAR(255))
  BEGIN
    SELECT *
    FROM user_field_change
    WHERE
      create_dttm LIKE CONCAT('%', create_date, '%') and user_email = email
    ORDER BY user_email;
  END$$


DROP PROCEDURE IF EXISTS `get_user_field_change_by_date_email_system`$$
CREATE PROCEDURE `get_user_field_change_by_date_email_system`(IN create_date VARCHAR(255), email VARCHAR(255),
                                                                 system_name VARCHAR(255))
  BEGIN
    SELECT *
    FROM user_field_change
    WHERE
      create_dttm LIKE CONCAT('%', create_date, '%') and user_email = email and system = system_name
    ORDER BY user_email;
  END$$

DROP PROCEDURE IF EXISTS `get_user_field_change_by_date_system`$$
CREATE PROCEDURE `get_user_field_change_by_date_system`(IN create_date VARCHAR(255), system_name VARCHAR(255))
  BEGIN
    SELECT *
    FROM user_field_change
    WHERE
      create_dttm LIKE CONCAT('%', create_date, '%') and system = system_name
    ORDER BY user_email;
  END$$

DROP PROCEDURE IF EXISTS `add_user_field_change`$$
CREATE PROCEDURE `add_user_field_change`(IN id         CHAR(255), sync CHAR(36), system_name VARCHAR(255),
                                            ad_user_id CHAR(36),
                                            first_n    VARCHAR(255), last_n VARCHAR(255), field VARCHAR(255),
                                            email      VARCHAR(255), old VARCHAR(255), new VARCHAR(255))
  BEGIN
    INSERT INTO `user_field_change` (`user_field_change_id`, `sync_id`, `system`, `field_name`, `active_directory_user_id`,
                                     `first_name`, `last_name`, `user_email`,
                                     `old_value`, `changed_to`, `create_dttm`)
    VALUES
      ( id, sync, system_name, field, ad_user_id, first_n, last_n, email, old, new, CURRENT_TIMESTAMP );
  END$$


DELIMITER ; $$