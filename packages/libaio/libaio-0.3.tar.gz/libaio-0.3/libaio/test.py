#!/usr/bin/env python
# Copyright (C) 2017-2018  Vincent Pelletier <plr.vincent@gmail.com>
#
# This file is part of python-libaio.
# python-libaio is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# python-libaio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with python-libaio.  If not, see <http://www.gnu.org/licenses/>.
from __future__ import absolute_import, print_function
import unittest
import tempfile
import libaio

class LibAIOTests(unittest.TestCase):
    def testBasicFunctionality(self):
        with tempfile.TemporaryFile() as temp, libaio.AIOContext(1) as io_context:
            def readall():
                temp.seek(0)
                return temp.read()
            temp.write(b'blah')
            temp.flush()
            read_buf_0 = bytearray(2)
            read_buf_1 = bytearray(2)
            read_completion_event_list = []
            read_block = libaio.AIOBlock(
                mode=libaio.AIOBLOCK_MODE_READ,
                target_file=temp,
                buffer_list=[
                    read_buf_0,
                    read_buf_1,
                ],
                offset=0,
                onCompletion=(
                    lambda block, res, res2:
                    read_completion_event_list.append((block, res, res2))
                ),
            )
            write_completion_event_list = []
            write_block = libaio.AIOBlock(
                mode=libaio.AIOBLOCK_MODE_WRITE,
                target_file=temp,
                buffer_list=[
                    bytearray(b'u'),
                    bytearray(b'ez'),
                ],
                offset=2,
                onCompletion=(
                    lambda block, res, res2:
                    write_completion_event_list.append((block, res, res2))
                ),
            )
            io_context.submit([read_block])
            read_event_list_reference = [(read_block, 4, 0)]
            self.assertEqual(
                read_event_list_reference,
                io_context.getEvents(min_nr=None),
            )
            self.assertEqual(
                read_event_list_reference,
                read_completion_event_list,
            )
            self.assertEqual(read_buf_0, bytearray(b'bl'))
            self.assertEqual(read_buf_1, bytearray(b'ah'))

            io_context.submit([write_block])
            write_event_list_reference = [(write_block, 3, 0)]
            self.assertEqual(
                write_event_list_reference,
                io_context.getEvents(min_nr=None),
            )
            self.assertEqual(
                write_event_list_reference,
                write_completion_event_list,
            )
            self.assertEqual(readall(), b'bluez')

if __name__ == '__main__':
    unittest.main()
