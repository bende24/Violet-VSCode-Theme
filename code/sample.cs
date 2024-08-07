using System;
using System.Collections.Generic;

interface IGreetable {
    void Greet();
}

class Person : IGreetable {
    private string Name;

    public Person(string name) {
        Name = name;
    }

    public void Greet() {
        Console.WriteLine("Hello, " + Name + "!");
    }
}

class Program {
    static void Main(string[] args) {
        IGreetable person = new Person("Alice");
        person.Greet();

        List<int> numbers = new List<int> { 1, 2, 3 };
        numbers.ForEach(n => Console.WriteLine("Number: " + n));
    }
}
