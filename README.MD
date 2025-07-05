# Dealer Evaluation Microservices Demo

This project contains three microservices:
- **Product Details**: Provides product information.
- **Dealer Pricing**: Provides dealer pricing information.
- **Frontend**: User interface for evaluating dealers and products.

## How to Run Locally

1. **Clone the repository**
2. **Build and start all services with Docker Compose:**
   ```sh
   docker-compose up --build
   ```
   - Frontend: http://localhost:5000/
   - Product Details API: http://localhost:5002/
   - Dealer Pricing API: http://localhost:5001/

## Usage
- Open the frontend in your browser.
- Select a product to view available dealers and prices.
- Select a dealer to view their price for the product.
- Use "All Dealers" to see prices from all dealers for a product.

## Notes
- All services use the `PORT` environment variable for configuration from their respective Dockerfile. At the root folder, docker-compose.yml contains port mapping configuration.
- The ports are mapped as follows:
  - Frontend: 5000 (host) → 80 (container)
  - Dealer Pricing: 5001 (host) → 80 (container)
  - Product Details: 5002 (host) → 80 (container)

---

For any issues, please check the Docker and service logs.