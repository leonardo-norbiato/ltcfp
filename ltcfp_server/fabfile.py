from fabric.api import local, settings, abort
from fabric.contrib.console import confirm

# prepare for deployment


def test():
    with settings(warn_only=True):
        result = local(
            "python test_tasks.py -v && python test_users.py -v", capture=True
        )
    if result.failed and not confirm("Testes falharam. Quer continuar?"):
        abort("Abortado a pedido do usuário.")


def commit():
    message = raw_input("Digite uma mensagem de texto para o commit no git:: ")
    local("git add . && git commit -am '{}'".format(message))


def push():
    local("git push origin master")


def prepare():
    test()
    commit()
    push()

# deploy to heroku


def pull():
    local("git pull origin master")


def heroku():
    local("git push heroku master")


def heroku_test():
    local(
        "heroku run python test_tasks.py -v && heroku run python test_users.py -v"
    )


def deploy():
    pull()
    test()
    commit()
    heroku()
    heroku_test()

# rollback


def rollback():
    local("heroku rollback")
