# Flight Deals Tracker

A Python application that automatically tracks and monitors flight prices from Delhi (DEL) to various destinations using the Amadeus API and manages data through Google Sheets via the Sheety API.

## 🚀 Features

- **Automated Flight Price Monitoring**: Continuously tracks flight prices from Delhi to multiple destinations
- **Google Sheets Integration**: Seamlessly reads from and updates flight data stored in Google Sheets
- **IATA Code Auto-Assignment**: Automatically finds and assigns IATA airport codes for destination cities
- **Smart Price Comparison**: Compares current prices with stored lowest prices and updates when better deals are found
- **Real Flight Data**: Uses Amadeus test API to fetch actual flight information
- **Non-stop Flight Focus**: Searches exclusively for direct flights

## 📁 Project Structure

```
flight-deals/
├── main.py           # Main execution script - orchestrates the entire process
├── flight_data.py    # FlightSearch class for Amadeus API authentication and token management
├── sheet_data.py     # Core functionality for Google Sheets integration and flight searching
└── .env             # Environment variables for API credentials (not tracked in git)
```

## 🛠️ Setup

### Prerequisites

- Python 3.6+
- [Amadeus API](https://developers.amadeus.com/) test environment credentials
- [Sheety API](https://sheety.co/) token for Google Sheets access
- Google Sheets document with flight destination data

### Installation

1. **Clone or download this repository**

2. **Install required dependencies:**
   ```bash
   pip install requests python-dotenv
   ```

3. **Create environment file:**
   Create a `.env` file in the project root with your API credentials:
   ```env
   AMADEUS_API_KEY=your_amadeus_api_key_here
   AMADEUS_SECRET=your_amadeus_secret_here
   SHEETY_TOKEN=your_sheety_bearer_token_here
   SHEET=your_sheety_endpoint_url_here
   ```

### Google Sheets Setup

Your Google Sheet should contain the following columns:
- **id**: Unique row identifier
- **city**: Destination city name (e.g., "Paris", "Tokyo")
- **iataCode**: Airport IATA code (auto-populated by the app)
- **lowestPrice**: Lowest recorded price in INR (auto-updated)

## 🚦 Usage

Run the application with:

```bash
python main.py
```

### What the application does:

1. **Fetches Data**: Retrieves destination data from your Google Sheet
2. **Assigns IATA Codes**: Automatically finds and assigns airport codes for cities missing them
3. **Searches Flights**: Looks for flight offers from Delhi to each destination
4. **Updates Prices**: Compares and updates the lowest prices found

## ⚙️ Configuration

### Flight Search Parameters

- **Origin Airport**: DEL (Delhi)
- **Departure Date**: Tomorrow
- **Return Date**: 6 months from departure
- **Currency**: INR (Indian Rupees)
- **Passengers**: 1 adult
- **Flight Type**: Non-stop flights only

### API Endpoints Used

**Amadeus API:**
- Authentication: `/v1/security/oauth2/token`
- City Lookup: `/v1/reference-data/locations/cities`
- Flight Search: `/v2/shopping/flight-offers`

**Sheety API:**
- Your custom endpoint for Google Sheets integration

## 📋 Core Functions

### `main.py`
Main execution script that:
- Imports necessary functions and classes
- Retrieves sheet data and displays it
- Assigns IATA codes to cities
- Updates flight prices

### `flight_data.py`
**FlightSearch Class:**
- Manages Amadeus API authentication
- Handles OAuth2 token generation and management
- Provides foundation for flight-related operations

### `sheet_data.py`
**Key Functions:**
- `get_data()`: Fetches flight destination data from Google Sheets
- `assign_iata()`: Finds and assigns IATA airport codes for cities
- `search_city(city)`: Searches for airport information using city names
- `search_flight()`: Queries flight offers between origin and destination
- `prices()`: Main price comparison and update logic

## 🔐 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `AMADEUS_API_KEY` | Your Amadeus API client ID | ✅ |
| `AMADEUS_SECRET` | Your Amadeus API client secret | ✅ |
| `SHEETY_TOKEN` | Your Sheety API bearer token for Google Sheets access | ✅ |
| `SHEET` | Your Sheety endpoint URL for the Google Sheet | ✅ |

## 🔄 How It Works

1. **Data Retrieval**: The app connects to your Google Sheet and pulls destination data
2. **IATA Assignment**: For any cities without airport codes, it searches Amadeus API and updates the sheet
3. **Price Search**: For each destination, it searches for flights departing tomorrow and returning in 6 months
4. **Price Comparison**: Compares found prices with stored lowest prices
5. **Data Update**: Updates the Google Sheet with new lowest prices when better deals are found

## ⚠️ Important Notes

- Uses **Amadeus test API** (provides mock flight data for development)
- OAuth2 tokens expire after ~30 minutes and are refreshed on each run
- Searches are limited to **non-stop flights only**
- All prices are in **Indian Rupees (INR)**
- Fixed search dates: departing tomorrow, returning in 6 months

## 🔧 Error Handling

The application includes handling for common scenarios:
- Missing or invalid flight data
- API authentication failures
- Cities with no available IATA codes
- Empty flight search results

## 🎯 Future Enhancements

- [ ] Email notifications for significant price drops
- [ ] Support for multiple origin airports
- [ ] Configurable search date ranges
- [ ] Include connecting flights option
- [ ] Token caching for API efficiency
- [ ] Enhanced logging and error reporting
- [ ] Price history tracking and analytics

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Fork this repository
- Create a feature branch
- Submit a pull request

## 📄 License

This project is for educational and personal use. Please ensure compliance with:
- [Amadeus API Terms of Service](https://developers.amadeus.com/terms-of-use)
- [Sheety API Terms](https://sheety.co/terms)

## 🆘 Troubleshooting

**Common Issues:**
- **Authentication errors**: Verify your API credentials in the `.env` file
- **No flight data**: Check if the destination IATA codes are valid
- **Sheet access errors**: Ensure your Sheety token has proper permissions

---

*Last updated: August 2025*
# flight-deals-tracker
