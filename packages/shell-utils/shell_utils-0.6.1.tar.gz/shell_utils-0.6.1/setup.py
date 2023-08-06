# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['shell_utils']

package_data = \
{'': ['*']}

install_requires = \
['click>=6.7,<7.0']

entry_points = \
{'console_scripts': ['notify = shell_utils.notify:notify_command',
                     'shell_utils = shell_utils.cli:cli']}

setup_kwargs = {
    'name': 'shell-utils',
    'version': '0.6.1',
    'description': 'Shell automation tools, like Make on steroids.',
    'long_description': '# Description\n\nThe `shell_utils` library provides some handy utilities for when you need to automate certain processes using shell commands.\n\nWhere you might otherwise write a bash script or muck around with the `subprocess`, `os`, and `sys`  modules in a Python script `shell_utils` provides\nsome patterns and shortcuts for your automation scripts.\n\nLet\'s say we have a new project we need to automate some build process(es) for. We might be tempted to write a Makefile or bash\nscript(s) to help with that task. If that works for you, great. However, if you\'re like me, you prefer to python-all-the-things.\n\nWe can use shell-utils to create an automation script that will behave much the same way a Makefile would, but with all the\nPython goodness we want.\n\nSome familiarity with the `click` library will be helpful.\n\n```bash\npip3 install shell_utils\nshell_utils generate_runner\n```\n\nThis will produce an executable python script with the following code\n```python\n#!/usr/bin/env python3\nimport os\nfrom pathlib import Path\n\nfrom shell_utils import shell, cd, env, path, quiet\n\nimport click\n\n\n@click.group()\ndef main():\n    """\n    Development tasks; programmatically generated\n    """\n\n    # ensure we\'re running commands from project root\n\n    root = Path(__file__).parent.absolute()\n    cwd = Path().absolute()\n\n    if root != cwd:\n        click.secho(f\'Navigating from {cwd} to {root}\',\n                    fg=\'yellow\')\n        os.chdir(root)\n\n    if root != cwd:\n        click.secho(f\'Navigating from {cwd} to {root}\', fg=\'yellow\')\n        os.chdir(root)\n\n\nif __name__ == \'__main__\':\n    main()\n```\n\nNow let\'s say that we\'re using sphinx to generate the documentation we have in our project\'s `docs` directory.\n\nIf we wanted to create a command that would re-generate our documentation and open a browser window when it\'s finished,\n\nwe could add the following code to our generated `run.py` script\n\n\n```python\n@main.command()\n@click.option(\'--no-browser\', is_flag=True, help="Don\'t open browser after building docs.")\ndef docs(no_browser):\n    """\n    Generate Sphinx HTML documentation, including API docs.\n    """\n    shell(\'rm -f docs/my_project.rst\')\n    shell(\'rm -f docs/modules.rst\')\n    shell(\'rm -f docs/my_project*\')\n    shell(\'sphinx-apidoc -o docs/ my_project\')\n\n    with cd(\'docs\'):\n        shell(\'make clean\')\n        shell(\'make html\')\n\n    shell(\'cp -rf docs/_build/html/ public/\')\n\n    if no_browser:\n        return\n\n    shell(\'open public/index.html\')\n```\n\nThen, we can execute the following command to do what we intended:\n\n`./run.py docs`\n\nThe strings sent to the `shell` function will be executed in a `bash` subprocess shell. Before they are executed,\nthe `shell` function will print the command to `stdout`, similar to a `Makefile`.\n\nAlso, notice we change directories into `docs` using a context manager, that way the commands passed to the `shell` function\nwill execute within that directory. Once we\'re out of the context manager\'s scope, further `shell` function commands are once-again run\nfrom the project root.\n\n# functions and context managers\n\n## shell\n\nExecutes the given command in a bash shell. It\'s just a thin wrapper around `subprocess.run` that adds a couple handy features,\nsuch as printing the command it\'s about to run to stdout before executing it.\n\n```python\nfrom shell_utils import shell\n\np1 = shell(\'echo hello, world\')\n\nprint(p1)\n\np2 = shell(\'echo goodbye, cruel world\', capture=True)\n\nprint(\'captured the string:\', p2.stdout.decode())\n```\n\n**outputs**\n\n```bash\nuser@hostname executing...\n\necho goodbye, cruel world\n\n\ncaptured the string: goodbye, cruel world\n```\n\n## cd\n\nTemporarily changes the current working directory while within the context scope.\n\nWithin a python shell...\n\n```\nshell(\'pwd\')\nuser@hostname executing...\npwd\n.../shell_utils\nCompletedProcess(args=\'pwd\', returncode=0)\n\nwith cd(\'tests\'):\n    shell(\'pwd\')\n    \nuser@hostname executing...\npwd\n.../shell_utils/tests\n\nshell(\'pwd\')\nuser@hostname executing...\npwd\n.../shell_utils\nCompletedProcess(args=\'pwd\', returncode=0)\n```\n\n## env\n\nTemporarily changes environment variables\n\n```python\nfrom shell_utils import env\nimport os\n\nprint(os.getenv(\'foo\', \'nothing\'))\n\nwith env(foo=\'bar\'):\n    print(os.getenv(\'foo\'))\n\nprint(os.getenv(\'foo\', \'nothing again\'))\n```\n\n**outputs**\n\n```bash\nnothing\nbar\nnothing again\n```\n\n## path\n\nA special case of the `env` context manager that alters your $PATH. It expands `~` to your home directory and returns\nthe elements of the $PATH variable as a list.\n\n```python\nfrom shell_utils import path\nimport os\n\ndef print_path():\n    print(\'$PATH ==\', os.getenv(\'PATH\'))\n\nprint_path()\n\nwith path(\'~\', prepend=True) as plist:\n    print_path()\n    print(plist)\n```\n\n**outputs**\n\n```bash\n$PATH == /Users/user/.venvs/shell-utils-py3.7/bin:/usr/local/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/TeX/texbin\n$PATH == /Users/user:/Users/user/.venvs/shell-utils-py3.7/bin:/usr/local/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/TeX/texbin\n[\'/Users/user\', \'/Users/user/.venvs/shell-utils-py3.7/bin\', \'/usr/local/sbin\', \'/usr/local/bin\', \'/usr/bin\', \'/bin\', \'/usr/sbin\', \'/sbin\', \'/Library/TeX/texbin\']\n```\n',
    'author': 'Stephan Fitzpatrick',
    'author_email': 'knowsuchagency@gmail.com',
    'url': 'https://github.com/knowsuchagency/shell-utils',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
}


setup(**setup_kwargs)
