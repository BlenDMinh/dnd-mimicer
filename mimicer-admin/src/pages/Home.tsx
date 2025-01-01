import React from "react";
import { Link } from "react-router";

const Home: React.FC = () => {
  return (
    <div className="hero">
      <div className="hero-content text-center">
        <div className="max-w-md">
          <h1 className="text-5xl font-bold">Welcome to Mimicer Admin</h1>
          <p className="py-6">
            Mimicer Admin is your go-to Discord utility for Dungeons & Dragons.
            Manage users, channels, and automate tasks with our powerful admin
            panel.
          </p>
          <Link to="/about" className="btn btn-primary">
            Learn More
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Home;
