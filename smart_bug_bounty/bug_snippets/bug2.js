function calculateTotalPrice(cartItems, discountPercent) {
    let total = 0;

    for (let i = 0; i <= cartItems.length; i++) { // Bug: <= causes undefined iteration
        total += cartItems[i].price;
    }

    if (discountPercent) {
        total = total - (total * discountPercent); // Bug: assumes percent is decimal (e.g. 20 instead of 0.2)
    }

    return total;
}

const cart = [
    { name: "Book", price: 15 },
    { name: "Pen", price: 5 }
];

console.log(calculateTotalPrice(cart, 10));
