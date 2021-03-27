def nth_power(exponent):
  def base_is(base):
    return pow(base,exponent)

  return base_is

square=nth_power(2)
cube=nth_power(3)
print(square(2))
print(square(3))
print(cube(2))
print(cube(3))
