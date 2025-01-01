import React from "react";

const About: React.FC = () => {
  return (
    <div className="space-y-8">
      <h1 className="text-4xl font-bold text-center mb-8">
        About Mimicer Admin
      </h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div className="card bg-base-100 shadow-xl">
          <div className="card-body">
            <h2 className="card-title">Our Mission</h2>
            <p>
              At Mimicer, we're dedicated to enhancing your D&D Discord
              experience. Our mission is to provide powerful tools for managing
              your server, automating tasks, and creating an immersive
              roleplaying environment.
            </p>
          </div>
        </div>
        <div className="card bg-base-100 shadow-xl">
          <div className="card-body">
            <h2 className="card-title">Features</h2>
            <ul className="list-disc list-inside">
              <li>User Management</li>
              <li>Channel Organization</li>
              <li>Automated Tasks with CronJobs</li>
              <li>Custom Discord Bot Integration</li>
            </ul>
          </div>
        </div>
      </div>
      <div className="text-center mt-8">
        <h2 className="text-2xl font-semibold mb-4">
          Ready to level up your D&D Discord?
        </h2>
        <button className="btn btn-secondary">Get Started</button>
      </div>
    </div>
  );
};

export default About;
