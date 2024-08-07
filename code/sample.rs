fn main() {
    println!("Hello, World!");

    let x = 10;
    let y = 20;
    let sum = add(x, y);
    println!("Sum: {}", sum);

    let numbers = vec![1, 2, 3];
    for number in &numbers {
        println!("Number: {}", number);
    }

    // Option and Pattern Matching
    let maybe_number = Some(42);
    match maybe_number {
        Some(n) => println!("Found a number: {}", n),
        None => println!("No number found"),
    }

    // Ownership and Borrowing
    let s = String::from("hello");
    takes_ownership(s);
    // s cannot be used here as its ownership has been moved

    let z = 5;
    makes_copy(z);
    // z can still be used here because i32 is Copy
}

fn add(a: i32, b: i32) -> i32 {
    a + b
}

fn takes_ownership(some_string: String) {
    println!("Taking ownership of: {}", some_string);
}

fn makes_copy(some_integer: i32) {
    println!("Making a copy of: {}", some_integer);
}
