use std::collections::VecDeque;
use std::env;
use std::fs;

fn read_input_file() -> String {
	let current_dir = env::current_dir();
	let file_path = current_dir.unwrap().parent().unwrap().join("input.txt");
	return fs::read_to_string(file_path).expect("Something went wrong reading the file");
}

fn solve_puzzle_1() -> i32 {
	let input = read_input_file();
	let mut sum = 0;
	let mut prev: Option<i32> = None;
	for line in input.lines() {
		let num = line.parse::<i32>().unwrap();
		if prev.is_some() {
			if prev.unwrap() < num {
				sum += 1;
			}
		}
		prev = Some(num);
	}
	return sum;
}

fn solve_puzzle_2() -> i32 {
	const SIZE_WINDOW: usize = 4;

	let input = read_input_file();
	let mut result = 0;

	let mut sum_front = 0;
	let mut sum_prev = 0;
	let mut prev = 0;
	let mut prev_to_rem = 0;
	let mut queue: VecDeque<i32> = VecDeque::new();

	for line in input.lines() {
		let num = line.parse::<i32>().unwrap();
		queue.push_front(num);
		sum_prev += prev;
		prev = num;
		sum_front += prev;
		if queue.len() == SIZE_WINDOW {
			sum_prev -= prev_to_rem;
			prev_to_rem = queue.pop_back().unwrap();
			sum_front -= prev_to_rem;
			if sum_front > sum_prev {
				result += 1
			}
		}
	}
	return result;
}

fn main() {
	println!("Puzzle 1: {}", solve_puzzle_1());
	println!("Puzzle 2: {}", solve_puzzle_2());
}
