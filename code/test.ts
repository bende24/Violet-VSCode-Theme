import * as path from "path";

enum Direction {
	Up = 1,
	Down,
	Left,
	Right,
}

let v!;
export const num = 123 + (2.3 % 3);
export const b = true;
const str = "This is a string";
const tstr: string = `This "is" ${num} ${1} \n`;
const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
const arr: number[] = [1];
// Comment

type TT = {
	key: string;
	num: number;
	asd: {
		keys: [];
	};
};

const obj = {
	key: "key",
	num: 22,
	asd: {
		keys: [],
	},
};

type Optional<T> = T | null | undefined | never;
type Type<TGeneric> = TGeneric;
interface Interface {
	func<T>(a: string, b: T): Type<T>;
}

arr[0];
arr["0"];
console.log();
obj.asd;

class Class implements Interface {
	public func<T>(a: string, b: T): Type<T> {
		let acc = 3;
		let c = () => {
			({});
		};
		const d = null;
		const obj = {
			num: num,
			str: str,
			a: a,
			b: acc,
			c: c,
			d: d,
		} as Type<T>;

		const obj2 = {
			str: "qwe",
		};

		obj2?.str;
		obj2["str"];
		obj2[0];
		if (a == "2" || true) {
		}
		for (let item of arr) {
		}

		return obj;
	}
}

export function foo(b = "string"): string {
	let v: TT;
	const a = new Class();
	const obj2 = {
		str: "qwe",
	};
	path?.asd.a;
	obj2[0];
	return a;
}

async function f(a: number, b: string, c: boolean) {
	await f(123, "", false);
}
f(123, "Hello", true);

/**
 * This function adds two numbers together
 * @param a
 * @param b
 * @returns
 */
function add(a: number, b: number): number {
	return a + b;
}
add(1, 2);

function call(name: string) {}
call("John");

function isTrue(b: boolean) {}
isTrue(false);
