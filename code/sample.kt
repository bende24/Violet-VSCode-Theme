interface Greetable {
    fun greet()
}

class Person(private val name: String) : Greetable {
    override fun greet() {
        println("Hello, $name!")
    }
}

fun main() {
    val person: Greetable = Person("Alice")
    person.greet()

    val numbers = listOf(1, 2, 3)
    numbers.forEach { n -> println("Number: $n") }
}
