#include <iostream>
#include <fstream>
#include <string>
#include <vector>

std::vector<std::string> read_input_file() {
    std::ifstream file("input.txt");
    std::vector<std::string> lines;
    std::string line;
    while (std::getline(file, line)) {
        lines.push_back(line);
    }
    return lines;
}

int puzzle_1(const std::vector<std::string>& lines) {
    return 0;
}

int puzzle_2(const std::vector<std::string>& lines) {
    return 0;
}

int main() {
    auto lines = read_input_file();
    std::cout << "Puzzle 1: " << puzzle_1(lines) << std::endl;
    // std::cout << "Puzzle 2: " << puzzle_2(lines) << std::endl;
    return 0;
}
