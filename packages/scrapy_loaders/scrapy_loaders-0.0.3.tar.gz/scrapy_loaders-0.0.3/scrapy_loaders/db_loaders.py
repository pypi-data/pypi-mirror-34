# -*- coding: utf-8 -*-
from sqlalchemy.orm import sessionmaker
from scrapy_loaders.errors import ImproperlyConfigured
from CheKnife.hashing import textmd5sum
from CheKnife.dynamic_import import get_attribute
from scrapy_loaders.db import Db


hash_functions = {
    'md5': textmd5sum
}


class DBLoader(object):
    model = None
    hash_field = 'md5sum'
    hash_fields = []
    update_fields = []
    hash_algorithm = 'md5'

    def __init__(self, item, spider):
        self.spider = spider
        self.item = item
        self.check_conf()
        self.db = Db(spider.settings['DATABASE'], self._get_declarative_base())

        if self.hash_fields:
            self.item[self.hash_field] = self.hash

        self.session = self.open_db_session()
        self.item_model = self.get_db_item()
        self.action, self.success = self.load_item()

    def check_conf(self):
        if self.model is None:
            raise ImproperlyConfigured("{} Must define model attribute".format(self.__class__.__name__))
        self.check_settings()

    def check_settings(self):
        required = ['DATABASE', 'DECLARATIVE_BASE']
        for setting in required:
            if self.spider.settings.get(setting) is None:
                raise ImproperlyConfigured("No {} defined at settings.py".format(setting))

    def _get_declarative_base(self):
        try:
            return get_attribute(self.spider.settings['DECLARATIVE_BASE'])
        except Exception as e:
            raise ImproperlyConfigured('Could not import declarative base: {}'.format(str(e)))

    def add(self):
        if self.item_model:
            self.session.add(self.item_model)
            return 'Created', self.try_commit()
        return 'Created', False

    def update(self):
        if not self.update_fields:
            return 'No fields defined in {}'.format(self.__class__.__name__), None
        for field in self.update_fields:
            setattr(self.item_model, field, self.item[field])
        return 'Updated', self.try_commit()

    def open_db_session(self):
        self.db.connect()
        self.db.create_all_tables()
        Session = sessionmaker(bind=self.db.engine)
        return Session()

    def try_commit(self):
        try:
            self.session.commit()
            success = True
        except Exception as e:
            self.session.rollback()
            self.spider.logger.exception(e)
            success = False
        finally:
            self.session.close()
        return success

    def has_changed(self):
        if self.hash_fields:
            return self.item[self.hash_field] != getattr(self.item_model, self.hash_field)

    def get_db_item(self):
        return self.session.query(self.model).filter(self.model.id == self.item['id']).first()

    def load_item(self):
        if self.item_model is None:
            self.item_model = self.model(**self.item)
            return self.add()
        elif self.has_changed():
            return self.update()
        else:
            return 'Nothing Done', True

    @property
    def exists(self):
        return self.item_model is not None

    @property
    def hash(self):
        seed = ''
        for field in self.hash_fields:
            seed += self.item[field]
        return self._get_hash_function()(seed)

    def _get_hash_function(self):
        try:
            return hash_functions[self.hash_algorithm]
        except KeyError:
            raise ImproperlyConfigured('Hash algorithm not supported. Supported are: {}'.format(
                ','.join(hash_functions.keys())
            ))

    def __str__(self):
        return "{action} {item_id}: {success}".format(
            action=self.action, item_id=self.item['id'], success=self.success)