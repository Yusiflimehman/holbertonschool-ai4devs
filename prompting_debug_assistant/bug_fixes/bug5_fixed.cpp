#include <iostream>
#include <vector>

int main() {
    std::vector<int> numbers = {10, 20, 30, 40, 50};

    // Accessing index safely within bounds
    size_t targetIndex = 2;
    if (targetIndex < numbers.size()) {
        std::cout << "Safe Element: " << numbers[targetIndex] << std::endl;
    } else {
        std::cout << "Index out of bounds!" << std::endl;
    }

    return 0;
}
