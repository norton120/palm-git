from pathlib import Path
from palm.plugins.base import BasePlugin
import pkg_resources

def get_version():
    try:
        version = pkg_resources.require("palm-git")[0].version
    except pkg_resources.DistributionNotFound:
        version = 'unknown'
    return version


GitPlugin = BasePlugin(
    name = 'git', 
    command_dir = Path(__file__).parent / 'commands',
    version = get_version(),
)