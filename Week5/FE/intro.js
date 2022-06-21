const add = (a, b) => a + b;
const subtract = (a, b) => a - b;
const multiply = (a, b) => a * b;
const divide = (a, b) => a / b;

function calculator(operation, num1, num2) {
  const result = operation(num1, num2);
  console.log(result);
  return result;
}

calculator(add, 34, 56);
calculator(subtract, 100, 56);
calculator(multiply, 343, 56);
calculator(divide, 394, 56);
