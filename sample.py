# Let's create a dictionary with sample code snippets for different programming languages and frameworks

sample_code = {
    "python.py": '''# Sample Python Code
def greet(name):
    print(f"Hello, {name}!")

class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello from the Greeter class, {self.name}!")

if __name__ == "__main__":
    greet("World")
    greeter = Greeter("VSCode")
    greeter.greet()
''',

    "javascript.js": '''// Sample JavaScript Code (Node.js)
function greet(name) {
    console.log(`Hello, ${name}!`);
}

class Greeter {
    constructor(name) {
        this.name = name;
    }
    greet() {
        console.log(`Hello from the Greeter class, ${this.name}!`);
    }
}

greet("World");
const greeter = new Greeter("VSCode");
greeter.greet();
''',

    "index.html": '''<!-- Sample HTML + CSS -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample HTML</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f0f0f0; }
        h1 { color: #333; }
    </style>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is a sample HTML file.</p>
</body>
</html>
''',

    "java.java": '''// Sample Java Code
public class Main {
    public static void main(String[] args) {
        greet("World");
        Greeter greeter = new Greeter("VSCode");
        greeter.greet();
    }

    public static void greet(String name) {
        System.out.println("Hello, " + name + "!");
    }
}

class Greeter {
    private String name;

    public Greeter(String name) {
        this.name = name;
    }

    public void greet() {
        System.out.println("Hello from the Greeter class, " + name + "!");
    }
}
''',

    "cpp.cpp": '''// Sample C++ Code
#include <iostream>
#include <string>

void greet(const std::string& name) {
    std::cout << "Hello, " << name << "!" << std::endl;
}

class Greeter {
    std::string name;
public:
    Greeter(const std::string& name) : name(name) {}
    void greet() {
        std::cout << "Hello from the Greeter class, " << name << "!" << std::endl;
    }
};

int main() {
    greet("World");
    Greeter greeter("VSCode");
    greeter.greet();
    return 0;
}
''',

    "csharp.cs": '''// Sample C# Code
using System;

class Program {
    static void Main(string[] args) {
        Greet("World");
        Greeter greeter = new Greeter("VSCode");
        greeter.Greet();
    }

    static void Greet(string name) {
        Console.WriteLine("Hello, " + name + "!");
    }
}

class Greeter {
    private string name;

    public Greeter(string name) {
        this.name = name;
    }

    public void Greet() {
        Console.WriteLine("Hello from the Greeter class, " + name + "!");
    }
}
''',

    "ruby.rb": '''# Sample Ruby Code
def greet(name)
  puts "Hello, #{name}!"
end

class Greeter
  def initialize(name)
    @name = name
  end

  def greet
    puts "Hello from the Greeter class, #{@name}!"
  end
end

greet("World")
greeter = Greeter.new("VSCode")
greeter.greet
''',

    "go.go": '''// Sample Go Code
package main

import "fmt"

func greet(name string) {
    fmt.Printf("Hello, %s!\\n", name)
}

type Greeter struct {
    name string
}

func (g Greeter) greet() {
    fmt.Printf("Hello from the Greeter class, %s!\\n", g.name)
}

func main() {
    greet("World")
    greeter := Greeter{"VSCode"}
    greeter.greet()
}
''',

    "rust.rs": '''// Sample Rust Code
fn greet(name: &str) {
    println!("Hello, {}!", name);
}

struct Greeter {
    name: String,
}

impl Greeter {
    fn greet(&self) {
        println!("Hello from the Greeter class, {}!", self.name);
    }
}

fn main() {
    greet("World");
    let greeter = Greeter { name: "VSCode".to_string() };
    greeter.greet();
}
''',

    "typescript.ts": '''// Sample TypeScript Code
function greet(name: string): void {
    console.log(`Hello, ${name}!`);
}

class Greeter {
    name: string;

    constructor(name: string) {
        this.name = name;
    }

    greet(): void {
        console.log(`Hello from the Greeter class, ${this.name}!`);
    }
}

greet("World");
const greeter = new Greeter("VSCode");
greeter.greet();
''',

    "php.php": '''<?php
// Sample PHP Code
function greet($name) {
    echo "Hello, $name!\\n";
}

class Greeter {
    private $name;

    public function __construct($name) {
        $this->name = $name;
    }

    public function greet() {
        echo "Hello from the Greeter class, $this->name!\\n";
    }
}

greet("World");
$greeter = new Greeter("VSCode");
$greeter->greet();
?>
''',

    "sql.sql": '''-- Sample SQL
CREATE TABLE Users (
    ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100)
);

INSERT INTO Users (ID, Name, Email)
VALUES (1, 'John Doe', 'john.doe@example.com');

SELECT * FROM Users WHERE ID = 1;
''',

    "bash.sh": '''#!/bin/bash
# Sample Bash Script
greet() {
  echo "Hello, $1!"
}

class Greeter {
  private name
  Greeter() { this.name=$1; }
  greet() { echo "Hello from the Greeter class, $this.name!"; }
}

greet "World"
greeter = Greeter "VSCode"
greeter.greet
''',

    "sample.json": '''{
  "name": "VSCode Theme Test",
  "description": "Sample JSON to test VSCode theme",
  "version": "1.0.0",
  "scripts": {
    "start": "node index.js",
    "test": "echo \\"Error: no test specified\\" && exit 1"
  },
  "dependencies": {
    "express": "^4.17.1"
  }
}
'''
}

# Saving all these snippets to separate files
import os

# Create a directory to store the files
output_dir = "/code"
os.makedirs(output_dir, exist_ok=True)

# Write each sample code to its respective file
for filename, code in sample_code.items():
    with open(os.path.join(output_dir, filename), "w") as file:
        file.write(code)

output_dir
