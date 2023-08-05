from nio.modules.persistence import Persistence as PersistenceModule
from nio.modules.scheduler import Job
from nio.properties import TimeDeltaProperty, BoolProperty


class Persistence(object):

    """ A block mixin that provides persistence for some variables.

    To use, override the persisted_values function and define which variables
    on your class you wish to have persisted. The values should be strings
    that correspond to the variable names to be saved.

    """

    backup_interval = TimeDeltaProperty(
        visible=False, title='Backup Interval', default={"seconds": 60 * 60})
    load_from_persistence = BoolProperty(
        title='Load from Persistence?', default=True, advanced=True, order=100
    )

    def __init__(self):
        super().__init__()
        self._persistence = None
        self._backup_job = None

    def persisted_values(self):
        """ Return a list containing the values to be persisted.

        This function should be overriden in a Block that wishes to use
        persistence. Return a list of the names of the instance level variables
        to save.

        For example, if your block class has an instance level attribute called
        `_values` and you wish to save it, you would return this list:
            ["_values"]
        """
        return []

    def _load(self):
        """ Load the values from persistence

        Item is loaded from persistence using block id, once item
        is loaded, all persisted values are examined against loaded
        item, if it exists, such value is then set as an attribute
        in the block instance
        """
        self.logger.debug("Loading from persistence")
        # load whole item from persistence
        item = self._persistence.load(self.id(), default={})
        for persisted_var in self.persisted_values():
            if persisted_var in item:
                self.logger.debug("Loaded value {} for attribute {}".format(
                    item[persisted_var], persisted_var))
                # Set the loaded value to the attribute on this class
                setattr(self, persisted_var, item[persisted_var])

    def _save(self):
        """ Save the values to persistence
        """
        self.logger.debug("Saving to persistence")
        # generate item to be persisted by gathering all variables
        # to be persisted into a dictionary
        item = {persisted_var: getattr(self, persisted_var)
                for persisted_var in self.persisted_values()}
        # save generated dictionary under block's id
        self._persistence.save(item, self.id())

    def configure(self, context):
        super().configure(context)
        # Create a persistence object using the block's id
        self._persistence = PersistenceModule()
        if self.load_from_persistence():
            self._load()

    def start(self):
        super().start()

        # If we have configured a backup interval, set up the job to
        # periodically save to persistence
        if self.backup_interval().total_seconds() > 0:
            self._backup_job = Job(self._save, self.backup_interval(), True)

    def stop(self):
        if self._backup_job:
            self._backup_job.cancel()

        # Do one last save before stopping
        self._save()
        super().stop()
