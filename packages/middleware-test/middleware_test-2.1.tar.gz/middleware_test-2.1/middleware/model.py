# -*- coding: utf-8 -*-

# python imports
import uuid
from datetime import datetime

import config
from tornado.options import options

from mysqlmodel import MysqlModel

config.initialize()


# project imports


class MiddlewareModel(MysqlModel):
    DATABASE_INSTANCE = options.middleware_db_instance
    DATABASE_GENERATION = "2"
    DATABASE_NAME = options.middleware_db_name
    HOSTNAME = options.middleware_db_ip


class Sync(MiddlewareModel):
    TABLE = 'sync'

    @classmethod
    def add_sync(cls):
        sync_uuid = uuid.uuid4().hex
        cls.insert(sync_id=sync_uuid)
        return sync_uuid


class SlackUserGroup(MiddlewareModel):
    TABLE = 'slack_user_group'

    @classmethod
    def add_slack_user_group(cls, group_name, active_directory_user_id):
        slack_user_group_id = cls.insert(slack_group_name=group_name, active_directory_user_id=active_directory_user_id)
        return slack_user_group_id

    @classmethod
    def get_slack_user_group_name(cls, active_directory_user_id):
        result = cls.find(active_directory_user_id=active_directory_user_id)
        return result[0]['slack_group_name'] if result else None

    @classmethod
    def update_slack_user_group(cls, group_name, active_directory_user_id):
        group = cls.find(active_directory_user_id=active_directory_user_id)
        id = group[0]["slack_user_group_id"]
        slack_user_group_id = cls.update(id, slack_group_name=group_name)
        return slack_user_group_id


class System(MiddlewareModel):
    TABLE = 'system'

    @classmethod
    def add_system(cls,  name, description, sync_enabled, system_id=uuid.uuid4().hex):
        cls.insert(system_id=system_id, name=name, description=description, sync_enabled=sync_enabled)
        return system_id

    @classmethod
    def get_system_by_system_id(cls, system_id):
        system = cls.find(system_id=system_id)
        return system[0] if system else None


class ActiveDirectoryUser(MiddlewareModel):
    TABLE = 'active_directory_user'

    @classmethod
    def add_active_directory_user(cls, first_name, last_name, login, email,
                                  metadata):
        active_directory_user_uuid = uuid.uuid4().hex
        cls.insert(active_directory_user_id=active_directory_user_uuid,
                   first_name=first_name, last_name=last_name,
                   login=login, email=email,
                   metadata=metadata)
        return active_directory_user_uuid

    @classmethod
    def update_active_directory_user(cls, active_directory_user_id, first_name, last_name, login, email,
                                     metadata):
        cls.update(active_directory_user_id,
                   first_name=first_name, last_name=last_name,
                   login=login, email=email,
                   metadata=metadata)
        return active_directory_user_id

    @classmethod
    def get_user_by_login(cls, login):
        user = cls.find(login=login)
        return user[0] if user else None

    @classmethod
    def get_user_by_id(cls, active_directory_user_id):
        return cls.get_id(active_directory_user_id)

    @classmethod
    def get_user_by_first_name_last_name(cls, first_name, last_name):
        user = cls.find(first_name=first_name, last_name=last_name)
        return user[0] if user else None

    @classmethod
    def get_all_users(cls):
        return cls.get_all()

    @classmethod
    def delete_active_directory_user(cls, active_directory_user_id):
        cls.delete(active_directory_user_id)

    @classmethod
    def get_manager(cls, manager_full_name):
        combinations = ActiveDirectoryUser.__create_manager_name_combinations__(manager_full_name)
        for first_name, last_name in combinations:
            manager = cls.get_user_by_first_name_last_name(first_name=first_name, last_name=last_name)
            if manager:
                return manager

        return None

    @staticmethod
    def __create_manager_name_combinations__(manager):
        result = []

        parts = manager.split(' ')
        count = len(parts)
        if count == 1:
            raise RuntimeError("Manager name contains only first_name (without last_name)")
        elif count == 2:
            result.append((parts[0], parts[1]))
        else:
            '''
            for example manager name is:  aaa bbb ccc ddd eee
            then possible combinations are:

            aaa --- bbb ccc ddd eee
            aaa bbb --- ccc ddd eee
            aaa bbb ccc --- ddd eee
            aaa bbb ccc ddd --- eee
            '''

            for position in range(count - 1):
                shift = position + 1
                result.append((' '.join(parts[:shift]), ' '.join(parts[shift:])))

        return result


