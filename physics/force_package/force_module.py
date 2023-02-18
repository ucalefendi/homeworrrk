from physics.acceleration_module import acceleration
# from ..acceleretion_module import acceleration

def force(mass, veloctity, seconds):
    return mass * acceleration(veloctity, seconds)
