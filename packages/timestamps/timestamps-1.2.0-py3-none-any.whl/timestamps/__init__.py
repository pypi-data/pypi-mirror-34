import datetime, time


class Timestamp:
	def __init__(self, value=None, *, _hex=None, _float=None, _datetime=None, nanosecond=False):
		"""Initialize a timestamp with a float, an hex value or a datetime object.
		You can initialize the object either by using _float, _hex or _datetime.
		You can also provide a value, which will be guessed after its type.
		If the object specified is a Timestamp, this will make a full copy of it, with its parameters.
		If `nanosecond` is evaluated to True, the number will be multiplied by 10^9 instead of 10^7 (by default)"""
		argc = sum(x is not None for x in (value, _float, _datetime, _hex))
		if argc != 1:
			raise ValueError('Incorrect amount of parameters provided (expected 1, got %s)' % argc)

		if value is not None:
			if isinstance(value, float):
				_float, value = value, None
			elif isinstance(value, bytes):
				_hex, value = value.decode(), None
			elif isinstance(value, str):
				_hex, value = value, None
			elif isinstance(value, datetime.datetime):
				_datetime, value = value, None
			elif isinstance(value, Timestamp):
				_float, value = value._float, None
			else:
				raise TypeError('Incorrect type', type(value))

		# This should never be True
		if value is not None:
			raise RuntimeError('Unhandled Error')

		self._multiply_by = 10**9 if nanosecond else 10**7
		self._float = None

		if _hex is not None:
			_hex = _hex.lower() \
				.strip() \
				.lstrip('0x') \
				.lstrip('#')
			value = int(_hex, 16)
			self._float = value / self._multiply_by
		elif _float is not None:
			self._float = _float
		elif _datetime is not None:
			self._float = _datetime.timestamp()

		if self._float is None:
			raise RuntimeError('Unhandled Error')

		if self._float < 0:
			raise ValueError('Timestamp should not be negative')

	@classmethod
	def from_float(cls, value):
		return cls(_float=value)

	@classmethod
	def from_hex(cls, value):
		return cls(_hex=value)

	@classmethod
	def from_datetime(cls, value):
		return cls(_datetime=value)

	@classmethod
	def now(cls):
		return cls.from_float(time.time())

	def cmp(self, other):
		if not isinstance(other, self.__class__):
			other = self.__class__(other)
		return (self._float > other._float) - (self._float < other._float)

	def __lt__(self, other):
		return self.cmp(other) < 0

	def __le__(self, other):
		return self.cmp(other) <= 0

	def __ne__(self, other):
		return self.cmp(other) != 0

	def __eq__(self, other):
		return self.cmp(other) == 0

	def __gt__(self, other):
		return self.cmp(other) > 0

	def __ge__(self, other):
		return self.cmp(other) >= 0

