from scrapy_loaders.errors import DbLoaderNotFound, ImproperlyConfigured


class DbPipeline(object):
    db_loaders = {}

    def __init__(self):
        if not self.db_loaders:
            raise ImproperlyConfigured('No {}.db_loaders dictionary defined.'.format(self.__class__.__name__))

    def process_item(self, item, spider):
        loader_class = self._get_loader_class(item.__class__.__name__)
        loader = loader_class(item, spider)
        return str(loader)

    def _get_loader_class(self, item_type):
        try:
            return self.db_loaders[item_type]
        except KeyError:
            raise DbLoaderNotFound(
                'Loader Not Found for {}. '
                'Make sure you created a subclass and added it to {}.db_loaders dictionary pipeline'.format(
                    item_type,
                    self.__class__.__name__))
