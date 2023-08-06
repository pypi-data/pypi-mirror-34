DELIMITER $$

DROP PROCEDURE IF EXISTS `get_full_logs`$$
CREATE PROCEDURE `get_full_logs`(IN create_date VARCHAR(255))
  BEGIN
    SELECT * FROM log WHERE create_dttm LIKE CONCAT('%', create_date, '%');
  END$$

DELIMITER ; $$
