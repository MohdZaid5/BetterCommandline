
from typing import Any, Tuple, Union


class ANSI:
    FOREGROUND  :str = '\033[38;2;{};{};{}m'
    BACKGROUND  :str = '\033[48;2;{};{};{}m'
    BOLD        :str = '\033[1m'
    ITALICS     :str = '\033[3m'
    UNDERLINED  :str = '\033[4m'
    INVERSE     :str = '\033[7m'
    BLINK       :str = '\033[5m'
    HIDDEN      :str = '\033[8m'
    RESET       :str = '\033[0;0m'


class Colored:
    """
    Utility class for generating `ANSI` escape codes for text color formatting.

    Usage:
    - Call the `Foreground` or `Background` methods to generate `ANSI` escape codes for text color formatting.

    Example:
    ```
        foreground: str = `Colored.Foreground((r, g, b))`
        background: str = `Colored.Background("#RRGGBB")`
    ```
    """

    @staticmethod
    def Foreground(color: Union[Tuple[int, int, int], str]) -> str:
        """
        Generate `ANSI` escape code for foreground color.

        `Parameters`:
        - `color`: Either an RGB `tuple (int, int, int)` or a hexadecimal color code `str` starting with `'#'`.

        `Returns`:
        - `ANSI` escape code for setting the foreground color.
        """
        if isinstance(color, tuple):
            return ANSI.FOREGROUND.format(*color)
        elif isinstance(color, str):
            color = color.lstrip('#')
            return ANSI.FOREGROUND.format(*[int(color[i:i+2], 16) for i in (0, 2, 4)])
        else:
            raise NotImplementedError(f'Colored.Foreground does not support {type(color)} for color')

    @staticmethod
    def Background(color: Union[Tuple[int, int, int], str]) -> str:
        """
        Generate `ANSI` escape code for background color.

        `Parameters`:
        - `color`: Either an RGB `tuple (int, int, int)` or a hexadecimal color code `str` starting with `'#'`.

        `Returns`:
        - `ANSI` escape code for setting the background color.
        """
        if isinstance(color, tuple):
            return ANSI.BACKGROUND.format(*color)
        elif isinstance(color, str):
            color = color.lstrip('#')
            return ANSI.BACKGROUND.format(*[int(color[i:i+2], 16) for i in (0, 2, 4)])
        else:
            raise NotImplementedError(f'Colored.Background does not support {type(color)} for color')
