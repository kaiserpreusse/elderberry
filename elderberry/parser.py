import logging
from graphio import Container

log = logging.getLogger(__name__)


class Parser:

    def __init__(self, root_dir):

        self.root_dir = root_dir

        self.datasource_instances = []

        self.container = Container()
        self.name = self.__class__.__name__

    def get_instance_by_name(self, name):
        """

        :param name:
        :return: The DataSourceInstance
        :rtype: DataSourceInstance
        """
        for datasource_instance in self.datasource_instances:
            if datasource_instance.datasource.name == name:
                return datasource_instance

    def get_nodeset(self, labels, merge_keys):
        return self.container.get_nodeset(labels, merge_keys)

    def reset_container(self):
        """
        Set container to empty Container() to allow for garbage collection.
        """
        del self.container
        self.container = Container()

    def run_with_mounted_arguments(self):
        """
        Unified interface_dev to run the parser. Does not take parameters (all necessary
        arguments must be stored in the Parser class).

        Returns the output of the parser function.
        """
        raise NotImplementedError

    def run(self, *args, **kwargs):
        """
        Run the parser with specific parameters.

        Returns the output of the parser function.
        """
        raise NotImplementedError


class ReturnParser(Parser):
    """
    Base class for parsers which run over files and store ouput in memory.

    They need an explicit .run() function.
    """
    TYPE = 'return'

    def __init__(self, root_dir):
        super(ReturnParser, self).__init__(root_dir)


class YieldParser(Parser):
    """
    Base class for parsers which mount yield functions into the ObjectSets.

    Used for very large data sets which do not fit into memory.
    """
    TYPE = 'yield'

    def __init__(self, root_dir):
        super(YieldParser, self).__init__(root_dir)

    def mount_generators(self):
        raise NotImplementedError
