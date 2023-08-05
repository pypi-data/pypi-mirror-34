"""nose2 test infrastructure."""

import os
import re
import sys
import doctest
import importlib

from nose2.events import Plugin


DOT = '.'
FLAGS = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE | doctest.REPORT_NDIFF


def as_object(path):
    if path is None:
        return None
    # mod.ule.object -> import(mod.ule); mod.ule.object
    module_name, dot, object_name = path.rpartition('.')
    if dot != '.' or len(object_name) == 0:
        return None
    module = importlib.import_module(module_name)
    return getattr(module, object_name, None)


class NosePlugin(Plugin):
    configSection = 'flufl.testing'

    def __init__(self):
        super().__init__()
        self.patterns = []
        self.stderr = False
        def set_stderr(ignore):                                  # noqa: E306
            self.stderr = True
        self.addArgument(self.patterns, 'P', 'pattern',
                         'Add a test matching pattern')
        self.addFlag(set_stderr, 'E', 'stderr',
                     'Enable stderr logging to sub-runners')
        # Get the topdir out of the plugin configuration file.
        self.package = self.config.as_str('package')
        if self.package is None:
            raise RuntimeError('flufl.nose2 plugin missing "package" setting')

    def startTestRun(self, event):
        callback = as_object(self.config.get('start_run'))
        if callback is not None:
            callback(self)

    def getTestCaseNames(self, event):
        if len(self.patterns) == 0:
            # No filter patterns, so everything should be tested.
            return
        # Does the pattern match the fully qualified class name?
        for pattern in self.patterns:
            full_class_name = '{}.{}'.format(
                event.testCase.__module__, event.testCase.__name__)
            if re.search(pattern, full_class_name):
                # Don't suppress this test class.
                return
        names = filter(event.isTestMethod, dir(event.testCase))
        for name in names:
            full_test_name = '{}.{}.{}'.format(
                event.testCase.__module__,
                event.testCase.__name__,
                name)
            for pattern in self.patterns:
                if re.search(pattern, full_test_name):
                    break
            else:
                event.excludedNames.append(name)

    def handleFile(self, event):
        package = importlib.import_module(self.package)
        path = event.path[len(os.path.dirname(package.__file__))+1:]
        if len(self.patterns) > 0:
            for pattern in self.patterns:
                if re.search(pattern, path):
                    break
            else:
                # Skip this doctest.
                return
        base, ext = os.path.splitext(path)
        if ext != '.rst':
            return
        # Look to see if the package defines a test layer, otherwise use the
        # default layer.  First turn the file system path into a dotted Python
        # module path.
        parent = os.path.dirname(path)
        dotted = '{}.{}'.format(
            self.package, DOT.join(parent.split(os.path.sep)))
        layer = None
        default_layer = as_object(self.config.get('default_layer'))
        try:
            module = importlib.import_module(dotted)
        except ImportError:
            layer = default_layer
        else:
            layer = getattr(module, 'layer', default_layer)
        setup = as_object(self.config.get('setup'))
        teardown = as_object(self.config.get('teardown'))
        test = doctest.DocFileTest(
            path, package=self.package,
            optionflags=FLAGS,
            setUp=setup,
            tearDown=teardown)
        test.layer = layer
        # Suppress the extra "Doctest: ..." line.
        test.shortDescription = lambda: None
        event.extraTests.append(test)

    def startTest(self, event):
        if self.config.as_bool('trace', False):
            print('vvvvv', event.test, file=sys.stderr)

    def stopTest(self, event):
        if self.config.as_bool('trace', False):
            print('^^^^^', event.test, file=sys.stderr)
