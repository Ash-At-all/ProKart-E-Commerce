// ── CONFIG ──────────────────────────────────────────────────
const API_BASE = 'https://prokart-e-commerce.onrender.com';
let cart = [];
let currentFilter = 'all';
let allProducts = [];
let visibleCount = 24;
let currentSort = 'default';

// ── FETCH PRODUCTS ──────────────────────────────────────────
async function fetchProducts(category = 'all') {
  try {
    const response = await fetch(`${API_BASE}/api/products?category=${category}`);
    const data = await response.json();
    return data.products || [];
  } catch (error) {
    console.error('Error fetching products:', error);
    return [];
  }
}

function shuffleArray(arr) {
  return [...arr].sort(() => Math.random() - 0.5);
}

// ── SORT ────────────────────────────────────────────────────
function sortProducts(products) {
  const sorted = [...products];
  switch (currentSort) {
    case 'price-asc':   return sorted.sort((a, b) => (a.price || 0) - (b.price || 0));
    case 'price-desc':  return sorted.sort((a, b) => (b.price || 0) - (a.price || 0));
    case 'rating-desc': return sorted.sort((a, b) => (b.rating || 0) - (a.rating || 0));
    case 'name-asc':    return sorted.sort((a, b) => a.name.localeCompare(b.name));
    case 'discount':    return sorted.sort((a, b) => {
      const discA = ((a.original - a.price) / a.original) || 0;
      const discB = ((b.original - b.price) / b.original) || 0;
      return discB - discA;
    });
    default: return shuffleArray(products);
  }
}

function setSort(val) {
  currentSort = val;
  displayProducts();
}

// ── RENDER ──────────────────────────────────────────────────
async function renderProducts(filter = 'all') {
  const grid = document.getElementById('productGrid');
  if (grid) {
    grid.innerHTML = Array(8).fill(0).map(() => `
      <div class="col-lg-3 col-md-4 col-sm-6">
        <div class="skeleton-card">
          <div class="skeleton-img skeleton-pulse"></div>
          <div class="skeleton-body">
            <div class="skeleton-line short skeleton-pulse"></div>
            <div class="skeleton-line skeleton-pulse"></div>
            <div class="skeleton-line medium skeleton-pulse"></div>
            <div class="skeleton-btn skeleton-pulse"></div>
          </div>
        </div>
      </div>`).join('');
  }
  allProducts = await fetchProducts(filter);
  visibleCount = 24;
  displayProducts();
}

function buildProductCard(p) {
  const discount = p.original > p.price
    ? Math.round(((p.original - p.price) / p.original) * 100)
    : 0;
  const stars = '★'.repeat(Math.floor(p.rating || 0)) + '☆'.repeat(5 - Math.floor(p.rating || 0));
  return `
    <div class="col-lg-3 col-md-4 col-sm-6 reveal-card" data-category="${p.category}">
      <div class="product-card">
        ${p.badge ? `<div class="product-badge ${p.badge === 'Sale' ? 'sale' : ''}">${p.badge}</div>` : ''}
        ${discount >= 5 ? `<div class="discount-chip">-${discount}%</div>` : ''}
        <div class="product-img-wrap" onclick="openQuickView(${p.id})" style="cursor:pointer;">
          <img src="${p.image || 'https://via.placeholder.com/200x200?text=ProKart'}"
               alt="${p.name}" class="product-image" loading="lazy"
               onerror="this.src='https://via.placeholder.com/200x200?text=No+Image'">
          <div class="quick-view-overlay">
            <span><i class="fas fa-eye me-1"></i>Quick View</span>
          </div>
        </div>
        <div class="product-info">
          <div class="product-category">${p.category.toUpperCase()}</div>
          <div class="product-name" title="${p.name}">${p.name}</div>
          <div class="product-rating">
            ${stars}
            <span>(${(p.reviews || 0).toLocaleString()})</span>
          </div>
          <div class="product-price">
            <span class="price-new">₹${(p.price || 0).toLocaleString('en-IN')}</span>
            ${p.original > p.price ? `<span class="price-old">₹${(p.original || 0).toLocaleString('en-IN')}</span>` : ''}
          </div>
          <button class="btn-cart" id="btn-${p.id}" onclick="addToCart(${p.id})">
            <i class="fas fa-shopping-cart me-2"></i>Add to Cart
          </button>
        </div>
      </div>
    </div>`;
}

