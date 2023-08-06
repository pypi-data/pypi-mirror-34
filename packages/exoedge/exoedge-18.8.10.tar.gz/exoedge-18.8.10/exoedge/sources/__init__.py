# pylint: disable=W1202
import logging
from murano_client.client import StoppableThread

'''
What am I after:

I need a thread started once and only once.
 - Implemented by AsyncSource.get_async_source()
I need module-level functions to be callable via exoedge in the 'async' mode.
 - Implemented by AsyncSource.exoedge_put(data)
I need to be able to write functions so they are simple and developers can write their own.
 - ExoEdge Source developers can add class and/or module level functions/methods (or both) that implement the desired behavior.
I need a thread that can be extended to maintain a connection to a hardware resource.
 - ExoEdge Source developers can add members and methods to classes that subclass AsyncSource that manage hardware connections and interactions.
 - The AsyncSource class can be used in both "poll" and "async" config_io types.

'''

logging.getLogger('SOURCES')
logging.basicConfig(level=logging.DEBUG)

class AsyncSource(StoppableThread):
    """ Template class for defining custom "async" and/or "poll" type
    ExoEdge sources. Instances of this class will be a separate threads
    that follow the "borg" design pattern. """
    __borg_state = {}
    def __init__(self, **kwargs):
        """

        """
        self.__dict__ = self.__borg_state

        t_kwargs = {}
        if kwargs.get('group'):
            t_kwargs.update(group=kwargs.get('group'))
        if kwargs.get('target'):
            t_kwargs.update(target=kwargs.get('target'))
        if kwargs.get('name'):
            t_kwargs.update(name=kwargs.get('name'))
        if kwargs.get('args'):
            t_kwargs.update(args=kwargs.get('args'))
        if kwargs.get('kwargs'):
            t_kwargs.update(kwargs=kwargs.get('kwargs'))

        logging.info("async source thread kwargs: {}".format(t_kwargs))
        logging.info("async source other kwargs: {}".format(kwargs))

        super(AsyncSource, self).__init__(**t_kwargs)
        self.setDaemon(True)
        # parse the function pointer from ExoEdge for sending
        # data to ExoSense
        self._exoedge_put = kwargs.get('_fn')
        # parse the event object from ExoEdge for notifying
        # that there is new data for ExoSense
        self._exoedge_event = kwargs.get('event')

    def exoedge_put(self, data):
        """ Use this method to send async data to ExoSense. """

        self._exoedge_put(data)
        self._exoedge_event.set()

    def get_async_source(self):
        """ Call this function atleast once to start the
        Async Source thread. Call this function and assign
        to a variable to gain access to members and methods
        associated with this thread. """

        if not self.is_started():
            super(AsyncSource, self).start()
        return self
