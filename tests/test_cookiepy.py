from ast import literal_eval
from shutil import rmtree

from cookiecutter.main import cookiecutter


extra_context_dir = './test_cookiecutter.json'
rmtree('cookiepy-test', ignore_errors=True)


with open(extra_context_dir, mode='r', encoding='utf-8') as test_file:
    extra_ctx = literal_eval(test_file.read())


cookiecutter(
    'https://github.com/erik-ingwersen-ey/cookiepy.git',
    no_input=True,
    extra_context=extra_ctx,
    replay=True,
)
