import os
import sys
import uuid

# Data for the first 15 white belt problems
problems = [
    {
        "id": 1,
        "title": "Hello World",
        "statement": "Your first task is to print the string \"Hello, Dojo!\" to the console.",
        "input_desc": "",
        "output_desc": "```\nHello, Dojo!\n```",
        "example_input": "",
        "example_output": "",
        "constraints": "Ensure the output matches the required string exactly.",
        "explanation": "Use the standard output function of your language to print the required string.",
        "c_solution": """#include <stdio.h>

int main() {
    printf("Hello, Dojo!\\n");
    return 0;
}""",
        "cpp_solution": """#include <iostream>

int main() {
    std::cout << "Hello, Dojo!" << std::endl;
    return 0;
}""",
        "java_solution": """public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, Dojo!");
    }
}""",
        "python_solution": """print("Hello, Dojo!")""",
        "javascript_solution": """console.log("Hello, Dojo!");"""
    },
    {
        "id": 2,
        "title": "Sum of Two",
        "statement": "Read two integers from the input and print their sum.",
        "input_desc": "Two space-separated integers, `a` and `b`.",
        "output_desc": "A single integer representing the sum.",
        "example_input": "5 10",
        "example_output": "15",
        "constraints": "-1,000,000,000 <= a, b <= 1,000,000,000",
        "explanation": "Declare two integer variables, read the values from standard input, and print their sum.",
        "c_solution": """#include <stdio.h>

int main() {
    long long a, b;
    scanf("%lld %lld", &a, &b);
    printf("%lld\\n", a + b);
    return 0;
}""",
        "cpp_solution": """#include <iostream>

int main() {
    long long a, b;
    std::cin >> a >> b;
    std::cout << a + b << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();
        long b = sc.nextLong();
        System.out.println(a + b);
    }
}""",
        "python_solution": """a, b = map(int, input().split())
print(a + b)""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const [a, b] = line.split(' ').map(Number);
    console.log(a + b);
    rl.close();
});"""
    },
    {
        "id": 3,
        "title": "Area of a Rectangle",
        "statement": "Given two integers, `length` and `width`, calculate and print the area of a rectangle.",
        "input_desc": "Two space-separated integers, `length` and `width`.",
        "output_desc": "A single integer representing the area.",
        "example_input": "5 10",
        "example_output": "50",
        "constraints": "1 <= length, width <= 1000",
        "explanation": "The area is calculated by multiplying length and width. Read the two integers and print their product.",
        "c_solution": """#include <stdio.h>

int main() {
    int length, width;
    scanf("%d %d", &length, &width);
    printf("%lld\\n", (long long)length * width);
    return 0;
}""",
        "cpp_solution": """#include <iostream>

int main() {
    int length, width;
    std::cin >> length >> width;
    long long area = (long long)length * width;
    std::cout << area << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int length = sc.nextInt();
        int width = sc.nextInt();
        System.out.println((long)length * width);
    }
}""",
        "python_solution": """length, width = map(int, input().split())
print(length * width)""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const [length, width] = line.split(' ').map(Number);
    console.log(length * width);
    rl.close();
});"""
    },
    {
        "id": 4,
        "title": "Even or Odd",
        "statement": "Given an integer `N`, determine if it is \"Even\" or \"Odd\".",
        "input_desc": "A single integer `N`.",
        "output_desc": "Print \"Even\" or \"Odd\".",
        "example_input": "7",
        "example_output": "Odd",
        "constraints": "-1,000,000,000 <= N <= 1,000,000,000",
        "explanation": "An integer is even if it's perfectly divisible by 2. Use the modulo operator (`%`). If `N % 2` is 0, it's even.",
        "c_solution": """#include <stdio.h>

int main() {
    long long n;
    scanf("%lld", &n);
    if (n % 2 == 0) {
        printf("Even\\n");
    } else {
        printf("Odd\\n");
    }
    return 0;
}""",
        "cpp_solution": """#include <iostream>

int main() {
    long long n;
    std::cin >> n;
    if (n % 2 == 0) {
        std::cout << "Even" << std::endl;
    } else {
        std::cout << "Odd" << std::endl;
    }
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        System.out.println(n % 2 == 0 ? "Even" : "Odd");
    }
}""",
        "python_solution": """n = int(input())
if n % 2 == 0:
    print("Even")
else:
    print("Odd")""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const n = parseInt(line);
    console.log(n % 2 === 0 ? "Even" : "Odd");
    rl.close();
});"""
    },
    {
        "id": 5,
        "title": "Positive Negative or Zero",
        "statement": "Given an integer `N`, determine if it is \"Positive\", \"Negative\", or \"Zero\".",
        "input_desc": "A single integer `N`.",
        "output_desc": "Print \"Positive\", \"Negative\", or \"Zero\".",
        "example_input": "-5",
        "example_output": "Negative",
        "constraints": "-1,000,000,000 <= N <= 1,000,000,000",
        "explanation": "Use an if-elif-else structure. If `N > 0`, it's positive. If `N < 0`, it's negative. Otherwise, it's zero.",
        "c_solution": """#include <stdio.h>

int main() {
    long long n;
    scanf("%lld", &n);
    if (n > 0) {
        printf("Positive\\n");
    } else if (n < 0) {
        printf("Negative\\n");
    } else {
        printf("Zero\\n");
    }
    return 0;
}""",
        "cpp_solution": """#include <iostream>

int main() {
    long long n;
    std::cin >> n;
    if (n > 0) {
        std::cout << "Positive" << std::endl;
    } else if (n < 0) {
        std::cout << "Negative" << std::endl;
    } else {
        std::cout << "Zero" << std::endl;
    }
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        if (n > 0) {
            System.out.println("Positive");
        } else if (n < 0) {
            System.out.println("Negative");
        } else {
            System.out.println("Zero");
        }
    }
}""",
        "python_solution": """n = int(input())
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const n = parseInt(line);
    if (n > 0) {
        console.log("Positive");
    } else if (n < 0) {
        console.log("Negative");
    } else {
        console.log("Zero");
    }
    rl.close();
});"""
    },
    {
        "id": 6,
        "title": "Leap Year Check",
        "statement": "Given a year, determine if it is a leap year. A year is a leap year if it is divisible by 4, except for end-of-century years, which must be divisible by 400.",
        "input_desc": "A single integer `year`.",
        "output_desc": "Print \"Yes\" or \"No\".",
        "example_input": "2000",
        "example_output": "Yes",
        "constraints": "1 <= year <= 10000",
        "explanation": "A year is a leap year if `(year % 4 == 0 AND year % 100 != 0) OR (year % 400 == 0)`.",
        "c_solution": """#include <stdio.h>

int main() {
    int year;
    scanf("%d", &year);
    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
        printf("Yes\\n");
    } else {
        printf("No\\n");
    }
    return 0;
}""",
        "cpp_solution": """#include <iostream>

int main() {
    int year;
    std::cin >> year;
    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
        std::cout << "Yes" << std::endl;
    } else {
        std::cout << "No" << std::endl;
    }
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int year = sc.nextInt();
        if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}""",
        "python_solution": """year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Yes")
else:
    print("No")""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const year = parseInt(line);
    if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {
        console.log("Yes");
    } else {
        console.log("No");
    }
    rl.close();
});"""
    },
    {
        "id": 7,
        "title": "Largest of Three Numbers",
        "statement": "Given three integers, find and print the largest one.",
        "input_desc": "Three space-separated integers `a`, `b`, and `c`.",
        "output_desc": "The largest of the three integers.",
        "example_input": "15 99 42",
        "example_output": "99",
        "constraints": "-1,000,000,000 <= a, b, c <= 1,000,000,000",
        "explanation": "Use the built-in `max()` function or nested if-else statements to compare the three numbers.",
        "c_solution": """#include <stdio.h>

int main() {
    long long a, b, c;
    scanf("%lld %lld %lld", &a, &b, &c);
    long long max = a;
    if (b > max) max = b;
    if (c > max) max = c;
    printf("%lld\\n", max);
    return 0;
}""",
        "cpp_solution": """#include <iostream>
#include <algorithm>

int main() {
    long long a, b, c;
    std::cin >> a >> b >> c;
    std::cout << std::max({a, b, c}) << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();
        long b = sc.nextLong();
        long c = sc.nextLong();
        System.out.println(Math.max(a, Math.max(b, c)));
    }
}""",
        "python_solution": """a, b, c = map(int, input().split())
print(max(a, b, c))""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const [a, b, c] = line.split(' ').map(Number);
    console.log(Math.max(a, b, c));
    rl.close();
});"""
    },
    {
        "id": 8,
        "title": "Simple Interest",
        "statement": "Given principal `P`, rate `R`, and time `T`, calculate the simple interest using the formula `SI = (P * R * T) / 100`.",
        "input_desc": "Three space-separated numbers: `P` (integer), `R` (float), `T` (integer).",
        "output_desc": "The simple interest.",
        "example_input": "1000 7.5 2",
        "example_output": "150.0",
        "constraints": "1 <= P, T <= 100000, 0.0 <= R <= 100.0",
        "explanation": "Read the inputs and apply the formula. Use floating-point variables for calculation to ensure precision.",
        "c_solution": """#include <stdio.h>

int main() {
    int p, t;
    float r;
    scanf("%d %f %d", &p, &r, &t);
    float si = (p * r * t) / 100.0;
    printf("%.1f\\n", si);
    return 0;
}""",
        "cpp_solution": """#include <iostream>
#include <iomanip>

int main() {
    int p, t;
    double r;
    std::cin >> p >> r >> t;
    double si = (p * r * t) / 100.0;
    std::cout << std::fixed << std::setprecision(1) << si << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int p = sc.nextInt();
        float r = sc.nextFloat();
        int t = sc.nextInt();
        float si = (p * r * t) / 100;
        System.out.printf("%.1f\\n", si);
    }
}""",
        "python_solution": """p, r, t = map(float, input().split())
si = (p * r * t) / 100
print(f"{si:.1f}")""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const [p, r, t] = line.split(' ').map(Number);
    const si = (p * r * t) / 100;
    console.log(si.toFixed(1));
    rl.close();
});"""
    },
    {
        "id": 9,
        "title": "Temperature Conversion",
        "statement": "Convert a given temperature from Celsius to Fahrenheit using the formula: `F = C * 9/5 + 32`.",
        "input_desc": "A single number `C` (Celsius).",
        "output_desc": "The temperature in Fahrenheit.",
        "example_input": "37",
        "example_output": "98.6",
        "constraints": "-100.0 <= C <= 100.0",
        "explanation": "Read the Celsius value and apply the conversion formula. Use floating-point division (`9.0/5.0` or `1.8`) for accuracy.",
        "c_solution": """#include <stdio.h>

int main() {
    float celsius;
    scanf("%f", &celsius);
    float fahrenheit = celsius * 9.0 / 5.0 + 32;
    printf("%.1f\\n", fahrenheit);
    return 0;
}""",
        "cpp_solution": """#include <iostream>
#include <iomanip>

int main() {
    double celsius;
    std::cin >> celsius;
    double fahrenheit = celsius * 9.0 / 5.0 + 32;
    std::cout << std::fixed << std::setprecision(1) << fahrenheit << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double celsius = sc.nextDouble();
        double fahrenheit = celsius * 9.0 / 5.0 + 32;
        System.out.printf("%.1f\\n", fahrenheit);
    }
}""",
        "python_solution": """celsius = float(input())
fahrenheit = celsius * 9/5 + 32
print(f"{fahrenheit:.1f}")""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const celsius = parseFloat(line);
    const fahrenheit = celsius * 9/5 + 32;
    console.log(fahrenheit.toFixed(1));
    rl.close();
});"""
    },
    {
        "id": 10,
        "title": "Swap Two Numbers",
        "statement": "Given two integers, `a` and `b`, swap their values and print them.",
        "input_desc": "Two space-separated integers `a` and `b`.",
        "output_desc": "Two space-separated integers, with values swapped.",
        "example_input": "10 20",
        "example_output": "20 10",
        "constraints": "-1,000,000,000 <= a, b <= 1,000,000,000",
        "explanation": "Use a third temporary variable to hold one value while you perform the swap. Python allows for direct tuple assignment `a, b = b, a`.",
        "c_solution": """#include <stdio.h>

int main() {
    long long a, b, temp;
    scanf("%lld %lld", &a, &b);
    temp = a;
    a = b;
    b = temp;
    printf("%lld %lld\\n", a, b);
    return 0;
}""",
        "cpp_solution": """#include <iostream>

int main() {
    long long a, b;
    std::cin >> a >> b;
    std::swap(a, b);
    std::cout << a << " " << b << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();
        long b = sc.nextLong();
        long temp = a;
        a = b;
        b = temp;
        System.out.println(a + " " + b);
    }
}""",
        "python_solution": """a, b = map(int, input().split())
a, b = b, a
print(a, b)""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    let [a, b] = line.split(' ').map(Number);
    [a, b] = [b, a];
    console.log(a + " " + b);
    rl.close();
});"""
    },
    {
        "id": 11,
        "title": "Print Numbers 1 to N",
        "statement": "Given a positive integer `N`, print all numbers from 1 to `N`, each on a new line.",
        "input_desc": "A single integer `N`.",
        "output_desc": "The numbers from 1 to `N`.",
        "example_input": "5",
        "example_output": "1\n2\n3\n4\n5",
        "constraints": "1 <= N <= 1000",
        "explanation": "Use a `for` loop that initializes a counter at 1, continues as long as the counter is less than or equal to `N`, and increments by 1.",
        "c_solution": """#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        printf("%d\\n", i);
    }
    return 0;
}""",
        "cpp_solution": """#include <iostream>

int main() {
    int n;
    std::cin >> n;
    for (int i = 1; i <= n; ++i) {
        std::cout << i << std::endl;
    }
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 1; i <= n; i++) {
            System.out.println(i);
        }
    }
}""",
        "python_solution": """n = int(input())
for i in range(1, n + 1):
    print(i)""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const n = parseInt(line);
    for (let i = 1; i <= n; i++) {
        console.log(i);
    }
    rl.close();
});"""
    },
    {
        "id": 12,
        "title": "Sum of N Natural Numbers",
        "statement": "Given `N`, find the sum of all numbers from 1 to `N`.",
        "input_desc": "A single integer `N`.",
        "output_desc": "The sum of natural numbers up to `N`.",
        "example_input": "10",
        "example_output": "55",
        "constraints": "1 <= N <= 10000",
        "explanation": "While a loop works, the most efficient method is the mathematical formula: `Sum = N * (N + 1) / 2`.",
        "c_solution": """#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    long long sum = (long long)n * (n + 1) / 2;
    printf("%lld\\n", sum);
    return 0;
}""",
        "cpp_solution": """#include <iostream>

int main() {
    int n;
    std::cin >> n;
    long long sum = (long long)n * (n + 1) / 2;
    std::cout << sum << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long sum = (long)n * (n + 1) / 2;
        System.out.println(sum);
    }
}""",
        "python_solution": """n = int(input())
total_sum = n * (n + 1) // 2
print(total_sum)""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const n = parseInt(line);
    const sum = n * (n + 1) / 2;
    console.log(sum);
    rl.close();
});"""
    },
    {
        "id": 13,
        "title": "Multiplication Table",
        "statement": "Given an integer `N`, print its multiplication table from 1 to 10.",
        "input_desc": "A single integer `N`.",
        "output_desc": "The table in the format 'N x i = result'.",
        "example_input": "5",
        "example_output": "5 x 1 = 5\n5 x 2 = 10\n...\n5 x 10 = 50",
        "constraints": "1 <= N <= 1000",
        "explanation": "Use a `for` loop that iterates from 1 to 10. In each iteration, print the formatted string with the product.",
        "c_solution": """#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    for (int i = 1; i <= 10; i++) {
        printf("%d x %d = %d\\n", n, i, n * i);
    }
    return 0;
}""",
        "cpp_solution": """#include <iostream>

int main() {
    int n;
    std::cin >> n;
    for (int i = 1; i <= 10; ++i) {
        std::cout << n << " x " << i << " = " << n * i << std::endl;
    }
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 1; i <= 10; i++) {
            System.out.println(n + " x " + i + " = " + (n * i));
        }
    }
}""",
        "python_solution": """n = int(input())
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const n = parseInt(line);
    for (let i = 1; i <= 10; i++) {
        console.log(`${n} x ${i} = ${n * i}`);
    }
    rl.close();
});"""
    },
    {
        "id": 14,
        "title": "Factorial Iterative",
        "statement": "Calculate the factorial of a number `N` (N!).",
        "input_desc": "A single integer `N`.",
        "output_desc": "The factorial of `N`.",
        "example_input": "5",
        "example_output": "120",
        "constraints": "0 <= N <= 20",
        "explanation": "Initialize a result variable to 1. Loop from 1 to N, multiplying the result by the loop counter in each step. Factorial of 0 is 1.",
        "c_solution": """#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    long long factorial = 1;
    for (int i = 1; i <= n; i++) {
        factorial *= i;
    }
    printf("%lld\\n", factorial);
    return 0;
}""",
        "cpp_solution": """#include <iostream>

int main() {
    int n;
    std::cin >> n;
    long long factorial = 1;
    for (int i = 1; i <= n; ++i) {
        factorial *= i;
    }
    std::cout << factorial << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long factorial = 1;
        for (int i = 1; i <= n; i++) {
            factorial *= i;
        }
        System.out.println(factorial);
    }
}""",
        "python_solution": """n = int(input())
factorial = 1
if n == 0:
    print(1)
else:
    for i in range(1, n + 1):
        factorial *= i
    print(factorial)""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const n = parseInt(line);
    let factorial = 1n;
    for (let i = 1; i <= n; i++) {
        factorial *= BigInt(i);
    }
    console.log(factorial.toString());
    rl.close();
});"""
    },
    {
        "id": 15,
        "title": "Count Digits",
        "statement": "Count the number of digits in a given integer.",
        "input_desc": "A single integer `N`.",
        "output_desc": "The number of digits in `N`.",
        "example_input": "12345",
        "example_output": "5",
        "constraints": "0 <= N <= 1,000,000,000",
        "explanation": "Use a while loop. Repeatedly divide the number by 10 and increment a counter until the number becomes 0. A special case is input 0, which has 1 digit.",
        "c_solution": """#include <stdio.h>

int main() {
    long long n;
    scanf("%lld", &n);
    if (n == 0) {
        printf("1\\n");
        return 0;
    }
    int count = 0;
    if (n < 0) n = -n;
    while (n > 0) {
        n /= 10;
        count++;
    }
    printf("%d\\n", count);
    return 0;
}""",
        "cpp_solution": """#include <iostream>

int main() {
    long long n;
    std::cin >> n;
    if (n == 0) {
        std::cout << 1 << std::endl;
        return 0;
    }
    int count = 0;
    if (n < 0) n = -n;
    while (n > 0) {
        n /= 10;
        count++;
    }
    std::cout << count << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        if (n == 0) {
            System.out.println(1);
            return;
        }
        if (n < 0) n = -n;
        int count = 0;
        while (n > 0) {
            n /= 10;
            count++;
        }
        System.out.println(count);
    }
}""",
        "python_solution": """n = int(input())
if n == 0:
    print(1)
else:
    print(len(str(abs(n))))""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const n = parseInt(line);
    if (n === 0) {
        console.log(1);
    } else {
        console.log(String(Math.abs(n)).length);
    }
    rl.close();
});"""
    },
]

