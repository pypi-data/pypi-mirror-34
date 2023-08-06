DELIMITER $$

DROP PROCEDURE IF EXISTS `delete_logs`$$
CREATE PROCEDURE `delete_logs`(in days int)
  BEGIN
    DELETE FROM `log` WHERE  `create_dttm` < CURRENT_DATE - INTERVAL days DAY;
  END$$

DELIMITER ; $$