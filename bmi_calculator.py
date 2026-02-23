"""Simple BMI calculator project
Users input height and weight, compute BMI, and display status.
"""


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI given weight in kilograms and height in meters.

    Returns:
        float: the computed BMI value.
    """
    if height_m <= 0:
        raise ValueError("Height must be greater than zero.")
    return weight_kg / (height_m ** 2)


if __name__ == "__main__":
    print("BMI Calculator")
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        bmi_value = calculate_bmi(weight, height)
        print(f"Your BMI is: {bmi_value:.2f}")

        # Determine health status based on BMI tiers
        if bmi_value < 18.5:
            status = "Underweight"
        elif 18.5 <= bmi_value < 25:
            status = "Normal weight"
        elif 25 <= bmi_value < 30:
            status = "Overweight"
        else:
            status = "Obese"

        print(f"Health status: {status}")
    except ValueError as e:
        print(f"Error: {e}")
