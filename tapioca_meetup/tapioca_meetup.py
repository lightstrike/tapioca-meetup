# coding: utf-8

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin)

from .resource_mapping import RESOURCE_MAPPING


class MeetupClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = 'https://api.meetup.com'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(MeetupClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)

        try:
            params['params'].update({'key': api_params.get('key')})
        except KeyError:
            params['params'] = {'key': api_params.get('key')}

        return params

    def get_iterator_list(self, response_data):
        return response_data

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs,
                                         response_data, response):
        pass


Meetup = generate_wrapper_from_adapter(MeetupClientAdapter)
