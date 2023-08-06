DELIMITER $$

DROP PROCEDURE IF EXISTS `add_user_field_change`$$
CREATE PROCEDURE `add_user_field_change`(IN id      CHAR(255), sync CHAR(36), system_name VARCHAR(255), ad_user_id CHAR(36),
                                            first_n VARCHAR(255), last_n VARCHAR(255), field VARCHAR(255),
                                            email   VARCHAR(255), old VARCHAR(255), new VARCHAR(255))
  BEGIN
    INSERT INTO `user_field_change` (`user_field_change_id`, `sync_id`, `system`, `field_name`, `active_directory_user_id`,
                                     `first_name`, `last_name`, `user_email`,
                                     `old_value`, `changed_to`, `create_dttm`)
    VALUES
      ( id, sync, system_name, field, ad_user_id, first_n, last_n, email, old, new, CURRENT_TIMESTAMP );
  END$$

DELIMITER ; $$