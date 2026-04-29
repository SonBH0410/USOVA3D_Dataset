# USOVA3D Dataset

Volume-level statistics for the USOVA3D dataset. For each volume the table lists
the number of slice images and, for every annotation, the number of fully-black
(all-zero) label slices out of the total label slices. A "black" slice is a
slice whose pixel values are all zero — i.e. no annotated structure on that
slice.

## Layout

```
<split>/                       split = train | val | test
├── images/<Volume>/slice_NNN.png            ultrasound slices
└── labels/<Volume>/
    ├── follicle_r1/slice_NNN.png            binary mask (0 / 255)
    ├── follicle_r1_color/slice_NNN.png      RGB color overlay (one color per follicle instance)
    ├── follicle_r1_labels/slice_NNN.png     instance-ID mask (0 = bg, 1, 2, ...)
    ├── follicle_r2/...                      same three variants for expert 2
    ├── follicle_r2_color/...
    ├── follicle_r2_labels/...
    ├── ovary_r1/slice_NNN.png               binary mask (0 / 255)
    └── ovary_r2/slice_NNN.png               binary mask (0 / 255)
```

## Annotation codes

Following the original USOVA3D naming `vol<X>_<Y>_r<Z>`:

- `Y = f` / `follicle` — **follicle** annotation
- `Y = o` / `ovary`    — **ovary** annotation
- `Z = 1` / `r1`       — annotation by **expert 1**
- `Z = 2` / `r2`       — annotation by **expert 2**

For each follicle annotation there are three co-registered variants:

| Variant suffix  | What it stores                                            |
|-----------------|-----------------------------------------------------------|
| (none)          | binary mask, `L` mode, values `{0, 255}`                  |
| `_color`        | RGB visualization, distinct color per follicle instance   |
| `_labels`       | instance-ID mask, `L` mode, values `{0, 1, 2, ...}`       |

The three follicle variants encode the same instances, so their black-slice
counts are identical and the tables below show one column per logical
annotation. Ovary masks have no instance variant (a single ovary per volume).

## train

| Volume | Images | follicle_r1 (black/total) | follicle_r2 (black/total) | ovary_r1 (black/total) | ovary_r2 (black/total) |
|--------|-------:|--------------------------:|--------------------------:|-----------------------:|-----------------------:|
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

| Volume | Images | follicle_r1 (black/total) | follicle_r2 (black/total) | ovary_r1 (black/total) | ovary_r2 (black/total) |
|--------|-------:|--------------------------:|--------------------------:|-----------------------:|-----------------------:|
| Vol104 | 199 | 21/199 | 22/199 | 16/199 | 17/199 |
| Vol109 | 199 | 31/199 | 34/199 | 21/199 | 25/199 |
| **Total** | **398** | **52/398** | **56/398** | **37/398** | **42/398** |

## test

| Volume | Images | follicle_r1 (black/total) | follicle_r2 (black/total) | ovary_r1 (black/total) | ovary_r2 (black/total) |
|--------|-------:|--------------------------:|--------------------------:|-----------------------:|-----------------------:|
| Vol1   | 247 | 114/247 | 123/247 | 87/247 | 92/247 |
| Vol106 | 181 |  24/181 |   9/181 | 19/181 |  4/181 |
| **Total** | **428** | **138/428** | **132/428** | **106/428** | **96/428** |

## Overall

| Split | Volumes | Images | Total label slices† | Total black labels† |
|-------|--------:|-------:|--------------------:|--------------------:|
| train | 12 | 2593 | 10372 | 2742 |
| val   |  2 |  398 |  1592 |  187 |
| test  |  2 |  428 |  1712 |  472 |
| **All** | **16** | **3419** | **13676** | **3401** |

† Counted across the four logical annotations (`follicle_r1`, `follicle_r2`,
`ovary_r1`, `ovary_r2`) — i.e. one row per slice per logical annotation. The
three follicle representation variants (plain / `_color` / `_labels`) are not
double-counted since they encode the same data.
