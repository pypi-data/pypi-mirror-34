#!/usr/bin/env python

# Copyright (c) 2018, DIANA-HEP
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import collections
import numbers

import numpy

import awkward.array.base
import awkward.util

class JaggedArray(awkward.array.base.AwkwardArray):
    @classmethod
    def fromoffsets(cls, offsets, content):
        return cls(offsets[:-1], offsets[1:], content)

    @classmethod
    def fromcounts(cls, counts, content):
        offsets = numpy.empty(len(counts) + 1, JaggedArray.INDEXTYPE)
        offsets[0] = 0
        numpy.cumsum(counts, offsets[1:])
        return cls(offsets[:-1], offsets[1:], content)

    @classmethod
    def fromuniques(cls, uniques, content):
        uniques = JaggedArray._toarray(uniques, self.INDEXTYPE, (numpy.ndarray, awkward.array.base.AwkwardArray))
        if len(uniques) != len(content):
            raise ValueError("uniques array must have the same length as content")
        changes = numpy.nonzero(uniques[1:] != uniques[:-1])[0] + 1
        offsets = numpy.empty(len(changes) + 2, dtype=JaggedArray.INDEXTYPE)
        offsets[0] = 0
        offsets[-1] = len(content)
        offsets[1:-1] = changes
        starts, stops = offsets[:-1], offsets[1:]
        return JaggedArray(starts, stops, content)

    @classmethod
    def fromparents(cls, parents, content):
        if len(parents) != len(content):
            raise ValueError("parents array must have the same length as content")

        tmp = numpy.nonzero(parents[1:] != parents[:-1])[0] + 1

        changes = numpy.empty(len(tmp) + 2, dtype=JaggedArray.INDEXTYPE)
        changes[0] = 0
        changes[-1] = len(parents)
        changes[1:-1] = tmp

        length = parents.max() + 1
        starts = numpy.zeros(length, dtype=JaggedArray.INDEXTYPE)
        counts = numpy.zeros(length, dtype=JaggedArray.INDEXTYPE)

        where = parents[changes[:-1]]
        real = (where >= 0)

        starts[where[real]] = (changes[:-1])[real]
        counts[where[real]] = (changes[1:] - changes[:-1])[real]

        return JaggedArray(starts, starts + counts, content)

    @classmethod
    def fromiter(cls, iterable):
        offsets = [0]
        content = []
        for x in iterable:
            offsets.append(offsets[-1] + len(x))
            content.extend(x)
        return cls(offsets[:-1], offsets[1:], content)

    @staticmethod
    def compatible(*jaggedarrays):
        if not all(isinstance(x, JaggedArray) for x in jaggedarrays):
            raise TypeError("not all objects passed to JaggedArray.compatible are JaggedArrays")

        if len(jaggedarrays) == 0:
            return True

        # empty subarrays can be represented by any start,stop as long as start == stop
        relevant, relevantstarts, relevantstops = None, None, None

        first = jaggedarrays[0]
        for next in jaggedarrays[1:]:
            if first._starts is not next._starts:
                if relevant is None:
                    relevant = (first.counts != 0)
                if relevantstarts is None:
                    relevantstarts = first._starts[relevant]
                if not numpy.array_equal(relevantstarts, next._starts[relevant]):
                    return False

            if first._stops is not next._stops:
                if relevant is None:
                    relevant = (first.counts != 0)
                if relevantstops is None:
                    relevantstops = first._stops[relevant]
                if not numpy.array_equal(relevantstops, next._stops[relevant]):
                    return False

        return True

    def __init__(self, starts, stops, content):
        self.starts = starts
        self.stops = stops
        self.content = content

    @property
    def starts(self):
        return self._starts

    @starts.setter
    def starts(self, value):
        value = self._toarray(value, self.INDEXTYPE, (numpy.ndarray, awkward.array.base.AwkwardArray))
        if (value < 0).any():
            raise ValueError("starts must be a non-negative array")
        self._starts = value

    @property
    def stops(self):
        return self._stops

    @stops.setter
    def stops(self, value):
        value = self._toarray(value, self.INDEXTYPE, (numpy.ndarray, awkward.array.base.AwkwardArray))
        if (value < 0).any():
            raise ValueError("stops must be a non-negative array")
        self._stops = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = self._toarray(value, self.CHARTYPE, (numpy.ndarray, awkward.array.base.AwkwardArray))

    @property
    def dtype(self):
        return numpy.dtype(object)   # specifically, subarrays

    @property
    def shape(self):
        return (len(self._starts),)

    def _offsets_is_aliased(self):
        return (isinstance(self._starts, numpy.ndarray) and isinstance(self._stops, numpy.ndarray) and
                self._starts.base is not None and self._stops.base is not None and self._starts.base is self._stops.base and
                self._starts.ctypes.data == self._starts.base.ctypes.data and
                self._stops.ctypes.data == self._stops.base.ctypes.data + self._stops.dtype.itemsize and
                len(self._starts) == len(self._starts.base) - 1 and
                len(self._stops) == len(self._stops.base) - 1)

    @property
    def offsets(self):
        if self._offsets_is_aliased():
            return self._starts.base
        elif numpy.array_equal(self._starts[1:], self.stops[:-1]):
            return numpy.append(self._starts, self.stops[-1])
        else:
            raise ValueError("starts and stops are not compatible with a single offsets array")

    @property
    def counts(self):
        return self._stops - self._starts

    @staticmethod
    def _parents(starts, stops):
        out = numpy.full(stops.max(), -1, dtype=awkward.array.base.AwkwardArray.INDEXTYPE)
        lenstarts = len(starts)
        i = 0
        while i < lenstarts:
            out[starts[i]:stops[i]] = i
            i += 1
        return out

    @property
    def parents(self):
        return self._parents(self._starts, self._stops)

    def __len__(self):                 # length is determined by starts
        return len(self._starts)       # data can grow by appending contents and stops before starts

    def _check_startsstops(self, starts=None, stops=None):
        if starts is None:
            starts = self._starts
        if stops is None:
            stops = self._stops

        if len(starts.shape) != 1:
            raise TypeError("starts must have 1-dimensional shape")
        if starts.shape[0] == 0:
            starts = starts.view(self.INDEXTYPE)
        if not issubclass(starts.dtype.type, numpy.integer):
            raise TypeError("starts must have integer dtype")

        if len(stops.shape) != 1:
            raise TypeError("stops must have 1-dimensional shape")
        if stops.shape[0] == 0:
            stops = stops.view(self.INDEXTYPE)
        if not issubclass(stops.dtype.type, numpy.integer):
            raise TypeError("stops must have integer dtype")

        if len(starts) > len(stops):
            raise ValueError("starts must be have as many or fewer elements as stops")

    def __getitem__(self, where):
        if self._isstring(where):
            return JaggedArray(self._starts, self._stops, self._content[where])

        if not isinstance(where, tuple):
            where = (where,)
        head, tail = where[0], where[1:]

        self._check_startsstops()
        starts = self._starts[head]
        stops = self._stops[head]

        if len(starts.shape) == len(stops.shape) == 0:
            return self.content[self._singleton((slice(starts, stops),) + tail)]
        else:
            return JaggedArray(starts, stops, self._content[self._singleton((slice(None),) + tail)])

    def tojagged(self, starts=None, stops=None, copy=True):
        if starts is None and stops is None:
            if copy:
                starts, stops = self._starts.copy(), self._stops.copy()
            else:
                starts, stops = self._starts, self._stops

        elif stops is None:
            starts = self._toarray(starts, self.INDEXTYPE, (numpy.ndarray, awkward.array.base.AwkwardArray))
            if len(self) != len(starts):
                raise IndexError("cannot fit JaggedArray of length {0} into starts of length {1}".format(len(self), len(starts)))

            stops = starts + self.counts

            if (stops[:-1] > starts[1:]).any():
                raise IndexError("cannot fit contents of JaggedArray into the given starts array")

        elif starts is None:
            stops = self._toarray(stops, self.INDEXTYPE, (numpy.ndarray, awkward.array.base.AwkwardArray))
            if len(self) != len(stops):
                raise IndexError("cannot fit JaggedArray of length {0} into stops of length {1}".format(len(self), len(stops)))

            starts = stops - self.counts

            if (stops[:-1] > starts[1:]).any():
                raise IndexError("cannot fit contents of JaggedArray into the given stops array")

        else:
            if not numpy.array_equal(stops - starts, self.counts):
                raise IndexError("cannot fit contents of JaggedArray into the given starts and stops arrays")

        if not copy and starts is self._starts and stops is self._stops:
            return self

        elif (starts is self._starts or numpy.array_equal(starts, self._starts)) and (stops is self._stops or numpy.array_equal(stops, self._stops)):
            if copy:
                return JaggedArray(starts, stops, self._content.copy())
            else:
                return JaggedArray(starts, stops, self._content)

        else:
            selfstarts, selfstops, selfcontent = self._starts, self._stops, self._content
            content = numpy.empty(stops.max(), dtype=selfcontent.dtype)
            
            lenstarts = len(starts)
            i = 0
            while i < lenstarts:
                content[starts[i]:stops[i]] = selfcontent[selfstarts[i]:selfstops[i]]
                i += 1
            
            return JaggedArray(starts, stops, content)

    def makecompatible(self, data):
        data = self._toarray(data, self._content.dtype, (numpy.ndarray, awkward.array.base.AwkwardArray))
        parents = self.parents
        good = (parents >= 0)
        content = numpy.empty(len(parents), dtype=data.dtype)
        if len(data.shape) == 0:
            content[good] = data
        else:
            content[good] = data[parents[good]]
        return JaggedArray(self._starts, self._stops, content)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        if method != "__call__":
            return NotImplemented

        inputs = list(inputs)
        starts, stops = None, None

        for i in range(len(inputs)):
            if isinstance(inputs[i], (numbers.Number, numpy.number)):
                pass

            elif isinstance(inputs[i], JaggedArray):
                if starts is stops is None:
                    inputs[i] = inputs[i].tojagged(copy=False)
                    starts, stops = inputs[i].starts, inputs[i].stops
                else:
                    inputs[i] = inputs[i].tojagged(starts, stops)

            else:
                inputs[i] = numpy.array(inputs[i], copy=False)

        for jaggedarray in inputs:
            if isinstance(jaggedarray, JaggedArray):
                starts, stops, parents, good = jaggedarray._starts, jaggedarray._stops, None, None
                break
        else:
            assert False

        for i in range(len(inputs)):
            if isinstance(inputs[i], numpy.ndarray):
                data = self._toarray(inputs[i], inputs[i].dtype, (numpy.ndarray, awkward.array.base.AwkwardArray))
                if parents is None:
                    parents = jaggedarray.parents
                    good = (parents >= 0)

                content = numpy.empty(len(parents), dtype=data.dtype)
                if len(data.shape) == 0:
                    content[good] = data
                else:
                    content[good] = data[parents[good]]
                inputs[i] = JaggedArray(starts, stops, content)

        for i in range(len(inputs)):
            if isinstance(inputs[i], JaggedArray):
                if good is None:
                    inputs[i] = inputs[i].content
                else:
                    inputs[i] = inputs[i].content[good]

        result = getattr(ufunc, method)(*inputs, **kwargs)

        if isinstance(result, tuple):
            return tuple(JaggedArray(starts, stops, x) for x in result)
        elif method == "at":
            return None
        else:
            return JaggedArray(starts, stops, result)

    def argproduct(self, other):
        import awkward.array.table 

        if not isinstance(other, JaggedArray):
            raise ValueError("other array must be a JaggedArray")
        
        if len(self._starts) != len(other):
            raise ValueError("other array is not compatible")
        
        selfcounts = self._stops - self._starts
        othercounts = other._stops - other._starts
        
        offsets = numpy.empty(len(self._starts) + 1, dtype=self.INDEXTYPE)
        offsets[0] = 0
        offsets[1:] = numpy.cumsum(selfcounts * othercounts, dtype=self.INDEXTYPE)

        indexes = numpy.arange(offsets[-1], dtype=self.INDEXTYPE)
        parents = self._parents(offsets[:-1], offsets[1:])
        parents = parents.astype(self.INDEXTYPE)

        left = numpy.empty_like(indexes)
        right = numpy.empty_like(indexes)

        left[indexes] = self._starts[parents[indexes]] + ((indexes - offsets[parents[indexes]]) // othercounts[parents[indexes]])
        right[indexes] = other._starts[parents[indexes]] + (indexes - offsets[parents[indexes]]) - othercounts[parents[indexes]] * ((indexes - offsets[parents[indexes]]) // othercounts[parents[indexes]])

        return JaggedArray(offsets[:-1], offsets[1:], awkward.array.table.Table(offsets[-1], left, right))

    def product(self, other):
        import awkward.array.table

        argproduct = self.argproduct(other)
        left, right = argproduct._content._content.values()

        return JaggedArray(argproduct.starts, argproduct.stops, awkward.array.table.Table(len(left), self._content[left], other.content[right]))

class ByteJaggedArray(JaggedArray):
    @classmethod
    def fromoffsets(cls, offsets, content, dtype):
        return cls(offsets[:-1], offsets[1:], content, dtype)

    @classmethod
    def fromiter(cls, iterable):
        offsets = [0]
        content = []
        for x in iterable:
            offsets.append(offsets[-1] + len(x))
            content.extend(x)
        offsets = numpy.array(offsets, dtype=ByteJaggedArray.INDEXTYPE)
        content = numpy.array(content)
        offsets *= content.dtype.itemsize
        return cls(offsets[:-1], offsets[1:], content, content.dtype)

    def __init__(self, starts, stops, content, dtype=awkward.array.base.AwkwardArray.CHARTYPE):
        super(ByteJaggedArray, self).__init__(starts, stops, content)
        self.dtype = dtype

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = self._toarray(value, self.CHARTYPE, numpy.ndarray).view(self.CHARTYPE).reshape(-1)

    @property
    def dtype(self):
        return self._dtype

    @dtype.setter
    def dtype(self, value):
        self._dtype = numpy.dtype(value)

    def __getitem__(self, where):
        if self._isstring(where):
            return ByteJaggedArray(self._starts, self._stops, self._content[where], self._dtype)

        if not isinstance(where, tuple):
            where = (where,)
        head, tail = where[0], where[1:]

        self._check_startsstops()
        starts = self._starts[head]
        stops = self._stops[head]

        if len(starts.shape) == len(stops.shape) == 0:
            return self._content[self._singleton((slice(starts, stops),) + tail)].view(self._dtype)
        else:
            return ByteJaggedArray(starts, stops, self._content[self._singleton((slice(None),) + tail)], self._dtype)

    def tojagged(self, starts=None, stops=None, copy=True):
        counts = self.counts

        if starts is None and stops is None:
            offsets = numpy.empty(len(self) + 1, dtype=self.INDEXTYPE)
            offsets[0] = 0
            numpy.cumsum(counts // self.dtype.itemsize, out=offsets[1:])
            starts, stops = offsets[:-1], offsets[1:]
            
        elif stops is None:
            starts = self._toarray(starts, self.INDEXTYPE, (numpy.ndarray, awkward.array.base.AwkwardArray))
            if len(self) != len(starts):
                raise IndexError("cannot fit ByteJaggedArray of length {0} into starts of length {1}".format(len(self), len(starts)))

            stops = starts + (counts // self.dtype.itemsize)

            if (stops[:-1] > starts[1:]).any():
                raise IndexError("cannot fit contents of ByteJaggedArray into the given starts array")

        elif starts is None:
            stops = self._toarray(stops, self.INDEXTYPE, (numpy.ndarray, awkward.array.base.AwkwardArray))
            if len(self) != len(stops):
                raise IndexError("cannot fit ByteJaggedArray of length {0} into stops of length {1}".format(len(self), len(stops)))

            starts = stops - (counts // self.dtype.itemsize)

            if (stops[:-1] > starts[1:]).any():
                raise IndexError("cannot fit contents of ByteJaggedArray into the given stops array")

        else:
            if not numpy.array_equal(stops - starts, counts):
                raise IndexError("cannot fit contents of ByteJaggedArray into the given starts and stops arrays")

        self._check_startsstops(starts, stops)

        selfstarts, selfstops, selfcontent, selfdtype = self._starts, self._stops, self._content, self._dtype
        content = numpy.empty(counts.sum() // selfdtype.itemsize, dtype=selfdtype)

        lenstarts = len(starts)
        i = 0
        while i < lenstarts:
            content[starts[i]:stops[i]] = selfcontent[selfstarts[i]:selfstops[i]].view(selfdtype)
            i += 1

        return JaggedArray(starts, stops, content)
