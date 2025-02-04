from traffic_lights import TrafficLight

lights = TrafficLight()

assert lights.g is not None
assert lights.y is not None
assert lights.r is not None

lights.green()
assert lights.g.is_lit == True
assert lights.y.is_lit == False
assert lights.r.is_lit == False

lights.yellow()
assert lights.g.is_lit == False
assert lights.y.is_lit == True
assert lights.r.is_lit == False

lights.red()
assert lights.g.is_lit == False
assert lights.y.is_lit == False
assert lights.r.is_lit == True

