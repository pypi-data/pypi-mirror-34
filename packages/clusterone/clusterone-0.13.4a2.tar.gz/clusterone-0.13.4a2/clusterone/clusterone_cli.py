#!/usr/bin/env python3

import os
import sys
import logging

import click
import click_log

from clusterone import authenticate

from clusterone.persistance.session import Session
from clusterone import __version__
from clusterone.utils import render_table, info

# TODO: Handle KeyBoardInterrup at high level here

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOME_DIR = os.getcwd()
logger = logging.getLogger(__name__)

# Bunch of global messages
session = Session()
session.__init__()
session.load()
if session.get('username') is None:
    owner_help_message = 'Specify owner by usernames'
else:
    owner_help_message = 'Specify owner by username, default: %s' % session.get(
        'username')

pass_config = click.make_pass_decorator(Session, ensure=True)


class Context(object):
    def __init__(self, client, session, cwd):
        self.client = client
        self.session = session
        self.cwd = cwd


from clusterone import ClusteroneException
from clusterone.utilities import log_error


from clusterone import client

@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=__version__)
@click.pass_context
def cli(context):
    """
    Welcome to the Clusterone Command Line Interface.
    """

    config = Session()
    config.load()
    context.obj = Context(client, config, HOME_DIR)


def main():
    try:
        cli()
    except ClusteroneException as exception:
        log_error(exception)
        sys.exit(exception.exit_code)
    # TODO: THIS
    #except Exception as exception:
    # here Sentry logger is a good idea
    #    pass

# ---------------------------------------

@cli.group()
@click_log.simple_verbosity_option()
@click_log.init(__name__)
@click.pass_obj
def get(context):
    """
    < project(s) | dataset(s) | job(s) | events >
    """
    pass


@cli.group()
@click_log.simple_verbosity_option()
@click_log.init(__name__)
@click.pass_obj
def create(context):
    """
    < project | dataset | job >
    """
    pass


@cli.group()
@click.pass_obj
def rm(context):
    """
    < project | dataset | job >
    """
    pass


@create.group()
@click.pass_obj
def job(context):
    """
    < single | distributed >
    """

    pass


@cli.group()
@click.pass_context
def init(context):
    """
    < project | dataset >
    """
    pass


@cli.group()
@click.pass_context
def ln(config):
    """
    < project | dataset >
    """
    pass


@cli.group()
@click.pass_context
def start(config):
    """
    < job | notebook >
    """
    pass


@cli.group()
@click.pass_context
def stop(config):
    """
    < job | notebook >
    """
    pass


@cli.group()
@click.pass_context
def run(config):
    pass


# TODO: Redo the above to be dynamic -> eg. job command goes through it's modules and lists single | distributed dynamically

# ------------------------

# TODO: Redo this to dynamic import
from clusterone import commands

get.add_command(commands.get.job.command, 'job')
get.add_command(commands.get.jobs.command, 'jobs')
get.add_command(commands.get.notebooks.command, 'notebooks')
get.add_command(commands.get.events.command, 'events')

create.add_command(commands.create.project.command, 'project')
create.add_command(commands.create.notebook.command, 'notebook')

job.add_command(commands.create.job.single.command, 'single')
job.add_command(commands.create.job.distributed.command, 'distributed')

rm.add_command(commands.rm.job.command, 'job')
rm.add_command(commands.rm.project.command, 'project')
rm.add_command(commands.rm.dataset.command, 'dataset')

get.add_command(commands.get.project.command, 'project')
get.add_command(commands.get.dataset.command, 'dataset')

init.add_command(commands.init.project.command, 'project')

ln.add_command(commands.ln.project.command, 'project')
ln.add_command(commands.ln.dataset.command, 'dataset')

start.add_command(commands.start.job.command, 'job')
start.add_command(commands.start.notebook.command, 'notebook')

create.add_command(commands.create.dataset.command, 'dataset')

stop.add_command(commands.stop.job.command, 'job')
stop.add_command(commands.stop.notebook.command, 'notebook')

