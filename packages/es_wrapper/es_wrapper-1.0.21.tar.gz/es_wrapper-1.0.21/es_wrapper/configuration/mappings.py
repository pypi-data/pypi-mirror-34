from es_wrapper.general.datatypes import build_nested_mapping_dictionary, merge_dicts, extract_value
from es_wrapper.configuration.parameters import AP_DATA_NEIGHBOR_DOC_TYPE, ES_LOGGER_DOC_TYPE, ES_WLC_AP_DOC_TYPE, \
    ES_WLC_ROGUE_DOC_TYPE, ES_ACTIONS_DOC_TYPE, ES_SUMMARIZED_DOC_TYPE, WLAN_BANDS,\
    ES_EVAL_PERIOD_SUMMARIZED_DOC_TYPE, ES_PROFILE_DOC_TYPE, ES_AP_OBJ_DOC_TYPE, AP_DATA_TOTAL_STA_INFO_DOC_TYPE, \
    AP_DATA_STA_INFO_DOC_TYPE, AP_DATA_PING_INFO_DOC_TYPE, AP_DATA_INFO_DOC_TYPE, AP_DATA_USAGE_DOC_TYPE, \
    AP_DATA_ALTERNATE_INTERFACE_DOC_TYPE, AP_DATA_SITE_SURVEY_DOC_TYPE, AP_DATA_INTERFACE_DOC_TYPE, \
    ES_WLC_CONFIG_DOC_TYPE


class ESMapping:

    BOOLEAN = "boolean"
    STRING = "string"
    INTEGER = "integer"
    LONG = "long"
    DOUBLE = "double"
    GEOPOINT = "geopoint"
    TIME = "time"
    EPOCH = "epoch_millis"
    NESTED = "object"

    def __init__(self):
        self.mapping = {}

        self.function_mapper = {self.BOOLEAN: self.set_boolean_field,
                                self.STRING: self.set_string_field,
                                self.LONG: self.set_long_field,
                                self.INTEGER: self.set_integer_field,
                                self.DOUBLE: self.set_double_field,
                                self.GEOPOINT: self.set_geo_point_field,
                                self.TIME: self.set_time_field,
                                self.EPOCH: self.set_epoch_field,
                                self.NESTED: self.set_nested_field,
                                }

    @staticmethod
    def get_analyzed_string(is_analyzed):
        """
        return the needed string for the analyzed statues
        :param bool is_analyzed: Analyzed status
        return str: String representing and analyzed status ("analyzed"/"not_analyzed")
        """
        if is_analyzed:
            return "analyzed"
        else:
            return "not_analyzed"

    @staticmethod
    def set_string_field(is_analyzed=True):
        """
        sets string mapping values
        :param bool is_analyzed: Analyzed status
        :return dictionary:
        """
        if is_analyzed:
            f_type = "text"
        else:
            f_type = "keyword"
        return {"type": f_type,}

    @staticmethod
    def set_nested_field():
        return {"type": "nested"}

    @staticmethod
    def set_boolean_field():
        """
        set integer mapping values
        :return dictionary:
        """
        return {"type": "boolean"}

    @staticmethod
    def set_integer_field():
        """
        set integer mapping values
        :return dictionary:
        """
        return {"type": "integer"}

    @staticmethod
    def set_long_field():
        """
        sets long mapping values
        :return dictionary:
        """
        return {"type": "long"}

    @staticmethod
    def set_double_field():
        """
        sets double mapping values
        :return dictionary:
        """
        return {"type": "double"}

    @staticmethod
    def set_geo_point_field():
        """
        sets geo_point data type
        :return dictionary:
        """
        # return {"type": "geo_point",
        #         "geohash_prefix": "true",
        #         "lat_lon": "true",
        #         "geohash_precision": 11}
        return {"type": "geo_point"}

    @staticmethod
    def set_time_field():
        """
        sets number mapping values
        :return dictionary:
        """
        return {"type": "date",
                "format": "dateOptionalTime"}

    @staticmethod
    def set_epoch_field():
        """
        sets number mapping values
        :return dictionary:
        """
        return {"type": "date",
                "format": "epoch_millis"}

    def get_field_func(self, field_type):
        """
        Return the parsing function
        :param field_type:
        :return func:
        :raise ValueError: When received a wrong field_type
        """
        field_func = extract_value(self.function_mapper[field_type])
        # When we got an invalid field_type
        if not field_func:
            raise ValueError("Wrong field type received %s" % field_type)

        return field_func

    def add_field(self, doc_type, field_name, field_type, **kwargs):
        """
        This method add a new field to the document mapping
        :param str doc_type: Name of the document
        :param str field_name: Name of the field
        :param str field_type:
        :param kwargs:
        """
        # Get the field function by the field type
        field_func = self.get_field_func(field_type)
        self.mapping[doc_type]["properties"][field_name] = field_func(**kwargs)

    def add_nested_field(self, father_doc, doc_type, field_name, field_type, **kwargs):
        """
        Add a nested key value
        :param father_doc:
        :param doc_type:
        :param field_name:
        :param field_type:
        :param kwargs:
        :return:
        """
        # Get the field function by the field type
        field_func = self.get_field_func(field_type)
        self.mapping[father_doc]["properties"][doc_type]["properties"][field_name] = field_func(**kwargs)

    def create_new_doc(self, *args):
        """
        Build mapping for a new document, to support nested document keys
        :param args: Arguments for new document mapping creation
        :return dict index_dict: A dictionary containing the right structure for a new mapping
        """
        # Create a key list of the arguments
        key_list = [arg for arg in args]
        temp_d = {}
        temp_d = build_nested_mapping_dictionary(temp_d, [key_list])
        # Add the new doc's mapping to the original dictionary
        self.mapping = merge_dicts(self.mapping, temp_d)

    def get_mapping(self):
        """
        Returns the mapping dictionary
        :return dict:
        """
        return self.mapping
