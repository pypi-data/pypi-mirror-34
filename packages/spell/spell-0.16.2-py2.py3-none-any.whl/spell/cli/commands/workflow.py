import click
import os

from spell.api.runs_client import RunsClient
from spell.cli.commands.logs import logs
from spell.cli.commands.run import create_run_request
from spell.cli.exceptions import (
    api_client_exception_handler,
    ExitException,
    SPELL_INVALID_CONFIG,
)
from spell.cli.log import logger
from spell.cli.utils import git_utils
from spell.cli.utils import parse_utils


@click.command(name="workflow",
               short_help="Execute a new workflow")
@click.argument("command")
@click.argument("args", nargs=-1)
@click.option("--local", is_flag=True,
              help="Execute command locally instead of remotely on Spell's infrastructure")
@click.option("-r", "--repo", "repo_paths", multiple=True,
              help="Add a git repository to this workflow by specifying name=path. "
                   "Optionally specify a commit-hash using name=<path>:<commit-hash>")
@click.option("--pip", "pip_packages",
              help="Single dependency to install using pip", multiple=True)
@click.option("--pip-req", "requirements_file",
              help="Requirements file to install using pip")
@click.option("--apt", "apt_packages",
              help="Dependency to install using apt", multiple=True)
@click.option("--from", "docker_image",
              help="Dockerfile on docker hub to run from")
@click.option("--python2", is_flag=True,
              help="set python version to python 2")
@click.option("--python3", is_flag=True,
              help="set python version to python 3 (default)")
@click.option("--conda-env", help="Name of conda environment name to activate. "
                                  "If omitted but --conda-file is specified then it is "
                                  "assumed that --conda-file is an 'explicit' env file.")
@click.option("--conda-file",
              help="Path to conda environment file, defaults to ./environment.yml "
                   "when --conda-env is specified",
              type=click.Path(exists=True, file_okay=True, dir_okay=False, writable=False, readable=True),
              default=None)
@click.option("-b", "--background", is_flag=True,
              help="Do not print logs")
@click.option("-c", "--commit-ref", default="HEAD",
              help="Git commit hash to run")
@click.option("-d", "--description", default=None,
              help="Description of the run. If unspecified defaults to the current commit message")
@click.option("-e", "--env", "envvars", multiple=True,
              help="Add an environment variable to the run")
@click.option("-f", "--force", is_flag=True,
              help="Skip interactive prompts")
@click.option("-v", "--verbose", is_flag=True,
              help="Print additional information")
@click.pass_context
def workflow(ctx, command, args, local, repo_paths,
             pip_packages, requirements_file, apt_packages, docker_image,
             python2, python3, commit_ref, description, envvars, background,
             conda_env, conda_file, force, verbose, **kwargs):
    """
    Execute WORKFLOW either remotely or locally

    The workflow command is used to create workflows which manage other runs.
    For complex problems, there are often many step pipelines of data loading,
    transforming, training, testing, and iterating, and workflows are designed
    to help you automate much of these interactions. While a workflow executes
    much like a normal run, it is capable of launching other runs that are
    all associate with each other. A workflow must specify every git repo that
    will be used by the given workflow script using the `--repo` flag.
    The various other options can be used to customize the environment that the
    workflow script runs in.
    """
    run_req = None
    if not local:
        try:
            repo_paths = parse_utils.parse_repos(repo_paths)
        except parse_utils.ParseException as e:
            raise ExitException(click.wrap_text(
                "Incorrect formatting of repo '{}', it must be "
                "<repo_name>=<repo_path>[:commit_ref]".format(e.token)),
                SPELL_INVALID_CONFIG)
        workspaces = git_utils.sync_repos(ctx, repo_paths, force)

        run_req = create_run_request(
            ctx=ctx,
            command=command,
            args=args,
            machine_type="CPU",
            pip_packages=pip_packages,
            requirements_file=requirements_file,
            apt_packages=apt_packages,
            docker_image=docker_image,
            framework=None,
            python2=python2,
            python3=python3,
            commit_ref=commit_ref,
            description=description,
            envvars=envvars,
            raw_resources=[],
            background=background,
            conda_env=conda_env,
            conda_file=conda_file,
            force=force,
            verbose=verbose,
            local_caching=False,
            idempotent=False,
            run_type="workflow")

    token = ctx.obj["config_handler"].config.token
    username = ctx.obj["config_handler"].config.user_name
    runs_client = RunsClient(owner=username, token=token, **ctx.obj["client_args"])
    logger.info("sending workflow request to api")
    with api_client_exception_handler():
        workflow = runs_client.workflow(run_req, workspaces)

    click.echo("💫 Casting workflow #{}…".format(workflow.id))
    if not local:
        if background:
            click.echo("View logs with `spell logs {}`".format(workflow.run.id))
        else:
            click.echo("✨ Following workflow at run {}.".format(workflow.run.id))
            click.echo("✨ Stop viewing logs with ^C")
            ctx.invoke(logs, run_id=str(workflow.run.id), follow=True, verbose=verbose)
    else:
        os.system(" ".join((command,) + args))
