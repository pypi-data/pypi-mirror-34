# -*- coding: utf8 -*-
import click
from .commons import add_to_data_if_not_none, output_result


@click.group('orgs')
def orgs_commands():
    pass


@orgs_commands.command('list')
@click.pass_context
def list_orgs(ctx):
    result = ctx.obj.handle_api(ctx.obj, ctx.obj.session, 'get', 'orgs')

    output_result(ctx, result.get('orgs', []), ['org', 'display_name'])


@orgs_commands.command('create')
@click.option('--org', required=True)
@click.option('--displayName', required=False)
@click.option('--description', required=False)
@click.pass_context
def create_org(ctx, org, displayname, description):
    data = {}

    add_to_data_if_not_none(data, displayname, 'display_name')
    add_to_data_if_not_none(data, description, 'description')
    add_to_data_if_not_none(data, org, 'org')

    result = ctx.obj.handle_api(ctx.obj, ctx.obj.session, 'post', 'orgs', data)

    output_result(ctx, result, ['ok'])


@orgs_commands.command('autoJoinDomain')
@click.option('--org', required=True)
@click.option('--domain', required=True, multiple=True)
@click.pass_context
def auto_join_domain(ctx, org, domain):
    data = {}

    add_to_data_if_not_none(data, list(domain), 'domains')

    result = ctx.obj.handle_api(ctx.obj, ctx.obj.session, 'post', 'orgs/{org}/autoJoin'.format(org=org), data)

    output_result(ctx, result, ['ok'])
