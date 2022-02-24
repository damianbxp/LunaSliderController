def lerp_1D(range_x: tuple, t:float):
    print(f"lerp range {range_x}")
    print(f"t = {t}")
    return range_x[0] + (range_x[1] - range_x[0]) * t

def clamp(max_x, min_x, x):
    result = max(min_x, min(x, max_x))
    print(f"clamp result = {result}")
    return result
