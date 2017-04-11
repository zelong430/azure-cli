from azure.cli.core.commands import cli_command
from azure.cli.command_modules.resource.custom import deploy_arm_template,create_resource_group

example_custom_format_path = 'azure.cli.command_modules.example.commands#{}'

def example(name, u, p, my_optional_arg='MyDefault'):
    '''Returns the params you passed in.
    :param str my_required_arg: The argument that is required
    '''
    params = '{"vmssName":{"value":"contosoDemo"},"adminUsername":{"value":"deployr_user"},"adminPassword":{"value":"allA2years!"}}'
    create_resource_group(name, "eastus")
    return deploy_arm_template(resource_group_name=name, template_file="C:/Users/zeq.REDMOND/Downloads/vm-scale-set-no-https-template.json", deployment_name=name, parameters=[params])


cli_command(__name__, 'mrs deploy', example_custom_format_path.format('example'))


