DELIMITER $$

DROP PROCEDURE IF EXISTS `delete_active_directory_user`$$
CREATE PROCEDURE `delete_active_directory_user`(in id char(36))
  BEGIN
    Update `active_directory_user` set `delete_dttm`=CURRENT_TIMESTAMP
    where `active_directory_user_id`=id;
  END$$

DELIMITER ; $$