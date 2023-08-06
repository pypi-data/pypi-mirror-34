CREATE TABLE IF NOT EXISTS `slack_user_group` (
  `slack_user_group_id`       MEDIUMINT         AUTO_INCREMENT,
  `slack_group_name`          VARCHAR(255)      NOT NULL,
  `active_directory_user_id`  CHAR(36) NOT NULL UNIQUE,
  `create_dttm` DATETIME      DEFAULT NULL,
  `update_dttm` DATETIME      DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `delete_dttm` DATETIME      DEFAULT NULL,
  PRIMARY KEY (`slack_user_group_id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

DELIMITER $$

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
    UPDATE `slack_user_group` SET `slack_group_name`=group_name
    WHERE `active_directory_user_id`=ad_user_id;

  END$$

DROP PROCEDURE IF EXISTS `get_slack_user_group_name`$$
CREATE PROCEDURE `get_slack_user_group_name`(ad_user_id CHAR(36))
  BEGIN
    SELECT `slack_group_name` FROM `slack_user_group` WHERE `active_directory_user_id`=ad_user_id;
  END$$

DELIMITER ; $$