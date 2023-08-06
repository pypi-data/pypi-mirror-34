ALTER TABLE sync  MODIFY COLUMN delete_dttm DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;
ALTER TABLE sync  MODIFY COLUMN update_dttm DATETIME DEFAULT NULL;

DELIMITER $$

DROP PROCEDURE IF EXISTS `add_actual_user_data`$$
CREATE PROCEDURE `add_actual_user_data`(IN id  CHAR(36), ad_user_id CHAR(36),
                                                IN new_data  longtext)
  BEGIN
    INSERT INTO `actual_user_data` (`actual_user_data_id`, `active_directory_user_id`, `data`, `create_dttm`)
    VALUES
      ( id, ad_user_id, new_data, CURRENT_TIMESTAMP );
  END$$

DROP PROCEDURE IF EXISTS `add_sync`$$
CREATE PROCEDURE `add_sync`(IN sync CHAR(36) )
  BEGIN
    INSERT INTO `sync` (`sync_id`, `create_dttm`)
    VALUES (sync, current_timestamp );
  END$$

DELIMITER ; $$