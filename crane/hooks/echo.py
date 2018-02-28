from os import environ

import click

from .. import deployment
from .base import Base


class Hook(Base):

    is_active = True

    def get_changelog(self):
        if deployment.is_redeploy:
            return 'Re-deploy without changes.'

        prefix = ''
        if deployment.is_rollback:
            prefix = 'Rolling back the following changes:\n'
        elif deployment.is_disconnected:
            prefix = (
                "Switching branches, so the exact changes can't be determined. "
                'The latest commit now is:\n'
            )
        return prefix + '\n'.join(
            (
                f'{environ["CI_PROJECT_URL"]}/commit/{commit.hexsha}|{commit.summary} '
                f'by {commit.author.name}'
            )
            for commit in deployment.commits
            if len(commit.parents) == 1  # skip Merge commit
        )

    def before_upgrade(self):
        click.echo("Alrighty, let's deploy! " + click.style('ᕕ( ᐛ )ᕗ', bold=True))
        click.echo(f'(But please supervise me at {deployment.stack.web_url})')
        click.echo(f'{self.get_changelog()}')
        click.echo('If this is not what you meant to deploy, you can cancel with the link above.')

    def after_upgrade_success(self):
        click.secho("…and we're done. Good job, everyone! " + click.style('(◕‿◕✿)', bold=True), fg='green')

    def after_upgrade_failure(self):
        click.echo()  # add newline before the traceback
