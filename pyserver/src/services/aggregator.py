#!/usr/bin/env python

from src.models.bookmark import Bookmark
from src.repository.bookmarkRepository import BookmarkRepository
from src.services.system import SystemService

import psutil


class AggregatorService:

    def getHardwareStatus():
        cpu = {
            'usage_percent': psutil.cpu_percent(),
            'temp': SystemService.get_cpu_temp()
        }
        return {
            'cpu': cpu,
            'memory': SystemService.get_virtual_memory(),
            'disk': SystemService.get_disk(),
            'network': SystemService.get_network()
        }

    def getBookmarks(database) -> list:
        try:
            bookmarks = []
            repository = BookmarkRepository(database)
            for b in repository.get_all_bookmarks():
                bookmarks.append(Bookmark(b[1], b[2], b[3]))
            return bookmarks
        except Exception as e:
            raise e
        finally:
            repository.close()
