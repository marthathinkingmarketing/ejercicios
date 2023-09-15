// Calcular el área de un triángulo.
var base = parseFloat(prompt("Por favor, ingresa la base del triangulo:"));
var altura = parseFloat( prompt("Por favor, ingresa la altura del rectángulo:"));
var area = base * altura
alert("El área del rectángulo es: " + area)

//Convertir grados Celsius a Fahrenheit.

var Celsius = parseFloat(prompt("ingresa la temperatura en grados Celsius: "));
var Fahrenheit = (Celsius* 9/5) + 32;
console.log(Celsius + "grados Celsius son equivalentes a " + Fahrenheit + "grados Farenheit.");
alert(Celsius + " grados Celsius son equivalentes a " + Fahrenheit + " grados Farenheit.")

//Encontrar el máximo de dos números.

var numero1 = 35;
var numero2 = 55;
var maximo = encontrarMaximo(numero1, numero2);

function encontrarMaximo(num1, num2) {
    if (num1 > num2) {
      return num1;
    } else {
      return num2;
    }
  }
  
  console.log("El número máximo es: " + maximo);


//Encontrar el mínimo de dos números.

var numero1 = 35;
var numero2 = 55;
var minimo = encontrarMinimo(numero1, numero2);

function encontrarMinimo(num1, num2) {
    if (num1 < num2) {
      return num1;
    } else {
      return num2;
    }
  }
  
  console.log("El número mínimo es: " + minimo);

//Calcular el factorial de un número.

const numero = 5;
const factorial = calcularFactorial(numero);

function calcularFactorial(numero) {
    if (numero < 0) {
      return "El factorial no está definido para números negativos";
    } else if (numero === 0 || numero === 1) {
      return 1;
    } else {
      let factorial = 1;
      for (let i = 2; i <= numero; i++) {
        factorial *= i;
      }
      return factorial;
    }
  }

  console.log("El factorial de ",numero,"es ", factorial);

