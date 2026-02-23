document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("bmiForm");
  const resultDiv = document.getElementById("result");

  form.addEventListener("submit", (event) => {
    event.preventDefault();

    const weight = parseFloat(document.getElementById("weight").value);
    const height = parseFloat(document.getElementById("height").value);

    if (isNaN(weight) || isNaN(height) || height <= 0) {
      resultDiv.textContent = "Please enter valid numbers.";
      return;
    }

    // BMI formula
    const bmi = weight / (height * height);
    const rounded = bmi.toFixed(2);

    let status;
    if (bmi < 18.5) {
      status = "Underweight";
    } else if (bmi < 25) {
      status = "Normal weight";
    } else if (bmi < 30) {
      status = "Overweight";
    } else {
      status = "Obese";
    }

    resultDiv.textContent = `Your BMI is ${rounded} (${status}).`;
  });
});
