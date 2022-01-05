import click

@click.command()
@click.argument('project_source', type=click.Choice(['NEW', 'GIT'], case_sensitive=False))
@click.option('--project_name', default=1)
@click.option('--git-url', default=1)
@click.option('--migrate/--no-migrate', default=False)
@click.option('--collect-static/--no-collect-static', default=False)
@click.option('--requirments', default=1)
@click.option('--python_version', default=1)
@click.option('--django_version', default=1)
@click.option('--domain', default=1)
def hello(project_source):
    """Simple Program to Deploy Django + Gunicorn + NGINX with Single Command."""
    
if __name__ == '__main__':
    hello()