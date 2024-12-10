document.addEventListener('DOMContentLoaded', function() {
    const mapView = document.getElementById('mapView');
    const gridView = document.getElementById('gridView');
    const viewToggleButtons = document.querySelectorAll('.view-toggle button');
    const eventTypeFilter = document.getElementById('eventTypeFilter');
    const monthFilter = document.getElementById('monthFilter');
    const yearFilter = document.getElementById('yearFilter');
    const eventCards = document.querySelectorAll('.event-card');
    let map;

    // Initialize map
    function initMap() {
        map = L.map('map').setView([53.349805, -6.26031], 8);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
        }).addTo(map);

        addEventMarkers();
    }

    // Add event markers to the map
    function addEventMarkers() {
        eventCards.forEach(card => {
            const lat = card.dataset.lat;
            const lng = card.dataset.lng;
            const title = card.querySelector('h3').textContent;
            const date = card.querySelector('p').textContent;

            if (lat && lng) {
                L.marker([lat, lng]).addTo(map)
                    .bindPopup(`<strong>${title}</strong><br>${date}`);
            }
        });
    }

    // Toggle between map and grid views
    viewToggleButtons.forEach(button => {
        button.addEventListener('click', function() {
            viewToggleButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');

            if (this.dataset.view === 'map') {
                mapView.classList.add('active');
                gridView.classList.remove('active');
                if (!map) {
                    initMap();
                }
            } else {
                gridView.classList.add('active');
                mapView.classList.remove('active');
            }
        });
    });

    // Filter events
    function filterEvents() {
        const selectedType = eventTypeFilter.value;
        const selectedMonth = monthFilter.value;
        const selectedYear = yearFilter.value;

        eventCards.forEach(card => {
            const cardType = card.dataset.eventType;
            const cardMonth = card.dataset.eventMonth;
            const cardYear = card.dataset.eventYear;

            const typeMatch = selectedType === 'all' || cardType === selectedType;
            const monthMatch = selectedMonth === 'all' || cardMonth === selectedMonth;
            const yearMatch = selectedYear === 'all' || cardYear === selectedYear;

            if (typeMatch && monthMatch && yearMatch) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    }

    eventTypeFilter.addEventListener('change', filterEvents);
    monthFilter.addEventListener('change', filterEvents);
    yearFilter.addEventListener('change', filterEvents);

    // Initialize map on load
    initMap();
});