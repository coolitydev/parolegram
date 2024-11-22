from aiogram import Router

from .command import router as command_router
from .menu import router as menu_router
from .generator import router as generator_router

router = Router(name="main")
router.include_routers(
    command_router,
    menu_router,
    generator_router
)
