INSERT INTO `field_read_configuration` (`field_read_configuration_id`, `system_id`, `from_path`, `to_field_name`, `active`, `create_dttm`)
VALUES
  ('52', '1', '$.thumbnailPhoto', 'photo', TRUE, '2017-05-05 12:00:00'),
  ('53', '3', '$.photo', 'photo', TRUE, '2017-05-05 12:00:00');


INSERT INTO `field_write_configuration` (`field_write_configuration_id`, `system_id`, `from_field_name`, `to_path`, `active`, `create_dttm`)
VALUES
  ('48', '1', 'photo', '$.thumbnailPhoto', TRUE, '2017-05-05 12:00:00');

DELIMITER $$
DROP PROCEDURE IF EXISTS `add_active_directory_user`$$
CREATE PROCEDURE `add_active_directory_user`(IN id   CHAR(36), IN f_name VARCHAR(127), IN l_name VARCHAR(127),
                              in login_v VARCHAR(127), in user_email VARCHAR(255), in m_data longtext)
  BEGIN
    INSERT INTO `active_directory_user` (`active_directory_user_id`, `first_name`, `last_name`, `login`, `email`, `metadata`, `create_dttm`)
    VALUES
      ( id, f_name, l_name, login_v, user_email,  m_data, current_timestamp );
  END$$

DELIMITER ; $$
