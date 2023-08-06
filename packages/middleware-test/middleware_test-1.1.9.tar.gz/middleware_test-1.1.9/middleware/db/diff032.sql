ALTER TABLE user_field_change  ADD COLUMN sync_id CHAR(36) DEFAULT NULL;
ALTER TABLE user_field_change  MODIFY COLUMN old_value VARCHAR(255);