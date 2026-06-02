// ===== COUNTDOWN TIMER =====
function startCountdown(endTime, elementId) {
    function update() {
        const now = new Date().getTime();
        const end = new Date(endTime).getTime();
        const diff = end - now;
        if (diff <= 0) return;
        const days = Math.floor(diff / (1000 * 60 * 60 * 24));
        const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const mins = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
        const secs = Math.floor((diff % (1000 * 60)) / 1000);
        const el = document.getElementById(elementId);
        if (el) {
            el.querySelector('.days').textContent = String(days).padStart(2, '0');
            el.querySelector('.hours').textContent = String(hours).padStart(2, '0');
            el.querySelector('.mins').textContent = String(mins).padStart(2, '0');
            el.querySelector('.secs').textContent = String(secs).padStart(2, '0');
        }
    }
    update();
    setInterval(update, 1000);
}

// ===== ADD TO CART =====
function addToCart(productId) {
    fetch(`/orders/add-to-cart/${productId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(r => r.json())
    .then(data => {
        if (data.success) {
            document.querySelector('.cart-badge').textContent = data.cart_count;
            showToast('Product added to cart!');
        }
    });
}

// ===== TOAST =====
function showToast(message) {
    const toast = document.createElement('div');
    toast.className = 'toast-notification';
    toast.textContent = message;
    document.body.appendChild(toast);
    setTimeout(() => toast.classList.add('show'), 100);
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 300);
    }, 2500);
}

// ===== COOKIE =====
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// ===== TOAST CSS =====
const toastStyle = document.createElement('style');
toastStyle.textContent = `
.toast-notification {
    position: fixed;
    bottom: 30px;
    right: 30px;
    background: #2d6a2d;
    color: white;
    padding: 14px 24px;
    border-radius: 10px;
    font-family: 'Poppins', sans-serif;
    font-size: 14px;
    font-weight: 500;
    z-index: 9999;
    transform: translateY(100px);
    opacity: 0;
    transition: all 0.3s ease;
    box-shadow: 0 5px 20px rgba(0,0,0,0.2);
}
.toast-notification.show {
    transform: translateY(0);
    opacity: 1;
}
`;
document.head.appendChild(toastStyle);