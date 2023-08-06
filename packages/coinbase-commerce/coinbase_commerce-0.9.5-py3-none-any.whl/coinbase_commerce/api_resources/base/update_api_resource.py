from coinbase_commerce import util
from coinbase_commerce.api_resources.base import APIResource


class UpdateAPIResource(APIResource):

    @classmethod
    def modify(cls, entity_id, **params):
        response = cls._api_client.put(cls.RESOURCE_PATH, entity_id, params=params)
        return util.convert_to_api_object(response, cls._api_client, cls)

    def save(self):
        entity_id = self.pop('id', None)
        if not entity_id:
            raise ValueError("Can't update {} without id. "
                             "Create or retrieve it first".format(self.__class__.__name__))
        response = self._api_client.put(self.RESOURCE_PATH, entity_id, params=self.copy())
        data = util.convert_to_api_object(response, self._api_client, self.__class__)
        self.refresh_from(**data)
        return self
