from azure.cli.core.commands import \
    (register_cli_argument, CliArgumentType)

from azure.cli.core.commands.parameters import \
    (tags_type, get_resource_name_completion_list, resource_group_name_type, enum_choice_list)

register_cli_argument("example", "my_required_arg")