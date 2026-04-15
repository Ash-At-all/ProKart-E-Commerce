const API_BASE = 'https://prokart-e-commerce.onrender.com';

let currentFilter = 'all';
let allProducts = [];
let visibleCount = 24;

// ================= PRODUCTS =================
async function fetchProducts(category = 'all') {
  try {
    const response = await fetch(`${API_BASE}/api/products?category=${category}`);
    const data = await response.json();
    return data.products;
  } catch (error) {
    console.error('Error fetching products:', error);
    return [];
  }
}

function shuffleArray(arr) {
  return arr.sort(() => Math.random() - 0.5);
}

async function renderProducts(filter = 'all') {
  allProducts = await fetchProducts(filter);
  allProducts = shuffleArray(allProducts);
  visibleCount = 24;
  displayProducts();
}

function displayProducts() {
  const grid = document.getElementById('productGrid');
  const visible = allProducts.slice(0, visibleCount);

  grid.innerHTML = visible.map(p => `
    <div class="col-lg-3 col-md-4 col-sm-6">
      <div class="product-card">
        <div class="product-img-wrap">
          <img src="${p.image || 'https://via.placeholder.com/200'}">
        </div>
        <div class="product-info">
          <div>${p.name}</div>
          <div>₹${p.price}</div>
          <button onclick="addToCart(${p.id})">Add to Cart</button>
        </div>
      </div>
    </div>
  `).join('');
}

// ================= ADD TO CART =================
async function addToCart(id) {
  const token = localStorage.getItem("token");

  if (!token) {
    alert("Login first");
    window.location.href = "login.html";
    return;
  }

  await fetch(`${API_BASE}/api/cart/add?product_id=${id}`, {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${token}`
    }
  });

  showToast("Added to cart 🛒");
  loadCart();
}

// ================= LOAD CART =================
async function loadCart() {
  const token = localStorage.getItem("token");
  if (!token) return;

  const res = await fetch(`${API_BASE}/api/cart`, {
    headers: {
      "Authorization": `Bearer ${token}`
    }
  });

  const data = await res.json();
  updateCartUI(data.items || []);
}

// ================= UPDATE UI =================
function updateCartUI(items) {
  const cartItems = document.getElementById('cartItems');
  const cartCount = document.getElementById('cartCount');
  const cartTotal = document.getElementById('cartTotal');

  cartCount.textContent = items.length;

  if (items.length === 0) {
    cartItems.innerHTML = "Cart empty";
    cartTotal.textContent = "₹0";
    return;
  }

  cartItems.innerHTML = items.map(item => `
    <div>
      ${item.name} - ₹${item.price}
      <button onclick="removeFromCart(${item.id})">❌</button>
    </div>
  `).join('');

  const total = items.reduce((sum, i) => sum + i.price, 0);
  cartTotal.textContent = "₹" + total;
}

// ================= REMOVE =================
async function removeFromCart(id) {
  const token = localStorage.getItem("token");

  await fetch(`${API_BASE}/api/cart/remove?product_id=${id}`, {
    method: "DELETE",
    headers: {
      "Authorization": `Bearer ${token}`
    }
  });

  loadCart();
}

// ================= CHECKOUT =================
async function checkout() {
  const token = localStorage.getItem("token");

  await fetch(`${API_BASE}/api/checkout`, {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${token}`
    }
  });

  showToast("Order placed 🎉");
  loadCart();
}

// ================= USER =================
function showUser() {
  const token = localStorage.getItem("token");

  if (!token) return;

  const payload = JSON.parse(atob(token.split('.')[1]));
  const username = payload.username;

  document.getElementById("navUser").innerHTML =
    `Welcome, ${username}`;
}

// ================= TOAST =================
function showToast(msg) {
  alert(msg);
}

// ================= LOAD =================
window.onload = () => {
  renderProducts();
  loadCart();
  showUser();
};
