"""
Demonstrate differences between default logger handler and one that does
implement soft-wrapping.
"""
import logging
from rich.console import Console
from rich.logging import RichHandler
from rich._log_render import FluidLogRender

handler_default = RichHandler(
    console=Console(
        force_terminal=True,
        width=50,
    )
)
handler_fluid = RichHandler(
    console=Console(
        force_terminal=True,
        width=50,
        soft_wrap=True,  # <-- This is required for fluid to work
    )
)
# Changing internal as constructor does not allow custom renderer
handler_fluid._log_render = FluidLogRender(
    show_time=True, show_level=True, show_path=True
)

logging.basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[handler_default, handler_fluid],
)
log = logging.getLogger("rich")

msg = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod "
    "tempor incididunt ut labore et dolore magna aliqua."
)
log.warning(msg)
