
from typing import Optional, Union, Tuple, TypeVar
from Source.Colors import ANSI, Colors, Colored

chr = TypeVar('chr', bound=str)

class Alias:

    """
    Class representing an alias with customizable formatting.

    `Parameters`:
    - `text`        : The main text content of the alias.
    - `foreground`  : `Foreground` color of the alias, specified as either an RGB `tuple` or a `hexadecimal` color code.
    - `background`  : `Background` color of the alias, specified as either an RGB `tuple` or a `hexadecimal` color code.
    - `banner_width`: `Optional` width for the banner. If not provided, the width will be determined by the length of the text.
    - `style`       : `Optional` text style for the alias, e.g., bold, italics.
    - `badge_sign`  : `Optional` character to represent a badge within the alias.


    `Properties`:
    - `Banner`  : Returns the formatted banner with foreground and background colors, text style, and badge.
    - `Bare`    : Returns the formatted alias without foreground and background colors, only including text and style.
    - `Badge`   : Returns the formatted badge with foreground and background colors, text style, and badge.

    `Example`:
    ```
        alias = Alias("Example", (255, 0, 0), "#00FF00", banner_width=20, style=ANSI.BOLD, badge_sign="*")
    ```
    """

    def __init__(self, text:str, foreground:Union[Tuple[int],str], background:Union[Tuple[int],str],
                banner_width:Optional[int]=None, style:Optional[str]=None, badge_sign:chr=' ') -> None:
        """
        Initialize an `Alias` instance with the provided parameters.

        If the provided `foreground` or `background` is not an ANSI escape code, it uses the `Colored` class to generate one.

        `Parameters`:
        - `text`            : The main text content of the alias.
        - `foreground`      : `Foreground` color of the alias, specified as either an RGB `tuple` or a `hexadecimal` color code.
        - `background`      : `Background` color of the alias, specified as either an RGB `tuple` or a `hexadecimal` color code.
        - `banner_width`    : `Optional` width for the banner. If not provided, the width will be determined by the length of the text.
        - `style`           : `Optional` text style for the alias, e.g., bold, italics.
        - `badge_sign`      : `Optional` character to represent a badge within the alias.
        """

        if not isinstance( foreground, str ) or not foreground.startswith('\033'):
            foreground:str = Colored.Foreground( foreground )
        if not isinstance( background, str ) or not background.startswith('\033'):
            background:str = Colored.Background( background )
        
        self.text        :str = text
        self.text_style  :str = style if not style==None else ''
        self.badge_sign  :chr = badge_sign if len(badge_sign)==1 else badge_sign[0]
        self.foreground  :str = foreground
        self.background  :str = background
        self.banner_width:int = banner_width-2 if not banner_width==None else 0
    
    @property
    def Banner(self) -> str:
        return f'{self.foreground}{self.background}{self.text_style}[{ self.text.center( self.banner_width ) }]{ANSI.RESET}'
    
    @property
    def Bare(self)->str:
        return f'{self.text_style}[{self.text.center( self.banner_width )}]'
    
    @property
    def Badge(self)->str:
        return f'{self.foreground}{self.background}{self.text_style}[{self.badge_sign}]{ANSI.RESET}'