cli.add_command(commands.login.command, 'login')
cli.add_command(commands.logout.command, 'logout')

cli.add_command(commands.matrix.command, 'matrix')
cli.add_command(commands.config.command, 'config')

run.add_command(commands.run.local.command, 'local')

# ------------------------


@click.command()
@authenticate()
@click.pass_obj
@click.option('--owner')
def get_projects(context, owner=None):
    """
    List projects
    """

    config = context.session

    # TODO: fix owner

    projects = client.get_projects()

    if projects:
        click.echo(info("All projects:"))
        data = []
        data.append(
            ['#', 'Project', 'Created at', 'Description'])

        i = 0
        for project in projects:
            try:
                data.append([
                    i,
                    "%s/%s" % (project.get('owner')
                               ['username'], project.get('name')),
                    project.get('created_at')[:19],
                    project.get('description')
                ])
                i += 1
            except:
                pass
        table = render_table(data, 36)
        click.echo(table.table)
        return projects
    else:
        click.echo(info(
            "No projects found. Use 'just create project' to start a new one."))
        return None


get.add_command(get_projects, 'projects')


@click.command()
@click.option('--owner')
@click_log.simple_verbosity_option()
@click_log.init(__name__)
@click.pass_obj
@authenticate()
def get_datasets(context, owner=None):
    """
    List datasets
    """
    client, config = context.client, context.session

    datasets = client.get_datasets(owner)

    if datasets:
        click.echo(info("All datasets:"))
        data = []
        data.append(
            ['#', 'Dataset', 'Modified at', 'Description'])

        i = 0
        for project in datasets:
            try:
                data.append([
                    i,
                    "%s/%s" % (project.get('owner')
                               ['username'], project.get('name')),
                    project.get('modified_at')[:19],
                    project.get('description')
                ])
                i += 1
            except:
                pass
        table = render_table(data, 36)
        click.echo(table.table)
        return datasets
    else:
        click.echo("It doesn't look like you have any datasets yet. You can create a new one with 'just create dataset'.")
        return None


get.add_command(get_datasets, 'datasets')

#@cli.command()
#@click.argument('path', type=click.Path(exists=True, file_okay=False, resolve_path=True))
#@click.option('--job-id')
#@click_log.simple_verbosity_option()
#@click_log.init(__name__)
#@click.pass_obj
#@authenticate()
#def download_files(context, path, job_id=None):
#    """
#    downloads all outputs and saves at specified path
#    """
#    config, client = context.session, context.client
#    try:
#        # We get list of user jobs and allow user to select them
#        if not job_id:
#            jobs = client.get_jobs()
#            if jobs:
#                job_id, job_name = select_job(jobs, 'Select the job you want to download files from')
#            else:
#                click.echo(
#                    info(
#                        "You do not seem to have any jobs. Use 'tport run' to run a job."
#                    ))
#                return
#        else:
#            job = client.get_job(params={'job_id': job_id})
#            if job:
#                job_id = job.get('job_id')
#                job_name = job.get('display_name')
#            else:
#                click.echo(info("%s is not a valid job id." % job_id))
#                return
#        # Download file list
#        job_file_list = client.get_file_list(job_id)
#        counter = 0
#        for file in job_file_list:
#            counter += 1
#            # Display the files
#            click.echo(
#                option('%s | %s | %s kb' % (counter, file['name'], file['size'] / 1024)))
#            try:
#                if file['size'] > 0:
#                    # Save file in specified path
#                    file_content = client.download_file(job_id, file['name'])
#                    file_path = os.path.join(path, file['name'])
#                    f = open(file_path, "w")
#                    f.write(file_content)
#                    f.close()
#
#            except Exception as e:
#                click.echo("Failed to download files: %s" % str(e))
#                logger.error("Failed to download file: %s" % str(e), exc_info=True)
#                continue
#
#    except Exception as e:
#        logger.error("Failed to download files", exc_info=True)
#        return


if __name__ == '__main__':
    main()
