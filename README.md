## CSP Anytime Solutions
This is an example script to show how to use the [python-constraint](https://github.com/python-constraint/python-constraint) library to generate as many solutions as possible to a Constraint Satsifaction Problem (CSP) until the user presses `Ctrl+c`.

### Example
Solving the problem for all solutions takes a few seconds

```
$ python __main__.py all_solutions          
Runtime: 0:00:13.455467
Solutions found (300): [{'a': 2990, 'b': 299}, {'a': 2980, 'b': 298}, {'a': 2970, 'b': 297}, {'a': 2960, 'b': 296}, {'a': 2950, 'b': 295}, {'a': 2940, 'b': 294}, {'a': 2930, 'b': 293}, {'a': 2920, 'b': 292}, {'a': 2910, 'b': 291}, {'a': 2900, 'b': 290}, {'a': 2890, 'b': 289}, {'a': 2880, 'b': 288}, {'a': 2870, 'b': 287}, {'a': 2860, 'b': 286}, {'a': 2850, 'b': 285}, {'a': 2840, 'b': 284}, {'a': 2830, 'b': 283}, {'a': 2820, 'b': 282}, {'a': 2810, 'b': 281}, {'a': 2800, 'b': 280}, {'a': 2790, 'b': 279}, {'a': 2780, 'b': 278}, {'a': 2770, 'b': 277}, {'a': 2760, 'b': 276}, {'a': 2750, 'b': 275}, {'a': 2740, 'b': 274}, {'a': 2730, 'b': 273}, {'a': 2720, 'b': 272}, {'a': 2710, 'b': 271}, {'a': 2700, 'b': 270}, {'a': 2690, 'b': 269}, {'a': 2680, 'b': 268}, {'a': 2670, 'b': 267}, {'a': 2660, 'b': 266}, {'a': 2650, 'b': 265}, {'a': 2640, 'b': 264}, {'a': 2630, 'b': 263}, {'a': 2620, 'b': 262}, {'a': 2610, 'b': 261}, {'a': 2600, 'b': 260}, {'a': 2590, 'b': 259}, {'a': 2580, 'b': 258}, {'a': 2570, 'b': 257}, {'a': 2560, 'b': 256}, {'a': 2550, 'b': 255}, {'a': 2540, 'b': 254}, {'a': 2530, 'b': 253}, {'a': 2520, 'b': 252}, {'a': 2510, 'b': 251}, {'a': 2500, 'b': 250}, {'a': 2490, 'b': 249}, {'a': 2480, 'b': 248}, {'a': 2470, 'b': 247}, {'a': 2460, 'b': 246}, {'a': 2450, 'b': 245}, {'a': 2440, 'b': 244}, {'a': 2430, 'b': 243}, {'a': 2420, 'b': 242}, {'a': 2410, 'b': 241}, {'a': 2400, 'b': 240}, {'a': 2390, 'b': 239}, {'a': 2380, 'b': 238}, {'a': 2370, 'b': 237}, {'a': 2360, 'b': 236}, {'a': 2350, 'b': 235}, {'a': 2340, 'b': 234}, {'a': 2330, 'b': 233}, {'a': 2320, 'b': 232}, {'a': 2310, 'b': 231}, {'a': 2300, 'b': 230}, {'a': 2290, 'b': 229}, {'a': 2280, 'b': 228}, {'a': 2270, 'b': 227}, {'a': 2260, 'b': 226}, {'a': 2250, 'b': 225}, {'a': 2240, 'b': 224}, {'a': 2230, 'b': 223}, {'a': 2220, 'b': 222}, {'a': 2210, 'b': 221}, {'a': 2200, 'b': 220}, {'a': 2190, 'b': 219}, {'a': 2180, 'b': 218}, {'a': 2170, 'b': 217}, {'a': 2160, 'b': 216}, {'a': 2150, 'b': 215}, {'a': 2140, 'b': 214}, {'a': 2130, 'b': 213}, {'a': 2120, 'b': 212}, {'a': 2110, 'b': 211}, {'a': 2100, 'b': 210}, {'a': 2090, 'b': 209}, {'a': 2080, 'b': 208}, {'a': 2070, 'b': 207}, {'a': 2060, 'b': 206}, {'a': 2050, 'b': 205}, {'a': 2040, 'b': 204}, {'a': 2030, 'b': 203}, {'a': 2020, 'b': 202}, {'a': 2010, 'b': 201}, {'a': 2000, 'b': 200}, {'a': 1990, 'b': 199}, {'a': 1980, 'b': 198}, {'a': 1970, 'b': 197}, {'a': 1960, 'b': 196}, {'a': 1950, 'b': 195}, {'a': 1940, 'b': 194}, {'a': 1930, 'b': 193}, {'a': 1920, 'b': 192}, {'a': 1910, 'b': 191}, {'a': 1900, 'b': 190}, {'a': 1890, 'b': 189}, {'a': 1880, 'b': 188}, {'a': 1870, 'b': 187}, {'a': 1860, 'b': 186}, {'a': 1850, 'b': 185}, {'a': 1840, 'b': 184}, {'a': 1830, 'b': 183}, {'a': 1820, 'b': 182}, {'a': 1810, 'b': 181}, {'a': 1800, 'b': 180}, {'a': 1790, 'b': 179}, {'a': 1780, 'b': 178}, {'a': 1770, 'b': 177}, {'a': 1760, 'b': 176}, {'a': 1750, 'b': 175}, {'a': 1740, 'b': 174}, {'a': 1730, 'b': 173}, {'a': 1720, 'b': 172}, {'a': 1710, 'b': 171}, {'a': 1700, 'b': 170}, {'a': 1690, 'b': 169}, {'a': 1680, 'b': 168}, {'a': 1670, 'b': 167}, {'a': 1660, 'b': 166}, {'a': 1650, 'b': 165}, {'a': 1640, 'b': 164}, {'a': 1630, 'b': 163}, {'a': 1620, 'b': 162}, {'a': 1610, 'b': 161}, {'a': 1600, 'b': 160}, {'a': 1590, 'b': 159}, {'a': 1580, 'b': 158}, {'a': 1570, 'b': 157}, {'a': 1560, 'b': 156}, {'a': 1550, 'b': 155}, {'a': 1540, 'b': 154}, {'a': 1530, 'b': 153}, {'a': 1520, 'b': 152}, {'a': 1510, 'b': 151}, {'a': 1500, 'b': 150}, {'a': 1490, 'b': 149}, {'a': 1480, 'b': 148}, {'a': 1470, 'b': 147}, {'a': 1460, 'b': 146}, {'a': 1450, 'b': 145}, {'a': 1440, 'b': 144}, {'a': 1430, 'b': 143}, {'a': 1420, 'b': 142}, {'a': 1410, 'b': 141}, {'a': 1400, 'b': 140}, {'a': 1390, 'b': 139}, {'a': 1380, 'b': 138}, {'a': 1370, 'b': 137}, {'a': 1360, 'b': 136}, {'a': 1350, 'b': 135}, {'a': 1340, 'b': 134}, {'a': 1330, 'b': 133}, {'a': 1320, 'b': 132}, {'a': 1310, 'b': 131}, {'a': 1300, 'b': 130}, {'a': 1290, 'b': 129}, {'a': 1280, 'b': 128}, {'a': 1270, 'b': 127}, {'a': 1260, 'b': 126}, {'a': 1250, 'b': 125}, {'a': 1240, 'b': 124}, {'a': 1230, 'b': 123}, {'a': 1220, 'b': 122}, {'a': 1210, 'b': 121}, {'a': 1200, 'b': 120}, {'a': 1190, 'b': 119}, {'a': 1180, 'b': 118}, {'a': 1170, 'b': 117}, {'a': 1160, 'b': 116}, {'a': 1150, 'b': 115}, {'a': 1140, 'b': 114}, {'a': 1130, 'b': 113}, {'a': 1120, 'b': 112}, {'a': 1110, 'b': 111}, {'a': 1100, 'b': 110}, {'a': 1090, 'b': 109}, {'a': 1080, 'b': 108}, {'a': 1070, 'b': 107}, {'a': 1060, 'b': 106}, {'a': 1050, 'b': 105}, {'a': 1040, 'b': 104}, {'a': 1030, 'b': 103}, {'a': 1020, 'b': 102}, {'a': 1010, 'b': 101}, {'a': 1000, 'b': 100}, {'a': 990, 'b': 99}, {'a': 980, 'b': 98}, {'a': 970, 'b': 97}, {'a': 960, 'b': 96}, {'a': 950, 'b': 95}, {'a': 940, 'b': 94}, {'a': 930, 'b': 93}, {'a': 920, 'b': 92}, {'a': 910, 'b': 91}, {'a': 900, 'b': 90}, {'a': 890, 'b': 89}, {'a': 880, 'b': 88}, {'a': 870, 'b': 87}, {'a': 860, 'b': 86}, {'a': 850, 'b': 85}, {'a': 840, 'b': 84}, {'a': 830, 'b': 83}, {'a': 820, 'b': 82}, {'a': 810, 'b': 81}, {'a': 800, 'b': 80}, {'a': 790, 'b': 79}, {'a': 780, 'b': 78}, {'a': 770, 'b': 77}, {'a': 760, 'b': 76}, {'a': 750, 'b': 75}, {'a': 740, 'b': 74}, {'a': 730, 'b': 73}, {'a': 720, 'b': 72}, {'a': 710, 'b': 71}, {'a': 700, 'b': 70}, {'a': 690, 'b': 69}, {'a': 680, 'b': 68}, {'a': 670, 'b': 67}, {'a': 660, 'b': 66}, {'a': 650, 'b': 65}, {'a': 640, 'b': 64}, {'a': 630, 'b': 63}, {'a': 620, 'b': 62}, {'a': 610, 'b': 61}, {'a': 600, 'b': 60}, {'a': 590, 'b': 59}, {'a': 580, 'b': 58}, {'a': 570, 'b': 57}, {'a': 560, 'b': 56}, {'a': 550, 'b': 55}, {'a': 540, 'b': 54}, {'a': 530, 'b': 53}, {'a': 520, 'b': 52}, {'a': 510, 'b': 51}, {'a': 500, 'b': 50}, {'a': 490, 'b': 49}, {'a': 480, 'b': 48}, {'a': 470, 'b': 47}, {'a': 460, 'b': 46}, {'a': 450, 'b': 45}, {'a': 440, 'b': 44}, {'a': 430, 'b': 43}, {'a': 420, 'b': 42}, {'a': 410, 'b': 41}, {'a': 400, 'b': 40}, {'a': 390, 'b': 39}, {'a': 380, 'b': 38}, {'a': 370, 'b': 37}, {'a': 360, 'b': 36}, {'a': 350, 'b': 35}, {'a': 340, 'b': 34}, {'a': 330, 'b': 33}, {'a': 320, 'b': 32}, {'a': 310, 'b': 31}, {'a': 300, 'b': 30}, {'a': 290, 'b': 29}, {'a': 280, 'b': 28}, {'a': 270, 'b': 27}, {'a': 260, 'b': 26}, {'a': 250, 'b': 25}, {'a': 240, 'b': 24}, {'a': 230, 'b': 23}, {'a': 220, 'b': 22}, {'a': 210, 'b': 21}, {'a': 200, 'b': 20}, {'a': 190, 'b': 19}, {'a': 180, 'b': 18}, {'a': 170, 'b': 17}, {'a': 160, 'b': 16}, {'a': 150, 'b': 15}, {'a': 140, 'b': 14}, {'a': 130, 'b': 13}, {'a': 120, 'b': 12}, {'a': 110, 'b': 11}, {'a': 100, 'b': 10}, {'a': 90, 'b': 9}, {'a': 80, 'b': 8}, {'a': 70, 'b': 7}, {'a': 60, 'b': 6}, {'a': 50, 'b': 5}, {'a': 40, 'b': 4}, {'a': 30, 'b': 3}, {'a': 20, 'b': 2}, {'a': 10, 'b': 1}, {'a': 0, 'b': 0}]
```

If we run the script with a different setting, we can use the multiprocess mode that reports all of the solutions found before `Ctrl+c` is pressed. For example if we run it an press `Ctrl+c` after a few seconds we might get results like the following. (`^C` is from pressing `Ctrl+c`)

```
$ python __main__.py until_ctrl_c
^CRuntime: 0:00:02.475917
Solutions found (53): [{'a': 2990, 'b': 299}, {'a': 2980, 'b': 298}, {'a': 2970, 'b': 297}, {'a': 2960, 'b': 296}, {'a': 2950, 'b': 295}, {'a': 2940, 'b': 294}, {'a': 2930, 'b': 293}, {'a': 2920, 'b': 292}, {'a': 2910, 'b': 291}, {'a': 2900, 'b': 290}, {'a': 2890, 'b': 289}, {'a': 2880, 'b': 288}, {'a': 2870, 'b': 287}, {'a': 2860, 'b': 286}, {'a': 2850, 'b': 285}, {'a': 2840, 'b': 284}, {'a': 2830, 'b': 283}, {'a': 2820, 'b': 282}, {'a': 2810, 'b': 281}, {'a': 2800, 'b': 280}, {'a': 2790, 'b': 279}, {'a': 2780, 'b': 278}, {'a': 2770, 'b': 277}, {'a': 2760, 'b': 276}, {'a': 2750, 'b': 275}, {'a': 2740, 'b': 274}, {'a': 2730, 'b': 273}, {'a': 2720, 'b': 272}, {'a': 2710, 'b': 271}, {'a': 2700, 'b': 270}, {'a': 2690, 'b': 269}, {'a': 2680, 'b': 268}, {'a': 2670, 'b': 267}, {'a': 2660, 'b': 266}, {'a': 2650, 'b': 265}, {'a': 2640, 'b': 264}, {'a': 2630, 'b': 263}, {'a': 2620, 'b': 262}, {'a': 2610, 'b': 261}, {'a': 2600, 'b': 260}, {'a': 2590, 'b': 259}, {'a': 2580, 'b': 258}, {'a': 2570, 'b': 257}, {'a': 2560, 'b': 256}, {'a': 2550, 'b': 255}, {'a': 2540, 'b': 254}, {'a': 2530, 'b': 253}, {'a': 2520, 'b': 252}, {'a': 2510, 'b': 251}, {'a': 2500, 'b': 250}, {'a': 2490, 'b': 249}, {'a': 2480, 'b': 248}, {'a': 2470, 'b': 247}]
```