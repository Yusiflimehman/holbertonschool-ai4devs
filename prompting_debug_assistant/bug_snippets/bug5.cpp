#include <iostream>
#include <vector>

int main() {
    std::vector<int> nums = {1, 2, 3};
    // Intentional Out of bounds / type misuse
    std::cout << nums[5] << std::endl;
    return 0;
}
