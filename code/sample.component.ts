import { Component } from "@angular/core";

@Component({
    selector: "app-root",
    templateUrl: "./app.component.html",
    styleUrls: ["./app.component.css"],
})
export class AppComponent {
    title = "Hello, Angular!";
    name = "Alice";
    numbers: number[] = [1, 2, 3];
    newNumber: number = 0;

    greet(): void {
        alert(`Hello, ${this.name}!`);
    }

    addNumber(): void {
        if (this.newNumber) {
            this.numbers.push(this.newNumber);
            this.newNumber = 0; // Reset the input
        }
    }

    removeNumber(index: number): void {
        this.numbers.splice(index, 1);
    }
}
