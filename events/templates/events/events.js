// Initialize the map
const map = L.map('map').setView([53.349805, -6.26031], 8);

// Define tile layers
const standardLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}).addTo(map);

// Event type to color mapping
const eventTypeColors = {
    "Comedy": "blue",
    "Festival": "green",
    "Sports": "red",
    "Music": "purple",
    "Halloween": "orange",
    "Workshop": "yellow",
    "Social": "pink",
    "Dance": "teal",
    "Film": "brown",
    "Theatre": "gray",
    "Broadcast": "black",
    "Exhibition": "cyan",
    "default": "black",
};

// Add event markers to the map
const addMarkers = (events) => {
    events.forEach(event => {
        if (event.latitude && event.longitude) {
            const markerColor = eventTypeColors[event.event_type] || eventTypeColors.default;
            const marker = L.circleMarker([event.latitude, event.longitude], {
                color: markerColor,
                radius: 8,
                fillOpacity: 0.8,
            }).addTo(map);

            marker.bindPopup(`
                <strong>${event.title}</strong><br>
                ${event.start_date}<br>
                <a href="${event.detailUrl}" target="_blank">More Info</a>
            `);
        }
    });
};

// Fetch events from server
fetch('/api/events') // Adjust the endpoint as per your setup
    .then(response => response.json())
    .then(data => {
        addMarkers(data.events); // Assume API response contains events array
    });

// Toggle views
document.querySelectorAll('.view-toggle button').forEach(button => {
    button.addEventListener('click', () => {
        document.querySelectorAll('.view').forEach(view => {
            view.classList.remove('active');
        });
        document.querySelector(`#${button.dataset.view}View`).classList.add('active');
    });
});
