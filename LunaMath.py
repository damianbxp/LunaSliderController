def lerp_1D(range_x: tuple, t:float):
    return range_x[0] + (range_x[1] - range_x[0]) * t

def clamp(min_x, max_x, x):
    return max(min(x, max_x), min_x)
