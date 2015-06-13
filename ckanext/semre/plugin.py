import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.lib.helpers as helpers

# Use this function in custom template to get dataset relationships
# It will enable us to represent them semantically
def semre_create(datasetName):
 
    # To get dataset relationships we call CKAN core function 'package_relationship_list'
    # to whom we forward the name of the dataset
    datasetRelationships = toolkit.get_action('package_relationships_list')(
        data_dict={'id': datasetName})
    
    # return results as dictionary
    return datasetRelationships


# Class which implements interface ITemplateHelpers to make our extension function available
# in CKAN template and interface IConfigurer to tell CKAN that our extension provides
# new custom template for RDF description of dataset
class SemRePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.ITemplateHelpers)

    plugins.implements(plugins.IConfigurer)


    def update_config(self, config):

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        toolkit.add_template_directory(config, 'templates_legacy')

    def get_helpers(self):
        return {'semre_create': semre_create}


