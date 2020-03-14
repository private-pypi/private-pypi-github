from private_pypi.backend import BackendRegistration
from private_pypi_backends.github.impl import (
        GITHUB_TYPE,
        GitHubConfig,
        GitHubAuthToken,
        GitHubPkgRepo,
        GitHubPkgRef,
        github_create_package_repo_cli,
)


class GitHubRegistration(BackendRegistration):
    type = GITHUB_TYPE
    pkg_repo_config_cls = GitHubConfig
    pkg_repo_secret_cls = GitHubAuthToken
    pkg_repo_cls = GitHubPkgRepo
    pkg_ref_cls = GitHubPkgRef
    cli_name_to_func = {'create_package_repo': github_create_package_repo_cli}
