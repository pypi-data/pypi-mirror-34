#!/usr/bin/env python3
#******************************************************************************
# Copyright (C) 2018 Thomas "Cakeisalie5" Touhey <thomas@touhey.fr>
# This file is part of the textoutpc project, which is MIT-licensed.
#******************************************************************************

from ..tags import TextoutBlockTag as _TextoutBlockTag
import re as _re
import urllib.parse as _urlparse
from html import escape as _htmlescape

__all__ = ["TextoutVideoTag"]

_hexcode = _re.compile('[a-zA-Z0-9_]+')
_numcode = _re.compile('^/[0-9]+$')
_dailypath = _re.compile('^/video/([a-z0-9]+)$')

class TextoutVideoTag(_TextoutBlockTag):
	""" The video tag, puts a preview of the video whose URL is given.
		Only a few 'big' services are supported for now.
		Example uses:
		
		[video]video_url[/video]
		[video tiny]video_url[/video tiny]
		[video]https://www.youtube.com/watch?v=yhXpV8hRKxQ[/video]
	"""

	aliases = ('[video]', '[video tiny]')
	raw = True

	def prepare(self, name, value):
		""" Prepare the video tag. """

		self._sizeclass = "video-tiny" if "tiny" in name \
			else "video-medium"
		self._center = False

	def _getvideo(self, url):
		""" Try to get the video type for preprocessing. """

		url = _urlparse.urlparse(url)
		if not url.scheme in ('http', 'https'):
			raise Exception

		if   url.netloc == "youtu.be":
			self._id = url.path[1:]
			if not _hexcode.match(self._id):
				raise Exception
			self._type = "youtube"
		elif url.netloc in ('youtube.com', 'www.youtube.com'):
			if url.path != '/watch':
				raise Exception
			self._id = _urlparse.parse_qs(url.query)['v'][0]
			if not _hexcode.fullmatch(self._id):
				raise Exception
			self._type = "youtube"
		elif url.netloc in ('dailymotion.com', 'www.dailymotion.com'):
			self._code = _dailypath.match(url.path).groups()[0]
			self._type = "dailymotion"
		elif url.netloc in ('vimeo.com', 'www.vimeo.com'):
			self._code = url.path[1:]
			if not _numcode.match(self._code):
				raise Exception
			self._type = "vimeo"
		else:
			raise Exception

	def preprocess(self, content):
		self._url = content

		try:
			self._getvideo(content)
		except:
			url = _urlparse.urlparse(content)
			if not url.scheme in ('http', 'https'):
				raise Exception("No allowed prefix!")
			self._type = None

	def content_html(self):
		""" Produce the embed code for the given type. """

		if not self._type:
			url = _htmlescape(self._url)
			return '<p><a href="{}">{}</a></p>'.format(url, url)

		code = '<div class="video-wrapper {}{}">'.format(self._sizeclass,
			" video-center" if self._center else "")

		if   self._type == "youtube":
			code += '<iframe ' \
				'src="https://www.youtube.com/embed/{}" frameborder="0" ' \
				'allowfullscreen></iframe>'.format(self._id)
		elif self._type == "dailymotion":
			code += '<iframe frameborder="0" ' \
				'src="https://www.dailymotion.com/embed/video/{}">' \
				'</iframe>'.format(self._code)
		elif self._type == "vimeo":
			code += '<iframe src="https://player.vimeo.com/video/{}' \
				'?title=0&byline=0&portrait=0" frameborder="0" ' \
				'webkitAllowFullScreen allowFullScreen>' \
				'</iframe>'.format(self._code)

		return code + '</div>'

	def content_lightscript(self):
		url = self._url.replace('[', '%5B').replace(']', '%5D')
		return '[[image:{}]]'.format(url)

# End of file.
