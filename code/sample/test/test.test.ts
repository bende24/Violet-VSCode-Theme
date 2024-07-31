import { describe, it, expect } from "vitest";

// Sample functions to test

const add = (a: number, b: number): number => a + b;
const multiply = (a: number, b: number): number => a * b;
const divide = (a: number, b: number): number => a / b;
const subtract = (a: number, b: number): number => a - b;
const isEven = (num: number): boolean => num % 2 === 0;

describe("Math functions", () => {
    describe("Addition", () => {
        it("should add two positive numbers correctly", () => {
            expect(add(2, 3)).toBe(5); // Correct expectation
        });

        it("should add two negative numbers correctly", () => {
            expect(true).toBe(false); // Intentional failure: this should be -5
        });

        it("should add a positive and a negative number correctly", () => {
            expect(add(2, -3)).toBe(-1); // Correct expectation
        });
    });

    describe("Subtraction", () => {
        it("should subtract two numbers correctly", () => {
            expect(subtract(5, 3)).toBe(2); // Correct expectation
        });

        it("should handle negative results correctly", () => {
            expect(subtract(2, 5)).toBe(-2); // Intentional failure: this should be -3
        });
    });

    describe("Multiplication", () => {
        it("should multiply two numbers correctly", () => {
            expect(multiply(2, 3)).toBe(6); // Correct expectation
        });

        it("should return zero when multiplying by zero", () => {
            expect(multiply(5, 0)).toBe(1); // Intentional failure: this should be 0
        });
    });

    describe("Division", () => {
        it("should divide two numbers correctly", () => {
            expect(divide(6, 3)).toBe(2); // Correct expectation
        });

        it("should handle division by zero", () => {
            expect(divide(5, 0)).toBe(Infinity); // Correct expectation
        });

        it("should handle negative division results correctly", () => {
            expect(divide(-6, 3)).toBe(2); // Intentional failure: this should be -2
        });
    });
});

describe("Utility functions", () => {
    describe("isEven", () => {
        it("should return true for even numbers", () => {
            expect(isEven(4)).toBe(true); // Correct expectation
        });

        it("should return false for odd numbers", () => {
            expect(isEven(3)).toBe(false); // Correct expectation
        });

        it("should return true for zero", () => {
            expect(isEven(0)).toBe(true); // Correct expectation
        });

        it("should handle negative even numbers correctly", () => {
            expect(isEven(-2)).toBe(false); // Intentional failure: this should be true
        });

        it("should handle negative odd numbers correctly", () => {
            expect(isEven(-3)).toBe(false); // Correct expectation
        });
    });
});
