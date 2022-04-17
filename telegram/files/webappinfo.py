#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2022
# Leandro Toledo de Souza <devs@python-telegram-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
"""This module contains an object that represents a Telegram Venue."""

from typing import TYPE_CHECKING, Any, Optional

from telegram import Location, TelegramObject
from telegram.utils.types import JSONDict

if TYPE_CHECKING:
    from telegram import Bot


class WebAppInfo(TelegramObject):
    """This object represents a WebAppInfo.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`url` and :attr:`url` are equal.

    Note:
      Foursquare details and Google Pace details are mutually exclusive. However, this
      behaviour is undocumented and might be changed by Telegram.

    Args:
        url (:obj:`str`): An HTTPS URL of a Web App to be opened.
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        url (:obj:`str`): An HTTPS URL of a Web App to be opened.

    """

    __slots__ = (
        'url'
    )

    def __init__(
        self,
        url: str,
        **_kwargs: Any,
    ):
        # Required
        self.url = url


    @classmethod
    def de_json(cls, data: Optional[JSONDict], bot: 'Bot') -> Optional['WebAppInfo']:
        """See :meth:`telegram.TelegramObject.de_json`."""
        data = cls._parse_data(data)

        if not data:
            return None

        data['url'] = Location.de_json(data.get('url'), bot)

        return cls(**data)
