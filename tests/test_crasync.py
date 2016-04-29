import asyncio
from unittest import TestCase
from unittest.mock import MagicMock
from crasync import crasync


@crasync
class SomeCarsyncClass(object):
    def __init__(self, mock_func):
        super(SomeCarsyncClass, self).__init__()

        self.mock_func = mock_func

    @crasync
    async def async_function(self):
        await asyncio.sleep(0.1)
        self.mock_func()


class CrasyncTest(TestCase):
    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(None)

    def test_crasync(self):
        Async1 = SomeCarsyncClass
        Async2 = SomeCarsyncClass.async
        Sync = SomeCarsyncClass.sync

        mock_async1 = MagicMock()
        mock_async2 = MagicMock()
        mock_sync = MagicMock()

        async1 = Async1(mock_async1)
        async2 = Async2(mock_async2)
        sync = Sync(mock_sync)

        self.loop.run_until_complete(async1.async_function())
        mock_async1.assert_called_once_with()
        self.loop.run_until_complete(async2.async_function())
        mock_async2.assert_called_once_with()

        sync.async_function()
        mock_sync.assert_called_with()
