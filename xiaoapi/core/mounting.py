"""
官方文档——静态文件：https://fastapi.tiangolo.com/tutorial/static-files/
"""

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles  # 依赖安装：pip install aiofiles

from ..conf import settings


def register_mounting(app: FastAPI):
    """
    挂载文件目录，并添加路由访问，此路由不会在接口文档中显示
    """

    app.mount(settings.DOCS_URL, app=StaticFiles(directory=settings.DOCS_ROOT))

    if settings.STATIC_ENABLE:
        app.mount(settings.STATIC_URL, app=StaticFiles(directory=settings.STATIC_ROOT))

    if settings.MEDIA_ENABLE:
        app.mount(settings.MEDIA_URL, app=StaticFiles(directory=settings.MEDIA_ROOT))
