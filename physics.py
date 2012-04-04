GRAVITY = -700.0

def gravity(y, dy, delta):
    dt       = delta * 0.001
    velocity = (y-dy)/(dt)
    dif      = -velocity * dt + GRAVITY * dt * dt
    return dif
