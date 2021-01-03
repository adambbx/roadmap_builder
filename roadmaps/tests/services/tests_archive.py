import os
from io import BytesIO
from unittest import TestCase

from roadmaps.services.archive import ArchiveInMemory


class ArchiveInMemoryTestCase(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.filename = 'test.txt'
        self.expected_buffer_size = 136
        with open(self.filename, 'w') as fl:
            fl.write("Some testing content")

    def tearDown(self) -> None:
        super().tearDown()
        os.remove(self.filename)

    def test_create(self):
        content = ArchiveInMemory.create([self.filename])
        self.assertIsInstance(content, BytesIO)
        self.assertEqual(self.expected_buffer_size, content.getbuffer().nbytes)
