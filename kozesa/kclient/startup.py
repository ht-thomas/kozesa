import sys
import builtins
from pathlib import Path
from kivy.resources import resource_add_path

mainpath = Path(__file__).parent
sys.path.append(str(mainpath))
resource_add_path(str(mainpath/"resources"))

from entrypoint import KozesaApp
KozesaApp().run()