# CA2: Event App (Around Eire)
<img src="https://github.com/user-attachments/assets/57b62c8c-d05b-4c50-a58d-9b08875cdbe7" alt="logo" width="200">

## Visit the Website
[Access the Event App here](https://c21716601awm24.xyz/events)

## Docker Hub Link

[Access DockerHub here](https://hub.docker.com/r/emilroy1/geodjango_tutorial/tags)

## Assignment Overview
The Event App is a dynamic web application designed to showcase events across Ireland, providing users with an intuitive interface to browse, filter, and navigate to events. This assignment demonstrates proficiency in GeoDjango, Docker, and mapping technologies, integrating functionalities like satellite view, event details, and seamless navigation.

## Functionalities

| 🎯 **Feature**               | ✨ **Description**                                                             |
|------------------------------|-------------------------------------------------------------------------------|
| 🗺️ **Interactive Maps**       | Real-time updates with interactive controls for navigating and zooming.       |
| 📍 **Event Navigation**      | Directly open event locations on Google Maps for user convenience.            |
| 🔍 **Event Filters**          | Filter events by type, date, and keywords for customised views.               |
| ❤️ **User Favorites**         | Save and filter favorite events for quick access.                             |
| 📄 **Event Details**          | Access detailed event information with images and sharing options.            |
| 🔗 **Share Event**            | Share events on popular platforms like Facebook, X (Twitter), and LinkedIn.   |
| 🛰️ **Satellite Mode**         | Toggle between standard and satellite map views.                              |
| 🔒 **Secure Deployment**      | Ensures user data and access are protected with HTTPS.                        |
| 📱 **Responsive Interface**   | Works seamlessly on mobile, tablet, and desktop devices.                      |
| 🛠️ **Event Management**       | Administrators can add, edit, and remove events via the database.             |

## Instructions to Use the Application

1. **Access the Website**:
   - Visit the website at [Event App](https://c21716601awm24.xyz).
   - Login/Register an account.

2. **Explore Events on the Map**:
   - Navigate the interactive map to view event locations.
   - Use the zoom and pan controls to explore different areas.

3. **Switch Between Views**:
   - Toggle between "Map View" and "Satellite Mode" for different perspectives.

4. **Search and Filter Events**:
   - Use the search bar to find events by name or keywords.
   - Apply filters to narrow down events by type, month, or year.

5. **View Event Details**:
   - Click on an event marker or card to view detailed information about the event.
   - See event details such as title, type, date, and location.

6. **Navigate to Events**:
   - Click the "Navigate to" button to open the event location on Google Maps.

7. **Mark Events as Favorites**:
   - Click the heart icon on an event card to add it to your favorites.
   - Use the favorites toggle to view only your saved events.

8. **Share Events**:
   - Use the share options to post events to Facebook, X (Twitter), or LinkedIn.

9. **Responsive Design**:
   - Enjoy seamless navigation across mobile, tablet, and desktop devices.

10. **Admin Features**:
    - Log in as an admin to manage events, including adding, editing, and deleting entries.

### Technologies Used
1. **GeoDjango**: For geospatial data handling and mapping.
2. **Docker**: To containerize the application for consistent deployment.
3. **PostgreSQL with PostGIS**: For robust geospatial database management.
4. **Leaflet.js**: Interactive map rendering.
5. **Certbot**: For securing the website with HTTPS.
6. **Data Integration**: Events data was processed from CSV files to JSON for seamless integration.


## Application Screenshots

### Event App Overview
<img width="1439" alt="image" src="https://github.com/user-attachments/assets/28f09f1f-f781-4eeb-b6d5-c24fd9b395cc" />


### Satellite Mode
<img width="1223" alt="image" src="https://github.com/user-attachments/assets/f0a95f38-2121-4194-84f7-f5582783c60e" />


### Event Details Popup
<img width="388" alt="image" src="https://github.com/user-attachments/assets/d2996f5a-8ae9-4864-8757-ed558b71b7b9" />

When the user presses “View Details,” they are presented with additional information about the event, including:

- **Online Search**: Opens Google with the event details.
- **Directions**: Opens Google Maps with the event location.
- **Share**: Options to share the event on Facebook, X (Twitter), and LinkedIn.
- **Back to Event List**: Return to browse other events.

<img width="1146" alt="image" src="https://github.com/user-attachments/assets/9dfd54ca-6756-407c-8331-e072d7f43654" />


### Certbot Configuration
![Certbot](https://github.com/user-attachments/assets/95beac83-6d45-43c3-8125-95f47dca0b14)

### Docker Process Status
![Docker PS](https://github.com/user-attachments/assets/f3e94af5-66aa-4bd2-837d-8f7d8fcbbd25)

### PG Admin Data Columns
![PG Admin](https://github.com/user-attachments/assets/02dc01b3-bb0e-4f84-9fc4-9b5a7cbf50c0)
These columns represent the data imported into the application. The data was sourced from [data.gov.ie](https://data.gov.ie/dataset/events). Initially, I attempted to use the API but opted to download the data as a CSV file and convert it to JSON for better compatibility.

