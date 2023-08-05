#!/usr/bin/env python
import logging
import os

import click
import yaml

import yadage.steering_api as steering_api
import yadage.utils as utils
import yadageschemas
from packtivity.plugins import enable_plugins

log = logging.getLogger(__name__)

RC_FAILED = 1
RC_SUCCEEDED = 0


def from_file(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    data = {}
    verbosity = 'INFO'
    logging.basicConfig(level=getattr(logging, verbosity), format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    click.secho('running from file')
    for v in value:
        data.update(**yaml.load(v))
    data['backend']  = utils.setupbackend_fromstring(data.pop('backend'),data.pop('backendopts'))

    enable_plugins(data.pop('plugins'))

    rc = RC_FAILED
    try:
        steering_api.run_workflow(**data)
        rc = RC_SUCCEEDED
    except:
        log.exception('workflow failed')
    if rc != RC_SUCCEEDED:
        exc = click.exceptions.ClickException(
            click.style("Workflow failed", fg='red')
        )
        exc.exit_code = rc
        raise exc

    ctx.exit()

@click.command()
@click.argument('dataarg', default = 'work')
@click.argument('workflow', default = 'workflow.yml')
@click.argument('initfiles', nargs=-1)
@click.option('-b', '--backend', default='multiproc:auto', help = 'packtivity backend string')
@click.option('-c', '--cache', default='')
@click.option('-d', '--dataopt', multiple=True, default=None, help = 'options for the workflow data state')
@click.option('-e', '--schemadir', default=yadageschemas.schemadir, help = 'schema directory for workflow validation')
@click.option('-f', '--from-file', expose_value=False, multiple=True, type=click.File('rb'), help = 'read entire configuration from file, no other flags settings are read.', callback=from_file, is_eager = True)
@click.option('-g', '--strategy', help = 'set execution stragegy')
@click.option('-i', '--loginterval', default=30, help = 'adage tracking interval in seconds')
@click.option('-k', '--backendopt', multiple=True, default=None, help = 'options for the workflow data state')
@click.option('-l', '--modelopt', multiple=True, default=None, help = 'options for the workflow state models')
@click.option('-m', '--metadir', default=None, help = 'directory to store workflow metadata')
@click.option('-o', '--ctrlopt', multiple=True, default=None, help = 'options for the workflow controller')
@click.option('-p', '--parameter', multiple=True, help = '<parameter name>=<yaml string> input parameter specifcations ')
@click.option('-r', '--controller', default = 'frommodel', help = 'controller')
@click.option('-s', '--modelsetup', default='inmem', help = 'wflow state model')
@click.option('-t', '--toplevel', default=os.getcwd(), help = 'toplevel uri to be used to resolve workflow name and references from')
@click.option('-u', '--updateinterval', default=0.02, help = 'adage graph inspection interval in seconds')
@click.option('-v', '--verbosity', default='INFO', help = 'logging verbosity')
@click.option('--accept-metadir/--no-accept-metadir', default=False)
@click.option('--plugins', default=None)
@click.option('--validate/--no-validate', default=True, help = 'en-/disable workflow spec validation')
@click.option('--visualize/--no-visualize', default=False, help = 'visualize workflow graph')
def main(dataarg,
         workflow,
         initfiles,
         controller,
         ctrlopt,
         toplevel,
         verbosity,
         loginterval,
         updateinterval,
         schemadir,
         backend,
         dataopt,
         backendopt,
         strategy,
         modelsetup,
         modelopt,
         metadir,
         parameter,
         validate,
         visualize,
         cache,
         plugins,
         accept_metadir
         ):


    logging.basicConfig(level=getattr(logging, verbosity), format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    from packtivity.plugins import enable_plugins
    if plugins:
        enable_plugins(plugins.split(','))

    initdata    = utils.getinit_data(initfiles, parameter)
    dataopts    = utils.options_from_eqdelimstring(dataopt)
    backendopts = utils.options_from_eqdelimstring(backendopt)
    modelopts   = utils.options_from_eqdelimstring(modelopt)
    ctrlopts    = utils.options_from_eqdelimstring(ctrlopt)

    backend  = utils.setupbackend_fromstring(backend,backendopts)
    rc = RC_FAILED
    try:
        steering_api.run_workflow(
            workflow = workflow,
            toplevel = toplevel,
            validate = validate,
            schemadir = schemadir,

            initdata = initdata,
            controller = controller,
            ctrlopts = ctrlopts,
            backend = backend,
            cache = cache,

            dataarg = dataarg,
            dataopts = dataopts,
            metadir = metadir,
            accept_metadir = accept_metadir,
            modelsetup = modelsetup,
            modelopts = modelopts,
            updateinterval = updateinterval,
            loginterval = loginterval,
            visualize = visualize,
            strategy = strategy,
        )
        rc = RC_SUCCEEDED
    except:
        log.exception('workflow failed')
    if rc != RC_SUCCEEDED:
        exc = click.exceptions.ClickException(
            click.style("Workflow failed", fg='red')
        )
        exc.exit_code = rc
        raise exc

if __name__ == '__main__':
    main()
