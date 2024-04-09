import folium
from geopy.geocoders import Nominatim
import webbrowser

def get_coordinates(city):
    geolocator = Nominatim(user_agent="my_map_app")
    location = geolocator.geocode(city)
    return location.latitude, location.longitude

def draw_path(source_city, destination_city):
    source_coordinates = get_coordinates(source_city)
    destination_coordinates = get_coordinates(destination_city)

    # Create a map centered at the source city
    my_map = folium.Map(location=source_coordinates, zoom_start=5)

    # Add markers for source and destination
    folium.Marker(location=source_coordinates, popup=source_city).add_to(my_map)
    folium.Marker(location=destination_coordinates, popup=destination_city).add_to(my_map)

    # Draw a line between source and destination
    folium.PolyLine([source_coordinates, destination_coordinates], color="blue", weight=2.5, opacity=1).add_to(my_map)

    # Save the map as an HTML file
    my_map.save("templates/path_map.html")

    # Open the map in the default web browser
    webbrowser.open("templates/path_map.html")

# Example usage
source_city = "patna, India"
destination_city = "Kochi, India"
draw_path(source_city, destination_city)