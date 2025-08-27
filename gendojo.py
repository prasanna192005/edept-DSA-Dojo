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
    {
        "id": 16,
        "title": "Reverse Number",
        "statement": "Given an integer `N`, reverse its digits and print the result.",
        "input_desc": "A single integer `N`.",
        "output_desc": "The reversed integer.",
        "example_input": "123",
        "example_output": "321",
        "constraints": "-1,000,000,000 <= N <= 1,000,000,000",
        "explanation": "Convert the number to a string and reverse it, or use a mathematical approach by extracting digits with modulo and division.",
        "c_solution": """#include <stdio.h>

int main() {
    long long n, reversed = 0;
    scanf("%lld", &n);
    int is_negative = n < 0;
    if (is_negative) n = -n;
    while (n > 0) {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }
    printf("%lld\\n", is_negative ? -reversed : reversed);
    return 0;
}""",
        "cpp_solution": """#include <iostream>

int main() {
    long long n, reversed = 0;
    std::cin >> n;
    int is_negative = n < 0;
    if (is_negative) n = -n;
    while (n > 0) {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }
    std::cout << (is_negative ? -reversed : reversed) << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        boolean isNegative = n < 0;
        if (isNegative) n = -n;
        long reversed = 0;
        while (n > 0) {
            reversed = reversed * 10 + n % 10;
            n /= 10;
        }
        System.out.println(isNegative ? -reversed : reversed);
    }
}""",
        "python_solution": """n = int(input())
is_negative = n < 0
if is_negative:
    n = -n
reversed_num = int(str(n)[::-1])
print(-reversed_num if is_negative else reversed_num)""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    let n = parseInt(line);
    const isNegative = n < 0;
    if (isNegative) n = -n;
    const reversed = parseInt(n.toString().split('').reverse().join(''));
    console.log(isNegative ? -reversed : reversed);
    rl.close();
});"""
    },
    {
        "id": 17,
        "title": "Sum of Digits",
        "statement": "Given an integer `N`, calculate the sum of its digits.",
        "input_desc": "A single integer `N`.",
        "output_desc": "The sum of digits of `N`.",
        "example_input": "123",
        "example_output": "6",
        "constraints": "0 <= N <= 1,000,000,000",
        "explanation": "Extract each digit using modulo (`% 10`) and division (`/ 10`), or convert to a string and sum the characters as integers.",
        "c_solution": """#include <stdio.h>

int main() {
    long long n;
    scanf("%lld", &n);
    if (n < 0) n = -n;
    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    printf("%d\\n", sum);
    return 0;
}""",
        "cpp_solution": """#include <iostream>

int main() {
    long long n;
    std::cin >> n;
    if (n < 0) n = -n;
    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    std::cout << sum << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        if (n < 0) n = -n;
        int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        System.out.println(sum);
    }
}""",
        "python_solution": """n = abs(int(input()))
print(sum(int(digit) for digit in str(n)))""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const n = Math.abs(parseInt(line));
    const sum = n.toString().split('').reduce((acc, digit) => acc + parseInt(digit), 0);
    console.log(sum);
    rl.close();
});"""
    },
    {
        "id": 18,
        "title": "Print Even Numbers",
        "statement": "Given `N`, print all even numbers from 2 to `N` in a single line, space-separated.",
        "input_desc": "A single integer `N`.",
        "output_desc": "All even numbers from 2 to `N`, space-separated.",
        "example_input": "10",
        "example_output": "2 4 6 8 10",
        "constraints": "2 <= N <= 1000",
        "explanation": "Use a loop to iterate from 2 to N with a step of 2, or check each number with modulo to identify evens.",
        "c_solution": """#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    for (int i = 2; i <= n; i += 2) {
        printf("%d", i);
        if (i < n) printf(" ");
    }
    printf("\\n");
    return 0;
}""",
        "cpp_solution": """#include <iostream>

int main() {
    int n;
    std::cin >> n;
    for (int i = 2; i <= n; i += 2) {
        std::cout << i;
        if (i < n) std::cout << " ";
    }
    std::cout << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 2; i <= n; i += 2) {
            System.out.print(i);
            if (i < n) System.out.print(" ");
        }
        System.out.println();
    }
}""",
        "python_solution": """n = int(input())
print(*[i for i in range(2, n + 1, 2)])""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const n = parseInt(line);
    const evens = [];
    for (let i = 2; i <= n; i += 2) {
        evens.push(i);
    }
    console.log(evens.join(' '));
    rl.close();
});"""
    },
    {
        "id": 19,
        "title": "Fibonacci Sequence",
        "statement": "Given `N`, print the first `N` numbers of the Fibonacci sequence (starting with 0, 1).",
        "input_desc": "A single integer `N`.",
        "output_desc": "The first `N` Fibonacci numbers, space-separated.",
        "example_input": "7",
        "example_output": "0 1 1 2 3 5 8",
        "constraints": "1 <= N <= 20",
        "explanation": "Use a loop to generate Fibonacci numbers, where each number is the sum of the two preceding ones. Store results in a list or print directly.",
        "c_solution": """#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    long long a = 0, b = 1;
    if (n >= 1) printf("%lld", a);
    if (n >= 2) printf(" %lld", b);
    for (int i = 3; i <= n; i++) {
        long long next = a + b;
        printf(" %lld", next);
        a = b;
        b = next;
    }
    printf("\\n");
    return 0;
}""",
        "cpp_solution": """#include <iostream>

int main() {
    int n;
    std::cin >> n;
    long long a = 0, b = 1;
    if (n >= 1) std::cout << a;
    if (n >= 2) std::cout << " " << b;
    for (int i = 3; i <= n; ++i) {
        long long next = a + b;
        std::cout << " " << next;
        a = b;
        b = next;
    }
    std::cout << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long a = 0, b = 1;
        if (n >= 1) System.out.print(a);
        if (n >= 2) System.out.print(" " + b);
        for (int i = 3; i <= n; i++) {
            long next = a + b;
            System.out.print(" " + next);
            a = b;
            b = next;
        }
        System.out.println();
    }
}""",
        "python_solution": """n = int(input())
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
print(*fib[:n])""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const n = parseInt(line);
    const fib = [0, 1];
    for (let i = 2; i < n; i++) {
        fib.push(fib[i-1] + fib[i-2]);
    }
    console.log(fib.slice(0, n).join(' '));
    rl.close();
});"""
    },
    {
        "id": 20,
        "title": "Count Divisors",
        "statement": "Given an integer `N`, count the number of its positive divisors.",
        "input_desc": "A single integer `N`.",
        "output_desc": "The number of positive divisors of `N`.",
        "example_input": "6",
        "example_output": "4",
        "constraints": "1 <= N <= 1,000,000",
        "explanation": "A number is a divisor if it divides `N` without a remainder. Check each number from 1 to N, or optimize by checking up to the square root.",
        "c_solution": """#include <stdio.h>
#include <math.h>

int main() {
    int n, count = 0;
    scanf("%d", &n);
    for (int i = 1; i <= sqrt(n); i++) {
        if (n % i == 0) {
            count++;
            if (i != n / i) count++;
        }
    }
    printf("%d\\n", count);
    return 0;
}""",
        "cpp_solution": """#include <iostream>
#include <cmath>

int main() {
    int n, count = 0;
    std::cin >> n;
    for (int i = 1; i <= std::sqrt(n); ++i) {
        if (n % i == 0) {
            count++;
            if (i != n / i) count++;
        }
    }
    std::cout << count << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int count = 0;
        for (int i = 1; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                count++;
                if (i != n / i) count++;
            }
        }
        System.out.println(count);
    }
}""",
        "python_solution": """n = int(input())
count = 0
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        count += 1
        if i != n // i:
            count += 1
print(count)""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const n = parseInt(line);
    let count = 0;
    for (let i = 1; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            count++;
            if (i !== n / i) count++;
        }
    }
    console.log(count);
    rl.close();
});"""
    },
    {
        "id": 21,
        "title": "Sum of Array",
        "statement": "Given an array of `N` integers, calculate their sum.",
        "input_desc": "The first line contains `N`, the size of the array. The second line contains `N` space-separated integers.",
        "output_desc": "The sum of the array elements.",
        "example_input": "5\n1 2 3 4 5",
        "example_output": "15",
        "constraints": "1 <= N <= 1000, -10^6 <= array elements <= 10^6",
        "explanation": "Read the array size and elements, then sum them using a loop or built-in sum function.",
        "c_solution": """#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    long long sum = 0;
    for (int i = 0; i < n; i++) {
        int x;
        scanf("%d", &x);
        sum += x;
    }
    printf("%lld\\n", sum);
    return 0;
}""",
        "cpp_solution": """#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    long long sum = 0;
    for (int i = 0; i < n; ++i) {
        int x;
        std::cin >> x;
        sum += x;
    }
    std::cout << sum << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long sum = 0;
        for (int i = 0; i < n; i++) {
            sum += sc.nextInt();
        }
        System.out.println(sum);
    }
}""",
        "python_solution": """n = int(input())
arr = list(map(int, input().split()))
print(sum(arr))""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
let input = [];
rl.on('line', (line) => {
    input.push(line);
    if (input.length === 2) {
        const arr = input[1].split(' ').map(Number);
        const sum = arr.reduce((acc, val) => acc + val, 0);
        console.log(sum);
        rl.close();
    }
});"""
    },
    {
        "id": 22,
        "title": "Maximum in Array",
        "statement": "Given an array of `N` integers, find the maximum element.",
        "input_desc": "The first line contains `N`, the size of the array. The second line contains `N` space-separated integers.",
        "output_desc": "The maximum element in the array.",
        "example_input": "5\n3 7 2 9 1",
        "example_output": "9",
        "constraints": "1 <= N <= 1000, -10^6 <= array elements <= 10^6",
        "explanation": "Iterate through the array and keep track of the maximum value using a variable.",
        "c_solution": """#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int max = -1000001;
    for (int i = 0; i < n; i++) {
        int x;
        scanf("%d", &x);
        if (x > max) max = x;
    }
    printf("%d\\n", max);
    return 0;
}""",
        "cpp_solution": """#include <iostream>
#include <algorithm>

int main() {
    int n;
    std::cin >> n;
    int max = -1000001;
    for (int i = 0; i < n; ++i) {
        int x;
        std::cin >> x;
        max = std::max(max, x);
    }
    std::cout << max << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int max = -1000001;
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            max = Math.max(max, x);
        }
        System.out.println(max);
    }
}""",
        "python_solution": """n = int(input())
arr = list(map(int, input().split()))
print(max(arr))""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
let input = [];
rl.on('line', (line) => {
    input.push(line);
    if (input.length === 2) {
        const arr = input[1].split(' ').map(Number);
        console.log(Math.max(...arr));
        rl.close();
    }
});"""
    },
    {
        "id": 23,
        "title": "Reverse Array",
        "statement": "Given an array of `N` integers, print the array in reverse order.",
        "input_desc": "The first line contains `N`, the size of the array. The second line contains `N` space-separated integers.",
        "output_desc": "The array elements in reverse order, space-separated.",
        "example_input": "5\n1 2 3 4 5",
        "example_output": "5 4 3 2 1",
        "constraints": "1 <= N <= 1000, -10^6 <= array elements <= 10^6",
        "explanation": "Store the array and print its elements from the last index to the first, or reverse the array in-place and print.",
        "c_solution": """#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int arr[1000];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    for (int i = n - 1; i >= 0; i--) {
        printf("%d", arr[i]);
        if (i > 0) printf(" ");
    }
    printf("\\n");
    return 0;
}""",
        "cpp_solution": """#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
    }
    for (int i = n - 1; i >= 0; --i) {
        std::cout << arr[i];
        if (i > 0) std::cout << " ";
    }
    std::cout << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        for (int i = n - 1; i >= 0; i--) {
            System.out.print(arr[i]);
            if (i > 0) System.out.print(" ");
        }
        System.out.println();
    }
}""",
        "python_solution": """n = int(input())
arr = list(map(int, input().split()))
print(*arr[::-1])""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
let input = [];
rl.on('line', (line) => {
    input.push(line);
    if (input.length === 2) {
        const arr = input[1].split(' ').map(Number);
        console.log(arr.reverse().join(' '));
        rl.close();
    }
});"""
    },
    {
        "id": 24,
        "title": "Count Positive Numbers",
        "statement": "Given an array of `N` integers, count how many are positive.",
        "input_desc": "The first line contains `N`, the size of the array. The second line contains `N` space-separated integers.",
        "output_desc": "The count of positive numbers in the array.",
        "example_input": "6\n-2 3 0 5 -1 7",
        "example_output": "3",
        "constraints": "1 <= N <= 1000, -10^6 <= array elements <= 10^6",
        "explanation": "Iterate through the array and increment a counter for each element greater than 0.",
        "c_solution": """#include <stdio.h>

int main() {
    int n, count = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int x;
        scanf("%d", &x);
        if (x > 0) count++;
    }
    printf("%d\\n", count);
    return 0;
}""",
        "cpp_solution": """#include <iostream>

int main() {
    int n, count = 0;
    std::cin >> n;
    for (int i = 0; i < n; ++i) {
        int x;
        std::cin >> x;
        if (x > 0) count++;
    }
    std::cout << count << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (sc.nextInt() > 0) count++;
        }
        System.out.println(count);
    }
}""",
        "python_solution": """n = int(input())
arr = list(map(int, input().split()))
print(sum(1 for x in arr if x > 0))""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
let input = [];
rl.on('line', (line) => {
    input.push(line);
    if (input.length === 2) {
        const arr = input[1].split(' ').map(Number);
        const count = arr.filter(x => x > 0).length;
        console.log(count);
        rl.close();
    }
});"""
    },
    {
        "id": 25,
        "title": "Array Element Frequency",
        "statement": "Given an array of `N` integers, find the frequency of a given number `X`.",
        "input_desc": "The first line contains `N` and `X`. The second line contains `N` space-separated integers.",
        "output_desc": "The number of times `X` appears in the array.",
        "example_input": "5 3\n1 3 2 3 4",
        "example_output": "2",
        "constraints": "1 <= N <= 1000, -10^6 <= X, array elements <= 10^6",
        "explanation": "Iterate through the array and count occurrences of `X`.",
        "c_solution": """#include <stdio.h>

int main() {
    int n, x, count = 0;
    scanf("%d %d", &n, &x);
    for (int i = 0; i < n; i++) {
        int a;
        scanf("%d", &a);
        if (a == x) count++;
    }
    printf("%d\\n", count);
    return 0;
}""",
        "cpp_solution": """#include <iostream>

int main() {
    int n, x, count = 0;
    std::cin >> n >> x;
    for (int i = 0; i < n; ++i) {
        int a;
        std::cin >> a;
        if (a == x) count++;
    }
    std::cout << count << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x = sc.nextInt();
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (sc.nextInt() == x) count++;
        }
        System.out.println(count);
    }
}""",
        "python_solution": """n, x = map(int, input().split())
arr = list(map(int, input().split()))
print(arr.count(x))""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
let input = [];
rl.on('line', (line) => {
    input.push(line);
    if (input.length === 2) {
        const [n, x] = input[0].split(' ').map(Number);
        const arr = input[1].split(' ').map(Number);
        const count = arr.filter(a => a === x).length;
        console.log(count);
        rl.close();
    }
});"""
    },
    {
        "id": 26,
        "title": "String Length",
        "statement": "Given a string, find its length without using built-in functions.",
        "input_desc": "A single string `S`.",
        "output_desc": "The length of the string.",
        "example_input": "hello",
        "example_output": "5",
        "constraints": "1 <= |S| <= 1000, S contains only lowercase letters.",
        "explanation": "Iterate through the string until the null terminator (C/C++) or end of string, counting characters.",
        "c_solution": """#include <stdio.h>

int main() {
    char s[1001];
    scanf("%s", s);
    int len = 0;
    while (s[len] != '\\0') len++;
    printf("%d\\n", len);
    return 0;
}""",
        "cpp_solution": """#include <iostream>
#include <string>

int main() {
    std::string s;
    std::cin >> s;
    int len = 0;
    for (char c : s) len++;
    std::cout << len << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int len = 0;
        for (char c : s.toCharArray()) len++;
        System.out.println(len);
    }
}""",
        "python_solution": """s = input()
count = 0
for _ in s:
    count += 1
print(count)""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    let len = 0;
    for (let c of line) len++;
    console.log(len);
    rl.close();
});"""
    },
    {
        "id": 27,
        "title": "Reverse String",
        "statement": "Given a string, print it in reverse order.",
        "input_desc": "A single string `S`.",
        "output_desc": "The reversed string.",
        "example_input": "hello",
        "example_output": "olleh",
        "constraints": "1 <= |S| <= 1000, S contains only lowercase letters.",
        "explanation": "Use two pointers to swap characters from start and end, or use string slicing in languages that support it.",
        "c_solution": """#include <stdio.h>
#include <string.h>

int main() {
    char s[1001];
    scanf("%s", s);
    int len = strlen(s);
    for (int i = len - 1; i >= 0; i--) {
        printf("%c", s[i]);
    }
    printf("\\n");
    return 0;
}""",
        "cpp_solution": """#include <iostream>
#include <string>

int main() {
    std::string s;
    std::cin >> s;
    for (int i = s.length() - 1; i >= 0; --i) {
        std::cout << s[i];
    }
    std::cout << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        for (int i = s.length() - 1; i >= 0; i--) {
            System.out.print(s.charAt(i));
        }
        System.out.println();
    }
}""",
        "python_solution": """s = input()
print(s[::-1])""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    console.log(line.split('').reverse().join(''));
    rl.close();
});"""
    },
    {
        "id": 28,
        "title": "Count Vowels",
        "statement": "Given a string, count the number of vowels (a, e, i, o, u).",
        "input_desc": "A single string `S`.",
        "output_desc": "The number of vowels in the string.",
        "example_input": "hello",
        "example_output": "2",
        "constraints": "1 <= |S| <= 1000, S contains only lowercase letters.",
        "explanation": "Iterate through the string and check each character against a set of vowels, incrementing a counter for matches.",
        "c_solution": """#include <stdio.h>
#include <string.h>

int main() {
    char s[1001];
    scanf("%s", s);
    int count = 0;
    for (int i = 0; s[i] != '\\0'; i++) {
        if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u') {
            count++;
        }
    }
    printf("%d\\n", count);
    return 0;
}""",
        "cpp_solution": """#include <iostream>
#include <string>

int main() {
    std::string s;
    std::cin >> s;
    int count = 0;
    for (char c : s) {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            count++;
        }
    }
    std::cout << count << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                count++;
            }
        }
        System.out.println(count);
    }
}""",
        "python_solution": """s = input()
print(sum(1 for c in s if c in 'aeiou'))""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const vowels = ['a', 'e', 'i', 'o', 'u'];
    const count = line.split('').filter(c => vowels.includes(c)).length;
    console.log(count);
    rl.close();
});"""
    },
    {
        "id": 29,
        "title": "Is Palindrome",
        "statement": "Given a string, determine if it is a palindrome (reads the same forwards and backwards).",
        "input_desc": "A single string `S`.",
        "output_desc": "Print \"Yes\" if the string is a palindrome, \"No\" otherwise.",
        "example_input": "racecar",
        "example_output": "Yes",
        "constraints": "1 <= |S| <= 1000, S contains only lowercase letters.",
        "explanation": "Compare characters from the start and end, moving inward. If all pairs match, it’s a palindrome.",
        "c_solution": """#include <stdio.h>
#include <string.h>

int main() {
    char s[1001];
    scanf("%s", s);
    int len = strlen(s);
    int is_palindrome = 1;
    for (int i = 0; i < len / 2; i++) {
        if (s[i] != s[len - 1 - i]) {
            is_palindrome = 0;
            break;
        }
    }
    printf("%s\\n", is_palindrome ? "Yes" : "No");
    return 0;
}""",
        "cpp_solution": """#include <iostream>
#include <string>

int main() {
    std::string s;
    std::cin >> s;
    int len = s.length();
    bool is_palindrome = true;
    for (int i = 0; i < len / 2; ++i) {
        if (s[i] != s[len - 1 - i]) {
            is_palindrome = false;
            break;
        }
    }
    std::cout << (is_palindrome ? "Yes" : "No") << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int len = s.length();
        boolean isPalindrome = true;
        for (int i = 0; i < len / 2; i++) {
            if (s.charAt(i) != s.charAt(len - 1 - i)) {
                isPalindrome = false;
                break;
            }
        }
        System.out.println(isPalindrome ? "Yes" : "No");
    }
}""",
        "python_solution": """s = input()
print("Yes" if s == s[::-1] else "No")""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const reversed = line.split('').reverse().join('');
    console.log(line === reversed ? "Yes" : "No");
    rl.close();
});"""
    },
    {
        "id": 30,
        "title": "Uppercase to Lowercase",
        "statement": "Given a string of uppercase letters, convert it to lowercase and print it.",
        "input_desc": "A single string `S`.",
        "output_desc": "The string converted to lowercase.",
        "example_input": "HELLO",
        "example_output": "hello",
        "constraints": "1 <= |S| <= 1000, S contains only uppercase letters.",
        "explanation": "Iterate through the string and convert each character by adding 32 to its ASCII value, or use a built-in lowercase function.",
        "c_solution": """#include <stdio.h>
#include <string.h>

int main() {
    char s[1001];
    scanf("%s", s);
    for (int i = 0; s[i] != '\\0'; i++) {
        s[i] = s[i] + 32;
    }
    printf("%s\\n", s);
    return 0;
}""",
        "cpp_solution": """#include <iostream>
#include <string>
#include <algorithm>

int main() {
    std::string s;
    std::cin >> s;
    for (char &c : s) {
        c = c + 32;
    }
    std::cout << s << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        StringBuilder result = new StringBuilder();
        for (char c : s.toCharArray()) {
            result.append((char)(c + 32));
        }
        System.out.println(result);
    }
}""",
        "python_solution": """s = input()
print(s.lower())""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    console.log(line.toLowerCase());
    rl.close();
});"""
    },

     {
        "id": 31,
        "title": "Count Characters",
        "statement": "Given a string, count the frequency of a specific character.",
        "input_desc": "The first line contains a string `S`. The second line contains a character `C`.",
        "output_desc": "The number of times `C` appears in `S`.",
        "example_input": "hello\nl",
        "example_output": "3",
        "constraints": "1 <= |S| <= 1000, C is a lowercase letter.",
        "explanation": "Iterate through the string and count occurrences of the given character.",
        "c_solution": """#include <stdio.h>
#include <string.h>

int main() {
    char s[1001], c;
    scanf("%s\\n%c", s, &c);
    int count = 0;
    for (int i = 0; s[i] != '\\0'; i++) {
        if (s[i] == c) count++;
    }
    printf("%d\\n", count);
    return 0;
}""",
        "cpp_solution": """#include <iostream>
#include <string>

int main() {
    std::string s;
    char c;
    std::cin >> s >> c;
    int count = 0;
    for (char x : s) {
        if (x == c) count++;
    }
    std::cout << count << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        char c = sc.nextLine().charAt(0);
        int count = 0;
        for (char x : s.toCharArray()) {
            if (x == c) count++;
        }
        System.out.println(count);
    }
}""",
        "python_solution": """s = input()
c = input()
print(s.count(c))""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
let input = [];
rl.on('line', (line) => {
    input.push(line);
    if (input.length === 2) {
        const s = input[0];
        const c = input[1];
        let count = 0;
        for (let x of s) {
            if (x === c) count++;
        }
        console.log(count);
        rl.close();
    }
});"""
    },
    {
        "id": 32,
        "title": "Is Substring",
        "statement": "Determine if one string is a substring of another.",
        "input_desc": "Two strings `S` and `T` on separate lines.",
        "output_desc": "Print \"Yes\" if `T` is a substring of `S`, \"No\" otherwise.",
        "example_input": "hello\ntell",
        "example_output": "No",
        "constraints": "1 <= |S|, |T| <= 1000, S and T contain only lowercase letters.",
        "explanation": "Check if string `T` appears within string `S` using string methods or manual comparison.",
        "c_solution": """#include <stdio.h>
#include <string.h>

int main() {
    char s[1001], t[1001];
    scanf("%s\\n%s", s, t);
    if (strstr(s, t) != NULL) {
        printf("Yes\\n");
    } else {
        printf("No\\n");
    }
    return 0;
}""",
        "cpp_solution": """#include <iostream>
#include <string>

int main() {
    std::string s, t;
    std::cin >> s >> t;
    if (s.find(t) != std::string::npos) {
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
        String s = sc.nextLine();
        String t = sc.nextLine();
        System.out.println(s.contains(t) ? "Yes" : "No");
    }
}""",
        "python_solution": """s = input()
t = input()
print("Yes" if t in s else "No")""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
let input = [];
rl.on('line', (line) => {
    input.push(line);
    if (input.length === 2) {
        const [s, t] = input;
        console.log(s.includes(t) ? "Yes" : "No");
        rl.close();
    }
});"""
    },
    {
        "id": 33,
        "title": "Toggle Case",
        "statement": "Given a string, toggle the case of each character (uppercase to lowercase and vice versa).",
        "input_desc": "A single string `S`.",
        "output_desc": "The string with each character's case toggled.",
        "example_input": "HeLLo",
        "example_output": "hEllO",
        "constraints": "1 <= |S| <= 1000, S contains only letters.",
        "explanation": "For each character, check if it’s uppercase or lowercase and convert accordingly (e.g., ASCII difference of 32).",
        "c_solution": """#include <stdio.h>
#include <string.h>

int main() {
    char s[1001];
    scanf("%s", s);
    for (int i = 0; s[i] != '\\0'; i++) {
        if (s[i] >= 'A' && s[i] <= 'Z') {
            s[i] += 32;
        } else if (s[i] >= 'a' && s[i] <= 'z') {
            s[i] -= 32;
        }
    }
    printf("%s\\n", s);
    return 0;
}""",
        "cpp_solution": """#include <iostream>
#include <string>

int main() {
    std::string s;
    std::cin >> s;
    for (char &c : s) {
        if (c >= 'A' && c <= 'Z') c += 32;
        else if (c >= 'a' && c <= 'z') c -= 32;
    }
    std::cout << s << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        StringBuilder result = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isUpperCase(c)) {
                result.append(Character.toLowerCase(c));
            } else {
                result.append(Character.toUpperCase(c));
            }
        }
        System.out.println(result);
    }
}""",
        "python_solution": """s = input()
print(''.join(c.lower() if c.isupper() else c.upper() for c in s))""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const result = line.split('').map(c => 
        c === c.toUpperCase() ? c.toLowerCase() : c.toUpperCase()
    ).join('');
    console.log(result);
    rl.close();
});"""
    },
    {
        "id": 34,
        "title": "First Non-Repeating Character",
        "statement": "Find the first non-repeating character in a string.",
        "input_desc": "A single string `S`.",
        "output_desc": "The first non-repeating character, or \"None\" if none exists.",
        "example_input": "aabbcc",
        "example_output": "None",
        "constraints": "1 <= |S| <= 1000, S contains only lowercase letters.",
        "explanation": "Use an array or hash map to count character frequencies, then find the first character with a count of 1.",
        "c_solution": """#include <stdio.h>
#include <string.h>

int main() {
    char s[1001];
    scanf("%s", s);
    int freq[26] = {0};
    for (int i = 0; s[i] != '\\0'; i++) {
        freq[s[i] - 'a']++;
    }
    for (int i = 0; s[i] != '\\0'; i++) {
        if (freq[s[i] - 'a'] == 1) {
            printf("%c\\n", s[i]);
            return 0;
        }
    }
    printf("None\\n");
    return 0;
}""",
        "cpp_solution": """#include <iostream>
#include <string>
#include <unordered_map>

int main() {
    std::string s;
    std::cin >> s;
    std::unordered_map<char, int> freq;
    for (char c : s) freq[c]++;
    for (char c : s) {
        if (freq[c] == 1) {
            std::cout << c << std::endl;
            return 0;
        }
    }
    std::cout << "None" << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        HashMap<Character, Integer> freq = new HashMap<>();
        for (char c : s.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }
        for (char c : s.toCharArray()) {
            if (freq.get(c) == 1) {
                System.out.println(c);
                return;
            }
        }
        System.out.println("None");
    }
}""",
        "python_solution": """s = input()
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1
for c in s:
    if freq[c] == 1:
        print(c)
        exit()
print("None")""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const freq = {};
    for (let c of line) {
        freq[c] = (freq[c] || 0) + 1;
    }
    for (let c of line) {
        if (freq[c] === 1) {
            console.log(c);
            rl.close();
            return;
        }
    }
    console.log("None");
    rl.close();
});"""
    },
    {
        "id": 35,
        "title": "GCD of Two Numbers",
        "statement": "Find the greatest common divisor (GCD) of two positive integers using the Euclidean algorithm.",
        "input_desc": "Two space-separated integers `a` and `b`.",
        "output_desc": "The GCD of `a` and `b`.",
        "example_input": "48 18",
        "example_output": "6",
        "constraints": "1 <= a, b <= 10^9",
        "explanation": "Use the Euclidean algorithm: GCD(a, b) = GCD(b, a % b) until b becomes 0.",
        "c_solution": """#include <stdio.h>

long long gcd(long long a, long long b) {
    while (b != 0) {
        long long temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    long long a, b;
    scanf("%lld %lld", &a, &b);
    printf("%lld\\n", gcd(a, b));
    return 0;
}""",
        "cpp_solution": """#include <iostream>
#include <algorithm>

int main() {
    long long a, b;
    std::cin >> a >> b;
    std::cout << std::gcd(a, b) << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static long gcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();
        long b = sc.nextLong();
        System.out.println(gcd(a, b));
    }
}""",
        "python_solution": """def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
print(gcd(a, b))""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const [a, b] = line.split(' ').map(Number);
    const gcd = (a, b) => {
        while (b) {
            [a, b] = [b, a % b];
        }
        return a;
    };
    console.log(gcd(a, b));
    rl.close();
});"""
    },
    {
        "id": 36,
        "title": "LCM of Two Numbers",
        "statement": "Find the least common multiple (LCM) of two positive integers.",
        "input_desc": "Two space-separated integers `a` and `b`.",
        "output_desc": "The LCM of `a` and `b`.",
        "example_input": "6 8",
        "example_output": "24",
        "constraints": "1 <= a, b <= 10^9",
        "explanation": "Use the formula LCM(a, b) = (a * b) / GCD(a, b). Compute GCD using the Euclidean algorithm.",
        "c_solution": """#include <stdio.h>

long long gcd(long long a, long long b) {
    while (b != 0) {
        long long temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    long long a, b;
    scanf("%lld %lld", &a, &b);
    long long lcm = (a / gcd(a, b)) * b;
    printf("%lld\\n", lcm);
    return 0;
}""",
        "cpp_solution": """#include <iostream>
#include <algorithm>

int main() {
    long long a, b;
    std::cin >> a >> b;
    long long lcm = (a / std::gcd(a, b)) * b;
    std::cout << lcm << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static long gcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();
        long b = sc.nextLong();
        long lcm = (a / gcd(a, b)) * b;
        System.out.println(lcm);
    }
}""",
        "python_solution": """def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
lcm = (a // gcd(a, b)) * b
print(lcm)""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const [a, b] = line.split(' ').map(Number);
    const gcd = (a, b) => {
        while (b) {
            [a, b] = [b, a % b];
        }
        return a;
    };
    const lcm = (a / gcd(a, b)) * b;
    console.log(lcm);
    rl.close();
});"""
    },
    {
        "id": 37,
        "title": "Prime Number Check",
        "statement": "Determine if a given number is prime.",
        "input_desc": "A single integer `N`.",
        "output_desc": "Print \"Yes\" if `N` is prime, \"No\" otherwise.",
        "example_input": "17",
        "example_output": "Yes",
        "constraints": "1 <= N <= 10^9",
        "explanation": "A number is prime if it’s greater than 1 and divisible only by 1 and itself. Check divisibility up to the square root of N.",
        "c_solution": """#include <stdio.h>
#include <math.h>

int main() {
    long long n;
    scanf("%lld", &n);
    if (n < 2) {
        printf("No\\n");
        return 0;
    }
    int is_prime = 1;
    for (long long i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            is_prime = 0;
            break;
        }
    }
    printf("%s\\n", is_prime ? "Yes" : "No");
    return 0;
}""",
        "cpp_solution": """#include <iostream>
#include <cmath>

int main() {
    long long n;
    std::cin >> n;
    if (n < 2) {
        std::cout << "No" << std::endl;
        return 0;
    }
    bool is_prime = true;
    for (long long i = 2; i <= std::sqrt(n); ++i) {
        if (n % i == 0) {
            is_prime = false;
            break;
        }
    }
    std::cout << (is_prime ? "Yes" : "No") << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        if (n < 2) {
            System.out.println("No");
            return;
        }
        boolean isPrime = true;
        for (long i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                isPrime = false;
                break;
            }
        }
        System.out.println(isPrime ? "Yes" : "No");
    }
}""",
        "python_solution": """n = int(input())
if n < 2:
    print("No")
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    print("Yes" if is_prime else "No")""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const n = parseInt(line);
    if (n < 2) {
        console.log("No");
        rl.close();
        return;
    }
    let isPrime = true;
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            isPrime = false;
            break;
        }
    }
    console.log(isPrime ? "Yes" : "No");
    rl.close();
});"""
    },
    {
        "id": 38,
        "title": "Sum of Primes",
        "statement": "Find the sum of all prime numbers up to `N`.",
        "input_desc": "A single integer `N`.",
        "output_desc": "The sum of all prime numbers from 2 to `N`.",
        "example_input": "10",
        "example_output": "17",
        "constraints": "2 <= N <= 1000",
        "explanation": "Identify all prime numbers up to N using a primality test, then sum them.",
        "c_solution": """#include <stdio.h>
#include <math.h>

int is_prime(int n) {
    if (n < 2) return 0;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int main() {
    int n;
    scanf("%d", &n);
    long long sum = 0;
    for (int i = 2; i <= n; i++) {
        if (is_prime(i)) sum += i;
    }
    printf("%lld\\n", sum);
    return 0;
}""",
        "cpp_solution": """#include <iostream>
#include <cmath>

bool is_prime(int n) {
    if (n < 2) return false;
    for (int i = 2; i <= std::sqrt(n); ++i) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    int n;
    std::cin >> n;
    long long sum = 0;
    for (int i = 2; i <= n; ++i) {
        if (is_prime(i)) sum += i;
    }
    std::cout << sum << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long sum = 0;
        for (int i = 2; i <= n; i++) {
            if (isPrime(i)) sum += i;
        }
        System.out.println(sum);
    }
}""",
        "python_solution": """def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
print(sum(i for i in range(2, n + 1) if is_prime(i)))""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const n = parseInt(line);
    const isPrime = (n) => {
        if (n < 2) return false;
        for (let i = 2; i <= Math.sqrt(n); i++) {
            if (n % i === 0) return false;
        }
        return true;
    };
    let sum = 0;
    for (let i = 2; i <= n; i++) {
        if (isPrime(i)) sum += i;
    }
    console.log(sum);
    rl.close();
});"""
    },
    {
        "id": 39,
        "title": "Power of Number",
        "statement": "Calculate `a` raised to the power of `b`.",
        "input_desc": "Two space-separated integers `a` and `b`.",
        "output_desc": "The value of `a` raised to the power `b`.",
        "example_input": "2 3",
        "example_output": "8",
        "constraints": "1 <= a, b <= 10",
        "explanation": "Use a loop to multiply `a` by itself `b` times, or use a built-in power function.",
        "c_solution": """#include <stdio.h>

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    long long result = 1;
    for (int i = 0; i < b; i++) {
        result *= a;
    }
    printf("%lld\\n", result);
    return 0;
}""",
        "cpp_solution": """#include <iostream>

int main() {
    int a, b;
    std::cin >> a >> b;
    long long result = 1;
    for (int i = 0; i < b; ++i) {
        result *= a;
    }
    std::cout << result << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        long result = 1;
        for (int i = 0; i < b; i++) {
            result *= a;
        }
        System.out.println(result);
    }
}""",
        "python_solution": """a, b = map(int, input().split())
print(a ** b)""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const [a, b] = line.split(' ').map(Number);
    console.log(Math.pow(a, b));
    rl.close();
});"""
    },
    {
        "id": 40,
        "title": "Binary to Decimal",
        "statement": "Convert a binary string to its decimal equivalent.",
        "input_desc": "A string `S` representing a binary number.",
        "output_desc": "The decimal equivalent of the binary number.",
        "example_input": "1010",
        "example_output": "10",
        "constraints": "1 <= |S| <= 32, S contains only 0s and 1s.",
        "explanation": "Iterate through the string, multiplying each bit by the corresponding power of 2 and summing the results.",
        "c_solution": """#include <stdio.h>
#include <string.h>

int main() {
    char s[33];
    scanf("%s", s);
    long long decimal = 0;
    for (int i = 0; s[i] != '\\0'; i++) {
        decimal = decimal * 2 + (s[i] - '0');
    }
    printf("%lld\\n", decimal);
    return 0;
}""",
        "cpp_solution": """#include <iostream>
#include <string>

int main() {
    std::string s;
    std::cin >> s;
    long long decimal = 0;
    for (char c : s) {
        decimal = decimal * 2 + (c - '0');
    }
    std::cout << decimal << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        long decimal = 0;
        for (char c : s.toCharArray()) {
            decimal = decimal * 2 + (c - '0');
        }
        System.out.println(decimal);
    }
}""",
        "python_solution": """s = input()
print(int(s, 2))""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    console.log(parseInt(line, 2));
    rl.close();
});"""
    },
    {
        "id": 41,
        "title": "Decimal to Binary",
        "statement": "Convert a decimal number to its binary representation.",
        "input_desc": "A single integer `N`.",
        "output_desc": "The binary representation of `N`.",
        "example_input": "10",
        "example_output": "1010",
        "constraints": "0 <= N <= 10^9",
        "explanation": "Repeatedly divide the number by 2, collecting remainders in reverse order to form the binary string.",
        "c_solution": """#include <stdio.h>
#include <string.h>

int main() {
    long long n;
    scanf("%lld", &n);
    if (n == 0) {
        printf("0\\n");
        return 0;
    }
    char binary[33] = {0};
    int i = 0;
    while (n > 0) {
        binary[i++] = (n % 2) + '0';
        n /= 2;
    }
    for (int j = i - 1; j >= 0; j--) {
        printf("%c", binary[j]);
    }
    printf("\\n");
    return 0;
}""",
        "cpp_solution": """#include <iostream>
#include <string>

int main() {
    long long n;
    std::cin >> n;
    if (n == 0) {
        std::cout << "0" << std::endl;
        return 0;
    }
    std::string binary;
    while (n > 0) {
        binary += (n % 2) + '0';
        n /= 2;
    }
    for (int i = binary.length() - 1; i >= 0; --i) {
        std::cout << binary[i];
    }
    std::cout << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        if (n == 0) {
            System.out.println("0");
            return;
        }
        StringBuilder binary = new StringBuilder();
        while (n > 0) {
            binary.append(n % 2);
            n /= 2;
        }
        System.out.println(binary.reverse());
    }
}""",
        "python_solution": """n = int(input())
if n == 0:
    print("0")
else:
    binary = ""
    while n > 0:
        binary += str(n % 2)
        n //= 2
    print(binary[::-1])""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    let n = parseInt(line);
    if (n === 0) {
        console.log("0");
        rl.close();
        return;
    }
    let binary = "";
    while (n > 0) {
        binary += n % 2;
        n = Math.floor(n / 2);
    }
    console.log(binary.split('').reverse().join(''));
    rl.close();
});"""
    },
    {
        "id": 42,
        "title": "Square Root Integer",
        "statement": "Find the integer square root of a number (floor value).",
        "input_desc": "A single integer `N`.",
        "output_desc": "The largest integer whose square is less than or equal to `N`.",
        "example_input": "17",
        "example_output": "4",
        "constraints": "0 <= N <= 10^9",
        "explanation": "Use a mathematical square root function and floor the result, or implement binary search to find the integer square root.",
        "c_solution": """#include <stdio.h>
#include <math.h>

int main() {
    long long n;
    scanf("%lld", &n);
    printf("%lld\\n", (long long)sqrt(n));
    return 0;
}""",
        "cpp_solution": """#include <iostream>
#include <cmath>

int main() {
    long long n;
    std::cin >> n;
    std::cout << (long long)std::sqrt(n) << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        System.out.println((long)Math.sqrt(n));
    }
}""",
        "python_solution": """n = int(input())
print(int(n ** 0.5))""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const n = parseInt(line);
    console.log(Math.floor(Math.sqrt(n)));
    rl.close();
});"""
    },
    {
        "id": 43,
        "title": "Check Armstrong Number",
        "statement": "Determine if a number is an Armstrong number (sum of its digits raised to the power of the number of digits equals the number).",
        "input_desc": "A single integer `N`.",
        "output_desc": "Print \"Yes\" if `N` is an Armstrong number, \"No\" otherwise.",
        "example_input": "153",
        "example_output": "Yes",
        "constraints": "1 <= N <= 10^9",
        "explanation": "Count the number of digits, then compute the sum of each digit raised to that power. Compare with the original number.",
        "c_solution": """#include <stdio.h>
#include <math.h>

int main() {
    long long n;
    scanf("%lld", &n);
    long long temp = n, sum = 0;
    int digits = 0;
    while (temp > 0) {
        digits++;
        temp /= 10;
    }
    temp = n;
    while (temp > 0) {
        sum += pow(temp % 10, digits);
        temp /= 10;
    }
    printf("%s\\n", sum == n ? "Yes" : "No");
    return 0;
}""",
        "cpp_solution": """#include <iostream>
#include <cmath>

int main() {
    long long n;
    std::cin >> n;
    long long temp = n, sum = 0;
    int digits = 0;
    while (temp > 0) {
        digits++;
        temp /= 10;
    }
    temp = n;
    while (temp > 0) {
        sum += std::pow(temp % 10, digits);
        temp /= 10;
    }
    std::cout << (sum == n ? "Yes" : "No") << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        long temp = n, sum = 0;
        int digits = 0;
        while (temp > 0) {
            digits++;
            temp /= 10;
        }
        temp = n;
        while (temp > 0) {
            sum += Math.pow(temp % 10, digits);
            temp /= 10;
        }
        System.out.println(sum == n ? "Yes" : "No");
    }
}""",
        "python_solution": """n = int(input())
digits = len(str(n))
sum_powers = sum(int(d) ** digits for d in str(n))
print("Yes" if sum_powers == n else "No")""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const n = parseInt(line);
    const digits = n.toString().length;
    const sum = n.toString().split('').reduce((acc, d) => acc + Math.pow(parseInt(d), digits), 0);
    console.log(sum === n ? "Yes" : "No");
    rl.close();
});"""
    },
    {
        "id": 44,
        "title": "Sum of Squares",
        "statement": "Calculate the sum of squares of the first `N` natural numbers.",
        "input_desc": "A single integer `N`.",
        "output_desc": "The sum of squares from 1 to `N`.",
        "example_input": "4",
        "example_output": "30",
        "constraints": "1 <= N <= 1000",
        "explanation": "Use the formula `sum = N * (N + 1) * (2N + 1) / 6`, or compute each square and sum.",
        "c_solution": """#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    long long sum = (long long)n * (n + 1) * (2 * n + 1) / 6;
    printf("%lld\\n", sum);
    return 0;
}""",
        "cpp_solution": """#include <iostream>

int main() {
    int n;
    std::cin >> n;
    long long sum = (long long)n * (n + 1) * (2 * n + 1) / 6;
    std::cout << sum << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long sum = (long)n * (n + 1) * (2 * n + 1) / 6;
        System.out.println(sum);
    }
}""",
        "python_solution": """n = int(input())
print(n * (n + 1) * (2 * n + 1) // 6)""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const n = parseInt(line);
    const sum = n * (n + 1) * (2 * n + 1) / 6;
    console.log(sum);
    rl.close();
});"""
    },
    {
        "id": 45,
        "title": "Check Sorted Array",
        "statement": "Determine if an array of `N` integers is sorted in non-decreasing order.",
        "input_desc": "The first line contains `N`. The second line contains `N` space-separated integers.",
        "output_desc": "Print \"Yes\" if the array is sorted, \"No\" otherwise.",
        "example_input": "5\n1 2 2 4 5",
        "example_output": "Yes",
        "constraints": "1 <= N <= 1000, -10^6 <= array elements <= 10^6",
        "explanation": "Check if each element is less than or equal to the next element.",
        "c_solution": """#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int arr[1000];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    int is_sorted = 1;
    for (int i = 0; i < n - 1; i++) {
        if (arr[i] > arr[i + 1]) {
            is_sorted = 0;
            break;
        }
    }
    printf("%s\\n", is_sorted ? "Yes" : "No");
    return 0;
}""",
        "cpp_solution": """#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
    }
    bool is_sorted = true;
    for (int i = 0; i < n - 1; ++i) {
        if (arr[i] > arr[i + 1]) {
            is_sorted = false;
            break;
        }
    }
    std::cout << (is_sorted ? "Yes" : "No") << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        boolean isSorted = true;
        for (int i = 0; i < n - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                isSorted = false;
                break;
            }
        }
        System.out.println(isSorted ? "Yes" : "No");
    }
}""",
        "python_solution": """n = int(input())
arr = list(map(int, input().split()))
print("Yes" if all(arr[i] <= arr[i + 1] for i in range(n - 1)) else "No")""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
let input = [];
rl.on('line', (line) => {
    input.push(line);
    if (input.length === 2) {
        const arr = input[1].split(' ').map(Number);
        let isSorted = true;
        for (let i = 0; i < arr.length - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                isSorted = false;
                break;
            }
        }
        console.log(isSorted ? "Yes" : "No");
        rl.close();
    }
});"""
    },
    {
        "id": 46,
        "title": "Rotate Array Left",
        "statement": "Rotate an array of `N` integers left by `K` positions.",
        "input_desc": "The first line contains `N` and `K`. The second line contains `N` space-separated integers.",
        "output_desc": "The array after rotating left by `K` positions, space-separated.",
        "example_input": "5 2\n1 2 3 4 5",
        "example_output": "3 4 5 1 2",
        "constraints": "1 <= N <= 1000, 0 <= K <= N, -10^6 <= array elements <= 10^6",
        "explanation": "Shift each element left by `K` positions, wrapping around to the end. Use modulo to handle the rotation.",
        "c_solution": """#include <stdio.h>

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    int arr[1000];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    k = k % n;
    for (int i = 0; i < n; i++) {
        printf("%d", arr[(i + k) % n]);
        if (i < n - 1) printf(" ");
    }
    printf("\\n");
    return 0;
}""",
        "cpp_solution": """#include <iostream>
#include <vector>

int main() {
    int n, k;
    std::cin >> n >> k;
    std::vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
    }
    k = k % n;
    for (int i = 0; i < n; ++i) {
        std::cout << arr[(i + k) % n];
        if (i < n - 1) std::cout << " ";
    }
    std::cout << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        k = k % n;
        for (int i = 0; i < n; i++) {
            System.out.print(arr[(i + k) % n]);
            if (i < n - 1) System.out.print(" ");
        }
        System.out.println();
    }
}""",
        "python_solution": """n, k = map(int, input().split())
arr = list(map(int, input().split()))
k = k % n
print(*(arr[(i + k) % n] for i in range(n)))""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
let input = [];
rl.on('line', (line) => {
    input.push(line);
    if (input.length === 2) {
        const [n, k] = input[0].split(' ').map(Number);
        const arr = input[1].split(' ').map(Number);
        const rotated = [];
        for (let i = 0; i < n; i++) {
            rotated.push(arr[(i + k) % n]);
        }
        console.log(rotated.join(' '));
        rl.close();
    }
});"""
    },
    {
        "id": 47,
        "title": "Factorial Recursive",
        "statement": "Calculate the factorial of a number `N` using recursion.",
        "input_desc": "A single integer `N`.",
        "output_desc": "The factorial of `N`.",
        "example_input": "5",
        "example_output": "120",
        "constraints": "0 <= N <= 20",
        "explanation": "Use a recursive function where factorial(N) = N * factorial(N-1), with base case factorial(0) = 1.",
        "c_solution": """#include <stdio.h>

long long factorial(int n) {
    if (n == 0) return 1;
    return n * factorial(n - 1);
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%lld\\n", factorial(n));
    return 0;
}""",
        "cpp_solution": """#include <iostream>

long long factorial(int n) {
    if (n == 0) return 1;
    return n * factorial(n - 1);
}

int main() {
    int n;
    std::cin >> n;
    std::cout << factorial(n) << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static long factorial(int n) {
        if (n == 0) return 1;
        return n * factorial(n - 1);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(factorial(n));
    }
}""",
        "python_solution": """def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

n = int(input())
print(factorial(n))""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const n = parseInt(line);
    const factorial = (n) => {
        if (n === 0) return 1n;
        return BigInt(n) * factorial(n - 1);
    };
    console.log(factorial(n).toString());
    rl.close();
});"""
    },
    {
        "id": 48,
        "title": "Fibonacci Recursive",
        "statement": "Calculate the `N`-th Fibonacci number (0-based, starting with 0, 1) using recursion.",
        "input_desc": "A single integer `N`.",
        "output_desc": "The `N`-th Fibonacci number.",
        "example_input": "6",
        "example_output": "8",
        "constraints": "0 <= N <= 20",
        "explanation": "Use recursion where fib(N) = fib(N-1) + fib(N-2), with base cases fib(0) = 0, fib(1) = 1.",
        "c_solution": """#include <stdio.h>

long long fib(int n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%lld\\n", fib(n));
    return 0;
}""",
        "cpp_solution": """#include <iostream>

long long fib(int n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}

int main() {
    int n;
    std::cin >> n;
    std::cout << fib(n) << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static long fib(int n) {
        if (n <= 1) return n;
        return fib(n - 1) + fib(n - 2);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(fib(n));
    }
}""",
        "python_solution": """def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

n = int(input())
print(fib(n))""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const n = parseInt(line);
    const fib = (n) => {
        if (n <= 1) return n;
        return fib(n - 1) + fib(n - 2);
    };
    console.log(fib(n));
    rl.close();
});"""
    },
    {
        "id": 49,
        "title": "Sum of Odd Numbers",
        "statement": "Calculate the sum of odd numbers from 1 to `N`.",
        "input_desc": "A single integer `N`.",
        "output_desc": "The sum of odd numbers from 1 to `N`.",
        "example_input": "7",
        "example_output": "16",
        "constraints": "1 <= N <= 1000",
        "explanation": "Sum odd numbers using a loop with step 2, or use the formula for the sum of the first k odd numbers: k^2, where k is the count of odd numbers.",
        "c_solution": """#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    long long sum = 0;
    for (int i = 1; i <= n; i += 2) {
        sum += i;
    }
    printf("%lld\\n", sum);
    return 0;
}""",
        "cpp_solution": """#include <iostream>

int main() {
    int n;
    std::cin >> n;
    long long sum = 0;
    for (int i = 1; i <= n; i += 2) {
        sum += i;
    }
    std::cout << sum << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long sum = 0;
        for (int i = 1; i <= n; i += 2) {
            sum += i;
        }
        System.out.println(sum);
    }
}""",
        "python_solution": """n = int(input())
sum_odds = sum(i for i in range(1, n + 1, 2))
print(sum_odds)""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', (line) => {
    const n = parseInt(line);
    let sum = 0;
    for (let i = 1; i <= n; i += 2) {
        sum += i;
    }
    console.log(sum);
    rl.close();
});"""
    },
    {
        "id": 50,
        "title": "String Concatenation",
        "statement": "Concatenate two strings and print the result.",
        "input_desc": "Two strings `S` and `T` on separate lines.",
        "output_desc": "The concatenated string `S + T`.",
        "example_input": "hello\nworld",
        "example_output": "helloworld",
        "constraints": "1 <= |S|, |T| <= 1000, S and T contain only lowercase letters.",
        "explanation": "Read two strings and concatenate them using string concatenation operations.",
        "c_solution": """#include <stdio.h>
#include <string.h>

int main() {
    char s[1001], t[1001];
    scanf("%s\\n%s", s, t);
    printf("%s%s\\n", s, t);
    return 0;
}""",
        "cpp_solution": """#include <iostream>
#include <string>

int main() {
    std::string s, t;
    std::cin >> s >> t;
    std::cout << s + t << std::endl;
    return 0;
}""",
        "java_solution": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        String t = sc.nextLine();
        System.out.println(s + t);
    }
}""",
        "python_solution": """s = input()
t = input()
print(s + t)""",
        "javascript_solution": """const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
let input = [];
rl.on('line', (line) => {
    input.push(line);
    if (input.length === 2) {
        const [s, t] = input;
        console.log(s + t);
        rl.close();
    }
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
    main_dir = "White-Belt-Problems"
    
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