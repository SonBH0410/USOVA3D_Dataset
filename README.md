# USOVA3D Dataset

Volume-level statistics for the USOVA3D dataset. For each volume the table lists
the number of slice images and, for every annotation sub-volume, the number of
fully-black (all-zero) label slices out of the total label slices.

`f_r1`, `f_r2`, `o_r1`, `o_r2` are the four annotation variants per volume.

## train

| Volume | Images | f_r1 (black/total) | f_r2 (black/total) | o_r1 (black/total) | o_r2 (black/total) |
|--------|-------:|-------------------:|-------------------:|-------------------:|-------------------:|
| Vol2   | 247 | 126/247 | 108/247 | 104/247 | 57/247 |
| Vol3   | 236 |  56/236 |  49/236 |  28/236 | 31/236 |
| Vol4   | 247 | 130/247 |  88/247 |  72/247 | 23/247 |
| Vol5   | 237 | 141/237 | 116/237 |  57/237 |  9/237 |
| Vol6   | 247 | 114/247 | 124/247 |  67/247 | 67/247 |
| Vol101 | 199 |  65/199 |  61/199 |  55/199 | 51/199 |
| Vol102 | 199 |  33/199 |  33/199 |  23/199 | 23/199 |
| Vol110 | 197 |  32/197 |  87/197 |   0/197 |  0/197 |
| Vol111 | 199 |  91/199 |  89/199 |  81/199 | 79/199 |
| Vol115 | 199 |  38/199 |  43/199 |  28/199 | 33/199 |
| Vol117 | 199 |  24/199 |  35/199 |  19/199 | 27/199 |
| Vol119 | 187 |  39/187 |  32/187 |  29/187 | 25/187 |
| **Total** | **2593** | **889/2593** | **865/2593** | **563/2593** | **425/2593** |

## val

| Volume | Images | f_r1 (black/total) | f_r2 (black/total) | o_r1 (black/total) | o_r2 (black/total) |
|--------|-------:|-------------------:|-------------------:|-------------------:|-------------------:|
| Vol104 | 199 | 21/199 | 22/199 | 16/199 | 17/199 |
| Vol109 | 199 | 31/199 | 34/199 | 21/199 | 25/199 |
| **Total** | **398** | **52/398** | **56/398** | **37/398** | **42/398** |

## test

| Volume | Images | f_r1 (black/total) | f_r2 (black/total) | o_r1 (black/total) | o_r2 (black/total) |
|--------|-------:|-------------------:|-------------------:|-------------------:|-------------------:|
| Vol1   | 247 | 114/247 | 123/247 | 87/247 | 92/247 |
| Vol106 | 181 |  24/181 |   9/181 | 19/181 |  4/181 |
| **Total** | **428** | **138/428** | **132/428** | **106/428** | **96/428** |

## Overall

| Split | Volumes | Images | Total label slices | Total black labels |
|-------|--------:|-------:|-------------------:|-------------------:|
| train | 12 | 2593 | 10372 | 2742 |
| val   |  2 |  398 |  1592 |  187 |
| test  |  2 |  428 |  1712 |  472 |
| **All** | **16** | **3419** | **13676** | **3401** |

A "black" label is a slice whose pixel values are all zero (i.e. no annotated
structure on that slice).
