const products = [
    {
        id: 1,
        name: 'Real Madrid Track Suit',
        price: 79.99,
        image: 'https://footballmonk.in/wp-content/uploads/2024/01/Real-Madrid-White-TrackSuit-23-24-1.jpg'
    },
    {
        id: 2,
        name: 'Football Player Image',
        price: 59.99,
        image: 'https://blog.lovellsoccer.co.uk/wp-content/uploads/2024/09/image-68-edited.png'
    },
    {
        id: 3,
        name: 'Mbappé Real Madrid 24/25 Season First Kit',
        price: 69.99,
        image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdODGducEcf_DFBOcOPszxT6VnC4CtP6kfNA&s'
    },
    {
        id: 4,
        name: 'Stylish Black Boots',
        price: 89.99,
        image: 'https://m.media-amazon.com/images/I/61GQuDAZbgL._AC_SL1500_.jpg'
    },
    {
        id: 5,
        name: 'Classic Brown Boots',
        price: 99.99,
        image: 'https://m.media-amazon.com/images/I/71jhSYdcz3L._AC_US218_.jpg'
    },
    {
        id: 6,
        name: 'Mbappé Real Madrid 24/25 Season Second Kit',
        price: 69.99,
        image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxnNVXVf2LMVLHhiYmL2jSBYjkwjB0JXsagg&s'
    },
    {
        id: 7,
        name: 'Mbappé Real Madrid 24/25 Season Third Kit',
        price: 69.99,
        image: 'https://underthelightsfutbol.com/cdn/shop/files/realmbappethird2.jpg?v=1724127768&width=533'
    }
];

let cartCount = 0;
let totalSpent = 0;

function displayProducts() {
    const productList = document.getElementById('product-list');
    products.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.className = 'product';
        productDiv.innerHTML = `
            <img src="${product.image}" alt="${product.name}">
            <h2>${product.name}</h2>
            <p>Price: $${product.price.toFixed(2)}</p>
            <button class="buy-button" onclick="addToCart(${product.id}, 1)">Buy</button>
        `;
        productList.appendChild(productDiv);
    });
}

function addToCart(productId, quantity) {
    const selectedProduct = products.find(product => product.id === productId);
    cartCount += quantity;
    totalSpent += selectedProduct.price * quantity;

    document.getElementById('cart-count').innerText = cartCount;
    document.getElementById('total-spent').innerText = totalSpent.toFixed(2); // Format to 2 decimal places
}

// Initialize the dropdown and product list
window.onload = () => {
    populateProductDropdown();
    displayProducts();

    const addToCartButton = document.getElementById('add-to-cart-button');
    addToCartButton.onclick = addToCart;
};