DELIMITER $$

DROP PROCEDURE IF EXISTS `add_sync`$$
CREATE PROCEDURE `add_sync`(IN sync CHAR(36) )
  BEGIN
    Insert into `sync` (`sync_id`)
    values (sync);
  END$$

DROP PROCEDURE IF EXISTS `add_system`$$
CREATE PROCEDURE `add_system`(IN id         CHAR(36), IN system_name VARCHAR(64), IN descrip VARCHAR(255),
                              IN enabled tinyint)
  BEGIN
    INSERT INTO `system` (`system_id`, `name`, `description`, `sync_enabled`)
    VALUES
      ( id, system_name, descrip, enabled );
  END$$

DROP PROCEDURE IF EXISTS `add_active_directory_user`$$
CREATE PROCEDURE `add_active_directory_user`(IN id   CHAR(36), IN f_name VARCHAR(127), IN l_name VARCHAR(127),
                              in login_v VARCHAR(127), in user_email VARCHAR(255), in m_data longtext)
  BEGIN
    INSERT INTO `active_directory_user` (`active_directory_user_id`, `first_name`, `last_name`, `login`, `email`, `metadata`)
    VALUES
      ( id, f_name, l_name, login_v, user_email,  m_data);
  END$$

DROP PROCEDURE IF EXISTS `update_active_directory_user`$$
CREATE PROCEDURE `update_active_directory_user`(IN id   CHAR(36), IN f_name VARCHAR(127), IN l_name VARCHAR(127),
                              in login_v VARCHAR(127), in user_email VARCHAR(255), in m_data longtext)
  BEGIN
    Update `active_directory_user` set
     `first_name`=f_name,  `last_name`=l_name,  `login`= login_v,  `email`=user_email,  `metadata`=m_data, `delete_dttm`=NULL
    where `active_directory_user_id` = id;
  END$$

DROP PROCEDURE IF EXISTS `add_actual_user_data`$$
CREATE PROCEDURE `add_actual_user_data`(IN id  CHAR(36), ad_user_id CHAR(36),
                                                IN new_data  longtext)
  BEGIN
    INSERT INTO `actual_user_data` (`actual_user_data_id`, `active_directory_user_id`, `data`)
    VALUES
      ( id, ad_user_id, new_data);
  END$$

DROP PROCEDURE IF EXISTS `update_actual_user_data`$$
CREATE PROCEDURE `update_actual_user_data`(IN id  CHAR(36), ad_user_id CHAR(36),
                                                IN new_data  longtext)
  BEGIN
    Update  `actual_user_data` set `active_directory_user_id`=ad_user_id,  `data` = new_data
    where `actual_user_data_id`=id;
  END$$


DROP PROCEDURE IF EXISTS `add_log`$$
CREATE PROCEDURE `add_log`(sync CHAR(36), component int(2), component_n varchar(36), data1 longtext,
data2 longtext, data3 longtext, data4 longtext, data5 longtext, is_success tinyint(1), message_ varchar(1024),
operation_name varchar(127), system char(36), ad_user_id char(36), exec_time int(11))
  BEGIN
    INSERT INTO  `log` (`sync_id`, `component_id`, `component_name`, `data_1`,
    `data_2`, `data_3`, `data_4`, `data_5`, `success`, `message`, `operation`, `system_id`, `active_directory_user_id`,
    `execution_time`, `create_dttm`)
    VALUES (sync, component, component_n, data1,
data2, data3, data4, data5, is_success, message_ ,
operation_name, system, ad_user_id, exec_time, CURRENT_TIMESTAMP );
  END$$

DELIMITER ; $$