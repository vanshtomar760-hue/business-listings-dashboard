# Business Listings Dashboard

A full-stack Business Listings Dashboard built using React.js, FastAPI, MySQL, and Python Web Scraping.

## Features

- Scrapes 500+ business listing records
- Stores data in MySQL database
- FastAPI backend APIs
- React dashboard frontend
- Data visualization using Recharts
- City-wise analytics
- Category-wise analytics
- Source-wise analytics

---

## Tech Stack

### Frontend
- React.js
- Axios
- Recharts

### Backend
- FastAPI
- SQLAlchemy
- PyMySQL

### Database
- MySQL

### Web Scraping
- Python
- BeautifulSoup
- Requests
---

## APIs

### Home API

```bash
/
```

### City Count API

```bash
/city-count
```

### Category Count API

```bash
/category-count
```

### Source Count API

```bash
/source-count
```

---

## Setup Instructions

### Backend Setup

Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy pymysql pandas beautifulsoup4 requests
```

Run backend:

```bash
uvicorn main:app --reload
```

Run scraper:

```bash
py scraper.py
```

---

### Frontend Setup

Install dependencies:

```bash
npm install
```

Run frontend:

```bash
npm run dev
```

---

## Database

Database Name:

```bash
business_dashboard
```

Table Name:

```bash
listing_master
```

---

## Challenges Faced

- Connecting React frontend with FastAPI backend
- MySQL database integration
- Handling CORS issues
- Chart rendering issues in React
- Structuring scraped data properly

---

## Future Improvements

- Real Google Maps scraping
- Search and filter functionality
- Authentication system
- Export reports feature
- Responsive mobile dashboard

---

## Author

Vansh Tomar
---

## Challenges Faced

- Connecting FastAPI backend with MySQL database
- Handling CORS issues between frontend and backend
- Configuring React charts using API data
- Managing GitHub branches and repository setup
- Exporting MySQL database dump correctly