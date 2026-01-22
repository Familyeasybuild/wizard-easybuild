from resources.lib.modules._service import Startup

from resources.lib.modules.whitelist import create_whitelist
from resources.lib.modules.quick_whitelist import ContextMenu

if __name__ == '__main__':
    create_whitelist()
    s = Startup()
    s.run_startup()
    ContextMenu()
