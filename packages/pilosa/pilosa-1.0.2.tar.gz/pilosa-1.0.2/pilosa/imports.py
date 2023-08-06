# Copyright 2017 Pilosa Corp.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
# contributors may be used to endorse or promote products derived
# from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
# DAMAGE.
#

import itertools
from collections import namedtuple

from pilosa.exceptions import PilosaError

__all__ = ("Columns", "csv_column_reader")

Columns = namedtuple("Column", "row_id column_id timestamp")


def csv_column_reader(file_obj, timefunc=int):
    """
    Reads columns from the given file-like object.

    Each line of the file-like object should correspond to a single bit and must be in the following form:
    rowID,columnID[,timestamp]

    :param file_obj:
    :param timefunc: optional time parsing function, defaults to int
    :return: a generator
    """
    for line in file_obj:
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        if len(parts) == 2:
            try:
                bit = Columns(row_id=int(parts[0]), column_id=int(parts[1]), timestamp=0)
            except ValueError:
                raise PilosaError("Invalid CSV line: %s", line)
        elif len(parts) == 3:
            try:
                bit = Columns(row_id=int(parts[0]), column_id=int(parts[1]), timestamp=timefunc(parts[2]))
            except ValueError:
                raise PilosaError("Invalid CSV line: %s", line)
        else:
            raise PilosaError("Invalid CSV line: %s", line)
        yield bit


def batch_columns(reader, batch_size):
    shard_width = 1048576
    while 1:
        batch = list(itertools.islice(reader, batch_size))
        if not batch:
            break
        bit_groups = {}
        for bit in batch:
            bit_groups.setdefault(bit.column_id // shard_width, []).append(bit)
        for shard_bit_group in bit_groups.items():
            yield shard_bit_group