class Log(MiddlewareModel):
    TABLE = 'log'

    @classmethod
    def add_log(cls, system_id=None, sync_id=None, data_1=None, data_2=None, data_3=None, data_4=None, data_5=None,
                success=None, message=None, operation=None, active_directory_user_id=None, execution_time=None,
                component_id=None, component_name=None):
        return cls.insert(sync_id=sync_id, component_id=component_id
                          , component_name=component_name, data_1=data_1
                          , data_2=data_2,
                          data_3=data_3, data_4=data_4, data_5=data_5,
                          success=success, message=message,
                          operation=operation, system_id=system_id,
                          active_directory_user_id=active_directory_user_id, execution_time=execution_time
                          )

    @classmethod
    def delete_logs(cls, days):
        sql = """DELETE FROM `log`
          WHERE `create_dttm` < CURRENT_DATE - INTERVAL {} DAY;""".format(days)
        with cls.transaction() as cursor:
            cursor.execute(sql)

class FieldReadConfiguration(MiddlewareModel):
    TABLE = 'field_read_configuration'

    @classmethod
    def get_configurations_by_system(cls, system_id):
        return cls.find(system_id=system_id)


class ActualUserData(MiddlewareModel):
    TABLE = 'actual_user_data'

    @classmethod
    def add_actual_user_data(cls, active_directory_user_id, data):
        actual_user_data_uuid = uuid.uuid4().hex
        cls.insert(actual_user_data_id=actual_user_data_uuid,
                   active_directory_user_id=active_directory_user_id, data=data)
        return actual_user_data_uuid

    @classmethod
    def update_actual_user_data(cls, actual_user_data_id, active_directory_user_id, data):
        cls.update(actual_user_data_id, active_directory_user_id=active_directory_user_id,
                   data=data)
        return actual_user_data_id

    @classmethod
    def get_actual_user_by_ad_user_id(cls, active_directory_user_id):
        result = cls.find(active_directory_user_id=active_directory_user_id)
        return result[0] if result else None


class FieldWriteConfiguration(MiddlewareModel):
    TABLE = 'field_write_configuration'

    @classmethod
    def get_configurations_by_system(cls, system_id):
        return cls.find(system_id=system_id, is_active=1)


class WriteForbiddenField(MiddlewareModel):
    TABLE = 'write_forbidden_field'

    @classmethod
    def get_forbidden_fields_by_system(cls, system_id):
        return cls.find(system_id=system_id, is_active=1)


class WriteRequiredField(MiddlewareModel):
    TABLE = 'write_required_field'

    @classmethod
    def get_required_fields_by_system(cls, system_id):
        return cls.find(system_id=system_id, is_active=1)


class WriteEmptyFieldByUser(MiddlewareModel):
    TABLE = 'write_empty_field_by_user'

    @classmethod
    def get_write_empty_field_by_user_by_system(cls, system_id, user_email):
        return cls.find(system_id=system_id, user_email=user_email)


class UserFieldChange(MiddlewareModel):
    TABLE = 'user_field_change'

    @classmethod
    def add_user_field_change(cls, sync_id, system, field_name, active_directory_user_id, first_name, last_name,
                              user_email, old_value, changed_to):
        user_field_change_id = uuid.uuid4().hex
        cls.insert(user_field_change_id=user_field_change_id,
                   sync_id=sync_id, system=system, field_name=field_name,
                   active_directory_user_id=active_directory_user_id, first_name=first_name,
                   last_name=last_name,
                   user_email=user_email, old_value=old_value, changed_to=changed_to)
        return user_field_change_id

    @classmethod
    def get_user_field_change_by_date(cls, date):
        sql = """SELECT *
            FROM user_field_change
            WHERE
              create_dttm LIKE CONCAT('%', {}, '%')
            ORDER BY user_email;
        """.format(date)
        return cls.process_query(sql)

    @classmethod
    def get_user_field_change_by_date_email(cls, date, email):
        sql = """SELECT *
            FROM user_field_change
            WHERE
              create_dttm LIKE CONCAT('%', {}, '%') and user_email = {}
            ORDER BY user_email;
                """.format(date, email)
        return cls.process_query(sql)

    @classmethod
    def get_user_field_change_by_date_email_system(cls, date, email, system):
        sql = """SELECT *
        FROM user_field_change
        WHERE
          create_dttm LIKE CONCAT('%', {}, '%') and user_email = {} and system = {}
        ORDER BY user_email;
                        """.format(date, email, system)
        return cls.process_query(sql)

    @classmethod
    def get_user_field_change_by_date_system(cls, date, system):
        sql = """SELECT *
                FROM user_field_change
                WHERE
                  create_dttm LIKE CONCAT('%', {}, '%') and system = {}
                ORDER BY user_email;
                                """.format(date, system)
        return cls.process_query(sql)