class Colors:
    
    '''
    Predefined RGB colors for convenience.
    '''

    ALICEBLUE            :Tuple[int,int,int] = (240, 248, 255)
    ANTIQUEWHITE         :Tuple[int,int,int] = (250, 235, 215)
    ANTIQUEWHITE1        :Tuple[int,int,int] = (255, 239, 219)
    ANTIQUEWHITE2        :Tuple[int,int,int] = (238, 223, 204)
    ANTIQUEWHITE3        :Tuple[int,int,int] = (205, 192, 176)
    ANTIQUEWHITE4        :Tuple[int,int,int] = (139, 131, 120)
    AQUA                 :Tuple[int,int,int] = (  0, 255, 255)
    AQUAMARINE1          :Tuple[int,int,int] = (127, 255, 212)
    AQUAMARINE2          :Tuple[int,int,int] = (118, 238, 198)
    AQUAMARINE3          :Tuple[int,int,int] = (102, 205, 170)
    AQUAMARINE4          :Tuple[int,int,int] = ( 69, 139, 116)
    AZURE1               :Tuple[int,int,int] = (240, 255, 255)
    AZURE2               :Tuple[int,int,int] = (224, 238, 238)
    AZURE3               :Tuple[int,int,int] = (193, 205, 205)
    AZURE4               :Tuple[int,int,int] = (131, 139, 139)
    BANANA               :Tuple[int,int,int] = (227, 207,  87)
    BEIGE                :Tuple[int,int,int] = (245, 245, 220)
    BISQUE1              :Tuple[int,int,int] = (255, 228, 196)
    BISQUE2              :Tuple[int,int,int] = (238, 213, 183)
    BISQUE3              :Tuple[int,int,int] = (205, 183, 158)
    BISQUE4              :Tuple[int,int,int] = (139, 125, 107)
    BLACK                :Tuple[int,int,int] = (  0,   0,   0)
    BLANCHEDALMOND       :Tuple[int,int,int] = (255, 235, 205)
    BLUE                 :Tuple[int,int,int] = (  0,   0, 255)
    BLUE2                :Tuple[int,int,int] = (  0,   0, 238)
    BLUE3                :Tuple[int,int,int] = (  0,   0, 205)
    BLUE4                :Tuple[int,int,int] = (  0,   0, 139)
    BLUEVIOLET           :Tuple[int,int,int] = (138,  43, 226)
    BRICK                :Tuple[int,int,int] = (156, 102,  31)
    BROWN                :Tuple[int,int,int] = (165,  42,  42)
    BROWN1               :Tuple[int,int,int] = (255,  64,  64)
    BROWN2               :Tuple[int,int,int] = (238,  59,  59)
    BROWN3               :Tuple[int,int,int] = (205,  51,  51)
    BROWN4               :Tuple[int,int,int] = (139,  35,  35)
    BURLYWOOD            :Tuple[int,int,int] = (222, 184, 135)
    BURLYWOOD1           :Tuple[int,int,int] = (255, 211, 155)
    BURLYWOOD2           :Tuple[int,int,int] = (238, 197, 145)
    BURLYWOOD3           :Tuple[int,int,int] = (205, 170, 125)
    BURLYWOOD4           :Tuple[int,int,int] = (139, 115,  85)
    BURNTSIENNA          :Tuple[int,int,int] = (138,  54,  15)
    BURNTUMBER           :Tuple[int,int,int] = (138,  51,  36)
    CADETBLUE            :Tuple[int,int,int] = ( 95, 158, 160)
    CADETBLUE1           :Tuple[int,int,int] = (152, 245, 255)
    CADETBLUE2           :Tuple[int,int,int] = (142, 229, 238)
    CADETBLUE3           :Tuple[int,int,int] = (122, 197, 205)
    CADETBLUE4           :Tuple[int,int,int] = ( 83, 134, 139)
    CADMIUMORANGE        :Tuple[int,int,int] = (255,  97,   3)
    CADMIUMYELLOW        :Tuple[int,int,int] = (255, 153,  18)
    CARROT               :Tuple[int,int,int] = (237, 145,  33)
    CHARTREUSE1          :Tuple[int,int,int] = (127, 255,   0)
    CHARTREUSE2          :Tuple[int,int,int] = (118, 238,   0)
    CHARTREUSE3          :Tuple[int,int,int] = (102, 205,   0)
    CHARTREUSE4          :Tuple[int,int,int] = ( 69, 139,   0)
    CHOCOLATE            :Tuple[int,int,int] = (210, 105,  30)
    CHOCOLATE1           :Tuple[int,int,int] = (255, 127,  36)
    CHOCOLATE2           :Tuple[int,int,int] = (238, 118,  33)
    CHOCOLATE3           :Tuple[int,int,int] = (205, 102,  29)
    CHOCOLATE4           :Tuple[int,int,int] = (139,  69,  19)
    COBALT               :Tuple[int,int,int] = ( 61,  89, 171)
    COBALTGREEN          :Tuple[int,int,int] = ( 61, 145,  64)
    COLDGREY             :Tuple[int,int,int] = (128, 138, 135)
    CORAL                :Tuple[int,int,int] = (255, 127,  80)
    CORAL1               :Tuple[int,int,int] = (255, 114,  86)
    CORAL2               :Tuple[int,int,int] = (238, 106,  80)
    CORAL3               :Tuple[int,int,int] = (205,  91,  69)
    CORAL4               :Tuple[int,int,int] = (139,  62,  47)
    CORNFLOWERBLUE       :Tuple[int,int,int] = (100, 149, 237)
    CORNSILK1            :Tuple[int,int,int] = (255, 248, 220)
    CORNSILK2            :Tuple[int,int,int] = (238, 232, 205)
    CORNSILK3            :Tuple[int,int,int] = (205, 200, 177)
    CORNSILK4            :Tuple[int,int,int] = (139, 136, 120)
    CRIMSON              :Tuple[int,int,int] = (220,  20,  60)
    CYAN2                :Tuple[int,int,int] = (  0, 238, 238)
    CYAN3                :Tuple[int,int,int] = (  0, 205, 205)
    CYAN4                :Tuple[int,int,int] = (  0, 139, 139)
    DARKGOLDENROD        :Tuple[int,int,int] = (184, 134,  11)
    DARKGOLDENROD1       :Tuple[int,int,int] = (255, 185,  15)
    DARKGOLDENROD2       :Tuple[int,int,int] = (238, 173,  14)
    DARKGOLDENROD3       :Tuple[int,int,int] = (205, 149,  12)
    DARKGOLDENROD4       :Tuple[int,int,int] = (139, 101,   8)
    DARKGRAY             :Tuple[int,int,int] = (169, 169, 169)
    DARKGREEN            :Tuple[int,int,int] = (  0, 100,   0)
    DARKKHAKI            :Tuple[int,int,int] = (189, 183, 107)
    DARKOLIVEGREEN       :Tuple[int,int,int] = ( 85, 107,  47)
    DARKOLIVEGREEN1      :Tuple[int,int,int] = (202, 255, 112)
    DARKOLIVEGREEN2      :Tuple[int,int,int] = (188, 238, 104)
    DARKOLIVEGREEN3      :Tuple[int,int,int] = (162, 205,  90)
    DARKOLIVEGREEN4      :Tuple[int,int,int] = (110, 139,  61)
    DARKORANGE           :Tuple[int,int,int] = (255, 140,   0)
    DARKORANGE1          :Tuple[int,int,int] = (255, 127,   0)
    DARKORANGE2          :Tuple[int,int,int] = (238, 118,   0)
    DARKORANGE3          :Tuple[int,int,int] = (205, 102,   0)
    DARKORANGE4          :Tuple[int,int,int] = (139,  69,   0)
    DARKORCHID           :Tuple[int,int,int] = (153,  50, 204)
    DARKORCHID1          :Tuple[int,int,int] = (191,  62, 255)
    DARKORCHID2          :Tuple[int,int,int] = (178,  58, 238)
    DARKORCHID3          :Tuple[int,int,int] = (154,  50, 205)
    DARKORCHID4          :Tuple[int,int,int] = (104,  34, 139)
    DARKSALMON           :Tuple[int,int,int] = (233, 150, 122)
    DARKSEAGREEN         :Tuple[int,int,int] = (143, 188, 143)
    DARKSEAGREEN1        :Tuple[int,int,int] = (193, 255, 193)
    DARKSEAGREEN2        :Tuple[int,int,int] = (180, 238, 180)
    DARKSEAGREEN3        :Tuple[int,int,int] = (155, 205, 155)
    DARKSEAGREEN4        :Tuple[int,int,int] = (105, 139, 105)
    DARKSLATEBLUE        :Tuple[int,int,int] = ( 72,  61, 139)
    DARKSLATEGRAY        :Tuple[int,int,int] = ( 47,  79,  79)
    DARKSLATEGRAY1       :Tuple[int,int,int] = (151, 255, 255)
    DARKSLATEGRAY2       :Tuple[int,int,int] = (141, 238, 238)
    DARKSLATEGRAY3       :Tuple[int,int,int] = (121, 205, 205)
    DARKSLATEGRAY4       :Tuple[int,int,int] = ( 82, 139, 139)
    DARKTURQUOISE        :Tuple[int,int,int] = (  0, 206, 209)
    DARKVIOLET           :Tuple[int,int,int] = (148,   0, 211)
    DEEPPINK1            :Tuple[int,int,int] = (255,  20, 147)
    DEEPPINK2            :Tuple[int,int,int] = (238,  18, 137)
    DEEPPINK3            :Tuple[int,int,int] = (205,  16, 118)
    DEEPPINK4            :Tuple[int,int,int] = (139,  10,  80)
    DEEPSKYBLUE1         :Tuple[int,int,int] = (  0, 191, 255)
    DEEPSKYBLUE2         :Tuple[int,int,int] = (  0, 178, 238)
    DEEPSKYBLUE3         :Tuple[int,int,int] = (  0, 154, 205)
    DEEPSKYBLUE4         :Tuple[int,int,int] = (  0, 104, 139)
    DIMGRAY              :Tuple[int,int,int] = (105, 105, 105)
    DODGERBLUE1          :Tuple[int,int,int] = ( 30, 144, 255)
    DODGERBLUE2          :Tuple[int,int,int] = ( 28, 134, 238)
    DODGERBLUE3          :Tuple[int,int,int] = ( 24, 116, 205)
    DODGERBLUE4          :Tuple[int,int,int] = ( 16,  78, 139)
    EGGSHELL             :Tuple[int,int,int] = (252, 230, 201)
    EMERALDGREEN         :Tuple[int,int,int] = (  0, 201,  87)
    FIREBRICK            :Tuple[int,int,int] = (178,  34,  34)
    FIREBRICK1           :Tuple[int,int,int] = (255,  48,  48)
    FIREBRICK2           :Tuple[int,int,int] = (238,  44,  44)
    FIREBRICK3           :Tuple[int,int,int] = (205,  38,  38)
    FIREBRICK4           :Tuple[int,int,int] = (139,  26,  26)
    FLESH                :Tuple[int,int,int] = (255, 125,  64)
    FLORALWHITE          :Tuple[int,int,int] = (255, 250, 240)
    FORESTGREEN          :Tuple[int,int,int] = ( 34, 139,  34)
    GAINSBORO            :Tuple[int,int,int] = (220, 220, 220)
    GHOSTWHITE           :Tuple[int,int,int] = (248, 248, 255)
    GOLD1                :Tuple[int,int,int] = (255, 215,   0)
    GOLD2                :Tuple[int,int,int] = (238, 201,   0)
    GOLD3                :Tuple[int,int,int] = (205, 173,   0)
    GOLD4                :Tuple[int,int,int] = (139, 117,   0)
    GOLDENROD            :Tuple[int,int,int] = (218, 165,  32)
    GOLDENROD1           :Tuple[int,int,int] = (255, 193,  37)
    GOLDENROD2           :Tuple[int,int,int] = (238, 180,  34)
    GOLDENROD3           :Tuple[int,int,int] = (205, 155,  29)
    GOLDENROD4           :Tuple[int,int,int] = (139, 105,  20)
    GRAY                 :Tuple[int,int,int] = (128, 128, 128)
    GRAY1                :Tuple[int,int,int] = (  3,   3,   3)
    GRAY10               :Tuple[int,int,int] = ( 26,  26,  26)
    GRAY11               :Tuple[int,int,int] = ( 28,  28,  28)
    GRAY12               :Tuple[int,int,int] = ( 31,  31,  31)
    GRAY13               :Tuple[int,int,int] = ( 33,  33,  33)
    GRAY14               :Tuple[int,int,int] = ( 36,  36,  36)
    GRAY15               :Tuple[int,int,int] = ( 38,  38,  38)
    GRAY16               :Tuple[int,int,int] = ( 41,  41,  41)
    GRAY17               :Tuple[int,int,int] = ( 43,  43,  43)
    GRAY18               :Tuple[int,int,int] = ( 46,  46,  46)
    GRAY19               :Tuple[int,int,int] = ( 48,  48,  48)
    GRAY2                :Tuple[int,int,int] = (  5,   5,   5)
    GRAY20               :Tuple[int,int,int] = ( 51,  51,  51)
    GRAY21               :Tuple[int,int,int] = ( 54,  54,  54)
    GRAY22               :Tuple[int,int,int] = ( 56,  56,  56)
    GRAY23               :Tuple[int,int,int] = ( 59,  59,  59)
    GRAY24               :Tuple[int,int,int] = ( 61,  61,  61)
    GRAY25               :Tuple[int,int,int] = ( 64,  64,  64)
    GRAY26               :Tuple[int,int,int] = ( 66,  66,  66)
    GRAY27               :Tuple[int,int,int] = ( 69,  69,  69)
    GRAY28               :Tuple[int,int,int] = ( 71,  71,  71)
    GRAY29               :Tuple[int,int,int] = ( 74,  74,  74)
    GRAY3                :Tuple[int,int,int] = (  8,   8,   8)
    GRAY30               :Tuple[int,int,int] = ( 77,  77,  77)
    GRAY31               :Tuple[int,int,int] = ( 79,  79,  79)
    GRAY32               :Tuple[int,int,int] = ( 82,  82,  82)
    GRAY33               :Tuple[int,int,int] = ( 84,  84,  84)
    GRAY34               :Tuple[int,int,int] = ( 87,  87,  87)
    GRAY35               :Tuple[int,int,int] = ( 89,  89,  89)
    GRAY36               :Tuple[int,int,int] = ( 92,  92,  92)
    GRAY37               :Tuple[int,int,int] = ( 94,  94,  94)
    GRAY38               :Tuple[int,int,int] = ( 97,  97,  97)
    GRAY39               :Tuple[int,int,int] = ( 99,  99,  99)
    GRAY4                :Tuple[int,int,int] = ( 10,  10,  10)
    GRAY40               :Tuple[int,int,int] = (102, 102, 102)
    GRAY42               :Tuple[int,int,int] = (107, 107, 107)
    GRAY43               :Tuple[int,int,int] = (110, 110, 110)
    GRAY44               :Tuple[int,int,int] = (112, 112, 112)
    GRAY45               :Tuple[int,int,int] = (115, 115, 115)
    GRAY46               :Tuple[int,int,int] = (117, 117, 117)
    GRAY47               :Tuple[int,int,int] = (120, 120, 120)
    GRAY48               :Tuple[int,int,int] = (122, 122, 122)
    GRAY49               :Tuple[int,int,int] = (125, 125, 125)
    GRAY5                :Tuple[int,int,int] = ( 13,  13,  13)
    GRAY50               :Tuple[int,int,int] = (127, 127, 127)
    GRAY51               :Tuple[int,int,int] = (130, 130, 130)
    GRAY52               :Tuple[int,int,int] = (133, 133, 133)
    GRAY53               :Tuple[int,int,int] = (135, 135, 135)
    GRAY54               :Tuple[int,int,int] = (138, 138, 138)
    GRAY55               :Tuple[int,int,int] = (140, 140, 140)
    GRAY56               :Tuple[int,int,int] = (143, 143, 143)
    GRAY57               :Tuple[int,int,int] = (145, 145, 145)
    GRAY58               :Tuple[int,int,int] = (148, 148, 148)
    GRAY59               :Tuple[int,int,int] = (150, 150, 150)
    GRAY6                :Tuple[int,int,int] = ( 15,  15,  15)
    GRAY60               :Tuple[int,int,int] = (153, 153, 153)
    GRAY61               :Tuple[int,int,int] = (156, 156, 156)
    GRAY62               :Tuple[int,int,int] = (158, 158, 158)
    GRAY63               :Tuple[int,int,int] = (161, 161, 161)
    GRAY64               :Tuple[int,int,int] = (163, 163, 163)
    GRAY65               :Tuple[int,int,int] = (166, 166, 166)
    GRAY66               :Tuple[int,int,int] = (168, 168, 168)
    GRAY67               :Tuple[int,int,int] = (171, 171, 171)
    GRAY68               :Tuple[int,int,int] = (173, 173, 173)
    GRAY69               :Tuple[int,int,int] = (176, 176, 176)
    GRAY7                :Tuple[int,int,int] = ( 18,  18,  18)
    GRAY70               :Tuple[int,int,int] = (179, 179, 179)
    GRAY71               :Tuple[int,int,int] = (181, 181, 181)
    GRAY72               :Tuple[int,int,int] = (184, 184, 184)
    GRAY73               :Tuple[int,int,int] = (186, 186, 186)
    GRAY74               :Tuple[int,int,int] = (189, 189, 189)
    GRAY75               :Tuple[int,int,int] = (191, 191, 191)
    GRAY76               :Tuple[int,int,int] = (194, 194, 194)
    GRAY77               :Tuple[int,int,int] = (196, 196, 196)
    GRAY78               :Tuple[int,int,int] = (199, 199, 199)
    GRAY79               :Tuple[int,int,int] = (201, 201, 201)
    GRAY8                :Tuple[int,int,int] = ( 20,  20,  20)
    GRAY80               :Tuple[int,int,int] = (204, 204, 204)
    GRAY81               :Tuple[int,int,int] = (207, 207, 207)
    GRAY82               :Tuple[int,int,int] = (209, 209, 209)
    GRAY83               :Tuple[int,int,int] = (212, 212, 212)
    GRAY84               :Tuple[int,int,int] = (214, 214, 214)
    GRAY85               :Tuple[int,int,int] = (217, 217, 217)
    GRAY86               :Tuple[int,int,int] = (219, 219, 219)
    GRAY87               :Tuple[int,int,int] = (222, 222, 222)
    GRAY88               :Tuple[int,int,int] = (224, 224, 224)
    GRAY89               :Tuple[int,int,int] = (227, 227, 227)
    GRAY9                :Tuple[int,int,int] = ( 23,  23,  23)
    GRAY90               :Tuple[int,int,int] = (229, 229, 229)
    GRAY91               :Tuple[int,int,int] = (232, 232, 232)
    GRAY92               :Tuple[int,int,int] = (235, 235, 235)
    GRAY93               :Tuple[int,int,int] = (237, 237, 237)
    GRAY94               :Tuple[int,int,int] = (240, 240, 240)
    GRAY95               :Tuple[int,int,int] = (242, 242, 242)
    GRAY97               :Tuple[int,int,int] = (247, 247, 247)
    GRAY98               :Tuple[int,int,int] = (250, 250, 250)
    GRAY99               :Tuple[int,int,int] = (252, 252, 252)
    GREEN                :Tuple[int,int,int] = (  0, 128,   0)
    GREEN1               :Tuple[int,int,int] = (  0, 255,   0)
    GREEN2               :Tuple[int,int,int] = (  0, 238,   0)
    GREEN3               :Tuple[int,int,int] = (  0, 205,   0)
    GREEN4               :Tuple[int,int,int] = (  0, 139,   0)
    GREENYELLOW          :Tuple[int,int,int] = (173, 255,  47)
    HONEYDEW1            :Tuple[int,int,int] = (240, 255, 240)
    HONEYDEW2            :Tuple[int,int,int] = (224, 238, 224)
    HONEYDEW3            :Tuple[int,int,int] = (193, 205, 193)
    HONEYDEW4            :Tuple[int,int,int] = (131, 139, 131)
    HOTPINK              :Tuple[int,int,int] = (255, 105, 180)
    HOTPINK1             :Tuple[int,int,int] = (255, 110, 180)
    HOTPINK2             :Tuple[int,int,int] = (238, 106, 167)
    HOTPINK3             :Tuple[int,int,int] = (205,  96, 144)
    HOTPINK4             :Tuple[int,int,int] = (139,  58,  98)
    INDIANRED            :Tuple[int,int,int] = (176,  23,  31)
    INDIANRED            :Tuple[int,int,int] = (205,  92,  92)
    INDIANRED1           :Tuple[int,int,int] = (255, 106, 106)
    INDIANRED2           :Tuple[int,int,int] = (238,  99,  99)
    INDIANRED3           :Tuple[int,int,int] = (205,  85,  85)
    INDIANRED4           :Tuple[int,int,int] = (139,  58,  58)
    INDIGO               :Tuple[int,int,int] = ( 75,   0, 130)
    IVORY1               :Tuple[int,int,int] = (255, 255, 240)
    IVORY2               :Tuple[int,int,int] = (238, 238, 224)
    IVORY3               :Tuple[int,int,int] = (205, 205, 193)
    IVORY4               :Tuple[int,int,int] = (139, 139, 131)
    IVORYBLACK           :Tuple[int,int,int] = ( 41,  36,  33)
    KHAKI                :Tuple[int,int,int] = (240, 230, 140)
    KHAKI1               :Tuple[int,int,int] = (255, 246, 143)
    KHAKI2               :Tuple[int,int,int] = (238, 230, 133)
    KHAKI3               :Tuple[int,int,int] = (205, 198, 115)
    KHAKI4               :Tuple[int,int,int] = (139, 134,  78)
    LAVENDER             :Tuple[int,int,int] = (230, 230, 250)
    LAVENDERBLUSH1       :Tuple[int,int,int] = (255, 240, 245)
    LAVENDERBLUSH2       :Tuple[int,int,int] = (238, 224, 229)
    LAVENDERBLUSH3       :Tuple[int,int,int] = (205, 193, 197)
    LAVENDERBLUSH4       :Tuple[int,int,int] = (139, 131, 134)
    LAWNGREEN            :Tuple[int,int,int] = (124, 252,   0)
    LEMONCHIFFON1        :Tuple[int,int,int] = (255, 250, 205)
    LEMONCHIFFON2        :Tuple[int,int,int] = (238, 233, 191)
    LEMONCHIFFON3        :Tuple[int,int,int] = (205, 201, 165)
    LEMONCHIFFON4        :Tuple[int,int,int] = (139, 137, 112)
    LIGHTBLUE            :Tuple[int,int,int] = (173, 216, 230)
    LIGHTBLUE1           :Tuple[int,int,int] = (191, 239, 255)
    LIGHTBLUE2           :Tuple[int,int,int] = (178, 223, 238)
    LIGHTBLUE3           :Tuple[int,int,int] = (154, 192, 205)
    LIGHTBLUE4           :Tuple[int,int,int] = (104, 131, 139)
    LIGHTCORAL           :Tuple[int,int,int] = (240, 128, 128)
    LIGHTCYAN1           :Tuple[int,int,int] = (224, 255, 255)
    LIGHTCYAN2           :Tuple[int,int,int] = (209, 238, 238)
    LIGHTCYAN3           :Tuple[int,int,int] = (180, 205, 205)
    LIGHTCYAN4           :Tuple[int,int,int] = (122, 139, 139)
    LIGHTGOLDENROD1      :Tuple[int,int,int] = (255, 236, 139)
    LIGHTGOLDENROD2      :Tuple[int,int,int] = (238, 220, 130)
    LIGHTGOLDENROD3      :Tuple[int,int,int] = (205, 190, 112)
    LIGHTGOLDENROD4      :Tuple[int,int,int] = (139, 129,  76)
    LIGHTGOLDENRODYELLOW :Tuple[int,int,int] = (250, 250, 210)
    LIGHTGREY            :Tuple[int,int,int] = (211, 211, 211)
    LIGHTPINK            :Tuple[int,int,int] = (255, 182, 193)
    LIGHTPINK1           :Tuple[int,int,int] = (255, 174, 185)
    LIGHTPINK2           :Tuple[int,int,int] = (238, 162, 173)
    LIGHTPINK3           :Tuple[int,int,int] = (205, 140, 149)
    LIGHTPINK4           :Tuple[int,int,int] = (139,  95, 101)
    LIGHTSALMON1         :Tuple[int,int,int] = (255, 160, 122)
    LIGHTSALMON2         :Tuple[int,int,int] = (238, 149, 114)
    LIGHTSALMON3         :Tuple[int,int,int] = (205, 129,  98)
    LIGHTSALMON4         :Tuple[int,int,int] = (139,  87,  66)
    LIGHTSEAGREEN        :Tuple[int,int,int] = ( 32, 178, 170)
    LIGHTSKYBLUE         :Tuple[int,int,int] = (135, 206, 250)
    LIGHTSKYBLUE1        :Tuple[int,int,int] = (176, 226, 255)
    LIGHTSKYBLUE2        :Tuple[int,int,int] = (164, 211, 238)
    LIGHTSKYBLUE3        :Tuple[int,int,int] = (141, 182, 205)
    LIGHTSKYBLUE4        :Tuple[int,int,int] = ( 96, 123, 139)
    LIGHTSLATEBLUE       :Tuple[int,int,int] = (132, 112, 255)
    LIGHTSLATEGRAY       :Tuple[int,int,int] = (119, 136, 153)
    LIGHTSTEELBLUE       :Tuple[int,int,int] = (176, 196, 222)
    LIGHTSTEELBLUE1      :Tuple[int,int,int] = (202, 225, 255)
    LIGHTSTEELBLUE2      :Tuple[int,int,int] = (188, 210, 238)
    LIGHTSTEELBLUE3      :Tuple[int,int,int] = (162, 181, 205)
    LIGHTSTEELBLUE4      :Tuple[int,int,int] = (110, 123, 139)
    LIGHTYELLOW1         :Tuple[int,int,int] = (255, 255, 224)
    LIGHTYELLOW2         :Tuple[int,int,int] = (238, 238, 209)
    LIGHTYELLOW3         :Tuple[int,int,int] = (205, 205, 180)
    LIGHTYELLOW4         :Tuple[int,int,int] = (139, 139, 122)
    LIMEGREEN            :Tuple[int,int,int] = ( 50, 205,  50)
    LINEN                :Tuple[int,int,int] = (250, 240, 230)
    MAGENTA              :Tuple[int,int,int] = (255,   0, 255)
    MAGENTA2             :Tuple[int,int,int] = (238,   0, 238)
    MAGENTA3             :Tuple[int,int,int] = (205,   0, 205)
    MAGENTA4             :Tuple[int,int,int] = (139,   0, 139)
    MANGANESEBLUE        :Tuple[int,int,int] = (  3, 168, 158)
    MAROON               :Tuple[int,int,int] = (128,   0,   0)
    MAROON1              :Tuple[int,int,int] = (255,  52, 179)
    MAROON2              :Tuple[int,int,int] = (238,  48, 167)
    MAROON3              :Tuple[int,int,int] = (205,  41, 144)
    MAROON4              :Tuple[int,int,int] = (139,  28,  98)
    MEDIUMORCHID         :Tuple[int,int,int] = (186,  85, 211)
    MEDIUMORCHID1        :Tuple[int,int,int] = (224, 102, 255)
    MEDIUMORCHID2        :Tuple[int,int,int] = (209,  95, 238)
    MEDIUMORCHID3        :Tuple[int,int,int] = (180,  82, 205)
    MEDIUMORCHID4        :Tuple[int,int,int] = (122,  55, 139)
    MEDIUMPURPLE         :Tuple[int,int,int] = (147, 112, 219)
    MEDIUMPURPLE1        :Tuple[int,int,int] = (171, 130, 255)
    MEDIUMPURPLE2        :Tuple[int,int,int] = (159, 121, 238)
    MEDIUMPURPLE3        :Tuple[int,int,int] = (137, 104, 205)
    MEDIUMPURPLE4        :Tuple[int,int,int] = ( 93,  71, 139)
    MEDIUMSEAGREEN       :Tuple[int,int,int] = ( 60, 179, 113)
    MEDIUMSLATEBLUE      :Tuple[int,int,int] = (123, 104, 238)
    MEDIUMSPRINGGREEN    :Tuple[int,int,int] = (  0, 250, 154)
    MEDIUMTURQUOISE      :Tuple[int,int,int] = ( 72, 209, 204)
    MEDIUMVIOLETRED      :Tuple[int,int,int] = (199,  21, 133)
    MELON                :Tuple[int,int,int] = (227, 168, 105)
    MIDNIGHTBLUE         :Tuple[int,int,int] = ( 25,  25, 112)
    MINT                 :Tuple[int,int,int] = (189, 252, 201)
    MINTCREAM            :Tuple[int,int,int] = (245, 255, 250)
    MISTYROSE1           :Tuple[int,int,int] = (255, 228, 225)
    MISTYROSE2           :Tuple[int,int,int] = (238, 213, 210)
    MISTYROSE3           :Tuple[int,int,int] = (205, 183, 181)
    MISTYROSE4           :Tuple[int,int,int] = (139, 125, 123)
    MOCCASIN             :Tuple[int,int,int] = (255, 228, 181)
    NAVAJOWHITE1         :Tuple[int,int,int] = (255, 222, 173)
    NAVAJOWHITE2         :Tuple[int,int,int] = (238, 207, 161)
    NAVAJOWHITE3         :Tuple[int,int,int] = (205, 179, 139)
    NAVAJOWHITE4         :Tuple[int,int,int] = (139, 121,  94)
    NAVY                 :Tuple[int,int,int] = (  0,   0, 128)
    OLDLACE              :Tuple[int,int,int] = (253, 245, 230)
    OLIVE                :Tuple[int,int,int] = (128, 128,   0)
    OLIVEDRAB            :Tuple[int,int,int] = (107, 142,  35)
    OLIVEDRAB1           :Tuple[int,int,int] = (192, 255,  62)
    OLIVEDRAB2           :Tuple[int,int,int] = (179, 238,  58)
    OLIVEDRAB3           :Tuple[int,int,int] = (154, 205,  50)
    OLIVEDRAB4           :Tuple[int,int,int] = (105, 139,  34)
    ORANGE               :Tuple[int,int,int] = (255, 128,   0)
    ORANGE1              :Tuple[int,int,int] = (255, 165,   0)
    ORANGE2              :Tuple[int,int,int] = (238, 154,   0)
    ORANGE3              :Tuple[int,int,int] = (205, 133,   0)
    ORANGE4              :Tuple[int,int,int] = (139,  90,   0)
    ORANGERED1           :Tuple[int,int,int] = (255,  69,   0)
    ORANGERED2           :Tuple[int,int,int] = (238,  64,   0)
    ORANGERED3           :Tuple[int,int,int] = (205,  55,   0)
    ORANGERED4           :Tuple[int,int,int] = (139,  37,   0)
    ORCHID               :Tuple[int,int,int] = (218, 112, 214)
    ORCHID1              :Tuple[int,int,int] = (255, 131, 250)
    ORCHID2              :Tuple[int,int,int] = (238, 122, 233)
    ORCHID3              :Tuple[int,int,int] = (205, 105, 201)
    ORCHID4              :Tuple[int,int,int] = (139,  71, 137)
    PALEGOLDENROD        :Tuple[int,int,int] = (238, 232, 170)
    PALEGREEN            :Tuple[int,int,int] = (152, 251, 152)
    PALEGREEN1           :Tuple[int,int,int] = (154, 255, 154)
    PALEGREEN2           :Tuple[int,int,int] = (144, 238, 144)
    PALEGREEN3           :Tuple[int,int,int] = (124, 205, 124)
    PALEGREEN4           :Tuple[int,int,int] = ( 84, 139,  84)
    PALETURQUOISE1       :Tuple[int,int,int] = (187, 255, 255)
    PALETURQUOISE2       :Tuple[int,int,int] = (174, 238, 238)
    PALETURQUOISE3       :Tuple[int,int,int] = (150, 205, 205)
    PALETURQUOISE4       :Tuple[int,int,int] = (102, 139, 139)
    PALEVIOLETRED        :Tuple[int,int,int] = (219, 112, 147)
    PALEVIOLETRED1       :Tuple[int,int,int] = (255, 130, 171)
    PALEVIOLETRED2       :Tuple[int,int,int] = (238, 121, 159)
    PALEVIOLETRED3       :Tuple[int,int,int] = (205, 104, 137)
    PALEVIOLETRED4       :Tuple[int,int,int] = (139,  71,  93)
    PAPAYAWHIP           :Tuple[int,int,int] = (255, 239, 213)
    PEACHPUFF1           :Tuple[int,int,int] = (255, 218, 185)
    PEACHPUFF2           :Tuple[int,int,int] = (238, 203, 173)
    PEACHPUFF3           :Tuple[int,int,int] = (205, 175, 149)
    PEACHPUFF4           :Tuple[int,int,int] = (139, 119, 101)
    PEACOCK              :Tuple[int,int,int] = ( 51, 161, 201)
    PINK                 :Tuple[int,int,int] = (255, 192, 203)
    PINK1                :Tuple[int,int,int] = (255, 181, 197)
    PINK2                :Tuple[int,int,int] = (238, 169, 184)
    PINK3                :Tuple[int,int,int] = (205, 145, 158)
    PINK4                :Tuple[int,int,int] = (139,  99, 108)
    PLUM                 :Tuple[int,int,int] = (221, 160, 221)
    PLUM1                :Tuple[int,int,int] = (255, 187, 255)
    PLUM2                :Tuple[int,int,int] = (238, 174, 238)
    PLUM3                :Tuple[int,int,int] = (205, 150, 205)
    PLUM4                :Tuple[int,int,int] = (139, 102, 139)
    POWDERBLUE           :Tuple[int,int,int] = (176, 224, 230)
    PURPLE               :Tuple[int,int,int] = (128,   0, 128)
    PURPLE1              :Tuple[int,int,int] = (155,  48, 255)
    PURPLE2              :Tuple[int,int,int] = (145,  44, 238)
    PURPLE3              :Tuple[int,int,int] = (125,  38, 205)
    PURPLE4              :Tuple[int,int,int] = ( 85,  26, 139)
    RASPBERRY            :Tuple[int,int,int] = (135,  38,  87)
    RAWSIENNA            :Tuple[int,int,int] = (199,  97,  20)
    RED1                 :Tuple[int,int,int] = (255,   0,   0)
    RED2                 :Tuple[int,int,int] = (238,   0,   0)
    RED3                 :Tuple[int,int,int] = (205,   0,   0)
    RED4                 :Tuple[int,int,int] = (139,   0,   0)
    ROSYBROWN            :Tuple[int,int,int] = (188, 143, 143)
    ROSYBROWN1           :Tuple[int,int,int] = (255, 193, 193)
    ROSYBROWN2           :Tuple[int,int,int] = (238, 180, 180)
    ROSYBROWN3           :Tuple[int,int,int] = (205, 155, 155)
    ROSYBROWN4           :Tuple[int,int,int] = (139, 105, 105)
    ROYALBLUE            :Tuple[int,int,int] = ( 65, 105, 225)
    ROYALBLUE1           :Tuple[int,int,int] = ( 72, 118, 255)
    ROYALBLUE2           :Tuple[int,int,int] = ( 67, 110, 238)
    ROYALBLUE3           :Tuple[int,int,int] = ( 58,  95, 205)
    ROYALBLUE4           :Tuple[int,int,int] = ( 39,  64, 139)
    SALMON               :Tuple[int,int,int] = (250, 128, 114)
    SALMON1              :Tuple[int,int,int] = (255, 140, 105)
    SALMON2              :Tuple[int,int,int] = (238, 130,  98)
    SALMON3              :Tuple[int,int,int] = (205, 112,  84)
    SALMON4              :Tuple[int,int,int] = (139,  76,  57)
    SANDYBROWN           :Tuple[int,int,int] = (244, 164,  96)
    SAPGREEN             :Tuple[int,int,int] = ( 48, 128,  20)
    SEAGREEN1            :Tuple[int,int,int] = ( 84, 255, 159)
    SEAGREEN2            :Tuple[int,int,int] = ( 78, 238, 148)
    SEAGREEN3            :Tuple[int,int,int] = ( 67, 205, 128)
    SEAGREEN4            :Tuple[int,int,int] = ( 46, 139,  87)
    SEASHELL1            :Tuple[int,int,int] = (255, 245, 238)
    SEASHELL2            :Tuple[int,int,int] = (238, 229, 222)
    SEASHELL3            :Tuple[int,int,int] = (205, 197, 191)
    SEASHELL4            :Tuple[int,int,int] = (139, 134, 130)
    SEPIA                :Tuple[int,int,int] = ( 94,  38,  18)
    SGIBEET              :Tuple[int,int,int] = (142,  56, 142)
    SGIBRIGHTGRAY        :Tuple[int,int,int] = (197, 193, 170)
    SGICHARTREUSE        :Tuple[int,int,int] = (113, 198, 113)
    SGIDARKGRAY          :Tuple[int,int,int] = ( 85,  85,  85)
    SGIGRAY12            :Tuple[int,int,int] = ( 30,  30,  30)
    SGIGRAY16            :Tuple[int,int,int] = ( 40,  40,  40)
    SGIGRAY32            :Tuple[int,int,int] = ( 81,  81,  81)
    SGIGRAY36            :Tuple[int,int,int] = ( 91,  91,  91)
    SGIGRAY52            :Tuple[int,int,int] = (132, 132, 132)
    SGIGRAY56            :Tuple[int,int,int] = (142, 142, 142)
    SGIGRAY72            :Tuple[int,int,int] = (183, 183, 183)
    SGIGRAY76            :Tuple[int,int,int] = (193, 193, 193)
    SGIGRAY92            :Tuple[int,int,int] = (234, 234, 234)
    SGIGRAY96            :Tuple[int,int,int] = (244, 244, 244)
    SGILIGHTBLUE         :Tuple[int,int,int] = (125, 158, 192)
    SGILIGHTGRAY         :Tuple[int,int,int] = (170, 170, 170)
    SGIOLIVEDRAB         :Tuple[int,int,int] = (142, 142,  56)
    SGISALMON            :Tuple[int,int,int] = (198, 113, 113)
    SGISLATEBLUE         :Tuple[int,int,int] = (113, 113, 198)
    SGITEAL              :Tuple[int,int,int] = ( 56, 142, 142)
    SIENNA               :Tuple[int,int,int] = (160,  82,  45)
    SIENNA1              :Tuple[int,int,int] = (255, 130,  71)
    SIENNA2              :Tuple[int,int,int] = (238, 121,  66)
    SIENNA3              :Tuple[int,int,int] = (205, 104,  57)
    SIENNA4              :Tuple[int,int,int] = (139,  71,  38)
    SILVER               :Tuple[int,int,int] = (192, 192, 192)
    SKYBLUE              :Tuple[int,int,int] = (135, 206, 235)
    SKYBLUE1             :Tuple[int,int,int] = (135, 206, 255)
    SKYBLUE2             :Tuple[int,int,int] = (126, 192, 238)
    SKYBLUE3             :Tuple[int,int,int] = (108, 166, 205)
    SKYBLUE4             :Tuple[int,int,int] = ( 74, 112, 139)
    SLATEBLUE            :Tuple[int,int,int] = (106,  90, 205)
    SLATEBLUE1           :Tuple[int,int,int] = (131, 111, 255)
    SLATEBLUE2           :Tuple[int,int,int] = (122, 103, 238)
    SLATEBLUE3           :Tuple[int,int,int] = (105,  89, 205)
    SLATEBLUE4           :Tuple[int,int,int] = ( 71,  60, 139)
    SLATEGRAY            :Tuple[int,int,int] = (112, 128, 144)
    SLATEGRAY1           :Tuple[int,int,int] = (198, 226, 255)
    SLATEGRAY2           :Tuple[int,int,int] = (185, 211, 238)
    SLATEGRAY3           :Tuple[int,int,int] = (159, 182, 205)
    SLATEGRAY4           :Tuple[int,int,int] = (108, 123, 139)
    SNOW1                :Tuple[int,int,int] = (255, 250, 250)
    SNOW2                :Tuple[int,int,int] = (238, 233, 233)
    SNOW3                :Tuple[int,int,int] = (205, 201, 201)
    SNOW4                :Tuple[int,int,int] = (139, 137, 137)
    SPRINGGREEN          :Tuple[int,int,int] = (  0, 255, 127)
    SPRINGGREEN1         :Tuple[int,int,int] = (  0, 238, 118)
    SPRINGGREEN2         :Tuple[int,int,int] = (  0, 205, 102)
    SPRINGGREEN3         :Tuple[int,int,int] = (  0, 139,  69)
    STEELBLUE            :Tuple[int,int,int] = ( 70, 130, 180)
    STEELBLUE1           :Tuple[int,int,int] = ( 99, 184, 255)
    STEELBLUE2           :Tuple[int,int,int] = ( 92, 172, 238)
    STEELBLUE3           :Tuple[int,int,int] = ( 79, 148, 205)
    STEELBLUE4           :Tuple[int,int,int] = ( 54, 100, 139)
    TAN                  :Tuple[int,int,int] = (210, 180, 140)
    TAN1                 :Tuple[int,int,int] = (255, 165,  79)
    TAN2                 :Tuple[int,int,int] = (238, 154,  73)
    TAN3                 :Tuple[int,int,int] = (205, 133,  63)
    TAN4                 :Tuple[int,int,int] = (139,  90,  43)
    TEAL                 :Tuple[int,int,int] = (  0, 128, 128)
    THISTLE              :Tuple[int,int,int] = (216, 191, 216)
    THISTLE1             :Tuple[int,int,int] = (255, 225, 255)
    THISTLE2             :Tuple[int,int,int] = (238, 210, 238)
    THISTLE3             :Tuple[int,int,int] = (205, 181, 205)
    THISTLE4             :Tuple[int,int,int] = (139, 123, 139)
    TOMATO1              :Tuple[int,int,int] = (255,  99,  71)
    TOMATO2              :Tuple[int,int,int] = (238,  92,  66)
    TOMATO3              :Tuple[int,int,int] = (205,  79,  57)
    TOMATO4              :Tuple[int,int,int] = (139,  54,  38)
    TURQUOISE            :Tuple[int,int,int] = ( 64, 224, 208)
    TURQUOISE1           :Tuple[int,int,int] = (  0, 245, 255)
    TURQUOISE2           :Tuple[int,int,int] = (  0, 229, 238)
    TURQUOISE3           :Tuple[int,int,int] = (  0, 197, 205)
    TURQUOISE4           :Tuple[int,int,int] = (  0, 134, 139)
    TURQUOISEBLUE        :Tuple[int,int,int] = (  0, 199, 140)
    VIOLET               :Tuple[int,int,int] = (238, 130, 238)
    VIOLETRED            :Tuple[int,int,int] = (208,  32, 144)
    VIOLETRED1           :Tuple[int,int,int] = (255,  62, 150)
    VIOLETRED2           :Tuple[int,int,int] = (238,  58, 140)
    VIOLETRED3           :Tuple[int,int,int] = (205,  50, 120)
    VIOLETRED4           :Tuple[int,int,int] = (139,  34,  82)
    WARMGREY             :Tuple[int,int,int] = (128, 128, 105)
    WHEAT                :Tuple[int,int,int] = (245, 222, 179)
    WHEAT1               :Tuple[int,int,int] = (255, 231, 186)
    WHEAT2               :Tuple[int,int,int] = (238, 216, 174)
    WHEAT3               :Tuple[int,int,int] = (205, 186, 150)
    WHEAT4               :Tuple[int,int,int] = (139, 126, 102)
    WHITE                :Tuple[int,int,int] = (255, 255, 255)
    WHITESMOKE           :Tuple[int,int,int] = (245, 245, 245)
    YELLOW1              :Tuple[int,int,int] = (255, 255,   0)
    YELLOW2              :Tuple[int,int,int] = (238, 238,   0)
    YELLOW3              :Tuple[int,int,int] = (205, 205,   0)
    YELLOW4              :Tuple[int,int,int] = (139, 139,   0)