function displayProducts() {
  const grid = document.getElementById('productGrid');
  if (!grid) return;
  const sorted = sortProducts(allProducts);
  const visible = sorted.slice(0, visibleCount);

  grid.innerHTML = visible.map(p => buildProductCard(p)).join('');

  const btn = document.getElementById('viewMoreBtn');
  if (btn) {
    btn.style.display = visibleCount >= allProducts.length ? 'none' : 'block';
  }

  // Scroll reveal
  observeCards();
}

function loadMore() {
  visibleCount += 24;
  displayProducts();
}

// ── ADD TO CART ─────────────────────────────────────────────
async function addToCart(id) {
  // Use cached allProducts first, fall back to fetch
  let product = allProducts.find(p => p.id === id);
  if (!product) {
    const products = await fetchProducts('all');
    product = products.find(p => p.id === id);
  }

  if (product) {
    const existing = cart.find(c => c.id === id);
    if (existing) {
      existing.qty += 1;
    } else {
      cart.push({ ...product, qty: 1 });
    }
    updateCartUI();
    showToast('🛒 ' + product.name.substring(0, 28) + '… added!');
    saveCartToStorage();
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

function saveCartToStorage() {
  localStorage.setItem('prokart_cart', JSON.stringify(cart));
}

// ── CART UI ─────────────────────────────────────────────────
function updateCartUI() {
  const cartItems = document.getElementById('cartItems');
  const cartCount = document.getElementById('cartCount');
  const cartTotal = document.getElementById('cartTotal');
  const cartFooter = document.getElementById('cartFooter');
  if (!cartItems) return;

  const totalQty = cart.reduce((sum, item) => sum + item.qty, 0);
  cartCount.textContent = totalQty;

  if (cart.length === 0) {
    cartItems.innerHTML = `
      <div class="cart-empty">
        <i class="fas fa-shopping-cart"></i>
        <div>Your cart is empty</div>
        <div style="font-size:0.78rem;margin-top:6px;color:var(--text-muted)">Add some products!</div>
      </div>`;
    cartFooter.style.display = 'none';
    return;
  }

  cartItems.innerHTML = cart.map(item => `
    <div class="cart-item">
      <img src="${item.image || 'https://via.placeholder.com/50'}"
           style="width:48px;height:48px;object-fit:contain;border-radius:8px;background:var(--bg-card2);flex-shrink:0;"
           onerror="this.src='https://via.placeholder.com/48'">
      <div class="cart-item-info">
        <div class="cart-item-name">${item.name.length > 32 ? item.name.substring(0, 32) + '…' : item.name}</div>
        <div class="cart-item-price">₹${item.price.toLocaleString('en-IN')}</div>
        <div class="cart-qty-ctrl">
          <button class="qty-btn" onclick="changeQty(${item.id}, -1)" aria-label="Decrease">−</button>
          <span class="qty-num">${item.qty}</span>
          <button class="qty-btn" onclick="changeQty(${item.id}, 1)" aria-label="Increase">+</button>
        </div>
      </div>
      <button class="cart-item-remove" onclick="removeFromCart(${item.id})" title="Remove">
        <i class="fas fa-trash"></i>
      </button>
    </div>`).join('');

  const total = cart.reduce((sum, item) => sum + (item.price * item.qty), 0);
  cartTotal.textContent = '₹' + total.toLocaleString('en-IN');
  cartFooter.style.display = 'block';
}

function changeQty(id, delta) {
  const item = cart.find(c => c.id === id);
  if (!item) return;
  item.qty += delta;
  if (item.qty <= 0) {
    cart = cart.filter(c => c.id !== id);
  }
  updateCartUI();
  saveCartToStorage();
}

function removeFromCart(id) {
  cart = cart.filter(item => item.id !== id);
  updateCartUI();
  saveCartToStorage();
}

function toggleCart() {
  document.getElementById('cartSidebar').classList.toggle('open');
  document.getElementById('cartOverlay').classList.toggle('open');
}

// ── FILTER ──────────────────────────────────────────────────
async function filterProducts(cat, btn) {
  currentFilter = cat;
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  await renderProducts(cat);
  // Reset search
  const si = document.getElementById('searchInput');
  if (si) si.value = '';
}

// ── SEARCH ──────────────────────────────────────────────────
function searchProducts() {
  const query = (document.getElementById('searchInput')?.value || '').toLowerCase().trim();
  const minPrice = parseInt(document.getElementById('minPrice')?.value || '0');
  const maxPrice = parseInt(document.getElementById('maxPrice')?.value || '999999');
  const grid = document.getElementById('productGrid');
  if (!grid) return;

  const filtered = allProducts.filter(p => {
    const nameMatch = p.name.toLowerCase().includes(query) ||
                      p.category.toLowerCase().includes(query);
    const priceMatch = p.price >= minPrice && p.price <= maxPrice;
    return nameMatch && priceMatch;
  });

  const sorted = sortProducts(filtered);

  if (sorted.length === 0) {
    grid.innerHTML = `
      <div class="col-12 text-center" style="padding:80px 20px;">
        <i class="fas fa-search" style="font-size:3.5rem;color:var(--border);display:block;margin-bottom:20px;"></i>
        <div style="font-family:'Orbitron',monospace;font-size:1rem;color:var(--text);margin-bottom:8px;">No Results Found</div>
        <div style="color:var(--text-muted);font-size:0.88rem;">Try a different search term or category.</div>
      </div>`;
    if (document.getElementById('viewMoreBtn'))
      document.getElementById('viewMoreBtn').style.display = 'none';
    return;
  }

  grid.innerHTML = sorted.slice(0, visibleCount).map(p => buildProductCard(p)).join('');
  if (document.getElementById('viewMoreBtn'))
    document.getElementById('viewMoreBtn').style.display =
      sorted.length > visibleCount ? 'block' : 'none';

  observeCards();
}

// ── QUICK VIEW MODAL ─────────────────────────────────────────
function openQuickView(id) {
  const product = allProducts.find(p => p.id === id);
  if (!product) return;

  const discount = product.original > product.price
    ? Math.round(((product.original - product.price) / product.original) * 100)
    : 0;
  const stars = '★'.repeat(Math.floor(product.rating || 0)) + '☆'.repeat(5 - Math.floor(product.rating || 0));

  let modal = document.getElementById('quickViewModal');
  if (!modal) {
    modal = document.createElement('div');
    modal.id = 'quickViewModal';
    modal.className = 'qv-overlay';
    modal.onclick = function(e) { if (e.target === this) closeQuickView(); };
    document.body.appendChild(modal);
  }

  modal.innerHTML = `
    <div class="qv-box">
      <button class="qv-close" onclick="closeQuickView()"><i class="fas fa-times"></i></button>
      <div class="qv-content">
        <div class="qv-img-wrap">
          <img src="${product.image || ''}" alt="${product.name}"
               onerror="this.src='https://via.placeholder.com/300x300?text=No+Image'">
          ${discount >= 5 ? `<div class="qv-discount-tag">-${discount}% OFF</div>` : ''}
        </div>
        <div class="qv-details">
          <div class="qv-cat">${product.category.toUpperCase()}</div>
          <h3 class="qv-name">${product.name}</h3>
          <div class="qv-stars">${stars} <span class="qv-reviews">(${(product.reviews || 0).toLocaleString()} reviews)</span></div>
          <div class="qv-price-row">
            <span class="qv-price-new">₹${(product.price || 0).toLocaleString('en-IN')}</span>
            ${product.original > product.price
              ? `<span class="qv-price-old">₹${(product.original || 0).toLocaleString('en-IN')}</span>`
              : ''}
            ${discount >= 5 ? `<span class="qv-save">You save ₹${(product.original - product.price).toLocaleString('en-IN')}</span>` : ''}
          </div>
          <div class="qv-badges">
            <span class="qv-badge"><i class="fas fa-shield-alt"></i> Official Warranty</span>
            <span class="qv-badge"><i class="fas fa-undo"></i> 7-Day Return</span>
            <span class="qv-badge"><i class="fas fa-truck"></i> Fast Delivery</span>
          </div>
          ${product.badge ? `<div class="qv-label qv-label-${product.badge.toLowerCase()}">${product.badge}</div>` : ''}
          <button class="btn-primary-glow qv-add-btn" onclick="addToCart(${product.id}); closeQuickView();">
            <i class="fas fa-shopping-cart me-2"></i>Add to Cart
          </button>
        </div>
      </div>
    </div>`;

  modal.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeQuickView() {
  const modal = document.getElementById('quickViewModal');
  if (modal) {
    modal.classList.remove('open');
    document.body.style.overflow = '';
  }
}

// Escape key closes modal
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') closeQuickView();
});

// ── CHECKOUT ────────────────────────────────────────────────
async function checkout() {
  if (cart.length === 0) { showToast('⚠️ Cart is empty!'); return; }
  localStorage.setItem('prokart_cart', JSON.stringify(cart));
  window.location.href = 'checkout.html';
}

// ── TOAST ────────────────────────────────────────────────────
function showToast(msg, type = 'info') {
  const toast = document.getElementById('toast');
  if (!toast) return;
  toast.textContent = msg;
  toast.className = 'toast-msg show' + (type === 'error' ? ' toast-error' : '');
  clearTimeout(toast._timer);
  toast._timer = setTimeout(() => toast.classList.remove('show'), 2800);
}

// ── STATS ────────────────────────────────────────────────────
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
      const step = Math.max(1, Math.ceil(target / 80));
      const el = document.getElementById(id);
      if (!el) return;
      const interval = setInterval(() => {
        current = Math.min(current + step, target);
        el.textContent = current.toLocaleString();
        if (current >= target) clearInterval(interval);
      }, 20);
    });
  } catch(e) {
    setTimeout(loadStats, 5000);
  }
}

