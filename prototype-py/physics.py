GRAVITY = -450.0
GRAVITY_MAX_SPEED = -15

def gravity(y, dy, delta):
    dt       = delta * 0.001
    velocity = (y-dy)/(dt)
    dif      = -velocity * dt + GRAVITY * dt * dt
    if GRAVITY_MAX_SPEED > dif:
        return GRAVITY_MAX_SPEED
    return dif
