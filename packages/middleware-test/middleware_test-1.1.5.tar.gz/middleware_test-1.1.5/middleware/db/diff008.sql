DELIMITER $$

DROP PROCEDURE IF EXISTS `get_all_users`$$
CREATE PROCEDURE `get_all_users`()
  BEGIN
    SELECT * FROM `active_directory_user`;
  END$$

DELIMITER ; $$