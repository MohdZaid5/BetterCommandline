
from typing import Any, Optional, Tuple, Union

from Source.Colors import ANSI, Colored, Colors


class Text:
    """
    Class representing styled text with customizable foreground color and style.

    `Parameters`:
    - `foreground`: `Foreground` color of the text, specified as either an RGB `tuple` or a `hexadecimal` color code.
    - `style`: `Optional` text style for the text, e.g., bold, italics.

    `Example`:
    ```
    Highlighter = Text( Colors.ORANGE, ANSI.BOLD)
    print( Highlighter("Hello World!") )
    ```

    `Methods`:
    - `__call__`: Format and return the styled text by concatenating multiple parts with an optional separator.

    `Attributes`:
    - `foreground`: The formatted `ANSI` escape code for the foreground color.
    - `style`: The formatted `ANSI` escape code for the text style.
    """

    def __init__(self, foreground:Union[Tuple[int],str], style:Optional[str]=None) -> None:
        """
        Initialize a `Text` instance with the provided foreground color and style.

        If the provided foreground is not an ANSI escape code, it uses the `Colored` class to generate one.

        `Parameters`:
        - `foreground`: `Foreground` color of the text, specified as either an RGB `tuple` or a `hexadecimal` color code.
        - `style`: `Optional` text style for the text, e.g., bold, italics.
        """

        if not isinstance( foreground, str ) or not foreground.startswith('\033'):
            foreground:str = Colored.Foreground( foreground )

        self.foreground :str = foreground
        self.style      :str = style if not style==None else ''
    
    def __call__(self, *parts: str, sep=' ') -> str:
        """
        Format and return the styled text by concatenating multiple parts with an optional separator.

        `Parameters`:
        - `*parts`: Variable string parts to be concatenated.
        - `sep`: Separator to be used between the parts. Defaults to a space.

        `Returns`:
        - The formatted styled text.
        """
        return f'{self.foreground}{self.style}{sep.join( parts )}{ANSI.RESET}'
