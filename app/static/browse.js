let allListings = [];

document.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById("listingContainer");

  // Fetch listings
  fetch("/listings")
    .then(res => res.json())
    .then(data => {
      if (!Array.isArray(data) || data.length === 0) {
        container.innerHTML = "<p>No listings available right now.</p>";
        return;
      }
      allListings = data;
      renderListings(allListings);
    })
    .catch(err => {
      console.error("Error fetching listings:", err);
      container.innerHTML = "<p>Failed to load listings.</p>";
    });

  // Redirect button
  document.querySelector(".btn").addEventListener("click", () => {
    window.location.href = "/listing";
  });
});

// ===== Render listings =====
function renderListings(listings) {
  const container = document.getElementById("listingContainer");
  container.innerHTML = "";

  if (!listings.length) {
    container.innerHTML = "<p>No listings found for this platform.</p>";
    return;
  }

  listings.forEach(listing => {
    const card = document.createElement("div");
    card.classList.add("listing-card");
    card.innerHTML = `
      <h3>${listing.name}</h3>
      <p>${listing.description}</p>
      <p class="price">₹${listing.price} for ${listing.validity_days} days</p>
      <button class="rent-btn" data-id="${listing.id}">Rent Now</button>
    `;
    container.appendChild(card);
  });
}

// ===== Platform filter =====
document.getElementById("platformFilter").addEventListener("change", (e) => {
  const selected = e.target.value.toLowerCase();
  if (selected === "all") {
    renderListings(allListings);
  } else {
    const filtered = allListings.filter(l => l.name.toLowerCase().includes(selected));
    renderListings(filtered);
  }
});

// ===== Rent popup =====
document.addEventListener("click", (e) => {
  if (e.target.classList.contains("rent-btn")) {
    const card = e.target.closest(".listing-card");
    const name = card.querySelector("h3").innerText;
    const desc = card.querySelector("p").innerText;
    const price = card.querySelector(".price").innerText;
    const id = e.target.dataset.id;

    document.getElementById("paymentDetails").innerHTML = `
      <p><strong>${name}</strong></p>
      <p>${desc}</p>
      <p style="color:#cbb977">${price}</p>
    `;
    document.getElementById("confirmPayment").dataset.listingId = id;
    document.getElementById("paymentModal").style.display = "flex";
  }
});

// ===== Close modal =====
document.getElementById("closePayment").addEventListener("click", () => {
  document.getElementById("paymentModal").style.display = "none";
});

// ===== Confirm payment =====
document.getElementById("confirmPayment").addEventListener("click", async () => {
  const btn = document.getElementById("confirmPayment");
  const listingId = btn.dataset.listingId;
  const method = document.getElementById("paymentMethod").value;

  btn.innerText = "Processing...";
  btn.disabled = true;

  await new Promise(r => setTimeout(r, 2000)); // simulate payment delay

  try {
    const response = await fetch("/transactions/create", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        listing_id: listingId,
        payment_method: method,
        status: "success"
      })
    });

    if (response.ok) {
      btn.innerText = "Payment Successful ✅";
      btn.style.background = "#9ccc65";
    } else {
      btn.innerText = "Payment Failed ❌";
      btn.style.background = "#e57373";
    }

    setTimeout(() => {
      document.getElementById("paymentModal").style.display = "none";
      btn.innerText = "Confirm Payment";
      btn.disabled = false;
      btn.style.background = "linear-gradient(90deg, #cbb977, #a2adbc)";
    }, 1500);
  } catch (error) {
    console.error("Payment error:", error);
    btn.innerText = "Error ❌";
  }
});
