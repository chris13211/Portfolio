# Find the cube of all numbers from 1 to a given number

def cube(number):
  """Returns the cube of a number."""
  return number * number * number

def main():
  """Prints the cube of all numbers from 1 to a given number."""

  # Get the input from the user.
  input_number = int(input("Enter a number: "))

  # Calculate the cube of all numbers from 1 to the given number.
  for i in range(1, input_number + 1):
    cube_of_number = cube(i)

    # Print the cube of the current number.
    print(f"The cube of {i} is {cube_of_number}.")

if __name__ == "__main__":
  main()