# Template for README.md
readme_template = """# Problem {id}: {title}

## Problem Statement
{statement}

## Input
{input_desc}

## Output
{output_desc}

## Example
**Input:**
```
{example_input}
```

**Output:**
```
{example_output}
```

## Constraints
{constraints}

## Explanation
{explanation}
"""

# Template for solution.md
solution_template = """# Solutions for Problem {id}: {title}

## C Solution
```c
{c_solution}
```

## C++ Solution
```cpp
{cpp_solution}
```

## Java Solution
```java
{java_solution}
```

## Python Solution
```python
{python_solution}
```

## JavaScript Solution
```javascript
{javascript_solution}
```
"""

def create_directory_structure():
    # Define the main directory
    main_dir = "WhiteBeltProblems"
    
    try:
        # Create main directory if it doesn't exist
        if not os.path.exists(main_dir):
            os.makedirs(main_dir)
        else:
            print(f"Directory '{main_dir}' already exists. Proceeding to create problem directories.")
        
        # Iterate through each problem
        for problem in problems:
            problem_id = problem["id"]
            problem_title = problem["title"]
            
            # Create problem directory directly under main_dir
            problem_dir_name = f"Problem_{problem_id}_{problem_title.replace(' ', '_')}"
            problem_dir = os.path.join(main_dir, problem_dir_name)
            
            try:
                if not os.path.exists(problem_dir):
                    os.makedirs(problem_dir)
                else:
                    print(f"Problem directory '{problem_dir}' already exists. Skipping directory creation.")
                
                # Create README.md
                readme_content = readme_template.format(
                    id=problem_id,
                    title=problem_title,
                    statement=problem["statement"],
                    input_desc=problem["input_desc"],
                    output_desc=problem["output_desc"],
                    example_input=problem["example_input"],
                    example_output=problem["example_output"],
                    constraints=problem["constraints"],
                    explanation=problem["explanation"]
                )
                
                readme_path = os.path.join(problem_dir, "README.md")
                with open(readme_path, "w", encoding="utf-8") as f:
                    f.write(readme_content)
                
                # Create solution.md
                solution_content = solution_template.format(
                    id=problem_id,
                    title=problem_title,
                    c_solution=problem["c_solution"],
                    cpp_solution=problem["cpp_solution"],
                    java_solution=problem["java_solution"],
                    python_solution=problem["python_solution"],
                    javascript_solution=problem["javascript_solution"]
                )
                
                solution_path = os.path.join(problem_dir, "solution.md")
                with open(solution_path, "w", encoding="utf-8") as f:
                    f.write(solution_content)
                
                print(f"Created files for Problem {problem_id} in '{problem_dir}'")
                
            except OSError as e:
                print(f"Error creating directory or files for Problem {problem_id}: {e}")
                continue
                
    except OSError as e:
        print(f"Error creating main directory '{main_dir}': {e}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        create_directory_structure()
        print("Directory structure and files created successfully for problems 1-15.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)