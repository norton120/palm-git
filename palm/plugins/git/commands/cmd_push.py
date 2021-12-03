import click


SUCCESS = 0

@click.command('push')
@click.pass_obj
def cli(environment):
    """A smarter git push. Sets the upstream branch if needed. """
    exit_status, stdout, stderr = environment.run_on_host("git push", capture_output=True)
    if exit_status == SUCCESS:
        click.echo("\n".join((stdout, stderr,)))
        message = "pushed to remote."
        color = "green"
        if stderr:
            message = "local was not " + message
            color = "red"
        click.secho(message.capitalize(), fg=color) 
        return 

    if "To push the current branch and set the remote as upstream, use" in stderr:
        click.echo("No upstream branch, setting that for you on origin...")
        environment.run_on_host(f"git push --set-upstream origin {current_git_branch(environment)}", 
                                bubble_error=True)
        click.secho("Remote set and pushed.", fg="green")
        return
    click.echo("\n".join((stdout, stderr,)))

def current_git_branch(environment) -> str:
    """gets the branch we are currently on.
        Args:
            environment: a click environment object
        Returns:
            str: the branch name
    """
    _, stdout, _ = environment.run_on_host('git branch | grep \* | sed "s/\* //"',
                                           capture_output=True,
                                           bubble_error=True)
    return stdout
