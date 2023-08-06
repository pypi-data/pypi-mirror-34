import os, empy, tempfile
import pretty_output
import random, string

from kooki.tools import get_front_matter, read_file

from .jars import search_file, search_file_in_context
from .common import apply_template
from .metadata import Metadata
from .renderer import render
from .exception import ErrorEvaluatingExpression, MissingFile

PREFIX = '@'
MARKDOWN_EXT = '.md'


class Extension():

    level = 0

    def __init__(self, document, extension_path):
        file_content = read_file(extension_path)
        _, self.file_extension = os.path.splitext(extension_path)
        self.extension_path = extension_path
        self.document = document
        self.front_matter, self.content = get_front_matter(file_content)

    def __call__(self, *args, **kwargs):

        try:
            metadata = self.parse_metadata(*args, **kwargs)
            content = self.content

            self.debug_tree_start()

            caller = Caller(self.document, self.extension_path, metadata=metadata)
            content = self.apply_interpreter(content, caller, prefix=PREFIX)

            if self.file_extension == MARKDOWN_EXT:
                content = render(content, caller)

            for placeholder_key, placeholder_value in Caller.placeholders.items():
                content = content.replace(placeholder_key, placeholder_value)

            self.debug_tree_stop()

            return content

        except ErrorEvaluatingExpression as e:
            e.add_path(self.extension_path)
            raise e

    def apply_interpreter(self, content, metadata, prefix):
        interpreter = empy.Interpreter()
        interpreter.setPrefix(prefix)
        result = interpreter.expand(content, metadata)
        return result

    def parse_metadata(self, *args, **kwargs):
        metadata = Metadata()
        metadata.update(self.front_matter)
        metadata.update(self.document.metadata)
        new_args = {}
        for index, arg in enumerate(args):
            new_args['arg{}'.format(index)] = arg
        metadata.update(**new_args)
        metadata.update(**kwargs)
        return metadata

    def debug_tree_start(self):
        pretty_output.debug_on()
        if Extension.level == 0:
            pretty_output.colored(self.extension_path, 'white', 'on_yellow')
        else:
            message = ''
            for i in range(0, self.level-1):
                message += '│   '
            message += '├'
            message += '─' * 2
            message += ' '
            pretty_output.colored(message, 'white', 'on_yellow', end='')
            pretty_output.colored(self.extension_path, 'white', 'on_yellow')
        Extension.level += 1
        char = '└'
        pretty_output.debug_off()

    def debug_tree_stop(self):
        Extension.level -= 1


def is_builtin_class_instance(obj):
    return obj.__class__.__module__ == '__builtin__'


class Caller():

    placeholders = {}

    def __init__(self, document, extension_path, metadata, call_path=''):
        self.document = document
        self.extension_path = extension_path
        self.call_path = call_path
        self.metadata = metadata
        self.metadata.update({
            'find': self.find,
            'load': self.load,
            'get': self.get})
        self.data = None

    def __getattr__(self, name):
        return self.get_item(name)

    def __getitem__(self, key):
        return self.get_item(key)

    def __setitem__(self, key, value):
        self.metadata[key] = value

    def get_item(self, key):

        if key == 'locals':
            def call_locals():
                return locals()
            return call_locals

        if self.call_path != '':
            new_call_path = '{}/{}'.format(self.call_path, key)
        else:
            new_call_path = key

        self.metadata.update(__builtins__)
        self.metadata.update(locals()['self'].metadata)
        value = self.metadata.get(key)

        if value != None:
            if is_builtin_class_instance(value):
                return type('', (type(value), Caller), {})(self.document, self.extension_path, self.metadata, new_call_path)
            else:
                return value
        else:
            return Caller(self.document, self.extension_path, self.metadata, new_call_path)

    def __repr__(self):
        return ''

    def __call__(self, *args, placeholder=True, **kwargs):

        path = search_file_in_context(self.document, self.extension_path, self.call_path)
        if not path:
            path = search_file(self.document, self.call_path)

        if not path:
            raise Exception('cannot find {}'.format(self.call_path))

        if os.path.isdir(path):
            full_path = os.path.join(path, '__kooki__.md')
            if not os.path.isfile(full_path):
                raise Exception('You try to call this extension ({}), but it is a directory and there no __kooki__.md inside.'.format(path))
        else:
            full_path = path

        extension = Extension(self.document, full_path)
        result = extension(*args, **kwargs)
        if placeholder:
            name = self.get_var_name()
            Caller.placeholders[name] = result
            return '{}'.format(name)
        else:
            return result

    def find(self, file_path):
        file_full_path = search_file(self.document, file_path)
        if file_full_path:
            return file_full_path
        else:
            raise MissingFile(self.document.jars, file_path)

    def load(self, content, template_extension):
        path = tempfile.NamedTemporaryFile(suffix=template_extension).name
        with open(path, 'w') as stream:
            stream.write(content)
        return Extension(self.document, path)

    def get(self, key, default=''):
        if key in self.metadata:
            return self.metadata[key]
        else:
            return default

    def get_var_name(self):
        name = ''.join(random.choice(string.ascii_uppercase) for _ in range(25))
        while name in Caller.placeholders:
            name = ''.join(random.choice(string.ascii_uppercase) for _ in range(25))
        return name