// ── SCROLL REVEAL ────────────────────────────────────────────
function observeCards() {
  const cards = document.querySelectorAll('.reveal-card:not(.revealed)');
  if (!('IntersectionObserver' in window)) {
    cards.forEach(c => c.classList.add('revealed'));
    return;
  }
  const obs = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });
  cards.forEach(c => obs.observe(c));
}

// ── BACK TO TOP ──────────────────────────────────────────────
function initBackToTop() {
  const btn = document.getElementById('backToTop');
  if (!btn) return;
  window.addEventListener('scroll', () => {
    btn.classList.toggle('visible', window.scrollY > 400);
  }, { passive: true });
  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

// ── NAVBAR SCROLL EFFECT ─────────────────────────────────────
function initNavbarScroll() {
  const nav = document.querySelector('.navbar');
  if (!nav) return;
  window.addEventListener('scroll', () => {
    if (window.scrollY > 60) {
      nav.style.background = 'rgba(8,12,20,0.98)';
      nav.style.boxShadow = '0 2px 24px rgba(0,0,0,0.4)';
    } else {
      nav.style.background = 'rgba(8,12,20,0.92)';
      nav.style.boxShadow = 'none';
    }
  }, { passive: true });
}

// ── INIT ─────────────────────────────────────────────────────
window.addEventListener('load', async () => {
  await renderProducts();
  loadStats();
  initBackToTop();
  initNavbarScroll();
});