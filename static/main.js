const API_BASE = 'https://prokart-e-commerce.onrender.com';
let cart = [];
let currentFilter = 'all';
let allProducts = [];
let visibleCount = 24;

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
    <div class="col-lg-3 col-md-4 col-sm-6" data-category="${p.category}">
      <div class="product-card">
        ${p.badge ? `<div class="product-badge ${p.badge==='Sale'?'sale':''}">${p.badge}</div>` : ''}
        <div class="product-img-wrap">
          <img src="${p.image || 'https://via.placeholder.com/200x200?text=ProKart'}" alt="${p.name}" class="product-image" loading="lazy">
        </div>
        <div class="product-info">
          <div class="product-category">${p.category.toUpperCase()}</div>
          <div class="product-name">${p.name}</div>
          <div class="product-rating">
            ${'★'.repeat(Math.floor(p.rating || 0))}${'☆'.repeat(5-Math.floor(p.rating || 0))}
            <span>(${(p.reviews || 0).toLocaleString()})</span>
          </div>
          <div class="product-price">
            <span class="price-new">₹${(p.price || 0).toLocaleString('en-IN')}</span>
            <span class="price-old">₹${(p.original || 0).toLocaleString('en-IN')}</span>
          </div>
          <button class="btn-cart" id="btn-${p.id}" onclick="addToCart(${p.id})">
            <i class="fas fa-shopping-cart me-2"></i>Add to Cart
          </button>
        </div>
      </div>
    </div>
  `).join('');

  const btn = document.getElementById('viewMoreBtn');
  if (btn) {
    btn.style.display = visibleCount >= allProducts.length ? 'none' : 'block';
  }
}

function loadMore() {
  visibleCount += 24;
  displayProducts();
}

async function addToCart(id) {
  const products = await fetchProducts('all');
  const product = products.find(p => p.id === id);

  if (product) {
    const existing = cart.find(c => c.id === id);
    if (existing) {
      existing.qty += 1;
    } else {
      cart.push({ ...product, qty: 1 });
    }
    updateCartUI();
    showToast('🛒 ' + product.name + ' added!');
  }

  const btn = document.getElementById(`btn-${id}`);
  if (btn) {
    btn.classList.add('added');
    btn.innerHTML = '<i class="fas fa-check me-2"></i>Added!';
    setTimeout(() => {
      btn.classList.remove('added');
      btn.innerHTML = '<i class="fas fa-shopping-cart me-2"></i>Add to Cart';
    }, 1500);
  }
}

async function filterProducts(cat, btn) {
  currentFilter = cat;
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  await renderProducts(cat);
}

async function checkout() {
  if (cart.length === 0) {
    showToast('⚠️ Cart is empty!');
    return;
  }
  // Save cart to localStorage for checkout page
  localStorage.setItem('prokart_cart', JSON.stringify(cart));
  window.location.href = 'checkout.html';
}
function toggleCart() {
  document.getElementById('cartSidebar').classList.toggle('open');
  document.getElementById('cartOverlay').classList.toggle('open');
}

function updateCartUI() {
  const cartItems = document.getElementById('cartItems');
  const cartCount = document.getElementById('cartCount');
  const cartTotal = document.getElementById('cartTotal');
  const cartFooter = document.getElementById('cartFooter');

  cartCount.textContent = cart.reduce((sum, item) => sum + item.qty, 0);

  if (cart.length === 0) {
    cartItems.innerHTML = '<div class="cart-empty"><i class="fas fa-shopping-cart"></i>Your cart is empty</div>';
    cartFooter.style.display = 'none';
    return;
  }

  cartItems.innerHTML = cart.map(item => `
    <div class="cart-item">
      <img src="${item.image || 'https://via.placeholder.com/50'}" style="width:50px;height:50px;object-fit:contain;border-radius:8px;">
      <div class="cart-item-info">
        <div class="cart-item-name">${item.name}</div>
        <div class="cart-item-price">₹${item.price.toLocaleString()} x ${item.qty}</div>
      </div>
      <button class="cart-item-remove" onclick="removeFromCart(${item.id})">
        <i class="fas fa-trash"></i>
      </button>
    </div>
  `).join('');

  const total = cart.reduce((sum, item) => sum + (item.price * item.qty), 0);
  cartTotal.textContent = '₹' + total.toLocaleString();
  cartFooter.style.display = 'block';
}

function removeFromCart(id) {
  cart = cart.filter(item => item.id !== id);
  updateCartUI();
}

function showToast(msg) {
  const toast = document.getElementById('toast');
  toast.textContent = msg;
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 2500);
}

// Stats with retry logic
async function loadStats() {
  try {
    const stats = await fetch(`${API_BASE}/api/stats`).then(r => r.json());

    const counters = [
      { id: 'count1', target: stats.products || 0 },
      { id: 'count2', target: stats.customers || 0 },
      { id: 'count3', target: stats.orders || 0 },
      { id: 'count4', target: stats.reviews || 0 }
    ];

    counters.forEach(({ id, target }) => {
      let current = 0;
      const step = Math.ceil(target / 100);
      const el = document.getElementById(id);
      if (!el) return;
      const interval = setInterval(() => {
        current += step;
        if (current >= target) {
          el.textContent = target.toLocaleString();
          clearInterval(interval);
        } else {
          el.textContent = current.toLocaleString();
        }
      }, 20);
    });

  } catch(e) {
    // 5 seconds baad retry karo
    console.log('Stats retry kar raha hai...');
    setTimeout(loadStats, 5000);
  }
}

function searchProducts() {
  const query = document.getElementById('searchInput').value.toLowerCase();
  const minPrice = parseInt(document.getElementById('minPrice').value);
  const maxPrice = parseInt(document.getElementById('maxPrice').value);

  const filtered = allProducts.filter(p => {
    const nameMatch = p.name.toLowerCase().includes(query);
    const priceMatch = p.price >= minPrice && p.price <= maxPrice;
    return nameMatch && priceMatch;
  });

  const grid = document.getElementById('productGrid');

  if (filtered.length === 0) {
    grid.innerHTML = '<div class="col-12 text-center" style="padding:60px;color:var(--text-muted)"><i class="fas fa-search" style="font-size:3rem;display:block;margin-bottom:16px;"></i>No products found!</div>';
    document.getElementById('viewMoreBtn').style.display = 'none';
    return;
  }

  grid.innerHTML = filtered.slice(0, visibleCount).map(p => `
    <div class="col-lg-3 col-md-4 col-sm-6">
      <div class="product-card">
        ${p.badge ? `<div class="product-badge ${p.badge==='Sale'?'sale':''}">${p.badge}</div>` : ''}
        <div class="product-img-wrap">
          <img src="${p.image || 'https://via.placeholder.com/200x200?text=ProKart'}" alt="${p.name}" class="product-image" loading="lazy">
        </div>
        <div class="product-info">
          <div class="product-category">${p.category.toUpperCase()}</div>
          <div class="product-name">${p.name}</div>
          <div class="product-rating">
            ${'★'.repeat(Math.floor(p.rating || 0))}${'☆'.repeat(5-Math.floor(p.rating || 0))}
            <span>(${(p.reviews || 0).toLocaleString()})</span>
          </div>
          <div class="product-price">
            <span class="price-new">₹${(p.price || 0).toLocaleString('en-IN')}</span>
            <span class="price-old">₹${(p.original || 0).toLocaleString('en-IN')}</span>
          </div>
          <button class="btn-cart" id="btn-${p.id}" onclick="addToCart(${p.id})">
            <i class="fas fa-shopping-cart me-2"></i>Add to Cart
          </button>
        </div>
      </div>
    </div>
  `).join('');

  document.getElementById('viewMoreBtn').style.display =
    filtered.length > visibleCount ? 'block' : 'none';
}

window.addEventListener('load', async () => {
  await renderProducts();
  loadStats();
});
