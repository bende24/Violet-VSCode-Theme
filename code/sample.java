import java.util.ArrayList;
import java.util.List;

interface Greetable {
    void greet();
}

class Person implements Greetable {
    private String name;

    public Person(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    @Override
    public void greet() {
        System.out.println("Hello, " + name + "!");
    }
}

public class HelloWorld {
    public static void main(String[] args) {
        Greetable person = new Person("Alice");
        person.greet();

        List<Integer> numbers = new ArrayList<>();
        numbers.add(1);
        numbers.add(2);
        numbers.add(3);

        numbers.forEach(n -> System.out.println("Number: " + n));
    }
}
