class NumberMachine:
    def __init__(self):
        """Initialize the number machine."""
        pass
    
    def validate_input(self, number):
        """
        Validate that the input is a positive five-digit integer.
        
        Args:
            number: The input to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        if not isinstance(number, int):
            return False
        
        if number < 10000 or number > 99999:
            return False
            
        return True
    
    def reverse_number(self, number):
        """
        Reverse a five-digit number without using built-in reverse functions.
        
        Args:
            number: A five-digit integer
            
        Returns:
            int: The reversed number
        """
        reversed_num = 0
        
        # Process each digit using modulus operator
        temp = number
        while temp > 0:
            digit = temp % 10  # Get the last digit
            reversed_num = reversed_num * 10 + digit  # Add digit to reversed number
            temp = temp // 10  # Remove the last digit
        
        return reversed_num
    
    def sum_of_digits(self, number):
        """
        Calculate the sum of all digits in a number.
        
        Args:
            number: A five-digit integer
            
        Returns:
            int: Sum of the digits
        """
        total = 0
        temp = number
        
        while temp > 0:
            digit = temp % 10  # Get the last digit
            total += digit      # Add to total
            temp = temp // 10   # Remove the last digit
        
        return total
    
    def add_one_to_each_digit(self, number):
        """
        Generate a new number by adding 1 to each digit.
        
        Args:
            number: A five-digit integer
            
        Returns:
            int: New number with each digit increased by 1
        """
        result = 0
        position = 1  # Tracks the current position (units, tens, hundreds, etc.)
        temp = number
        
        while temp > 0:
            digit = temp % 10  # Get the last digit
            new_digit = (digit + 1) % 10  # Add 1 and handle overflow (9+1=0)
            
            # Add the new digit to the result at the correct position
            result = new_digit * position + result
            
            # Update position and remove processed digit
            position *= 10
            temp = temp // 10
        
        return result
    
    def process_number(self, number):
        """
        Process a number through all three transformations.
        
        Args:
            number: A five-digit integer
            
        Returns:
            dict: Dictionary containing all results
        """
        if not self.validate_input(number):
            raise ValueError("Input must be a positive five-digit integer (10000-99999)")
        
        results = {
            'original': number,
            'reversed': self.reverse_number(number),
            'digit_sum': self.sum_of_digits(number),
            'incremented': self.add_one_to_each_digit(number)
        }
        
        return results
    
    def display_results(self, results):
        """
        Display the results in a formatted way.
        
        Args:
            results: Dictionary containing the transformation results
        """
        print("\n" + "=" * 50)
        print("NUMBER MACHINE RESULTS")
        print("=" * 50)
        print(f"Original number: {results['original']}")
        print(f"Reversed number: {results['reversed']}")
        print(f"Sum of digits:   {results['digit_sum']}")
        print(f"Incremented:     {results['incremented']}")
        print("=" * 50)


def manual_verification_example():
    """Show manual calculation examples to verify the algorithm."""
    print("\n" + "=" * 50)
    print("MANUAL VERIFICATION EXAMPLES")
    print("=" * 50)
    
    examples = [
        12345,
        99999,
        10000,
        54321,
        12391  # Example from the problem
    ]
    
    for num in examples:
        print(f"\nExample: {num}")
        
        # Manual reversal explanation
        print("  Reversal calculation:")
        digits = []
        temp = num
        while temp > 0:
            digit = temp % 10
            digits.append(digit)
            temp //= 10
        reversed_manual = int(''.join(map(str, digits)))
        print(f"    Digits extracted: {digits}")
        print(f"    Reversed: {reversed_manual}")
        
        # Manual sum calculation
        print("  Sum calculation:")
        temp = num
        sum_digits = 0
        digit_list = []
        while temp > 0:
            digit = temp % 10
            digit_list.append(digit)
            sum_digits += digit
            temp //= 10
        print(f"    Digits: {digit_list[::-1]}")
        print(f"    Sum: {' + '.join(map(str, digit_list))} = {sum_digits}")
        
        # Manual increment calculation
        print("  Increment calculation:")
        temp = num
        new_digits = []
        while temp > 0:
            digit = temp % 10
            new_digit = (digit + 1) % 10
            new_digits.append(new_digit)
            temp //= 10
        incremented = int(''.join(map(str, new_digits[::-1])))
        print(f"    Original digits: {digit_list[::-1]}")
        print(f"    New digits: {new_digits[::-1]}")
        print(f"    Incremented number: {incremented}")


def test_number_machine():
    """Test the number machine with various test cases."""
    print("\n" + "=" * 50)
    print("TESTING NUMBER MACHINE")
    print("=" * 50)
    
    machine = NumberMachine()
    
    test_cases = [
        (12345, {
            'reversed': 54321,
            'digit_sum': 15,  # 1+2+3+4+5
            'incremented': 23456  # Each digit +1
        }, "Basic example"),
        
        (12391, {
            'reversed': 19321,
            'digit_sum': 16,  # 1+2+3+9+1
            'incremented': 23402  # Example from problem: 1→2, 2→3, 3→4, 9→0, 1→2
        }, "Example from problem"),
        
        (99999, {
            'reversed': 99999,
            'digit_sum': 45,  # 9+9+9+9+9
            'incremented': 00000  # All 9's become 0
        }, "All nines"),
        
        (10000, {
            'reversed': 00001,
            'digit_sum': 1,  # 1+0+0+0+0
            'incremented': 21111  # 1→2, 0→1, 0→1, 0→1, 0→1
        }, "One followed by zeros"),
        
        (54321, {
            'reversed': 12345,
            'digit_sum': 15,  # 5+4+3+2+1
            'incremented': 65432  # Each digit +1
        }, "Reverse of basic example"),
        
        (88888, {
            'reversed': 88888,
            'digit_sum': 40,  # 8+8+8+8+8
            'incremented': 99999  # Each digit +1
        }, "All eights"),
    ]
    
    all_passed = True
    
    for number, expected, description in test_cases:
        print(f"\nTest: {description}")
        print(f"Input: {number}")
        
        try:
            results = machine.process_number(number)
            
            # Check each result
            errors = []
            for key in ['reversed', 'digit_sum', 'incremented']:
                if results[key] != expected[key]:
                    errors.append(f"{key}: expected {expected[key]}, got {results[key]}")
            
            if errors:
                all_passed = False
                print(f"  ✗ FAILED")
                for error in errors:
                    print(f"    {error}")
            else:
                print(f"  ✓ PASSED")
                print(f"    Reversed: {results['reversed']}")
                print(f"    Sum of digits: {results['digit_sum']}")
                print(f"    Incremented: {results['incremented']}")
                
        except ValueError as e:
            print(f"  ✗ ERROR: {e}")
            all_passed = False
    
    # Test invalid inputs
    print("\n" + "-" * 50)
    print("Testing invalid inputs:")
    
    invalid_inputs = [
        (1234, "Four-digit number"),
        (123456, "Six-digit number"),
        (-12345, "Negative number"),
        ("12345", "String instead of number"),
        (12.345, "Float instead of integer"),
    ]
    
    for invalid_num, description in invalid_inputs:
        try:
            results = machine.process_number(invalid_num)
            print(f"  ✗ {description}: Should have raised error but didn't")
            all_passed = False
        except (ValueError, TypeError):
            print(f"  ✓ {description}: Correctly rejected")
    
    return all_passed


def interactive_mode():
    """Interactive mode for users to test their own numbers."""
    print("\n" + "=" * 50)
    print("INTERACTIVE NUMBER MACHINE")
    print("=" * 50)
    print("Enter a five-digit number to process (or 'quit' to exit):")
    
    machine = NumberMachine()
    
    while True:
        user_input = input("\nEnter a five-digit number: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            break
        
        try:
            # Try to convert to integer
            number = int(user_input)
            
            if not machine.validate_input(number):
                print("Error: Please enter a valid five-digit number (10000-99999)")
                continue
            
            # Process and display results
            results = machine.process_number(number)
            machine.display_results(results)
            
            # Show step-by-step explanation
            print("\nStep-by-step explanation:")
            print(f"1. Reverse {number}:")
            temp = number
            rev_steps = []
            while temp > 0:
                digit = temp % 10
                rev_steps.append(str(digit))
                temp //= 10
            print(f"   Digits extracted (from right to left): {', '.join(rev_steps)}")
            print(f"   Reconstructed as: {''.join(rev_steps)} = {results['reversed']}")
            
            print(f"\n2. Sum of digits of {number}:")
            temp = number
            sum_steps = []
            while temp > 0:
                digit = temp % 10
                sum_steps.append(str(digit))
                temp //= 10
            print(f"   Digits: {', '.join(sum_steps[::-1])}")
            print(f"   Sum: {' + '.join(sum_steps[::-1])} = {results['digit_sum']}")
            
            print(f"\n3. Add 1 to each digit of {number}:")
            temp = number
            orig_digits = []
            new_digits = []
            while temp > 0:
                digit = temp % 10
                orig_digits.append(digit)
                new_digit = (digit + 1) % 10
                new_digits.append(new_digit)
                temp //= 10
            orig_digits.reverse()
            new_digits.reverse()
            print(f"   Original digits: {orig_digits}")
            print(f"   After adding 1:  {new_digits}")
            print(f"   New number: {results['incremented']:05d}")  # Pad with leading zeros if needed
            
        except ValueError:
            print("Error: Please enter a valid integer")
        except Exception as e:
            print(f"Unexpected error: {e}")


def demonstrate_modulus_operator():
    """Demonstrate how the modulus operator works for this problem."""
    print("\n" + "=" * 50)
    print("DEMONSTRATING MODULUS OPERATOR USAGE")
    print("=" * 50)
    
    example = 12345
    print(f"Example number: {example}")
    print()
    
    print("1. Extracting digits using % operator:")
    temp = example
    step = 1
    while temp > 0:
        digit = temp % 10
        print(f"   Step {step}: {temp} % 10 = {digit} (last digit)")
        print(f"        {temp} // 10 = {temp // 10} (remaining digits)")
        temp = temp // 10
        step += 1
    
    print("\n2. Reversing a number using % and * operators:")
    temp = example
    reversed_num = 0
    print(f"   Start: reversed_num = 0")
    while temp > 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        print(f"   Get digit {digit}, reversed_num = {reversed_num // 10} * 10 + {digit} = {reversed_num}")
        temp = temp // 10
    
    print(f"\n   Final reversed number: {reversed_num}")
    
    print("\n3. Handling 9+1 overflow:")
    print(f"   For digit 9: (9 + 1) % 10 = {10 % 10} = 0")
    print(f"   For digit 5: (5 + 1) % 10 = {6 % 10} = 6")


def main():
    """Main function to run all demonstrations."""
    print("NUMBER MACHINE IMPLEMENTATION")
    print("=" * 50)
    print("This machine performs three transformations on five-digit numbers:")
    print("1. Reverse the number")
    print("2. Calculate sum of digits")
    print("3. Add 1 to each digit (9+1 wraps to 0)")
    print("=" * 50)
    
    # Run demonstrations
    manual_verification_example()
    
    print("\n" + "=" * 50)
    print("RUNNING AUTOMATED TESTS")
    print("=" * 50)
    
    if test_number_machine():
        print("\n✓ All automated tests passed!")
    else:
        print("\n✗ Some tests failed!")
    
    demonstrate_modulus_operator()
    interactive_mode()
    
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    print("""
    Key techniques used:
    1. Modulus operator (%): Extracts the last digit of a number
    2. Integer division (//): Removes the last digit
    3. Digit reconstruction: reversed_num = reversed_num * 10 + digit
    4. Overflow handling: (digit + 1) % 10 for 9+1=0 case
    
    The number machine successfully implements all three required
    transformations using only basic arithmetic operations without
    converting to strings or using built-in reversal functions.
    """)


if __name__ == "__main__":
    main()