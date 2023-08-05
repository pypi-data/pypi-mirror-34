from pyravendb.data.indexes import SortOptions
from datetime import datetime, timedelta
from pyravendb.tools.utils import Utils
from inflector import Inflector

inflector = Inflector()


class DocumentConventions(object):
    def __init__(self, **kwargs):
        self.max_number_of_request_per_session = kwargs.get("max_number_of_request_per_session", 30)
        self.max_ids_to_catch = kwargs.get("max_ids_to_catch", 32)
        # timeout for wait to server in seconds
        self.timeout = kwargs.get("timeout", timedelta(seconds=30))
        self.use_optimistic_concurrency = kwargs.get("use_optimistic_concurrency", False)
        self.json_default_method = DocumentConventions.json_default
        self.max_length_of_query_using_get_url = kwargs.get("max_length_of_query_using_get_url", 1024 + 512)
        self.identity_parts_separator = "/";
        self.disable_topology_update = kwargs.get("disable_topology_update", False)
        # If set to 'true' then it will throw an exception when any query is performed (in session)
        # without explicit page size set
        self.raise_if_query_page_size_is_not_set = kwargs.get("raise_if_query_page_size_is_not_set", False)

    @staticmethod
    def json_default(o):
        if o is None:
            return None

        if isinstance(o, datetime):
            return Utils.datetime_to_string(o)
        elif isinstance(o, timedelta):
            return Utils.timedelta_to_str(o)
        elif getattr(o, "__dict__", None):
            return o.__dict__
        elif isinstance(o, int) or isinstance(o, float):
            return str(o)
        else:
            raise TypeError(repr(o) + " is not JSON serializable (Try add a json default method to store convention)")

    @staticmethod
    def default_transform_plural(name):
        return inflector.conditional_plural(2, name)

    @staticmethod
    def default_transform_type_tag_name(name):
        count = sum(1 for c in name if c.isupper())
        if count <= 1:
            return DocumentConventions.default_transform_plural(name.lower())
        return DocumentConventions.default_transform_plural(name)

    @staticmethod
    def build_default_metadata(entity):
        if entity is None:
            return {}
        return {"@collection": DocumentConventions.default_transform_plural(entity.__class__.__name__),
                "Raven-Python-Type": "{0}.{1}".format(entity.__class__.__module__, entity.__class__.__name__)}

    @staticmethod
    def try_get_type_from_metadata(metadata):
        if "Raven-Python-Type" in metadata:
            return metadata["Raven-Python-Type"]
        return None

    @staticmethod
    def uses_range_type(obj):
        if obj is None:
            return False

        if isinstance(obj, int) or isinstance(obj, float):
            return True
        return False

    @staticmethod
    def get_default_sort_option(type_name):
        if not type_name:
            return None
        if type_name == "int" or type_name == "float" or type_name == "long":
            return SortOptions.numeric

    @staticmethod
    def range_field_name(field_name, type_name):
        if type_name == "long":
            field_name = "{0}_L_Range".format(field_name)
        else:
            field_name = "{0}_D_Range".format(field_name)

        return field_name
