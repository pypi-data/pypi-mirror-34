from collections import OrderedDict

from click.testing import CliRunner

from clusterone.clusterone_cli import cli
from clusterone import ClusteroneClient
from clusterone.mocks import GET_FRAMEWORKS_RESPONSE, GET_INSTANCE_TYPES_RESPONSE
from clusterone.commands.create.job import distributed


# client call is not explicitly tested as other tests depend on that call
# base_options call is not explicitly tested as other tests depend on that call

def test_passing(mocker):
    # This mocks will propagate across the tests
    mocker.patch.object(ClusteroneClient, '__init__', autospec=True, return_value=None)
    ClusteroneClient.create_job = mocker.Mock()

    ClusteroneClient.get_frameworks = mocker.Mock(return_value=GET_FRAMEWORKS_RESPONSE)
    ClusteroneClient.get_instance_types = mocker.Mock(return_value=GET_INSTANCE_TYPES_RESPONSE)

    distributed.base = mocker.Mock(return_value={'meta': {'name': 'late-moon-758', 'description': ''}, 'parameters': {'package_path': '', 'requirements': 'requirements.txt', 'time_limit': 2880, 'module': 'main', 'framework': {'slug': 'tensorflow-1.3.0'}, 'git_commit_hash': '4a82d16c7995856c7973af38f2f5ba4eac0cd2d1', 'code': 'aaf4de71-f506-48c0-855c-02c7c485c5a4', 'package_manager': 'pip', 'clusterone_api_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im9sZ2llcmRAa2FzcHJvd2ljei5wcm8iLCJ1c2VyX2lkIjo3OTUsImV4cCI6MTUxNzMxNjUzMCwidXNlcm5hbWUiOiJhbGxncmVlZCJ9.IJhEZWwMYf2sjHhoxUsjCj0Xll5CVX-RO3eUqvH7myU', 'python_version': 2.7}})

    CliRunner().invoke(cli, [
        'create',
        'job',
        'distributed',
        '--project', 'someproject',
        '--worker-replicas', '3',
        '--ps-replicas', '2',
        '--worker-type', 't2.small',
        '--ps-type', 't2.small',
        '--gpu-count', '4',
    ])

    args, kwargs = ClusteroneClient.create_job.call_args
    assert kwargs['parameters']['workers']['replicas'] == 3
    assert kwargs['parameters']['parameter_servers']['replicas'] == 2
    assert kwargs['parameters']['workers']['slug'] == 't2.small'
    assert kwargs['parameters']['parameter_servers']['slug'] == 't2.small'
    assert kwargs['parameters']['workers']['gpu_count'] == 4


def test_default(mocker):
    distributed.client = mocker.Mock()
    mocker.patch.object(ClusteroneClient, '__init__', autospec=True, return_value=None)
    ClusteroneClient.create_job = mocker.Mock()
    distributed.base = mocker.Mock(return_value={'meta': {'name': 'late-moon-758', 'description': ''}, 'parameters': {'package_path': '', 'requirements': 'requirements.txt', 'time_limit': 2880, 'module': 'main', 'framework': {'slug': 'tensorflow-1.3.0'}, 'git_commit_hash': '4a82d16c7995856c7973af38f2f5ba4eac0cd2d1', 'code': 'aaf4de71-f506-48c0-855c-02c7c485c5a4', 'package_manager': 'pip', 'Clusterone_api_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im9sZ2llcmRAa2FzcHJvd2ljei5wcm8iLCJ1c2VyX2lkIjo3OTUsImV4cCI6MTUxNzMxNjUzMCwidXNlcm5hbWUiOiJhbGxncmVlZCJ9.IJhEZWwMYf2sjHhoxUsjCj0Xll5CVX-RO3eUqvH7myU', 'python_version': 2.7}})

    CliRunner().invoke(cli, [
        'create',
        'job',
        'distributed',
        '--project', 'someproject',
    ])

    args, kwargs = ClusteroneClient.create_job.call_args
    assert kwargs['parameters']['workers']['replicas'] == 2
    assert kwargs['parameters']['parameter_servers']['replicas'] == 1
    assert kwargs['parameters']['workers']['slug'] == 't2.small'
    assert kwargs['parameters']['parameter_servers']['slug'] == 't2.small'
    assert 'gpu_count' not in kwargs['parameters']['workers']


def test_call_to_base(mocker):
    distributed.client = mocker.Mock()
    mocker.patch.object(ClusteroneClient, '__init__', autospec=True, return_value=None)
    distributed.base = mocker.Mock()
    CliRunner().invoke(cli, [
        'create',
        'job',
        'distributed',
        '--project', 'someproject',
    ])

    assert distributed.base.call_count == 1


