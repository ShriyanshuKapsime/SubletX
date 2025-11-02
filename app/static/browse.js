let allListings = [];

document.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById("listingContainer");
  const filter = document.getElementById("platformFilter");
  const listButton = document.querySelector(".btn");

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
      populateDropdown(data);
    })
    .catch(err => {
      console.error("Error fetching listings:", err);
      container.innerHTML = "<p>Failed to load listings.</p>";
    });

  // Redirect to listing page
  listButton.addEventListener("click", () => {
    window.location.href = "/listing";
  });

  // Filter change event
  filter.addEventListener("change", (e) => {
    const selected = e.target.value.toLowerCase();
    if (selected === "all") {
      renderListings(allListings);
    } else {
      const filtered = allListings.filter(l => 
        l.platform?.toLowerCase() === selected || 
        l.name.toLowerCase().includes(selected)
      );
      renderListings(filtered);
    }
  });
});

// ===== Function to render listings =====
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

// ===== Function to dynamically populate dropdown =====
function populateDropdown(data) {
  const filter = document.getElementById("platformFilter");
  const uniquePlatforms = [
    ...new Set(
      data.map(l => (l.platform || l.name).trim())
    ),
  ];

  filter.innerHTML = `<option value="all">All Platforms</option>`;
  uniquePlatforms.forEach(p => {
    const option = document.createElement("option");
    option.value = p.toLowerCase();
    option.textContent = p;
    filter.appendChild(option);
  });
}

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
