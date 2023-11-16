from .Text import Text

from typing import Tuple
from datetime import datetime

class Utility:

    def date( date:datetime, color:Tuple[int] ) ->str:
        return Text( foreground=color )( str(date) )
    