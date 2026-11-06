#include <iostream>
#include <vector>

int main() {
    // Initialize a vector with sample integer values
    std::vector<int> numbers = {10, 20, 30, 40, 50};

    std::cout << "Accessing vector elements safely..." << std::endl;
    for (size_t i = 0; i < numbers.size(); ++i) {
        std::cout << "Item: " << numbers[i] << std::endl;
    }

    // Intentional Out of bounds memory access
    std::cout << "Accessing invalid index:" << std::endl;
    std::cout << numbers[10] << std::endl;

    return 0;
}
