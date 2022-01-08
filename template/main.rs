use std::env;
use std::fs;

fn read_input_file() -> String {
	let current_dir = env::current_dir();
	let file_path = current_dir.unwrap().parent().unwrap().join("input.txt");
	return fs::read_to_string(file_path).expect("Something went wrong reading the file");
}

fn solve_puzzle_1() -> i32 {
	let _input = read_input_file();
	return 1;
}

fn solve_puzzle_2() -> i32 {
	let _input = read_input_file();
	return 2;
}

fn main() {
	println!("Puzzle 1: {}", solve_puzzle_1());
	println!("Puzzle 2: {}", solve_puzzle_2());
}
