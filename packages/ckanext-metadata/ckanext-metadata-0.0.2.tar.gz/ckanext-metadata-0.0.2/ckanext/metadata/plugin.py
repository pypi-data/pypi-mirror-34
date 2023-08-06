import logging

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


def create_country_codes():
    user = toolkit.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    try:
        data = {'id': 'country_codes'}
        toolkit.get_action('vocabulary_show')(context, data)
        logging.info("Example genre vocabulary already exists, skipping.")
    except toolkit.ObjectNotFound:
        logging.info("Creating vocab 'country_codes'")
        data = {'name': 'country_codes'}
        vocab = toolkit.get_action('vocabulary_create')(context, data)
        for tag in (u'uk', u'ie', u'de', u'fr', u'es'):
            logging.info(
                    "Adding tag {0} to vocab 'country_codes'".format(tag))
            data = {'name': tag, 'vocabulary_id': vocab['id']}
            toolkit.get_action('tag_create')(context, data)


def country_codes():
    '''Return the list of country codes from the country codes vocabulary.'''
    create_country_codes()
    try:
        country_codes = toolkit.get_action('tag_list')(
                data_dict={'vocabulary_id': 'country_codes'})
        return country_codes
    except toolkit.ObjectNotFound:
        return None


class ExampleIDatasetFormPlugin(plugins.SingletonPlugin,
        toolkit.DefaultDatasetForm):
    '''An example IDatasetForm CKAN plugin.

    Uses a tag vocabulary to add a custom metadata field to datasets.

    '''
    plugins.implements(plugins.IConfigurer, inherit=False)
    plugins.implements(plugins.IDatasetForm, inherit=False)
    plugins.implements(plugins.ITemplateHelpers, inherit=False)

    # These record how many times methods that this plugin's methods are
    # called, for testing purposes.
    num_times_new_template_called = 0
    num_times_read_template_called = 0
    num_times_edit_template_called = 0
    num_times_search_template_called = 0
    num_times_history_template_called = 0
    num_times_package_form_called = 0
    num_times_check_data_dict_called = 0
    num_times_setup_template_variables_called = 0

    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        toolkit.add_template_directory(config, 'templates')

    def get_helpers(self):
        return {'country_codes': country_codes}

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []

    def _modify_package_schema(self, schema):
        # Add our custom country_code metadata field to the schema.
        schema.update({
                'country_code': [toolkit.get_validator('ignore_missing'),
                    toolkit.get_converter('convert_to_tags')('country_codes')]
                })
        # Add our custom_test metadata field to the schema, this one will use
        # convert_to_extras instead of convert_to_tags.
        schema.update({
                'frekuensi_penerbitan': [toolkit.get_validator('ignore_missing'),
                    toolkit.get_converter('convert_to_extras')]
                })
        schema.update({
                'level_penyajian': [toolkit.get_validator('ignore_missing'),
                    toolkit.get_converter('convert_to_extras')]
                })
        schema.update({
                'tahun': [toolkit.get_validator('ignore_missing'),
                    toolkit.get_converter('convert_to_extras')]
                })
        schema.update({
                'cakupan': [toolkit.get_validator('ignore_missing'),
                    toolkit.get_converter('convert_to_extras')]
                })
        schema.update({
                'rujukan': [toolkit.get_validator('ignore_missing'),
                    toolkit.get_converter('convert_to_extras')]
                })
        return schema

    def create_package_schema(self):
        schema = super(ExampleIDatasetFormPlugin, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def update_package_schema(self):
        schema = super(ExampleIDatasetFormPlugin, self).update_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def show_package_schema(self):
        schema = super(ExampleIDatasetFormPlugin, self).show_package_schema()

        # Don't show vocab tags mixed in with normal 'free' tags
        # (e.g. on dataset pages, or on the search page)
        schema['tags']['__extras'].append(toolkit.get_converter('free_tags_only'))

        # Add our custom country_code metadata field to the schema.
        schema.update({
            'country_code': [
                toolkit.get_converter('convert_from_tags')('country_codes'),
                toolkit.get_validator('ignore_missing')]
            })

        # Add our frekuensi_penerbitan field to the dataset schema.
        schema.update({
            'frekuensi_penerbitan': [toolkit.get_converter('convert_from_extras'),
                toolkit.get_validator('ignore_missing')]
            })
        # Add our Level Penyajian field to the dataset schema.
        schema.update({
            'level_penyajian': [toolkit.get_converter('convert_from_extras'),
                toolkit.get_validator('ignore_missing')]
            })
        # Add our tahun field to the dataset schema.
        schema.update({
            'tahun': [toolkit.get_converter('convert_from_extras'),
                toolkit.get_validator('ignore_missing')]
            })
        # Add our cakupan field to the dataset schema.
        schema.update({
            'cakupan': [toolkit.get_converter('convert_from_extras'),
                toolkit.get_validator('ignore_missing')]
            })
        schema.update({
            'rujukan': [toolkit.get_converter('convert_from_extras'),
                toolkit.get_validator('ignore_missing')]
            })
        return schema

    # These methods just record how many times they're called, for testing
    # purposes.
    # TODO: It might be better to test that custom templates returned by
    # these methods are actually used, not just that the methods get
    # called.

    def setup_template_variables(self, context, data_dict):
        ExampleIDatasetFormPlugin.num_times_setup_template_variables_called += 1
        return super(ExampleIDatasetFormPlugin, self).setup_template_variables(
                context, data_dict)

    def new_template(self):
        ExampleIDatasetFormPlugin.num_times_new_template_called += 1
        return super(ExampleIDatasetFormPlugin, self).new_template()

    def read_template(self):
        ExampleIDatasetFormPlugin.num_times_read_template_called += 1
        return super(ExampleIDatasetFormPlugin, self).read_template()

    def edit_template(self):
        ExampleIDatasetFormPlugin.num_times_edit_template_called += 1
        return super(ExampleIDatasetFormPlugin, self).edit_template()

    def search_template(self):
        ExampleIDatasetFormPlugin.num_times_search_template_called += 1
        return super(ExampleIDatasetFormPlugin, self).search_template()

    def history_template(self):
        ExampleIDatasetFormPlugin.num_times_history_template_called += 1
        return super(ExampleIDatasetFormPlugin, self).history_template()

    def package_form(self):
        ExampleIDatasetFormPlugin.num_times_package_form_called += 1
        return super(ExampleIDatasetFormPlugin, self).package_form()

    # check_data_dict() is deprecated, this method is only here to test that
    # legacy support for the deprecated method works.
    def check_data_dict(self, data_dict, schema=None):
        ExampleIDatasetFormPlugin.num_times_check_data_dict_called += 1
