DELIMITER $$

DROP PROCEDURE IF EXISTS `delete_active_directory_user`$$
CREATE PROCEDURE `delete_active_directory_user`(in id char(36))
  BEGIN
    Update `active_directory_user` set `delete_dttm`=CURRENT_TIMESTAMP
    where `active_directory_user`=id;
  END$$

DROP PROCEDURE IF EXISTS `get_all_users`$$
CREATE PROCEDURE `get_all_users`()
  BEGIN
    SELECT * FROM `active_directory_user` where `delete_dttm` is NULL;
  END$$

DELIMITER ; $$