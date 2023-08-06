DELETE FROM `write_required_field` WHERE `system_id`='3' AND `field_name`='person_number';
DELETE FROM `field_write_configuration` WHERE `to_path`='$.employeeID';