def test_is_distributed(mocker):
    distributed.client = mocker.Mock()
    distributed.base = mocker.Mock(return_value={'meta': {'name': 'late-moon-758', 'description': ''}, 'parameters': {'package_path': '', 'requirements': 'requirements.txt', 'time_limit': 2880, 'module': 'main', 'tf_version': '', 'framework': {'slug': 'tensorflow-1.3.0'}, 'git_commit_hash': '4a82d16c7995856c7973af38f2f5ba4eac0cd2d1', 'code': 'aaf4de71-f506-48c0-855c-02c7c485c5a4', 'package_manager': 'pip', 'Clusterone_api_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im9sZ2llcmRAa2FzcHJvd2ljei5wcm8iLCJ1c2VyX2lkIjo3OTUsImV4cCI6MTUxNzMxNjUzMCwidXNlcm5hbWUiOiJhbGxncmVlZCJ9.IJhEZWwMYf2sjHhoxUsjCj0Xll5CVX-RO3eUqvH7myU', 'python_version': 2.7}})

    CliRunner().invoke(cli, [
        'create',
        'job',
        'distributed',
        '--project', 'someproject',
    ])

    args, kwargs = ClusteroneClient.create_job.call_args
    assert kwargs['parameters']['mode'] == 'distributed'


def test_many_workers_ps_warning(mocker):
    distributed.client = mocker.Mock()
    mocker.patch.object(ClusteroneClient, '__init__', autospec=True, return_value=None)
    ClusteroneClient.create_job = mocker.Mock()
    distributed.base = mocker.Mock(return_value={'meta': {'name': 'late-moon-758', 'description': ''}, 'parameters': {'package_path': '', 'requirements': 'requirements.txt', 'time_limit': 2880, 'module': 'main', 'framework': 'tensorflow', 'git_commit_hash': '4a82d16c7995856c7973af38f2f5ba4eac0cd2d1', 'code': 'aaf4de71-f506-48c0-855c-02c7c485c5a4', 'package_manager': 'pip', 'Clusterone_api_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im9sZ2llcmRAa2FzcHJvd2ljei5wcm8iLCJ1c2VyX2lkIjo3OTUsImV4cCI6MTUxNzMxNjUzMCwidXNlcm5hbWUiOiJhbGxncmVlZCJ9.IJhEZWwMYf2sjHhoxUsjCj0Xll5CVX-RO3eUqvH7myU', 'python_version': 2.7}})
    distributed.PS_REPLICAS_WARNING_THRESHOLD = 5
    distributed.WORKER_REPLICAS_WARNING_THRESHOLD = 10

    result = CliRunner().invoke(cli, [
        'create',
        'job',
        'distributed',
        '--project', 'someproject',
        '--worker-replicas', '21',
        '--ps-replicas', '52',
    ])

    assert "Caution: You are creating a job with more than 5 parameter servers" in result.output
    assert "Caution: You are creating a job with more than 10 workers." in result.output


def test_invalid_framework(mocker):
    distributed.client = mocker.Mock()
    mocker.patch.object(ClusteroneClient, '__init__', autospec=True, return_value=None)
    ClusteroneClient.create_job = mocker.Mock()
    distributed.base = mocker.Mock(return_value={'meta': {'name': 'late-moon-758', 'description': ''}, 'parameters': {'package_path': '', 'requirements': 'requirements.txt', 'time_limit': 2880, 'module': 'main', 'tf_version': '1.2', 'framework': {'slug': 'pytorch-1.0.0'}, 'git_commit_hash': '4a82d16c7995856c7973af38f2f5ba4eac0cd2d1', 'code': 'aaf4de71-f506-48c0-855c-02c7c485c5a4', 'package_manager': 'pip', 'Clusterone_api_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im9sZ2llcmRAa2FzcHJvd2ljei5wcm8iLCJ1c2VyX2lkIjo3OTUsImV4cCI6MTUxNzMxNjUzMCwidXNlcm5hbWUiOiJhbGxncmVlZCJ9.IJhEZWwMYf2sjHhoxUsjCj0Xll5CVX-RO3eUqvH7myU', 'python_version': 2.7}})

    result = CliRunner().invoke(cli, [
        'create',
        'job',
        'distributed',
        '--project', 'someproject'
        '--framework', 'pytorch-1.0.0',
    ])

    # Click internal exception
    assert str(result.exception) == '2'
