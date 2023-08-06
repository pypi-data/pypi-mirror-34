# -*- coding: utf8 -*-
import click
from mali_commands.commons import add_to_data_if_not_none, create_validate_length, output_result
from mali_commands.options import project_id_option, alert_type_option


@click.group('projects')
def projects_commands():
    pass


@projects_commands.command('list')
@click.pass_context
def list_projects(ctx):
    projects = ctx.obj.handle_api(ctx.obj, ctx.obj.session, 'get', 'projects')

    output_result(ctx, projects.get('projects', []), ['project_id', 'display_name', 'description', 'token', 'org'])


max_project_display_name = 140
min_project_display_name = 1

max_project_description = 140
min_project_description = 0


@projects_commands.group('alerts')
def alerts_commands():
    pass


@alerts_commands.command('subscribe')
@project_id_option(required=True)
@alert_type_option(required=True, multiple=True)
@click.pass_context
def subscribe_alert(ctx, projectid, alerttype):
    data = {
        'alert_types': alerttype,
        'project_ids': projectid,
    }

    result = ctx.obj.handle_api(ctx.obj, ctx.obj.session, 'post', 'projects/subscribe', data)

    output_result(ctx, result, ['ok'])


@alerts_commands.command('unsubscribe')
@project_id_option(required=True, multiple=True)
@alert_type_option(required=True, multiple=True)
@click.pass_context
def unsubscribe_alert(ctx, projectid, alerttype):
    data = {
        'alert_types': alerttype,
        'project_ids': projectid,
    }

    result = ctx.obj.handle_api(ctx.obj, ctx.obj.session, 'post', 'projects/unsubscribe', data)

    output_result(ctx, result, ['ok'])


@alerts_commands.command('list')
@click.pass_context
def list_alert(ctx):
    alerts = ctx.obj.handle_api(ctx.obj, ctx.obj.session, 'get', 'projects/subscriptions')

    output_result(ctx, alerts.get('alerts', []), ['project_id', 'display_name', 'org', 'alert_type', 'subscribed'])


@projects_commands.command('create')
@click.option(
    '--displayName', required=True, callback=create_validate_length(min_project_display_name, max_project_display_name))
@click.option(
    '--description', required=False, callback=create_validate_length(min_project_description, max_project_description))
@click.option('--org', required=False)
# deprecated option but some clients use it
@click.pass_context
def create_project(ctx, displayname, description, org):
    data = {}

    add_to_data_if_not_none(data, displayname, "display_name")
    add_to_data_if_not_none(data, org, "org")
    add_to_data_if_not_none(data, description, "description")

    result = ctx.obj.handle_api(ctx.obj, ctx.obj.session, 'post', 'projects', data)

    output_result(ctx, result, ['id', 'token'])


@projects_commands.command('transfer')
@project_id_option(required=True)
@click.option('--transferTo', required=False)
@click.pass_context
def transfer_project(ctx, projectid, transferto):
    data = {}

    add_to_data_if_not_none(data, transferto, "transfer_to")

    result = ctx.obj.handle_api(
        ctx.obj, ctx.obj.session, 'post', 'projects/{project_id}/transfer'.format(project_id=projectid), data)

    output_result(ctx, result, ['ok'])
