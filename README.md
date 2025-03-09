# Inter University Cricket

This project is a web application for managing and displaying cricket statistics for inter-university competitions. It consists of a FastAPI backend and a React frontend.

## Project Structure

- **Back-end**: Contains the FastAPI application, database models, and services.
    - `main.py`: Entry point for the FastAPI application.
    - `models/`: Pydantic models for request validation.
    - `db/`: Database connection and data ingestion scripts.
    - `routes/`: API routes for handling requests.
    - `services/`: Business logic and utility functions.
    - `requirements.txt`: Python dependencies.

- **Front-end**: Contains the React application.
    - `src/`: Source code for the React application.
    - `index.html`: Entry point for the web application.
    - `package.json`: JavaScript dependencies and scripts.
    - `tsconfig.json`: TypeScript configuration.

## Setup Instructions

### Backend

1. **Install Dependencies**:
     ```sh
     pip install -r Back-end/requirements.txt
     ```

2. **Set Up Environment Variables**:
     Create a `.env` file in the `Back-end` directory and add your environment variables (e.g., `GOOGLE_API_KEY`).

3. **Run the Application**:
     ```sh
     uvicorn Back-end.main:app --reload
     ```

4. **Set up the MySQL database**:
     - Create a MySQL database named `CricketGame`.
     - Update the `db/db.py` file with your MySQL credentials.

5. **Load sample data into the database**:
     ```sh
     python db/ingest.py
     ```

## API Endpoints

### Chat Routes
- **POST `/chats`**: Process a user query and return a response.
    - Request Body: `{ "question": "Your question here" }`
    - Response: `{ "response": "Generated response" }`

### Player Routes
- **GET `/players`**: Retrieve a list of all players.
    - Response: `List of player objects`

## Database Schema

The `cricketers` table schema:
```sql
CREATE TABLE cricketers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        university VARCHAR(255),
        category VARCHAR(50),
        totalRuns INT,
        ballsFaced INT,
        inningsPlayed INT,
        wickets INT,
        oversBowled INT,
        runsConceded INT,
        batting_strike_rate FLOAT,
        batting_average FLOAT,
        bowling_strike_rate FLOAT,
        economy_rate FLOAT,
        points FLOAT,
        value INT
);
```

## Environment Variables

Create a `.env` file in the root directory and add the following environment variables:
```
GOOGLE_API_KEY=your_google_api_key
```

## Running the Application

1. **Start the FastAPI server**:
     ```sh
     uvicorn main:app --reload
     ```

2. **Access the API documentation**:
     Open your browser and navigate to `http://127.0.0.1:8000/docs` to view the interactive API documentation.

### Frontend

A web application built with React and TypeScript for managing inter-university cricket tournaments. This front-end application provides interfaces for both regular users and administrators to view tournament information, team standings, match schedules, and results.

## Features

- **User Interface**: View tournament details, team information, match schedules, and results.
- **Admin Panel**: Manage teams, players, schedules, and tournament settings.
- **Responsive Design**: Works seamlessly across desktop and mobile devices.

## Technology Stack

- React 19
- TypeScript
- Tailwind CSS
- React Router v7
- TanStack Query (React Query)
- Vite as build tool
- Axios for API communication

## Getting Started

### Prerequisites

- Node.js (v18 or later recommended)
- npm, yarn, or pnpm

### Installation

1. Clone the repository:
     ```bash
     git clone <repository-url>
     cd inter-university-cricket
     ```

2. Install dependencies:
     ```bash
     npm install
     # or
     yarn install
     # or
     pnpm install
     ```

3. Start the development server:
     ```bash
     npm run dev
     # or
     yarn dev
     # or
     pnpm dev
     ```

4. Open your browser and visit `http://localhost:5173`

5. For go to admin page vist `http://localhost:5173/admin`

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build locally
- `npm run lint` - Run ESLint

## Project Structure

- `/src` - Source code
    - `/pages` - Page components
    - `/components` - Reusable UI components
    - `/hooks` - Custom React hooks
    - `/services` - API service functions
    - `/utils` - Utility functions
    - `/types` - TypeScript type definitions

## Deployment

Build the application for production:
```bash
npm run build
```

The build output will be in the `dist` directory, which can be deployed to any static hosting service.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/amazing-feature`).
3. Commit your changes (`git commit -m 'Add some amazing feature'`).
4. Push to the branch (`git push origin feature/amazing-feature`).
5. Open a Pull Request.

## Usage

- Access the frontend at `http://localhost:5173`.
- The backend API is available at `http://localhost:8000`.

## Contributing

Feel free to open issues or submit pull requests for improvements and bug fixes.

## License

This project is licensed under the MIT License.
